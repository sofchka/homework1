import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("127.0.0.1", 9999))

server_socket.listen(1)

print("Loading...")

client_socket, client_address = server_socket.accept()

print(f"Connection: {client_address}")

while True:
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break
    print(f"Client: {data}")
    ans = input("You: ")
    client_socket.send(ans.encode('utf-8'))

client_socket.close()
server_socket.close()
