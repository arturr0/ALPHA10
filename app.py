import os
from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
# Use async_mode='threading' to support async mode with gevent on Heroku
socketio = SocketIO(app, async_mode='threading')

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

# Use os.environ.get('PORT') to get the port provided by Heroku
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Use 0.0.0.0 to bind to all available interfaces
    socketio.run(app, host='0.0.0.0', port=port, debug=True)
