import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:webview_flutter/webview_flutter.dart';

/// Bulgarca Rehber: uygulama içeriği assets/web/index.html'dedir (internetsiz çalışır).
void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(const RehberApp());
}

class RehberApp extends StatelessWidget {
  const RehberApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Bulgarca Rehber',
      debugShowCheckedModeBanner: false,
      home: RehberPage(),
    );
  }
}

class RehberPage extends StatefulWidget {
  const RehberPage({super.key});
  @override
  State<RehberPage> createState() => _RehberPageState();
}

class _RehberPageState extends State<RehberPage> {
  late final WebViewController controller;

  @override
  void initState() {
    super.initState();
    controller = WebViewController()
      ..setJavaScriptMode(JavaScriptMode.unrestricted)
      ..setBackgroundColor(const Color(0xFFF4F6F3))
      ..loadFlutterAsset('assets/web/index.html');
  }

  Future<void> _back() async {
    if (await controller.canGoBack()) {
      await controller.goBack();
    } else {
      await SystemNavigator.pop();
    }
  }

  @override
  Widget build(BuildContext context) {
    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, _) {
        if (!didPop) _back();
      },
      child: Scaffold(
        backgroundColor: const Color(0xFFF4F6F3),
        body: SafeArea(child: WebViewWidget(controller: controller)),
      ),
    );
  }
}
