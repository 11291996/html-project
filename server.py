import socket

server_socket = socket.socket()
server_socket.bind((str(socket.gethostbyname(socket.gethostname())), 1234))
server_socket.listen()

while True:    
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Parse HTTP headers
    headers = request.split('\n')
    filename = headers[0].split()[1]

    # Get the content of the file
    if filename == '/':
        filename = '/index.html'

    fin = open('.' + filename)
    content = fin.read()
    fin.close()
    
    """
    # Get the content of htdocs/index.html
    fin = open('./index.html')
    content = fin.read()
    fin.close()
    """

    # Send HTTP response
    response = 'HTTP/1.0 200 OK\n\n' + content
    client_connection.sendall(response.encode())

# Close socket
server_socket.close()