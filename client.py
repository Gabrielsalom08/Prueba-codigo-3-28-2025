import socket


def start_client():
    host = '127.0.0.1'
    port = 5000
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Conectado al servidor en {host}:{port}")
    
    while True:
        message = input("Ingrese un mensaje: ")
        client_socket.send(message.encode())
        
        if message.strip().upper() == "DESCONEXION":
            print("Desconectando del servidor...")
            client_socket.close()
            break
        
        response = client_socket.recv(1024).decode()
        print(f"Respuesta del servidor: {response}")
        
if __name__ == "__main__":
        start_client()
