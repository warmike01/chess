import chess
import csv
from errors import *
from tkinter import *
from os.path import exists
i=0
while True:
    if exists("games/game{0}.csv".format(i)):
        i+=1
    else:
        break
file_name="games/game{0}.csv".format(i)
f=open(file_name, 'w+')
f.close()
b=chess.board()
root = Tk()     
root.title("Chess Game")
root.geometry("800x600")
def hint():
    popup = Toplevel(root)
    popup.geometry("640x80")
    popup.title("Справка")
    Label(popup, text = "Для ввода хода нажмите на фигуру, которой хотите походить, затем на поле, куда хотите походить. \n Чтобы выиграть, нужно побить короля противника. \n Партии записываются в папку games, находящуюся в папке с программой. \n (с) Михаил Клопов \n НИУ ИТМО, 2023").pack()
    X = Button(popup, text="OK", command = popup.destroy).pack()
def draw():
    popup = Toplevel(root)
    popup.geometry("300x80")
    popup.title("Предложение ничьей")
    Label(popup, text = "Вы действительно хотите согласиться на ничью?").pack()
    Y = Button(popup, text="Да" )
    Y.configure(command = lambda r=root,x=2: [popup.destroy,win(r, x)])
    Y.pack()
    N = Button(popup, text="Нет", command = popup.destroy).pack()
def resign():
    popup = Toplevel(root)
    popup.geometry("300x80")
    popup.title("Сдача")
    Label(popup, text = "Вы действительно хотите сдаться?").pack()
    Y = Button(popup, text="Да" )
    Y.configure(command = lambda r=root,x=(b.turn+1) % 2: [popup.destroy,win(r, x)])
    Y.pack()
    N = Button(popup, text="Нет", command = popup.destroy).pack()
def square_pic(b: chess.board, i: int, j: int):
    square = b.board_state[i][j]
    color = (i + j) %2
    if square.s_piece !=0:
        return "resources/{0}_{1}_{2}.PNG".format(square.s_piece, square.s_color, color)
    else:
        return "resources/0_{0}.PNG".format(color)
def error_popup(root: Tk, error: str):
    popup = Toplevel(root)
    popup.geometry("300x60")
    popup.title("Невозможный ход")
    Label(popup, text = error).pack()
    X = Button(popup, text="OK", command = popup.destroy).pack()
def win(root: Tk, win_flag: int):
    popup = Toplevel(root)
    popup.geometry("300x60")
    popup.title("Конец игры")
    if win_flag == 1:
        Label(popup, text = "Белые выиграли!").pack()
        l=["Result", "1", "0"]
    elif win_flag == 0:
        Label(popup, text = "Черные выиграли!").pack()
        l=["Result", "0", "1"]
    else:
        Label(popup, text = "Ничья!").pack()
        l=["Result", "0.5", "0.5"]
    f=open(file_name, 'a')
    writer=csv.writer(f)
    writer.writerow(l)
    f.close()
    X = Button(popup, text="OK", command = quit).pack()
mainmenu = Menu(root) 
root.config(menu=mainmenu) 
mainmenu.add_command(label="Предложить ничью", command = draw)
mainmenu.add_command(label="Сдаться", command = resign)
mainmenu.add_command(label="Справка", command = hint)
board_gfx=[]
pics=[]
moving_piece = None
ready_to_move = False
def press(b: chess.board, t: Button):
    global moving_piece
    global ready_to_move
    x = t.grid_info()["column"] 
    y = 7-t.grid_info()["row"]
    if ready_to_move:
        try:
            start = chr(moving_piece.s_file+97)+str(moving_piece.s_rank+1)
            ret=moving_piece.move(y, x)
        except IllegalMove as error:
            error_popup(root, error)
        else:
            board_update(b)
            l=[str(b.turn), start, chr(x+97)+str(y+1)]
            f=open(file_name, 'a')
            writer=csv.writer(f)
            writer.writerow(l)
            f.close()
            b.turn += 1
            if ret != -1:
                win(root, ret)
        finally:
            moving_piece = None
            ready_to_move = False
    else:
        try:
            if b.board_state[y][x].s_piece == 0:
                raise NoPiece
            elif b.board_state[y][x].s_color != b.turn % 2:
                raise WrongPlayer
            else:
                moving_piece = b.board_state[y][x]
        except IllegalMove as error:
            error_popup(root, error)
        else:
            ready_to_move = True

    
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
board_update(b)
root.mainloop()