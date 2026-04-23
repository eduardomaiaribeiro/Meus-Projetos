import 'package:flutter/material.dart';

class Dicas extends StatelessWidget {
  final List<Map<String, dynamic>> dicas = [
    {
      'title': 'Eliminar água parada',
      'description': 'Remova água parada em pneus, garrafas e vasos de plantas para evitar a criação de mosquitos.',
      'image': 'assets/images/agua_parada.jpg'
    },
    {
      'title': 'Usar repelente',
      'description': 'Aplique repelente regularmente para proteger contra picadas de mosquito.',
      'image': 'assets/images/repelente.jpg'
    },
    {
      'title': 'Sintomas da Dengue',
      'description': 'Os sintomas incluem febre alta, dor de cabeça severa, dor atrás dos olhos, fadiga, náusea e erupções cutâneas.',
      'image': 'assets/images/sintomas_dengue.jpg'
    },
    {
      'title': 'Cuidados ao tratar a Dengue',
      'description': 'Mantenha-se hidratado, repouse bastante e use medicamentos antipiréticos sob orientação médica. Evite aspirina.',
      'image': 'assets/images/cuidados_dengue.jpg'
    },
    {
      'title': 'Prevenção de picadas',
      'description': 'Use roupas de manga longa, calças compridas e repelente para evitar picadas de mosquito.',
      'image': 'assets/images/prevencao_picadas.jpg'
    },
    {
      'title': 'Evitar acúmulo de água',
      'description': 'Mantenha recipientes como baldes e caixas d\'água sempre tampados para evitar o acúmulo de água parada.',
      'image': 'assets/images/acumulo_agua.jpg'
    },
    {
      'title': 'Limpar calhas e ralos',
      'description': 'Realize a limpeza regular das calhas e ralos para evitar o acúmulo de água parada.',
      'image': 'assets/images/limpar_calhas.jpg'
    },
    {
      'title': 'Cuidados com piscinas',
      'description': 'Mantenha a piscina sempre limpa e com tratamento adequado para evitar a proliferação de mosquitos.',
      'image': 'assets/images/cuidados_piscinas.jpg'
    },
    {
      'title': 'Evitar horários de pico',
      'description': 'Evite sair de casa nos horários de pico dos mosquitos, que são ao amanhecer e ao entardecer.',
      'image': 'assets/images/horarios_pico.jpg'
    },    
    {
      'title': 'Uso de mosquiteiros',
      'description': 'Utilize mosquiteiros nas camas e berços para evitar picadas de mosquitos durante o sono.',
      'image': 'assets/images/mosquiteiros.jpg'
    },
    {
      'title': 'Cuidados com gestantes',
      'description': 'Gestantes devem redobrar os cuidados para evitar picadas de mosquitos, pois algumas doenças podem ser transmitidas ao feto.',
      'image': 'assets/images/cuidados_gestantes.jpg'
    },
    {
      'title': 'Descarte adequado de lixo',
      'description': 'Descarte o lixo de forma adequada, evitando que se torne um local propício para a proliferação de mosquitos.',
      'image': 'assets/images/descarte_lixo.jpg'
    },
    {
      'title': 'Cuidados com animais',
      'description': 'Mantenha os animais domésticos protegidos contra mosquitos, utilizando repelentes específicos para pets.',
      'image': 'assets/images/cuidados_animais.jpg'
    },
    {
      'title': 'Informar autoridades',
      'description': 'Em caso de suspeita de focos de mosquitos, informe as autoridades de saúde para que possam tomar as devidas providências.',
      'image': 'assets/images/informar_autoridades.jpg'
    }  
    // Adicione mais dicas conforme necessário
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Dicas sobre Dengue"),
      ),
      body: ListView.builder(
        itemCount: dicas.length,
        itemBuilder: (context, index) {
          return Card(
            child: ListTile(
              leading: Image.asset(dicas[index]['image'], width: 100),  // Certifique-se que as imagens são adequadas para a exibição.
              title: Text(dicas[index]['title']),
              subtitle: Text(dicas[index]['description']),
            ),
          );
        },
      ),
    );
  }
}
