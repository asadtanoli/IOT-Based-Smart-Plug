# IOT-Based-Smart-Plug
This project implements a Wi-Fi based smart plug using an ESP32, Python socket programming, and a Flask web interface to remotely control electrical appliances.

The system follows a three-layer architecture:

Browser → Flask Web App → TCP Socket Server → ESP32 → Relay → Appliance.

The ESP32 connects to a local Wi-Fi network and establishes a TCP connection with a Python server (port 5000).
A Flask web app (port 8000) provides ON/OFF buttons in the browser.
When a user clicks a button, Flask sends a TCP command (ON / OFF) to the socket server.
The ESP32 reads the command and toggles a relay connected to the appliance.

Technologies Used:

ESP32 (Embedded C / Arduino IDE)

Python (Socket Programming)

Flask (Web Interface)

TCP/IP Networking
