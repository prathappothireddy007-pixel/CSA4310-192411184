import socket

def run_server():
    # Define host and port
    HOST = '127.0.0.1'  # Localhost
    PORT = 65432        # Non-privileged port
    
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"[*] Server is listening on {HOST}:{PORT}...")
    
    while True:
        # Accept client connection
        conn, addr = server_socket.accept()
        print(f"[+] Connected to client at {addr}")
        
        try:
            while True:
                # Receive data from the client
                data = conn.recv(1024).decode('utf-8')
                if not data or data.lower() == 'exit':
                    print("[-] Client disconnected.")
                    break
                
                print(f"[Request] Received expression: {data}")
                
                # Parse and evaluate the basic expression
                try:
                    # Expecting space-separated string: "operand1 operator operand2"
                    parts = data.split()
                    if len(parts) != 3:
                        raise ValueError("Invalid format. Use: num1 operator num2")
                        
                    num1 = float(parts[0])
                    operator = parts[1]
                    num2 = float(parts[2])
                    
                    # Perform math operations
                    if operator == '+':
                        result = num1 + num2
                    elif operator == '-':
                        result = num1 - num2
                    elif operator == '*':
                        result = num1 * num2
                    elif operator == '/':
                        if num2 == 0:
                            result = "Error: Division by zero!"
                        else:
                            result = num1 / num2
                    else:
                        result = "Error: Invalid operator. Use +, -, *, or /"
                except ValueError:
                    result = "Error: Invalid format or inputs. Must be numbers."
                except Exception as e:
                    result = f"Error: {str(e)}"
                
                # Send the answer back to the client
                conn.sendall(str(result).encode('utf-8'))
        except ConnectionResetError:
            print("[-] Connection reset by client.")
        finally:
            conn.close()

if __name__ == '__main__':
    run_server()