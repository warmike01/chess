class square:
    __s_rank: str
    __s_file: int
    s_piece: int=0
    def __init__(self, r: int, f: int):
        self.s_rank=r
        self.s_file=f
class piece(square):
    __s_rank: str
    __s_file: int
    s_piece: int=-1
    s_color: int #0 for white, 1 for black
    def __init__(self, r: int, f: int, c: int):
        s_color = c
        super().__init__(r, f)
class pawn(piece):
    __s_rank: str
    __s_file: int
    s_piece: int=1
    s_color: int
    def __init__(self, r: int, f: int, c: int):
        s_color = c
        super().__init__(r, f)
class knight(piece):
    __s_rank: str
    __s_file: int
    s_piece: int=2
    s_color: int
    def __init__(self, r: int, f: int, c: int):
        s_color = c
        super().__init__(r, f)
class bishop(piece):
    __s_rank: str
    s_color: int
    s_piece: int=3
    __s_file: int
    def __init__(self, r: int, f: int, c: int):
        s_color = c
        super().__init__(r, f)
class rook(piece):
    __s_rank: str
    __s_file: int
    s_piece: int=4
    s_color: int
    def __init__(self, r: int, f: int, c: int):
        s_color = c
        super().__init__(r, f)
class queen(piece):
    __s_rank: str
    __s_file: int
    s_piece: int=5
    s_color: int
    def __init__(self, r: int, f: int, c: int):
        s_color = c
        super().__init__(r, f)
class king(piece):
    __s_rank: str
    __s_file: int
    s_piece: int=6
    s_color: int
    def __init__(self, r: int, f: int, c: int):
        s_color = c
        super().__init__(r, f)
