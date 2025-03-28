# server.py
import socket

def start_server():
    host = '127.0.0.1'
    port = 5000
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Servidor escuchando en {host}:{port}")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexión establecida con {client_address}")
        
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Cliente envió: {message}")
            
            if message.strip().upper() == "DESCONEXION":
                print("Cliente solicitó desconexión.")
                client_socket.close()
                break
            elif message.strip().upper() == "TERMINAR SERVIDOR":
                print("Servidor cerrando...")
                client_socket.close()
                server_socket.close()
                return
            else:
                response = message.upper()
                
            client_socket.send(response.encode())


if __name__ == "__main__":
        start_server()
