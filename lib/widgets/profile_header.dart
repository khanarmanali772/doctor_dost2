// lib/widgets/profile_header.dart
import 'package:flutter/material.dart';

class ProfileHeader extends StatelessWidget {
  const ProfileHeader({super.key});

  @override
  Widget build(BuildContext context) {
    return const Padding(
      padding: EdgeInsets.all(12.0),
      child: Row(
        children: [
          CircleAvatar(
            radius: 30,
            child: Icon(Icons.person),
          ),
          SizedBox(width: 12),
          Text(
            'Your Name',
            style: TextStyle(fontSize: 18),
          ),
        ],
      ),
    );
  }
}
