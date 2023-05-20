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
