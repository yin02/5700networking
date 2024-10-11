import socket

# Implement the process_message function
def process_message(message, option):
    if option == 1:
        return message.upper()  # Convert to uppercase
    elif option == 2:
        return message.lower()  # Convert to lowercase
    else:
        raise ValueError("Invalid option. Use 1 for uppercase or 2 for lowercase.")

def run_server():
    server_port = 12000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)  # Allow 1 connection
    print('The server is ready to receive')

    while True:
        connection_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        while True:
            data = connection_socket.recv(1024).decode()
            if not data:
                print(f"Received empty data from {addr}. Sending error message.")
                connection_socket.send("Error: Empty data received. Please send a valid message.".encode())
                continue 

            try:
                option, message = data.split(':', 1)
                option = int(option)

                if option == 3:
                    print(f'Client initiated termination.')
                    connection_socket.close()
                    break

                # Call the process_message function and send the result back to the client
                processed_message = process_message(message.strip(), option)  # Process the message
                connection_socket.send(processed_message.encode())  # Send the processed message back to the client
   
                print(f"Received: {message.strip()}, Option: {option}, Sent: {processed_message}")
            except (ValueError, IndexError) as e:
                error_msg = 'Invalid data format. Please try again.'
                connection_socket.send(error_msg.encode())
                print(f"Sent error message to {addr}: {error_msg}")

    server_socket.close()

if __name__ == "__main__":
    run_server()
