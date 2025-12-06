// test/widget_test.dart
import 'package:flutter_test/flutter_test.dart';
import 'package:doctor_dost/app.dart';

void main() {
  testWidgets('App builds without crashing', (WidgetTester tester) async {
    await tester.pumpWidget(const DoctorDostApp());
    expect(find.byType(DoctorDostApp), findsOneWidget);
  });
}
