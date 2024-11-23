import socket

def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        print("UDP Client started.")

        while True:
            expression = input("Enter an arithmetic expression (e.g., 5 + 3 or 'exit' to quit): ")
            if expression.lower() == 'exit':
                print("Exiting...")
                break
            client_socket.sendto(expression.encode('utf-8'), (host, port))
            data, _ = client_socket.recvfrom(1024)
            print(f"Server response: {data.decode('utf-8')}")

if __name__ == "__main__":
    start_client()