import socket

server_name = '127.0.0.1'
server_port = 12010

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((server_name, server_port))

sentence = input('Input string: ')
options = list(map(int, input('Options (separated by space): ').split()))

client.send(sentence.encode())
client.send(' '.join(str(x) for x in options).encode())

modifiedSentence = client.recv(2048)

print('\n'.join(modifiedSentence.decode().split('\n')))
client.close()
