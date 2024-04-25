
from flask import Flask
from flask_socketio import SocketIO, emit

a = random.randint(1, 100) # This should be randomly generated in a real scenario

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')

def modular_pow(base, exponent, modulus):
    """Perform modular exponentiation using a base, exponent, and modulus."""
    return int(math.pow(base,exponent)) % modulus 

@socketio.on('connect')
def handle_connect():
    emit('notification', 'You are now connected!')
    a = random.randint(1, 100)  # This should be randomly generated in a real scenario
    A = modular_pow(5, a, 23)  # Server's public key
    # Send A to the client
    emit('data', str(A))

@socketio.on('message')
def handle_message(data):
    message = data['message']
    S = modular_pow(int(message), a, 23)
    emit('data',"Server's shared secret:" + S)


if __name__ == '__main__':
    socketio.run(app)