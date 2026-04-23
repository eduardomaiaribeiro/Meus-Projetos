import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'dart:convert'; // Para decodificar o JSON
import 'package:flutter/services.dart';
import 'package:geolocator/geolocator.dart'; // Para obter a localização do dispositivo
import 'package:permission_handler/permission_handler.dart'; // Para solicitar permissão

// Função para determinar o nível de risco de dengue com base no número de casos
String determinarNivelDeRisco(int casos) {
  if (casos >= 4000) {
    return 'Muito Alto';
  } else if (casos >= 2000) {
    return 'Alto';
  } else if (casos >= 1000) {
    return 'Médio';
  } else if (casos >= 500) {
    return 'Baixo';
  } else {
    return 'Muito Baixo';
  }
}

Future<List<Marker>> loadDengueMarkers() async {
  String data = await rootBundle.loadString('assets/json_dengue.json');
  List<dynamic> jsonResult = json.decode(data);
  List<Marker> markers = [];
  for (var element in jsonResult) {
    final marker = Marker(
      markerId: MarkerId('dengue_${element["Casos"]}'),
      position: LatLng(element['LAT'], element['LONG']),
      infoWindow: InfoWindow(
        title: '${element["Bairro"]}',
        snippet:
            'Casos: ${element["Casos"]}, Risco: ${determinarNivelDeRisco(element["Casos"])}',
      ),
      icon: BitmapDescriptor.defaultMarkerWithHue(
        _getColorForRiskLevel(determinarNivelDeRisco(element["Casos"])),
      ),
    );
    markers.add(marker);
  }
  return markers;
}

// Função para obter a cor com base no nível de risco
double _getColorForRiskLevel(String riskLevel) {
  switch (riskLevel) {
    case 'Muito Alto':
      return BitmapDescriptor.hueRed;
    case 'Alto':
      return BitmapDescriptor.hueOrange;
    case 'Médio':
      return BitmapDescriptor.hueYellow;
    case 'Baixo':
      return BitmapDescriptor.hueGreen;
    case 'Muito Baixo':
    default:
      return BitmapDescriptor.hueBlue;
  }
}

class MapaScreen extends StatefulWidget {
  @override
  _MapaScreenState createState() => _MapaScreenState();
}

class _MapaScreenState extends State<MapaScreen> {
  GoogleMapController? mapController;
  Set<Marker> _markers = {};
  Position? _currentPosition;
  LatLng? _initialCameraPosition;

  @override
  void initState() {
    super.initState();
    _requestLocationPermission(); // Solicita permissão na inicialização
    _requestNotificationPermission(); // Solicita permissão de notificação
    _loadMarkersAndPosition(); // Carrega marcadores e posição inicial
  }

  void _onMapCreated(GoogleMapController controller) {
    mapController = controller;
  }

  Future<void> _requestLocationPermission() async {
    // Verifica se a permissão já foi concedida
    LocationPermission permission = await Geolocator.checkPermission();
    if (permission == LocationPermission.denied) {
      // Solicita permissão ao usuário
      permission = await Geolocator.requestPermission();
      if (permission == LocationPermission.denied) {
        // Permissão negada pelo usuário
        print('Permissão de localização negada pelo usuário.');
      } else if (permission == LocationPermission.deniedForever) {
        // Permissão negada permanentemente
        print('Permissão de localização negada permanentemente.');
      } else {
        // Permissão concedida
        print('Permissão de localização concedida.');
      }
    } else if (permission == LocationPermission.deniedForever) {
      // Permissão negada permanentemente
      print('Permissão de localização negada permanentemente.');
    } else {
      // Permissão concedida
      print('Permissão de localização concedida.');
    }
  }

  Future<void> _requestNotificationPermission() async {
    // Solicita permissão de notificação
    PermissionStatus status = await Permission.notification.request();
    if (status.isGranted) {
      print('Permissão de notificação concedida.');
    } else if (status.isDenied) {
      print('Permissão de notificação negada.');
    } else if (status.isPermanentlyDenied) {
      print('Permissão de notificação negada permanentemente.');
    }
  }

