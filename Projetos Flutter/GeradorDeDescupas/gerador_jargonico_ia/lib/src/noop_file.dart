// Fallback para dart:io em Flutter web
class File {
  File(String path);
  Future<void> writeAsString(String _) async {}
}