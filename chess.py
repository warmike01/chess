from copy import deepcopy
from errors import *
class square:
    __s_rank: str
    __s_file: int
    s_piece: int
    def __init__(self, r: int, f: int):
        self.s_rank=r
        self.s_file=f
        self.s_piece = 0
class piece(square):
    __s_rank: str
    __s_file: int
    s_piece: int=-1
    s_color: int #1 for white, 0 for black
    def __init__(self, r: int, f: int, c: int):       
        super().__init__(r, f)
        self.s_piece = 0
        self.s_color = c
        """
    def move(self, t_file, t_rank):
        if self.s_board.board_state[t_rank][t_file].s_piece != 0:
            if self.s_board.board_state[t_rank][t_file].color() ==  self.color():
                raise SelfCapture()
        self.s_board.board_state[self.s_rank][self.s_file] = square(self.s_rank, self.s_file)
        self.s_file=t_file
        self.s_rank=t_rank
        self.s_board.board_state[t_rank][t_file]=self
        """
class pawn(piece):
    __s_rank: str
    __s_file: int
    s_piece: int
    s_color: int
    def __init__(self, r: int, f: int, c: int):
        super().__init__(r, f, c)
        self.s_piece = 1
class knight(piece):
    __s_rank: str
    __s_file: int
    s_piece: int
    s_color: int
    def __init__(self, r: int, f: int, c: int):
        super().__init__(r, f, c)
        self.s_piece = 2
class bishop(piece):
    __s_rank: str
    s_color: int
    s_piece: int
    __s_file: int
    def __init__(self, r: int, f: int, c: int):
        super().__init__(r, f, c)
        self.s_piece = 3
class rook(piece):
    __s_rank: str
    __s_file: int
    s_piece: int
    s_color: int
    def __init__(self, r: int, f: int, c: int):
        super().__init__(r, f, c)
        self.s_piece = 4
class queen(piece):
    __s_rank: str
    __s_file: int
    s_piece: int
    s_color: int
    def __init__(self, r: int, f: int, c: int):
        super().__init__(r, f, c)
        self.s_piece = 5
class king(piece):
    __s_rank: str
    __s_file: int
    s_piece: int
    s_color: int
    def __init__(self, r: int, f: int, c: int):
        super().__init__(r, f, c)
        self.s_piece = 6

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


