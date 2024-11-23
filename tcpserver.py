import socket

def calculate(expression):
    try:
        # Split the expression into operands and operator
        parts = expression.split()
        if len(parts) != 3:
            return "Invalid format. Use: <number1> <operator> <number2>"

        num1, operator, num2 = parts
        num1 = float(num1)
        num2 = float(num2)

        if operator == '+':
            return f"Result: {num1 + num2}"
        elif operator == '-':
            return f"Result: {num1 - num2}"
        elif operator == '*':
            return f"Result: {num1 * num2}"
        elif operator == '/':
            if num2 == 0:
                return "Error: Division by zero"
            return f"Result: {num1 / num2}"
        else:
            return "Error: Unsupported operator. Use +, -, *, /"
    except ValueError:
        return "Error: Invalid numbers"
    except Exception as e:
        return f"Error: {e}"

def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server started and listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    expression = data.decode('utf-8')
                    print(f"Received expression: {expression}")
                    result = calculate(expression)
                    conn.sendall(result.encode('utf-8'))

if __name__ == "__main__":
    start_server()