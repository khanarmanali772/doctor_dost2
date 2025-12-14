// lib/config/theme.dart
import 'package:flutter/material.dart';

class AppColors {
  static const primary = Color(0xFF6C4CF5); // purple
  static const bg = Color(0xFFFDF5F9); // soft pink-ish
  static const card = Color(0xFFFAF7FF);
  static const accent = Color(0xFF8B6BFF);
  static const muted = Color(0xFF9E9EA7);
  static const surface = Color(0xFFFFFFFF);
}

ThemeData buildAppTheme() {
  final colorScheme = ColorScheme.fromSeed(seedColor: AppColors.primary).copyWith(
    primary: AppColors.primary,
    secondary: AppColors.accent,
    surface: AppColors.surface, // use surface instead of background
  );

  return ThemeData(
    brightness: Brightness.light,
    scaffoldBackgroundColor: AppColors.bg,
    primaryColor: AppColors.primary,
    colorScheme: colorScheme,
    appBarTheme: const AppBarTheme(
      elevation: 0,
      centerTitle: false,
      foregroundColor: Colors.black87,
      backgroundColor: AppColors.bg,
      titleTextStyle: TextStyle(fontSize: 20, fontWeight: FontWeight.w600, color: Colors.black87),
    ),
    // Removed cardTheme because your SDK expects a different CardTheme type.
    cardColor: AppColors.card,
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: AppColors.primary,
        foregroundColor: Colors.white,
        elevation: 0,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
        padding: const EdgeInsets.symmetric(vertical: 14, horizontal: 18),
      ),
    ),
    textTheme: const TextTheme(
      headlineSmall: TextStyle(fontSize: 22, fontWeight: FontWeight.w700),
      titleMedium: TextStyle(fontSize: 16, fontWeight: FontWeight.w600),
      bodyMedium: TextStyle(fontSize: 14),
      labelLarge: TextStyle(fontSize: 14, fontWeight: FontWeight.w600),
    ),
    inputDecorationTheme: InputDecorationTheme(
      filled: true,
      fillColor: AppColors.surface,
      contentPadding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
      border: OutlineInputBorder(borderRadius: BorderRadius.circular(12), borderSide: BorderSide.none),
    ),
  );
}
