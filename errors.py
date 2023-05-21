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
class RookIllegalMove(IllegalMove):
    def __str__(self): 
        return("Ладья так не ходит")
class BishopIllegalMove(IllegalMove):
    def __str__(self): 
        return("Слон так не ходит")
