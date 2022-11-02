import socket

# constructor del socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# se vincula a una dirección IP y a un puerto
server.bind(('localhost', 9999))

# almacena el número de veces que un cliente se ha conectado a este servidor
client_messages = 0

while True:
    # espera un mensaje de cualquier cliente
    message, address = server.recvfrom(1024)
    print(message.decode('utf-8'))

    # aumenta el número de "conexiones"
    client_messages += 1

    # envía la información al último cliente
    server.sendto(f'He recibido {client_messages} mensajes.'.encode('utf-8'), address)

    