import chess
from tkinter import *
b=chess.board()
root = Tk()     
root.title("Chess Game")
root.geometry("800x600")
def square_pic(i: int, j: int):
    square = b.board_state[i][j]
    color = (i + j) %2
    if square.s_piece !=0:
        return "{0}_{1}_{2}.PNG".format(square.s_piece, square.s_color, color)
    else:
        return "0_{0}".format(color)