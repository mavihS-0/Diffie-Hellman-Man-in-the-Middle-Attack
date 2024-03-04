import socket
import random


p = int(input('Enter a prime number : '))
g = int(input('Enter a number : '))

class B:
	def __init__(self):
		# Generating a random private number selected for alice
		self.a = random.randint(1, p)
		# Generating a random private number selected for bob
		self.b = random.randint(1, p)
		self.arr = [self.a,self.b]

	def publish(self, i):
		# generating public values
		return (g**self.arr[i])%p

	def compute_secret(self, ga, i):
		# computing secret key
		return (ga**self.arr[i])%p

def start_client(gea):
    # Define the server address
    server_address = ('localhost', 12345)

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(server_address)
    received_number = 0

    try:
        # Send a number to the server
        print(f"Sending number to server: {gea}")
        client_socket.sendall(str(gea).encode('utf-8'))

        # Receive a number from the server
        data = client_socket.recv(1024)
        received_number = int(data.decode('utf-8'))
        print(f"Received number from server: {received_number}")

    finally:
        # Clean up the connection
        client_socket.close()
        return received_number
	
def start_server(geb):
    # Define the server address (empty string means any available interface)
    server_address = ('localhost', 12345)

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address
    server_socket.bind(server_address)

    # Listen for incoming connections (maximum 1 connection in this example)
    server_socket.listen(1)

    print(f"Server is listening on {server_address}")

    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
	
    received_number = 0
	
    try:
        # Receive a number from the client
        data = client_socket.recv(1024)
        received_number = int(data.decode('utf-8'))
        print(f"Received number from client: {received_number}")

        # Send a number back to the client
        print(f"Sending number to client: {geb}")
        
        client_socket.sendall(str(geb).encode('utf-8'))
		

    finally:
        # Clean up the connection
        client_socket.close()
        server_socket.close()
        return received_number

eve = B()
# Printing out the private selected number 
print(f'Eve selected private number for Alice (c) : {eve.a}')
# Generating public value
gea = eve.publish(0)
print(f'Eve published value for Alice (gc): {gea}')
ga = start_client(gea)
# Computing the secret key
sea = eve.compute_secret(ga,0)
print(f'Eve computed key for Alice (S1) : {sea}')
# Printing out the private selected number
print(f'Eve selected private number for Bob (d) : {eve.b}')
# Generating public value
geb = eve.publish(1)
print(f'Eve published value for Bob (gd): {geb}')
gb = start_server(geb)
# Computing the secret key
seb = eve.compute_secret(gb,1)
print(f'Eve computed key for Bob (S2) : {seb}')



