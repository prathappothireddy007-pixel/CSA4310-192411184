import socket

def run_client():
    HOST = '127.0.0.1'
    PORT = 65432
    
    # Create TCP socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
        print(f"[+] Successfully connected to the server at {HOST}:{PORT}")
    except ConnectionRefusedError:
        print("[-] Connection failed. Is the server running?")
        return

    print("--------------------------------------------------")
    print("Enter expressions with spaces. Example: '10 + 5' or '23.5 * 2'")
    print("Type 'exit' to close the connection.")
    print("--------------------------------------------------")
    
    while True:
        # Get input from user
        expression = input("Enter equation: ").strip()
        
        if not expression:
            continue
            
        # Send expression to server
        client_socket.sendall(expression.encode('utf-8'))
        
        if expression.lower() == 'exit':
            print("[-] Exiting.")
            break
            
        # Wait for response from server
        response = client_socket.recv(1024).decode('utf-8')
        print(f"[Response] Result: {response}\n")
        
    client_socket.close()

if __name__ == '__main__':
    run_client()