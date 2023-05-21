from copy import deepcopy
from pieces import *
from errors import *
class board:
    board_state: square = []
    turn: int
    kingside_castling_white : bool = False
    queenside_castling_white : bool = False
    kingside_castling_black : bool = False
    queenside_castling_black: bool = False
    def __init__(self, fen: str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        fen = fen.split()
        rank_number=7
        file_number = 0
        rank=[]
        for c in fen[0]:
            if c == '/':
                self.board_state.insert(0, deepcopy(rank))
                rank.clear()
                rank_number -= 1
                file_number = 0
            elif c.isnumeric():
                p=square(rank_number, file_number)
                for i in range(int(c)):
                    rank.append(p)
                    file_number += 1
            elif c == 'P':
                p=pawn(rank_number, file_number, 1)
                rank.append(p)
                file_number += 1
            elif c == 'p':
                p=pawn(rank_number, file_number, 0)
                rank.append(p)
                file_number += 1
            elif c == 'N':
                p=knight(rank_number, file_number, 1)
                rank.append(p)
                file_number += 1
            elif c == 'n':
                p=knight(rank_number, file_number, 0)
                rank.append(p)
                file_number += 1
            elif c == 'B':
                p=bishop(rank_number, file_number, 1)
                rank.append(p)
                file_number += 1
            elif c == 'b':
                p=bishop(rank_number, file_number, 0)
                rank.append(p)
                file_number += 1
            elif c == 'R':
                p=rook(rank_number, file_number, 1)
                rank.append(p)
                file_number += 1
            elif c == 'r':
                p=rook(rank_number, file_number, 0)
                rank.append(p)
                file_number += 1
            elif c == 'Q':
                p=queen(rank_number, file_number, 1)
                rank.append(p)
                file_number += 1
            elif c == 'q':
                p=queen(rank_number, file_number, 0)
                rank.append(p)
                file_number += 1
            elif c == 'K':
                p=king(rank_number, file_number, 1)
                rank.append(p)
                file_number += 1
            elif c == 'k':
                p=king(rank_number, file_number, 0)
                rank.append(p)
                file_number += 1
        self.board_state.insert(0, deepcopy(rank))
        self.turn = (int(fen[5]) - 1) *2 +1
        if fen[1] == 'b':
            self.turn += 1


