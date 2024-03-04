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
      

def start_server(ga):
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
        print(f"Sending number to client: {ga}")
        
        client_socket.sendall(str(ga).encode('utf-8'))
		

    finally:
        # Clean up the connection
        client_socket.close()
        server_socket.close()
        return received_number
		

alice = A()
# Printing out the private selected number
print(f'Alice selected (a) : {alice.n}')
# Generating public values 
ga = alice.publish()
print(f'Alice published (ga): {ga}')
gea = start_server(ga)
# Computing the secret key
sa = alice.compute_secret(gea)
print(f'Alice computed (S1) : {sa}')
