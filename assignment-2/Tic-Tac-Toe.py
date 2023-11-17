import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root, board_size=3):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.board_size = board_size
        self.current_player = "X"
        self.board = [[" " for _ in range(board_size)]
                      for _ in range(board_size)]
        self.move_history = []

        # Scores
        self.player_x_score = 0
        self.player_o_score = 0

        for i in range(board_size):
            for j in range(board_size):
                button = tk.Button(
                    self.root,
                    text=" ",
                    font=("normal", 20),
                    width=8,
                    height=4,
                    command=lambda row=i, col=j: self.on_button_click(
                        row, col),
                )
                button.grid(row=i, column=j)

        # Labels for displaying scores
        tk.Label(root, text="Player X Score:").grid(row=board_size, column=0)
        self.label_player_x_score = tk.Label(root, text="0")
        self.label_player_x_score.grid(row=board_size, column=1)

        tk.Label(root, text="Player O Score:").grid(
            row=board_size + 1, column=0)
        self.label_player_o_score = tk.Label(root, text="0")
        self.label_player_o_score.grid(row=board_size + 1, column=1)

        # Button to reset the board and scores
        tk.Button(root, text="Reset", command=self.reset_board).grid(
            row=board_size, column=2
        )

    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            # Save the current state before making a move
            self.move_history.append([row, col, self.board[row][col]])

            self.board[row][col] = self.current_player
            self.update_button_text(row, col)

            if self.check_winner():
                self.update_score()
                messagebox.showinfo(
                    "Tic Tac Toe", f"Player {self.current_player} wins!"
                )
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def update_button_text(self, row, col):
        button = self.root.grid_slaves(row=row, column=col)[0]
        button["text"] = self.board[row][col]
        button["state"] = tk.DISABLED  # Disable the button after it's clicked

    def check_winner(self):
        for i in range(self.board_size):
            if all(
                self.board[i][j] == self.current_player for j in range(self.board_size)
            ) or all(
                self.board[j][i] == self.current_player for j in range(self.board_size)
            ):
                return True
        if all(
            self.board[i][i] == self.current_player for i in range(self.board_size)
        ) or all(
            self.board[i][self.board_size - 1 - i] == self.current_player
            for i in range(self.board_size)
        ):
            return True
        return False

    def is_board_full(self):
        return all(
            self.board[i][j] != " "
            for i in range(self.board_size)
            for j in range(self.board_size)
        )

    def update_score(self):
        if self.current_player == "X":
            self.player_x_score += 1
            self.label_player_x_score.config(text=str(self.player_x_score))
        else:
            self.player_o_score += 1
            self.label_player_o_score.config(text=str(self.player_o_score))

    def reset_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                button = self.root.grid_slaves(row=i, column=j)[0]
                button["text"] = " "
                button["state"] = tk.NORMAL
                self.board[i][j] = " "
        self.current_player = "X"
        self.move_history = []


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
