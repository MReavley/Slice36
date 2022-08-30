import board

from kb import KMKKeyboard

import adafruit_pioasm

#from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

#split_side = SplitSide.RIGHT
split_side = SplitSide.LEFT

split = Split(split_flip=False,split_type=SplitType.UART, split_side=split_side, use_pio=True,
split_target_left=False, target_left=False, data_pin= board.D5,
data_pin2=board.D4)

layers_ext = Layers()

keyboard.modules.append(split)
keyboard.modules.append(layers_ext)
    
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3, board.D6, board.D7 )
keyboard.row_pins = (board.D10, board.D9, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)
ADJUST = KC.LT(3, KC.SPC)



keyboard.keymap = [
    [  #QWERTY
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                     KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  \
        KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                     KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, \
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                     KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, \
                            KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    ],
    [  #LOWER
        KC.ESC,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                         KC.N6,   KC.N7,  KC.N8,   KC.N9,   KC.N0, KC.BSPC,\
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT, XXXXXXX, XXXXXXX,\
        KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
                                            KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    ],
    [  #RAISE
        KC.ESC, KC.EXLM,   KC.AT, KC.HASH,  KC.DLR, KC.PERC,                         KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.BSPC,\
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.MINS,  KC.EQL, KC.LCBR, KC.RCBR, KC.PIPE,  KC.GRV,\
        KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.UNDS, KC.PLUS, KC.LBRC, KC.RBRC, KC.BSLS, KC.TILD,\
                                            KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    ]
]



if __name__ == '__main__':
    keyboard.go()

