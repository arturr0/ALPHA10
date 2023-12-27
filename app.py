import os
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print('Received message:', msg)
    socketio.emit('message', msg)

if __name__ == '__main__':
    # Use eventlet or gevent as the production server
    # For Heroku, it's common to use eventlet
    import eventlet
    eventlet.monkey_patch()

    # Run the application with SocketIO
    socketio.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
