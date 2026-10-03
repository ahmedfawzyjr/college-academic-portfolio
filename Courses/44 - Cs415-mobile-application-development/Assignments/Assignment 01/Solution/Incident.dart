class Incident {
  final String id;
  final String title;
  final String description;
  final double latitude;
  final double longitude;
  final DateTime timestamp;

  Incident({
    required this.id,
    required this.title,
    required this.description,
    required this.latitude,
    required this.longitude,
    required this.timestamp,
  });

  factory Incident.fromJson(Map<String, dynamic> json) {
    return Incident(
      id: json['id'] as String,
      title: json['title'] as String,
      description: json['description'] as String,
      latitude: (json['latitude'] as num).toDouble(),
      longitude: (json['longitude'] as num).toDouble(),
      timestamp: DateTime.parse(json['timestamp'] as String),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'title': title,
      'description': description,
      'latitude': latitude,
      'longitude': longitude,
      'timestamp': timestamp.toIso8601String(),
    };
  }
}

void main() {
  final sampleJson = {
    'id': 'INC-101',
    'title': 'Traffic Delay',
    'description': 'Minor congestion on highway',
    'latitude': 30.0444,
    'longitude': 31.2357,
    'timestamp': '2026-09-11T12:00:00Z',
  };

  final incident = Incident.fromJson(sampleJson);
  print("Parsed Incident: ${incident.title} (${incident.latitude}, ${incident.longitude})");
}
