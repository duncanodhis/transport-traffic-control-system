import 'package:flutter/material.dart';
import '../widgets/custom_navigation_bar.dart';
import '../widgets/traffic_alert_widget.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Transport Control System'),
      ),
      bottomNavigationBar: CustomNavigationBar(),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Welcome to the Transport Control System!'),
            SizedBox(height: 20),
            TrafficAlertWidget(),
          ],
        ),
      ),
    );
  }
}
