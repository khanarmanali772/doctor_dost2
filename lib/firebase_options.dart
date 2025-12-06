// File: lib/firebase_options.dart

import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/foundation.dart';

class DefaultFirebaseOptions {
  static FirebaseOptions get currentPlatform {
    if (kIsWeb) {
      return web;
    } else {
      return android;
    }
  }

  // 👉 WEB CONFIG
  static const FirebaseOptions web = FirebaseOptions(
    apiKey: "AIzaSyDNbccC11DDSupPjJzZoQChPpgvnPhoAvK4",
    authDomain: "doctor-dost2.firebaseapp.com",
    projectId: "doctor-dost2",
    storageBucket: "doctor-dost2.firebasestorage.app",
    messagingSenderId: "347260024328",
    appId: "1:347260024328:web:a2e2de4e90880ad9be403bd",
    measurementId: "G-7KLZWLMRWN",
  );

  // 👉 ANDROID CONFIG (json se liya hua)
  static const FirebaseOptions android = FirebaseOptions(
    apiKey: "AIzaSyCmn0eung6oUHjrabBhc_7_EvGl_LNLv5y",
    appId: "1:347260024328:android:1cb953dc745c26f2e403bd",
    messagingSenderId: "347260024328",
    projectId: "doctor-dost2",
    storageBucket: "doctor-dost2.firebasestorage.app",
  );
}
