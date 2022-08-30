import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.D0, board.D1, board.D2, board.D3, board.D6, board.D7 )
    row_pins = (board.D10, board.D9, board.D8)
    diode_orientation = DiodeOrientation.COL2ROW




    # flake8: noqa
    coord_mapping = [
     5,  4,  3,  2,  1,  19, 20, 21, 22, 23, 
    11, 10,  9,  8,  7,  25, 26, 27, 28, 29, 
    17, 16, 15, 14, 13,  31, 32, 33, 34, 35, 
            12,  6,  0,	 18, 24, 30    ]