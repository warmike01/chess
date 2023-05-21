import chess
import os.path
from errors import *
from tkinter import *
root = Tk()     
root.title("Chess Game")
root.geometry("800x600")
def square_pic(b: chess.board, i: int, j: int):
    square = b.board_state[i][j]
    color = (i + j) %2
    if square.s_piece !=0:
        return "resources/{0}_{1}_{2}.PNG".format(square.s_piece, square.s_color, color)
    else:
        return "resources/0_{0}.PNG".format(color)
board_gfx=[]
pics=[]
moving_piece = None
ready_to_move = False
def press(b: chess.board, t: Button):
    global moving_piece
    global ready_to_move
    y = t.grid_info()["column"] 
    x = 7-t.grid_info()["row"]
    try:
        if ready_to_move:
            pass
        else:
            if b.board_state[x][y].s_piece == 0:
                raise NoPiece
            elif b.board_state[x][y].s_color != b.turn % 2:
                raise WrongPlayer
    except IllegalMove as error:
        popup = Toplevel(root)
        popup.geometry("300x60")
        popup.title("Невозможный ход")
        Label(popup, text = error).pack()
        X = Button(popup, text="OK", command = popup.destroy).pack()
def board_update(b: chess.board):
    for i in range(len(board_gfx)):
        board_gfx[i].destroy()
    board_gfx.clear()
    for i in range(7, -1, -1):
        for j in range(8):
            photo = PhotoImage(file=square_pic(b, i, j))
            pics.append(photo)
            t=Button(root, height=40, width=40, image=photo)
            t.grid(row=7-i,column=j, sticky=W) 
            t.configure(command = lambda x=b, y=t: press (x, y ))
            board_gfx.append(t)
b=chess.board()
board_update(b)
root.mainloop()