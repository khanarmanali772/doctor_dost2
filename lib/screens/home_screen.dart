// lib/screens/home_screen.dart
import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold( // <- removed `const` here
      appBar: AppBar(title: const Text('Home')),
      body: const Center(child: Text('Welcome to Doctor Dost')),
    );
  }
}