  Future<void> _loadMarkersAndPosition() async {
    try {
      // Carrega os marcadores
      List<Marker> markers = await loadDengueMarkers();
      setState(() {
        _markers = markers.toSet();
      });

      // Tenta obter a localização atual
      Position position = await Geolocator.getCurrentPosition(
        desiredAccuracy: LocationAccuracy.best,
      );
      setState(() {
        _currentPosition = position;
        _initialCameraPosition = LatLng(position.latitude, position.longitude);
      });
    } catch (e) {
      // Se houver erro ao obter a localização, exibe um alerta e define a posição inicial com hardcode
      showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            title: Text('Erro ao Obter Localização'),
            content: Text('Não foi possível obter sua localização atual.'),
            actions: [
              TextButton(
                onPressed: () {
                  Navigator.of(context).pop();
                },
                child: Text('OK'),
              ),
            ],
          );
        },
      );
      setState(() {
        _initialCameraPosition = LatLng(_currentPosition!.latitude,
            _currentPosition!.longitude); // Coordenadas iniciais
      });
    }
  }

  void _checkRiskArea() {
    if (_currentPosition != null) {
      for (Marker marker in _markers) {
        double distance = Geolocator.distanceBetween(
          _currentPosition!.latitude,
          _currentPosition!.longitude,
          marker.position.latitude,
          marker.position.longitude,
        );
        if (distance <= 800 &&
            (determinarNivelDeRisco(
                        int.parse(marker.markerId.value.split('_')[1])) ==
                    'Alto' ||
                determinarNivelDeRisco(
                        int.parse(marker.markerId.value.split('_')[1])) ==
                    'Muito Alto')) {
          _showRiskAlert(); // Exibe o alerta de risco
          break;
        }
      }
    }
  }

  void _showRiskAlert() {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Alerta de Risco'),
          content: Text(
              'Você está entrando em uma área de risco de dengue. Tome cuidado!'),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: Text('OK'),
            ),
          ],
        );
      },
    );
  }

  void _goToCurrentLocation() {
    if (_currentPosition != null) {
      mapController?.animateCamera(
        CameraUpdate.newCameraPosition(
          CameraPosition(
            target:
                LatLng(_currentPosition!.latitude, _currentPosition!.longitude),
            zoom: 13.5,
          ),
        ),
      );
    }
    _checkRiskArea(); // Verifica se a localização atual está em uma área de risco
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Mapa de Dengue'),
      ),
      body: Column(
        children: [
          // Legenda
          Container(
            padding: EdgeInsets.all(10),
            color: Colors.white,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                _buildLegendItem('Muito Alto', Colors.red),
                _buildLegendItem('Alto', Colors.orange),
                _buildLegendItem('Médio', Colors.yellow),
                _buildLegendItem('Baixo', Colors.green),
                _buildLegendItem('Muito Baixo', Colors.blue),
              ],
            ),
          ),
          // Mapa
          Expanded(
            child: Stack(
              children: [
                GoogleMap(
                  onMapCreated: _onMapCreated,
                  initialCameraPosition: _initialCameraPosition != null
                      ? CameraPosition(
                          target: _initialCameraPosition!, zoom: 13.5)
                      : CameraPosition(
                          target: LatLng(
                              -23.5337, -46.6252), // Coordenadas iniciais
                          zoom: 13.5,
                        ),
                  markers: _markers,
                ),
                // Botão para ir para a localização atual
                Align(
                  alignment: Alignment.bottomCenter,
                  child: Padding(
                    padding: const EdgeInsets.only(bottom: 20.0),
                    child: FloatingActionButton(
                      onPressed: _goToCurrentLocation,
                      child: Icon(Icons.my_location),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  // Widget para criar um item da legenda
  Widget _buildLegendItem(String riskLevel, Color color) {
    return Row(
      children: [
        Container(
          width: 10,
          height: 10,
          decoration: BoxDecoration(
            shape: BoxShape.circle,
            color: color,
          ),
        ),
        SizedBox(width: 5),
        Text(riskLevel),
      ],
    );
  }
}
