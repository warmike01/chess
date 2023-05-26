from tkinter import *
class IllegalMove(Exception):
    def __str__(self): 
        return("Невозможный ход")
class NoPiece(IllegalMove):
    def __str__(self): 
        return("Выберите фигуру")
class WrongPlayer(IllegalMove):
    def __str__(self): 
        return("Сейчас ход другого игрока")
class SelfCapture(IllegalMove):
    def __str__(self): 
        return("Нельзя бить фигуры своего цвета")
class KingIllegalMove(IllegalMove):
    def __str__(self): 
        return("Король так не ходит")
class QueenIllegalMove(IllegalMove):
    def __str__(self): 
        return("Ферзь так не ходит")
class RookIllegalMove(IllegalMove):
    def __str__(self): 
        return("Ладья так не ходит")
class BishopIllegalMove(IllegalMove):
    def __str__(self): 
        return("Слон так не ходит")
class KnightIllegalMove(IllegalMove):
    def __str__(self): 
        return("Конь так не ходит")
class PawnIllegalMove(IllegalMove):
    def __str__(self): 
        return("Пешка так не ходит")
class IllegalCastling(IllegalMove):
    def __str__(self): 
        return("Рокировка в эту сторону невозможна")

