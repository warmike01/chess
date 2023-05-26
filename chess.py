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
                p=pawn(self, rank_number, file_number, 1)
                rank.append(p)
                file_number += 1
            elif c == 'p':
                p=pawn(self, rank_number, file_number, 0)
                rank.append(p)
                file_number += 1
            elif c == 'N':
                p=knight(self, rank_number, file_number, 1)
                rank.append(p)
                file_number += 1
            elif c == 'n':
                p=knight(self, rank_number, file_number, 0)
                rank.append(p)
                file_number += 1
            elif c == 'B':
                p=bishop(self, rank_number, file_number, 1)
                rank.append(p)
                file_number += 1
            elif c == 'b':
                p=bishop(self, rank_number, file_number, 0)
                rank.append(p)
                file_number += 1
            elif c == 'R':
                p=rook(self, rank_number, file_number, 1)
                rank.append(p)
                file_number += 1
            elif c == 'r':
                p=rook(self, rank_number, file_number, 0)
                rank.append(p)
                file_number += 1
            elif c == 'Q':
                p=queen(self, rank_number, file_number, 1)
                rank.append(p)
                file_number += 1
            elif c == 'q':
                p=queen(self, rank_number, file_number, 0)
                rank.append(p)
                file_number += 1
            elif c == 'K':
                p=king(self, rank_number, file_number, 1)
                rank.append(p)
                file_number += 1
            elif c == 'k':
                p=king(self, rank_number, file_number, 0)
                rank.append(p)
                file_number += 1
        self.board_state.insert(0, deepcopy(rank))
        self.turn = (int(fen[5]) - 1) *2 +1
        if fen[1] == 'b':
            self.turn += 1
class piece(square):
    __s_board: board
    __s_rank: str
    __s_file: int
    s_piece: int=-1
    s_color: int #1 for white, 0 for black
    def __init__(self, b: board, r: int, f: int, c: int):       
        super().__init__(r, f)
        self.s_board = b
        self.s_piece = 0
        self.s_color = c
    def move(self, t_rank,t_file):
        if self.s_board.board_state[t_rank][t_file].s_piece != 0: 
            if self.s_board.board_state[t_rank][t_file].s_color ==  self.s_color:
                raise SelfCapture()
        self.s_board.board_state[self.s_rank][self.s_file] = square(self.s_rank, self.s_file)
        self.s_file=t_file
        self.s_rank=t_rank
        self.s_board.board_state[t_rank][t_file]=self
class pawn(piece):
    __s_board: board
    __s_rank: str
    __s_file: int
    s_piece: int
    s_color: int
    def __init__(self, b: board, r: int, f: int, c: int):
        super().__init__(b, r, f, c)
        self.s_piece = 1
    def move(self, t_rank,t_file):
        if self.s_color == 1:
            if self.s_file == t_file and t_rank - self.s_rank == 1:
                if self.s_board.board_state[t_rank][t_file].s_piece == 0:
                    super().move(t_rank, t_file)
                else:
                    raise PawnIllegalMove
            elif self.s_file == t_file and t_rank - self.s_rank == 2:
                if self.s_board.board_state[t_rank][t_file].s_piece == 0 and self.s_rank == 1:
                    if self.s_board.board_state[2][t_file].s_piece == 0:
                        super().move(t_rank, t_file)
                    else:
                        raise PawnIllegalMove
                else:
                    raise PawnIllegalMove
            elif abs(t_file - self.s_file) == 1 and t_rank - self.s_rank == 1:
                if self.s_board.board_state[t_rank][t_file].s_piece != 0:
                    super().move(t_rank, t_file)
                else:
                    raise PawnIllegalMove
            else:
                raise PawnIllegalMove
        else:
            if self.s_file == t_file and t_rank - self.s_rank == -1:
                if self.s_board.board_state[t_rank][t_file].s_piece == 0:
                    super().move(t_rank, t_file)
                else:
                    raise PawnIllegalMove
            elif self.s_file == t_file and t_rank - self.s_rank == -2:
                if self.s_board.board_state[t_rank][t_file].s_piece == 0 and self.s_rank == 6:
                    if self.s_board.board_state[5][t_file].s_piece == 0:
                        super().move(t_rank, t_file)
                    else:
                        raise PawnIllegalMove
                else:
                    raise PawnIllegalMove
            elif abs(t_file - self.s_file) == 1 and t_rank - self.s_rank == -1:
                if self.s_board.board_state[t_rank][t_file].s_piece != 0:
                    super().move(t_rank, t_file)
                else:
                    raise PawnIllegalMove
            else:
                raise PawnIllegalMove
class knight(piece):
    __s_board: board
    __s_rank: str
    __s_file: int
    s_piece: int
    s_color: int
    def __init__(self, b: board, r: int, f: int, c: int):
        super().__init__(b, r, f, c)
        self.s_piece = 2
    def move(self, t_rank,t_file):
        if abs(self.s_rank - t_rank) == 2 and abs(self.s_file - t_file) == 1:
            super().move(t_rank, t_file)
        elif abs(self.s_rank - t_rank) == 1 and abs(self.s_file - t_file) == 2:
            super().move(t_rank, t_file)
        else:
            raise KnightIllegalMove
