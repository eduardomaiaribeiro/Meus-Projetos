import 'package:flutter/material.dart';

class SobreNos extends StatelessWidget {
  final List<Map<String, String>> developers = [
    {
      'name': 'Alexandre Garcia Bezerra',
      'summary': 'Desenvolvedor de software com foco em soluções móveis.',
      'image': 'assets/images/alexandre.jpg'  // Certifique-se de ter esta imagem em assets/images
    },
    {
      'name': 'Eduardo Maia Ribeiro',
      'summary': 'Especialista em back-end e infraestrutura.',
      'image': 'assets/images/eduardo.jpg'
    },
    {
      'name': 'Guilherme José de Moraes',
      'summary': 'Especialista em front-end e UI/UX design.',
      'image': 'assets/images/guilherme.jpg'
    },
    {
      'name': 'Jackson Aparecido de Souza',
      'summary': 'Desenvolvedor full-stack com experiência em bancos de dados.',
      'image': 'assets/images/jackson.jpg'
    },
    {
      'name': 'Jeferson Matsuji Matsui',
      'summary': 'Engenheiro de software com conhecimento em arquitetura de sistemas.',
      'image': 'assets/images/jeferson.jpg'
    },
    {
      'name': 'José Marcelino Neto',
      'summary': 'Desenvolvedor mobile com experiência em desenvolvimento nativo.',
      'image': 'assets/images/jose.jpg'
    },
    {
      'name': 'Lilian Sampaio Souza Machado',
      'summary': 'Especialista em testes de software e qualidade.',
      'image': 'assets/images/lilian.jpg'
    }
    // Adicione todos os desenvolvedores seguindo o mesmo padrão
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Sobre Nós"),
      ),
      body: ListView.builder(
        itemCount: developers.length,
        itemBuilder: (context, index) {
          return ListTile(
            leading: CircleAvatar(
              backgroundImage: AssetImage(developers[index]['image']!),
            ),
            title: Text(developers[index]['name']!),
            subtitle: Text(developers[index]['summary']!),
          );
        },
      ),
    );
  }
}
