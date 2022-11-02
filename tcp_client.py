import socket

# constructor del socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# se conecta a la misma dirección donde está el servidor
client.connect(('localhost', 9999))

# envía un mensaje al servidor y espera una respuesta
client.send('Solicito la fecha y la hora actual.'.encode('utf-8'))
print(client.recv(1024).decode('utf-8'))

# envía un último mensaje
client.send('Desconectando.'.encode('utf-8'))
print(client.recv(1024).decode('utf-8'))

