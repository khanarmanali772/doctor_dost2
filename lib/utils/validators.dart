class Validators {
  static String? isEmail(String? value) {
    if (value == null || !value.contains('@')) {
      return "Enter valid email";
    }
    return null;
  }
}
