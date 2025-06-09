import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master, rows=10, cols=10, mines=10):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.mine_locations = set()
        self.game_over = False
        self.first_click = True
        self.create_board()

    def create_board(self):
        for r in range(self.rows):
            for c in range(self.cols):
                button = tk.Button(self.master, width=2, height=1,
                                   command=lambda row=r, col=c: self.on_click(row, col))
                button.grid(row=r, column=c)
                self.buttons[r][c] = button

    def on_click(self, row, col):
        if self.game_over:
            return

        if self.first_click:
            self.place_mines(row, col)
            self.first_click = False

        if (row, col) in self.mine_locations:
            self.buttons[row][col].config(text="*", bg="red")
            self.reveal_all()
            self.game_over = True
        else:
            count = self.count_adjacent_mines(row, col)
            self.buttons[row][col].config(text=str(count) if count > 0 else "",
                                          state=tk.DISABLED,
                                          disabledforeground="black")
            if count == 0:
                self.reveal_adjacent_squares(row, col)
            if self.check_win():
                self.reveal_all()
                self.game_over = True

    def place_mines(self, start_row, start_col):
        while len(self.mine_locations) < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if (row, col) != (start_row, start_col) and (row, col) not in self.mine_locations:
                self.mine_locations.add((row, col))

    def count_adjacent_mines(self, row, col):
        count = 0
        for r in range(max(0, row - 1), min(self.rows, row + 2)):
            for c in range(max(0, col - 1), min(self.cols, col + 2)):
                if (r, c) in self.mine_locations:
                    count += 1
        return count

    def reveal_adjacent_squares(self, row, col):
        for r in range(max(0, row - 1), min(self.rows, row + 2)):
            for c in range(max(0, col - 1), min(self.cols, col + 2)):
                if (r, c) == (row, col):
                    continue
                if self.buttons[r][c]["state"] == tk.NORMAL:
                    self.on_click(r, c)

    def reveal_all(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) in self.mine_locations:
                    self.buttons[r][c].config(text="*", bg="red")
                else:
                    count = self.count_adjacent_mines(r, c)
                    self.buttons[r][c].config(text=str(count) if count > 0 else "",
                                              state=tk.DISABLED,
                                              disabledforeground="black")

    def check_win(self):
        revealed_squares = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.buttons[r][c]["state"] == tk.DISABLED:
                    revealed_squares += 1
        return revealed_squares == (self.rows * self.cols - self.mines)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minesweeper")
    game = Minesweeper(root)
    root.mainloop()