import 'package:flutter/material.dart';
import 'screens/home_screen.dart';
import 'screens/auth/login_screen.dart';
import 'screens/auth/signup_screen.dart';

class Routes {
  Routes._();
  static const String home = '/';
  static const String login = '/login';
  static const String signup = '/signup';
}

final Map<String, WidgetBuilder> appRoutes = {
  Routes.home: (context) => const HomeScreen(),
  Routes.login: (context) => const LoginScreen(),
  Routes.signup: (context) => const SignupScreen(),
};
