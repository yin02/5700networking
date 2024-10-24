import socket
import sys

class TicTacToeClient:
    def __init__(self, server_name='192.168.1.1', port=None):
        self.server_name = server_name
        self.port = port
        self.client_socket = None
        self.board = [' ' for _ in range(9)]
        self.player_symbol = None
        self.game_active = True

    def print_board(self):
        """Print the board with consistent spacing"""
        print("\nCurrent board:")
        print(" -------------")
        for i in range(0, 9, 3):
            print(f" | {self.board[i] if self.board[i] != ' ' else ' '} | {self.board[i+1] if self.board[i+1] != ' ' else ' '} | {self.board[i+2] if self.board[i+2] != ' ' else ' '} |")
            print(" -------------")
        
        # Print position reference board
        print("\nPosition numbers:")
        print(" -------------")
        print(" | 1 | 2 | 3 |")
        print(" -------------")
        print(" | 4 | 5 | 6 |")
        print(" -------------")
        print(" | 7 | 8 | 9 |")
        print(" -------------")

    def connect_to_server(self):
        """Establish a connection to the game server."""
        if not self.port:
            while True:
                try:
                    port_input = input("Enter port number (12000 for Player X, 12001 for Player O): ")
                    self.port = int(port_input)
                    if self.port not in [12000, 12001]:
                        print("Invalid port. Please use 12000 for Player X or 12001 for Player O")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid port number.")

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((self.server_name, self.port))
            data = self.client_socket.recv(1024).decode()
            if data.startswith("SYMBOL:"):
                self.player_symbol = data.split(":")[1].strip()
                print(f"You are player {self.player_symbol}")
        except socket.error as e:
            print(f"Failed to connect to server: {e}")
            sys.exit(1)

    def get_player_move(self):
        """Prompt the player to enter their move."""
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if 0 <= move <= 8 and self.board[move].strip() == '':
                    return str(move)
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1-9.")

    def process_server_message(self, message):
        """Process a single message from the server."""
        try:
            message = message.strip()
            # 1. Process "BOARD:" messages
            if message.startswith("BOARD:"):
                board_state = message.split(":")[1].strip()
                self.board = board_state.split(',')
                self.print_board()  # Print the updated board
                
            elif message.startswith("MSG:"):
                msg_text = message.split(":", 1)[1].strip()
                print(f"\n{msg_text}")
                if "Game Over" in msg_text:
                    self.game_active = False  # End the game if "Game Over" is mentioned
                    return False
                
            elif message == "YOUR_TURN":
                print("It's your turn!")
                move = self.get_player_move()  # Get player move
                self.client_socket.send(move.encode())  # Send the move to the server

            elif message.startswith("INVALID:"):
                invalid_reason = message.split(":", 1)[1].strip()
                print(f"Invalid move: {invalid_reason}. Try again.")
                
            if "Game Over" in message:
                self.game_active = False
                return False
        except Exception as e:
            print(f"Error processing message '{message}': {e}")
        return True

    def handle_server_messages(self):
        """Handle incoming messages from the server."""
        buffer = ""
        while self.game_active:
            try:
                data = self.client_socket.recv(1024).decode()
                if not data:
                    print("Lost connection to server")
                    self.game_active = False
                    break
                
                buffer += data
                
                while "\n" in buffer:
                    message, buffer = buffer.split("\n", 1)
                    if not self.process_server_message(message):
                        return

            except Exception as e:
                print(f"Error receiving data: {e}")
                self.game_active = False
                break

    def run(self):
        """Run the client."""
        self.connect_to_server()
        print(f"Connected to server as Player {self.player_symbol}")
        print("Waiting for game to start...")
        
        try:
            self.handle_server_messages()
        except KeyboardInterrupt:
            print("\nGame interrupted by user")
        finally:
            if self.client_socket:
                self.client_socket.close()
            print("\nGame over. Connection closed.")

if __name__ == "__main__":
    SERVER_IP = input("Enter the server IP address (default is 192.168.1.1): ") or '192.168.1.1'
    client = TicTacToeClient(server_name=SERVER_IP)
    client.run()
