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
        self.client_socket.settimeout(5)  # Set a 5 second timeout
        try:
            self.client_socket.connect((self.server_name, self.server_port))
        except socket.error as e:
            print(f"Failed to connect to server: {e}")
            sys.exit(1)

    def get_player_move(self):
        # TODO: Implement the get_player_move method
        # Hint: Use a while loop to keep asking for input until a valid move is entered
        # Hint: A valid move is a number between 1-9 that corresponds to an empty space on the board
        pass

    def make_move(self):
        move = self.get_player_move()
        self.client_socket.send(str(move).encode())
        self.board[move] = 'X'
        self.print_board()
        return move

    def handle_server_response(self):
        print("Waiting for server's move...")
        server_response = self.client_socket.recv(1024).decode()
        
        # TODO: Implement the handle_server_response method
        # Hint: Check different possible responses from the server:
        # - "You win", "Tie", "Server wins", "Invalid move"
        # - If it's none of these, it's the server's move (a number)
        # Hint: Update the board with the server's move
        # Hint: Return True if the game is over, False otherwise
        pass

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


