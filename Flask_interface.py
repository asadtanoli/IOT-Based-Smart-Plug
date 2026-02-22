from flask import Flask, render_template_string #it imports flask and HTML template so no seperate html file
#is written
import socket

# ----- Flask app setup -----
app = Flask(__name__)

# ----- TCP client to talk to the ESP or TCP server -----
HOST = "10.254.146.110"  # IP of your server (your PC)
PORT = 5000               # Port of TCP server

# Create socket and connect to TCP server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# ----- HTML template for web page -----
html_template = """
<!doctype html>
<html>
<head>
    <title>IoT Smart Plug</title>
</head>
<body>
    <h1>Smart Plug Control</h1>
    <form action="/on">
        <button type="submit">Turn ON</button>
    </form>
    <form action="/off">
        <button type="submit">Turn OFF</button>
    </form>
</body>
</html>
"""

# ----- Flask routes -----
@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/on')
def turn_on():
    client.send(b'ON\n')
    return "<h2>Turned ON</h2><a href='/'>Back</a>"

@app.route('/off')
def turn_off():
    client.send(b'OFF\n')
    return "<h2>Turned OFF</h2><a href='/'>Back</a>"

# ----- Run Flask -----
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)