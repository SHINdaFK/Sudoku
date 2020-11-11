from tkinter import *
import random
import sys
import os
import numpy as np
root = Tk()
root.geometry("800x600")

class JIWOO:
    def __init__(self):


    grid = [
        [0,0,0,7,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0],
        [0,0,0,4,3,0,2,0,0],
        [0,0,0,0,0,0,0,0,6],
        [0,0,0,5,0,9,0,0,0],
        [0,0,0,0,0,0,4,1,8],
        [0,0,0,0,8,1,0,0,0],
        [0,0,2,0,0,0,0,5,0],
        [0,4,0,0,0,0,3,0,0]
    ]

    def possible(y,x,n):
        global grid
        for i in range(0,9):
            if grid[y][i] == n:
                return False
        for i in range(0,9):
            if grid[i][x] == n:
                return False
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0,3):
            for j in range(0,3):
                if grid[y0+i][x0+j] == n:
                    return False
        return True

    def solve():
        global grid
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    for n in range(1,10):
                        if possible(y,x,n):
                            grid[y][x] = n
                            solve()
                            grid[y][x] = 0
                    return
        print(np.matrix(grid))
        input("MOrE? ")

    solve()

class SudokuGUI:
    def __init__(self, hello):
        hello.title("Sudoku_Solver")
        my_font = ("Airal", 18)
        self.entry_box = []
        for i in range(9):
            sudoku_board += [[0, 0, 0, 0, 0, 0, 0 , 0, 0]]
            for i in range(9):
                for j in range (9):
                    self.entry_box = Entry(hello, font = my_font, bg = "white", highlightcolor = "yellow", borderwidth = 1, width = 2, cursor = 'star', highlightthickness = 1, highlightbackground = 'black', textvar = retrieve_input[i][j])
                    self.entry_box.grid(row = [i], columnn = [j])
        entry_box.pack()

        entry_box.focus_set()

        menu = Menu(hello)
        file = Menu(menu)
        file.add_command(hello, label = "Reset", command= self.restart_program)
        file.add_command(hello, label = "Solve", command= self.solve_sudoku)
        file.add_command(hello, label = "Quit the game", command = hello.quit)
        menu.add_cascade(hello, label = "Menu", menu=file)
        main.config(menu=menu)

def storing_numbers(self):
    pass

def restart_program(self):
    pass

def solve_sudoku(self):
    solution = JIWOO()

b = SudokuGUI(root)
root.mainloop()
