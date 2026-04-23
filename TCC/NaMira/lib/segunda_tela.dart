import 'package:flutter/material.dart';
import 'mapa.dart';
import 'sobrenos.dart';
import 'dicas.dart';

class SegundaTela extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Todos Juntos Contra a Dengue'),
      ),
      body: Container(
        decoration: BoxDecoration(
          image: DecorationImage(
            image: AssetImage('assets/images/principal_branco.jpg'),
            fit: BoxFit.cover,
          ),
        ),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              buildButton(context, 'Mapa', Colors.blue, () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => MapaScreen()),
                );
              }),
              SizedBox(height: 10), // Espaço entre os botões
              buildButton(context, 'Dicas', Colors.blue, () {
                // Implementação de navegação para 'Dicas'
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => Dicas()),
                );
              }),
              SizedBox(height: 10), // Espaço entre os botões
              buildButton(context, 'Sobre Nós', Colors.blue, () {
                // Implementação de navegação para 'Sobre Nós'
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => SobreNos()),
                );
              }),
            ],
          ),
        ),
      ),
    );
  }

  Widget buildButton(
      BuildContext context, String text, Color color, VoidCallback onPressed) {
    return Container(
      width: double.infinity,
      padding: EdgeInsets.symmetric(horizontal: 16),
      child: ElevatedButton(
        onPressed: onPressed,
        child: Text(text),
        style: ElevatedButton.styleFrom(
          backgroundColor: color,
          foregroundColor: Colors.white,
          elevation: 0,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8),
          ),
          padding: EdgeInsets.symmetric(vertical: 20),
        ),
      ),
    );
  }
}
