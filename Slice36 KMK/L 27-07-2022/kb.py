import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    row_pins = (board.D10, board.D9, board.D8)
    col_pins = (board.D0, board.D1, board.D2, board.D3, board.D6, board.D7 )
    diode_orientation = DiodeOrientation.COL2ROW




    # flake8: noqa
    coord_mapping = [
     3,  4,  5,  6,  7,   25, 24, 23, 22, 21, 
     8,  9, 10, 11, 12,   30, 29, 28, 27, 26, 
    13, 14, 15, 16, 17,   35, 34, 33, 32, 31, 
            0, 1, 2,	  20, 19, 18
    ]