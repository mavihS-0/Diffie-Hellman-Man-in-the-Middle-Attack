import socket
import random

p = int(input('Enter a prime number : '))
g = int(input('Enter a number : '))

class A:
	def __init__(self):
		# Generating a random private number selected by alice
		self.n = random.randint(1, p)	 

	def publish(self):
		# generating public values
		return (g**self.n)%p

	def compute_secret(self, gb):
		# computing secret key
		return (gb**self.n)%p

def start_client(gb):
    # Define the server address
    server_address = ('localhost', 12345)

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(server_address)
    received_number = 0

    try:
        # Send a number to the server
        print(f"Sending number to server: {gb}")
        client_socket.sendall(str(gb).encode('utf-8'))

        # Receive a number from the server
        data = client_socket.recv(1024)
        received_number = int(data.decode('utf-8'))
        print(f"Received number from server: {received_number}")

    finally:
        # Clean up the connection
        client_socket.close()
        return received_number
	
bob = A()
# Printing out the private selected number
print(f'Bob selected (b) : {bob.n}')
# Generating public values
gb = bob.publish()
print(f'Bob published (gb): {gb}')
geb = start_client(gb)
# Computing the secret key
sb = bob.compute_secret(geb)
print(f'Bob computed (S2) : {sb}')
