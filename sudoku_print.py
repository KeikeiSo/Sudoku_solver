""" trying to print a sudoku """
from create_sudoku import generate, empty
from copy import deepcopy
import tkinter as tk


# generate a sudoku
board = generate()

sudoku = deepcopy(board)

empty(sudoku, 50)

# print
root = tk.Tk()

for i in range(9):
    for j in range(9):
        num = sudoku[i][j]
        if num == 0:
            e = tk.Entry(root, width = 3)
            e.grid(row = i, column = j)
        else:
            l = tk.Label(root, text = str(num))
            l.grid(row = i, column = j)

root.mainloop()