class bishop(piece):
    __s_board: board
    __s_rank: str
    s_color: int
    s_piece: int
    __s_file: int
    def __init__(self, b: board, r: int, f: int, c: int):
        super().__init__(b, r, f, c)
        self.s_piece = 3
    def move(self, t_rank,t_file):
        if self.s_rank - t_rank == self.s_file - t_file:
            if self.s_rank < t_rank:
                for i in range(1, abs(self.s_rank - t_rank)):
                    if self.s_board.board_state[self.s_rank+i][self.s_file+i].s_piece != 0:
                        raise BishopIllegalMove
                else:
                    super().move(t_rank, t_file)
            else:
                for i in range(1, self.s_rank - t_rank):
                    if self.s_board.board_state[self.s_rank-i][self.s_file-i].s_piece != 0:
                        raise BishopIllegalMove
                else:
                    super().move(t_rank, t_file)
        elif self.s_rank - t_rank == -( self.s_file - t_file):
            if self.s_rank < t_rank:
                for i in range(1, abs(self.s_rank - t_rank)):
                    if self.s_board.board_state[self.s_rank+i][self.s_file-i].s_piece != 0:
                        raise BishopIllegalMove
                else:
                    super().move(t_rank, t_file)
            else:
                for i in range(1, self.s_rank - t_rank):
                    if self.s_board.board_state[self.s_rank-i][self.s_file+i].s_piece != 0:
                        raise BishopIllegalMove
                else:
                    super().move(t_rank, t_file)
        else:
            raise BishopIllegalMove

class rook(piece):
    __s_board: board
    __s_rank: str
    __s_file: int
    s_piece: int
    s_color: int
    def __init__(self, b: board, r: int, f: int, c: int):
        super().__init__(b, r, f, c)
        self.s_piece = 4
    def move(self, t_rank,t_file):
        if self.s_rank == t_rank:
            if self.s_file > t_file:
                for i in range(t_file+1, self.s_file):
                    if self.s_board.board_state[t_rank][i].s_piece != 0:
                        raise RookIllegalMove
                else:
                    super().move(t_rank, t_file)
            else:
                for i in range(self.s_file+1, t_file):
                    if self.s_board.board_state[t_rank][i].s_piece != 0:
                        raise RookIllegalMove
                else:
                    super().move(t_rank, t_file)
        elif self.s_file == t_file:
            if self.s_rank > t_rank:
                for i in range(t_rank+1, self.s_rank):
                    if self.s_board.board_state[i][t_file].s_piece != 0:
                        raise RookIllegalMove
                else:
                    super().move(t_rank, t_file)
            else:
                for i in range(self.s_rank+1, t_rank):
                    if self.s_board.board_state[i][t_file].s_piece != 0:
                        raise RookIllegalMove
                else:
                    super().move(t_rank, t_file)
        else:
            raise RookIllegalMove
class queen(piece):
    __s_board: board
    __s_rank: str
    __s_file: int
    s_piece: int
    s_color: int
    def __init__(self, b: board, r: int, f: int, c: int):
        super().__init__(b, r, f, c)
        self.s_piece = 5
    def move(self, t_rank,t_file):
            if self.s_rank == t_rank:
                if self.s_file > t_file:
                    for i in range(t_file+1, self.s_file):
                        if self.s_board.board_state[t_rank][i].s_piece != 0:
                            raise QueenIllegalMove
                    else:
                        super().move(t_rank, t_file)
                else:
                    for i in range(self.s_file+1, t_file):
                        if self.s_board.board_state[t_rank][i].s_piece != 0:
                            raise QueenIllegalMove
                    else:
                        super().move(t_rank, t_file)
            elif self.s_file == t_file:
                if self.s_rank > t_rank:
                    for i in range(t_rank+1, self.s_rank):
                        if self.s_board.board_state[i][t_file].s_piece != 0:
                            raise QueenIllegalMove
                    else:
                        super().move(t_rank, t_file)
                else:
                    for i in range(self.s_rank+1, t_rank):
                        if self.s_board.board_state[i][t_file].s_piece != 0:
                            raise QueenIllegalMove
                    else:
                        super().move(t_rank, t_file)
            elif self.s_rank - t_rank == self.s_file - t_file:
                if self.s_rank < t_rank:
                    for i in range(1, abs(self.s_rank - t_rank)):
                        if self.s_board.board_state[self.s_rank+i][self.s_file+i].s_piece != 0:
                            raise QueenIllegalMove
                    else:
                        super().move(t_rank, t_file)
                else:
                    for i in range(1, self.s_rank - t_rank):
                        if self.s_board.board_state[self.s_rank-i][self.s_file-i].s_piece != 0:
                            raise QueenIllegalMove
                    else:
                        super().move(t_rank, t_file)
            elif self.s_rank - t_rank == -( self.s_file - t_file):
                if self.s_rank < t_rank:
                    for i in range(1, abs(self.s_rank - t_rank)):
                        if self.s_board.board_state[self.s_rank+i][self.s_file-i].s_piece != 0:
                            raise QueenIllegalMove
                    else:
                        super().move(t_rank, t_file)
                else:
                    for i in range(1, self.s_rank - t_rank):
                        if self.s_board.board_state[self.s_rank-i][self.s_file+i].s_piece != 0:
                            raise QueenIllegalMove
                    else:
                        super().move(t_rank, t_file)
            else:
                raise QueenIllegalMove
class king(piece):
    __s_board: board
    __s_rank: str
    __s_file: int
    s_piece: int
    s_color: int
    def __init__(self, b: board, r: int, f: int, c: int):
        super().__init__(b, r, f, c)
        self.s_piece = 6
    def move(self, t_rank, t_file):
        if abs(self.s_rank - t_rank) <= 1 and abs(self.s_file- t_file) <= 1:
            super().move(t_rank, t_file)
        else:
            raise KingIllegalMove
    


