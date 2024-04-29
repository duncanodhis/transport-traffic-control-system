import 'package:flutter/material.dart';

class TrafficAlertWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Icon(Icons.warning, color: Colors.red),
        Text('Traffic Alert: Heavy traffic on Main Street'),
      ],
    );
  }
}
