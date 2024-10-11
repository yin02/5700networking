import socket

class TicTacToeServer:
    def __init__(self, port=12000):
        self.port = port
        self.board = [' ' for _ in range(9)]
        self.server_socket = None

    def print_board(self):
        print("\nCurrent board:")
        print(" -------------")
        for i in range(0, 9, 3):
            print(f" | {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} | ")
            if i < 6:
                print(" -------------")
        print(" -------------")

    def check_winner(self):
        # Define win combinations
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]

        if ' ' not in self.board:
            return 'Tie'

        return None

    def setup_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('', self.port))
        self.server_socket.listen(1)
        print('Tic-Tac-Toe Server is ready to play!')

    def handle_client_move(self, connection_socket):
        while True:
            client_move = connection_socket.recv(1024).decode()
            # TODO: Implement the validation of the client's move
            # Hint: Check if the move 1. is a digit, 2. within range, and 3. the chosen spot is empty
            # Hint: If the move is invalid, send "Invalid move" to the client
            # Hint: If the move is valid, update the board and break the loop
            pass
        self.print_board()

    def make_server_move(self):
        while True:
            try:
                server_move = int(input("Enter your move (1-9): ")) - 1
                if 0 <= server_move <= 8 and self.board[server_move] == ' ':
                    self.board[server_move] = 'O'
                    break
                else:
                    print("Invalid move. Please enter a number between 1 and 9 for an empty space.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        self.print_board() # Display the board after a server's move
        return server_move

    def play_game(self, connection_socket):
        self.board = [' ' for _ in range(9)]
        game_over = False

        while not game_over:
            print("Waiting for client's move...")
            self.handle_client_move(connection_socket)

            winner = self.check_winner()
            # TODO: Implement game-over logic for client's move
            # Hint: Check if there's a winner 'X' or 'O' or tie after the client's move
            # Hint: Send appropriate message to the client and set game_over to True if the game has ended

            if not game_over:
                server_move = self.make_server_move()
                winner = self.check_winner()
                # TODO: Implement game-over logic for server's move
                # Hint: Check if there's a winner or tie after the server's move
                # Hint: Send appropriate message to the client and set game_over to True if the game has ended
                # Hint: If the game hasn't ended, send the server's move to the client

    def run(self):
        self.setup_server()
        while True:
            connection_socket, addr = self.server_socket.accept()
            print(f"Game started with {addr}")
            self.play_game(connection_socket)
            play_again = connection_socket.recv(1024).decode()
            if play_again.lower() != 'yes':
                break
            connection_socket.close()
        self.server_socket.close()

if __name__ == "__main__":
    server = TicTacToeServer()
    server.run()