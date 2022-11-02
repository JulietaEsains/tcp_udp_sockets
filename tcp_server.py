import socket
from datetime import datetime

# constructor del socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# se vincula a una dirección IP y a un puerto
server.bind(('localhost', 9999))

# escucha conexiones entrantes
server.listen()

# almacena la fecha y hora actuales
data = datetime.now()

while True:
    # almacena la dirección del cliente conectado
    client, address = server.accept()
    print(f'Conectado a {address}.')

    # espera recibir un mensaje del cliente
    print(client.recv(1024).decode('utf-8'))

    # envía un mensaje al cliente
    client.send(f'Fecha y hora actuales: {data}'.encode('utf-8'))

    print(client.recv(1024).decode('utf-8'))
    client.send('Desconectando.'.encode('utf-8'))

    # se cierra la conexión
    client.close()

    