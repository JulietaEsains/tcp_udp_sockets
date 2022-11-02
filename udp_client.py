import socket

# constructor del socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# envía directamente el mensaje al servidor, sin conectarse
client.sendto('¿Cuántos clientes han enviado un mensaje?'.encode('utf-8'), ('localhost', 9999))

# recibe la respuesta del servidor
print(client.recvfrom(1024)[0].decode('utf-8'))

