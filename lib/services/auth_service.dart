import '../models/user_model.dart';

class AuthService {
  Future<UserModel?> login(String email, String password) async {
    await Future.delayed(const Duration(seconds: 1));

    if (email == "test@gmail.com" && password == "123456") {
      return UserModel(
        id: "1",
        name: "Test User",
        email: email,
      );
    }
    return null;
  }

  Future<UserModel> signup(String name, String email, String password) async {
    await Future.delayed(const Duration(seconds: 1));

    return UserModel(
      id: DateTime.now().millisecondsSinceEpoch.toString(),
      name: name,
      email: email,
    );
  }
}
