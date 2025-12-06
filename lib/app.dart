import 'package:flutter/material.dart';
import 'routes.dart';

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Doctor Dost',
      debugShowCheckedModeBanner: false,
      initialRoute: Routes.home,
      routes: appRoutes,
      theme: ThemeData(primarySwatch: Colors.blue),
    );
  }
}

class DoctorDostApp extends StatelessWidget {
  const DoctorDostApp({super.key});
  @override
  Widget build(BuildContext context) => const MyApp();
}
