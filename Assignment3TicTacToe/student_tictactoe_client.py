import socket
import sys

class TicTacToeClient:
    def __init__(self, server_name='127.0.0.1', server_port=12000):
        self.server_name = server_name
        self.server_port = server_port
        self.client_socket = None
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        print("\nCurrent board:")
        print(" -------------")
        for i in range(0, 9, 3):
            print(f" | {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} | ")
            if i < 6:
                print(" -------------")
        print(" -------------")

    def connect_to_server(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.settimeout(335)  # Set a 5 second timeout
        try:
            self.client_socket.connect((self.server_name, self.server_port))
        except socket.error as e:
            print(f"Failed to connect to server: {e}")
            sys.exit(1)

    def get_player_move(self):
        while True:
            try:
                move = int(input("Your move (1-9): ")) - 1  # Convert to 0-based index
                if 0 <= move < 9 and self.board[move] == ' ':
                    return move
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def make_move(self):
        move = self.get_player_move()
        self.client_socket.send(str(move).encode())  # Send the move to the server
        print(f"Sent move {move + 1} to server")  # Debugging print
        self.board[move] = 'X'
        self.print_board()
        return move


    def handle_server_response(self):
        print("Waiting for server's move...")
        server_response = self.client_socket.recv(1024).decode()

        if server_response == "You win":
            print("Congratulations! You win!")
            return True
        elif server_response == "Tie":
            print("It's a tie!")
            return True
        elif server_response == "Server wins":
            print("Server wins. Better luck next time!")
            return True
        elif server_response == "Invalid move. Try another position.":
            print("Invalid move. Please try again.")
            return False
        else:
            try:
                # Server's move (a number between 1 and 9)
                move = int(server_response) - 1  # Convert to 0-based index
                self.board[move] = 'O'  # Server's move is marked as 'O'
                self.print_board()
                return False
            except ValueError:
                print("Unexpected response from server.")
                return True


    def play_game(self):
        game_over = False
        while not game_over:
            self.print_board()
            self.make_move()
            game_over = self.handle_server_response()

    def run(self):
        self.connect_to_server()
        self.play_game()
        self.client_socket.close()
        print("Game over. Connection closed.")

if __name__ == "__main__":
    client = TicTacToeClient()
    client.run()


