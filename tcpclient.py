import socket

def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print("Connected to the server.")

        while True:
            expression = input("Enter an arithmetic expression (e.g., 5 + 3 or 'exit' to quit): ")
            if expression.lower() == 'exit':
                print("Closing connection.")
                break
            client_socket.sendall(expression.encode('utf-8'))
            data = client_socket.recv(1024)
            print(f"Server response: {data.decode('utf-8')}")

if __name__ == "__main__":
    start_client()