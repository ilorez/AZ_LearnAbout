import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        self.turn = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.frame = tk.Frame(master)
        self.frame.pack()

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.frame, text="", width=5, height=2, font=("Arial", 20), command=lambda x=i, y=j: self.mark_square(x, y))
                button.grid(row=i, column=j, padx=2, pady=2)
                self.buttons[i][j] = button

        self.restart_button = tk.Button(self.frame, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=3, column=1, padx=2, pady=2)

    def mark_square(self, x, y):
        if self.board[x][y] != "":
            return

        self.board[x][y] = self.turn
        self.buttons[x][y].configure(text=self.turn)

        if self.check_winner():
            messagebox.showinfo("Tic Tac Toe", f"{self.turn} wins!")
            self.restart_game()
        elif self.check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            self.restart_game()
        else:
            self.turn = "O" if self.turn == "X" else "X"

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return True

        # Check columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True

        return False

    def check_draw(self):
        for row in self.board:
            for square in row:
                if square == "":
                    return False
        return True

    def restart_game(self):
        self.turn = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(text="")
        self.restart_button.focus()

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()