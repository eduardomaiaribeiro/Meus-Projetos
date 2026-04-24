import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:io' if (dart.library.html) 'src/noop_file.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

Future<void> main() async {
  await dotenv.load();
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // TRY THIS: Try running your application with "flutter run". You'll see
        // the application has a purple toolbar. Then, without quitting the app,
        // try changing the seedColor in the colorScheme below to Colors.green
        // and then invoke "hot reload" (save your changes or press the "hot
        // reload" button in a Flutter-supported IDE, or press "r" if you used
        // the command line to start the app).
        //
        // Notice that the counter didn't reset back to zero; the application
        // state is not lost during the reload. To reset the state, use hot
        // restart instead.
        //
        // This works for code too, not just values: Most code changes can be
        // tested with just a hot reload.
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {      
      Future<void> _gerarDesculpaEsposa() async {
        final prompt = "Crie uma desculpa esfarrapada, extremamente criativa, muito bem elaborada, com tom de sarcasmo e muita ironia, para dar para minha esposa. Responda em português. Seja ousado, engraçado e surpreendente.";
        await _gerarJargao(promptPersonalizado: prompt);
      }
    void _copiarResultado() {
      if (_resultado != null && _resultado!.isNotEmpty) {
        Clipboard.setData(ClipboardData(text: _resultado!));
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('Conteúdo copiado!')),
        );
      }
    }
  void _limparCampos() {
    setState(() {
      _controller.clear();
      _resultado = null;
    });
  }

  final TextEditingController _controller = TextEditingController();
  String? _resultado;
  bool _loading = false;

  Future<void> _gerarJargao({String? promptPersonalizado}) async {
    final tema = promptPersonalizado ?? _controller.text.trim();
    if (tema.isEmpty) return;
    setState(() {
      _loading = true;
      _resultado = null;
    });

    try {
      final apiKey = dotenv.env['IA_API_KEY'];
      if (apiKey == null) {
        setState(() {
          _resultado = 'Configuração da IA não encontrada. Verifique o arquivo .env.';
          _loading = false;
        });
        return;
      }
      // Use o modelo e endpoint recomendados para v1beta
      const model = 'gemini-flash-latest'; // ou 'gemini-pro-latest'
      final apiUrl = 'https://generativelanguage.googleapis.com/v1beta/models/$model:generateContent?key=$apiKey';
      final response = await http.post(
        Uri.parse(apiUrl),
        headers: {
          'Content-Type': 'application/json',
        },
        body: jsonEncode({
          'contents': [
            {
              'parts': [
                {'text': tema}
              ]
            }
          ],
          'generationConfig': {
            'maxOutputTokens': 512,
            'temperature': 0.7,
          },
        }),
      );

        // Para depuração: imprime o conteúdo completo do response.body no console
        print('Gemini response: ' + response.body);

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        final parts = data['candidates']?[0]?['content']?['parts'] as List?;
        String textoGerado = '';
        if (parts != null && parts.isNotEmpty) {
          textoGerado = parts.map((p) => p['text'] ?? '').join(' ').trim();
        } else {
          textoGerado = 'Não foi possível gerar uma frase.';
        }
        setState(() {
          _resultado = textoGerado;
          _loading = false;
        });
      } else {
        setState(() {
          _resultado = 'Erro ao gerar frase: ${response.statusCode}';
          _loading = false;
        });
      }
    } catch (e) {
      setState(() {
        _resultado = 'Erro ao conectar com a IA: $e';
        _loading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: const Text('Gerador de Desculpas Esfarrapadas'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            TextField(
              controller: _controller,
              decoration: const InputDecoration(
                labelText: 'Digite uma frase ou tema',
                border: OutlineInputBorder(),
              ),
              minLines: 1,
              maxLines: 3,
              keyboardType: TextInputType.multiline,
              textInputAction: TextInputAction.newline,
              enableSuggestions: true,
              autocorrect: true,
              // O TextField do Flutter já aceita acentuação, mas garantimos que não há restrições
              // Caso esteja testando em emulador ou dispositivo físico, verifique o teclado do sistema
            ),
            const SizedBox(height: 16),
            Row(
              children: [
                Expanded(
                  child: ElevatedButton(
                    onPressed: _loading ? null : _gerarJargao,
                    child: _loading
                        ? const SizedBox(height: 20, width: 20, child: CircularProgressIndicator(strokeWidth: 2))
                        : const Text('Corporativa'),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: ElevatedButton(
                    onPressed: _loading ? null : _gerarDesculpaEsposa,
                    style: ElevatedButton.styleFrom(backgroundColor: Colors.pink[100]),
                    child: const Text('Esposa', style: TextStyle(color: Colors.black)),
                  ),
                ),
                const SizedBox(width: 12),
                ElevatedButton(
                  onPressed: _limparCampos,
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.grey[300]),
                  child: const Text('Limpar', style: TextStyle(color: Colors.black)),
                ),
              ],
            ),
            const SizedBox(height: 32),
            if (_resultado != null)
              Card(
                color: Colors.grey[100],
                child: Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      Text(
                        _resultado!,
                        style: const TextStyle(fontSize: 16),
                      ),
                      const SizedBox(height: 12),
                      ElevatedButton.icon(
                        onPressed: _copiarResultado,
                        icon: const Icon(Icons.copy, size: 18),
                        label: const Text('Copiar'),
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.deepPurple[100],
                          foregroundColor: Colors.black,
                          padding: const EdgeInsets.symmetric(vertical: 10),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
          ],
        ),
      ),
    );
  }
}
