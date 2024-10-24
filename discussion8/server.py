import socket
import threading
import time


class TicTacToeJudgeServer:
    def __init__(self, port1=12000, port2=12001):
        self.port1 = port1
        self.port2 = port2
        self.board = [' ' for _ in range(9)]
        self.server_socket1 = None
        self.server_socket2 = None
        self.player1 = None
        self.player2 = None
        self.current_player = 'X'
        self.game_active = True
        self.lock = threading.Lock()

    def print_board(self):
        print("\nCurrent board state:")
        print(" -------------")
        for i in range(0, 9, 3):
            print(f" | {self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]} | ")
            if i < 6:
                print(" -------------")
        print(" -------------")

    def check_winner(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]

        return 'Tie' if ' ' not in self.board else None

    def setup_server(self):
        self.server_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket1.bind(('', self.port1))
        self.server_socket1.listen(1)

        self.server_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket2.bind(('', self.port2))
        self.server_socket2.listen(1)

        print('Tic-Tac-Toe Judge Server is ready!')
        print(f'Listening on ports {self.port1} and {self.port2}')

    def send_to_player(self, player_socket, message, delay=0.1):
        """Safely send message to a player with message terminator"""
        try:
            full_message = message + "\n"
            player_socket.send(full_message.encode())
            time.sleep(delay)  # Add small delay between messages
            return True
        except Exception as e:
            print(f"Error sending message: {e}")
            return False

    def broadcast_state(self):
        """Send current board state to both players"""
        board_str = ','.join(self.board)
        message = f"BOARD:{board_str}"
        self.send_to_player(self.player1, message)
        self.send_to_player(self.player2, message)
        time.sleep(0.1)  # Small delay after broadcasting state

    def broadcast_message(self, message):
        """Send a message to both players"""
        encoded_message = f"MSG:{message}"
        self.send_to_player(self.player1, encoded_message)
        self.send_to_player(self.player2, encoded_message)
        time.sleep(0.1)  # Small delay after broadcasting message

    def validate_move(self, move):
        """Validates if a player's move is legal."""
        if not move.isdigit():
            return False

        move = int(move)

        return 0 <= move <= 8 and self.board[move] == ' '

    def get_player_move(self, player_socket):
        """Get a move from the specified player."""
        try:
            self.send_to_player(player_socket, "YOUR_TURN")
            move = player_socket.recv(1024).decode().strip()
            return move
        except Exception as e:
            print(f"Error getting player move: {e}")
            return None

    def run_game(self):
        """Main game loop."""
        try:
            self.broadcast_message("Game is starting!")
            time.sleep(0.5)  # Give clients time to initialize
            self.broadcast_state()

            while self.game_active:
                current_socket = self.player1 if self.current_player == 'X' else self.player2

                print(f"\nWaiting for Player {self.current_player}'s move...")
                self.broadcast_message(f"Player {self.current_player}'s turn")

                move = self.get_player_move(current_socket)

                if not move:
                    print(f"Lost connection to Player {self.current_player}")
                    self.game_active = False
                    break

                with self.lock:
                    if self.validate_move(move):
                        move = int(move)
                        self.board[move] = self.current_player
                        self.print_board()
                        self.broadcast_state()

                        winner = self.check_winner()
                        if winner:
                            if winner == 'Tie':
                                self.broadcast_message("Game Over - It's a Tie!")
                            else:
                                self.broadcast_message(f"Game Over - Player {winner} wins!")
                            self.game_active = False
                            break

                        self.current_player = 'O' if self.current_player == 'X' else 'X'
                    else:
                        self.send_to_player(current_socket, "INVALID:Invalid move")
                        continue

        except Exception as e:
            print(f"Error in game loop: {e}")
            self.game_active = False

    def run(self):
        """Run the server and start the game."""
        self.setup_server()

        try:
            print("Waiting for Player X to connect...")
            self.player1, addr1 = self.server_socket1.accept()
            print(f"Player X connected from {addr1}")
            self.send_to_player(self.player1, "SYMBOL:X")

            print("Waiting for Player O to connect...")
            self.player2, addr2 = self.server_socket2.accept()
            print(f"Player O connected from {addr2}")
            self.send_to_player(self.player2, "SYMBOL:O")

            # Start game with a delay to ensure clients are ready
            time.sleep(0.5)
            self.run_game()

        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            if self.player1:
                self.player1.close()
            if self.player2:
                self.player2.close()
            self.server_socket1.close()
            self.server_socket2.close()
            print("Game ended. Server shutting down.")


if __name__ == "__main__":
    server = TicTacToeJudgeServer()
    server.run()
