import asyncio
import websockets
from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

connected = set()

@socketio.on('message')
def handle_message(message):
    print('Received message:', message)
    for conn in connected:
        socketio.emit('message', f'Got a new MSG FOR YOU: {message}', room=conn)

@socketio.on('connect')
def handle_connect():
    connected.add(request.sid)
    print('Client connected:', request.sid)

@socketio.on('disconnect')
def handle_disconnect():
    connected.remove(request.sid)
    print('Client disconnected:', request.sid)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, port=5000, debug=True)
