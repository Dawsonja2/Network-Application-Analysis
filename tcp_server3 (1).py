import socket
import string

def process_string(sentence, options):
    result = []
    if 1 in options:
        result.append(sentence.upper())
    if 2 in options:
        result.append(sentence.lower())
    if 3 in options:
        result.append(str(len(sentence)))
    if 4 in options:
        count = 0
        vowels = "aeiouAEIOU"
        for char in sentence:
            if char in vowels:
                count += 1
        result.append(str(count))
    if 5 in options:
        words = sentence.split()
        result.append(str(len(words)))
    return result

server_port = 12010

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', server_port))
server.listen(1)
print("The server is ready to receive")
while 1:
    print("Waiting ...")
    connection_socket, addr = server.accept()
    print("accept")
    sentence = connection_socket.recv(2048).decode()
    options = list(map(int, connection_socket.recv(2048).decode().split()))
    print("Message Received: " + sentence)
    result = process_string(sentence, options)
    connection_socket.send('\n'.join(result).encode())
    connection_socket.close()