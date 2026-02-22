#include <WiFi.h>

const char* ssid = "AsadNet";
const char* password = "asad123";

const char* serverIP = "192.168.1.5";  // Laptop IP
const uint16_t serverPort = 5000;      // TCP server port

WiFiClient client;

const int relayPin = 5;  // Change to your relay GPIO

void setup() {
  Serial.begin(115200);

  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, LOW);  // Start OFF

  // Connect to WiFi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected to WiFi");
  Serial.print("ESP IP: ");
  Serial.println(WiFi.localIP());

  // Connect to TCP server
  Serial.println("Connecting to TCP server...");

  if (client.connect(serverIP, serverPort)) {
    Serial.println("Connected to server");
  } else {
    Serial.println("Connection failed");
  }
}

void loop() {

  // If connection lost, try reconnecting
  if (!client.connected()) {
    Serial.println("Reconnecting...");
    client.connect(serverIP, serverPort);
    delay(1000);
    return;
  }

  // Check if data available
  if (client.available()) {

    String command = client.readStringUntil('\n');
    command.trim();   // Remove spaces/newlines

    Serial.print("Received: ");
    Serial.println(command);

    if (command == "ON") {
      digitalWrite(relayPin, HIGH);
      Serial.println("Relay ON");
    }

    else if (command == "OFF") {
      digitalWrite(relayPin, LOW);
      Serial.println("Relay OFF");
    }
  }
}