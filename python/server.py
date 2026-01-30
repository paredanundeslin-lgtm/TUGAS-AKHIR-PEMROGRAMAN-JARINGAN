from flask import Flask, request, jsonify
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def on_message(client, userdata, msg):
    suhu = msg.payload.decode()
    print("Terima:", suhu)
    socketio.emit("suhu", {"nilai": suhu})

client = mqtt.Client()
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.subscribe("kampus/pj/suhu")
client.loop_start()

@app.route("/login", methods=["POST"])
def login():
    d = request.json
    if d["username"] == "admin" and d["password"] == "123":
        return jsonify({"status":"ok"})
    return jsonify({"status":"fail"})

if __name__ == "__main__":
    socketio.run(app, port=5000)