import 'package:flutter/material.dart';
import 'segunda_tela.dart'; // Este é o arquivo para a segunda tela que vamos criar

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Na Mira',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: LoginScreen(),
    );
  }
}

class LoginScreen extends StatefulWidget {
  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        fit: StackFit.expand,
        children: <Widget>[
          Image.asset(
            'assets/images/login.jpg',
            fit: BoxFit.cover,
          ),
          Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              SizedBox(height: 100),
              ElevatedButton(
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => SegundaTela()),
                  );
                },
                child: Text('Entrar'),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.blue, // Define a cor do botão
                  foregroundColor: Colors.white, // Define a cor do texto
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
