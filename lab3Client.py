import socket
import random
import math
#34.217.64.132
def client(server_host='http://34.217.64.132/rsa', server_port=12345, p=23, g=5):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    print("got here")
    # Client's private key (b)
    b = random.randint(1, 100)  # This should be randomly generated in a real scenario
    B = modular_pow(g, b, p)  # Client's public key

    # Send B to the server
    client_socket.sendall(str(B).encode())

    # Receive A from the server
    A = int(client_socket.recv(1024).decode())

    # Compute shared secret
    S = modular_pow(A, b, p)
    print("Client's shared secret:", S)

    client_socket.close()

def modular_pow(base, exponent, modulus):
    """Perform modular exponentiation using a base, exponent, and modulus."""
    return int(math.pow(base,exponent)) % modulus 


client()