import board

from kb import KMKKeyboard

import adafruit_pioasm
import neopixel

from digitalio import DigitalInOut, Direction ,Pull

#from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.lock_status import LockStatus
from kmk.handlers.sequences import simple_key_sequence
from kmk.extensions.RGB import RGB

#pixel_pin = board.NEOPIXEL
#num_pixels = 1
rgb_ext = RGB(pixel_pin = board.NEOPIXEL, num_pixels=1, hue_default= 180, val_limit=10,
              val_default=10, hue_step=18)
#rgb_ext.rgb_config['hue_default']= 200
#rgb_ext.rgb_config['val_limit'] = 50

#pixels=neopixel.NeoPixel(pixel_pin, num_pixels, brightness = 0.05, auto_write=False)

#pixels[0]= (0,255,255)
#pixels.show()

red = DigitalInOut(board.LED_RED)
red.direction = Direction.OUTPUT
red.value = 1

green = DigitalInOut(board.LED_GREEN)
green.direction = Direction.OUTPUT
green.value = 1

blue = DigitalInOut(board.LED_BLUE)
blue.direction = Direction.OUTPUT
blue.value = 1


keyboard = KMKKeyboard()

modtap = ModTap()

mousekeys=MouseKeys()




split_side = SplitSide.RIGHT
#split_side = SplitSide.LEFT

split = Split(split_flip=True,split_type=SplitType.UART, split_side=split_side, use_pio=True,
split_target_left=False, target_left=False, data_pin= board.D5,
data_pin2=board.D4)

layers_ext = Layers()
locks = LockStatus()


keyboard.modules.append(split)
keyboard.modules.append(layers_ext)
keyboard.modules.append(modtap)
keyboard.modules.append(mousekeys)
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(locks)
keyboard.extensions.append(rgb_ext)

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

QWERTY = simple_key_sequence((KC.TO(0),KC.RGB_M_P))
LOWER = KC.MO(1)
RAISE = KC.MO(2)
COMBO = KC.MO(3)
GAME =  simple_key_sequence((KC.TO(4),KC.RGB_M_BR))


#Press and hold for modifiers
HLCtrl = KC.MT(KC.Z, KC.LCTL)
HLAlt = KC.MT(KC.X, KC.LALT)
HLGUI = KC.MT(KC.C, KC.LGUI)

HRCtrl = KC.MT(KC.SLSH, KC.LCTL)
HRAlt = KC.MT(KC.DOT, KC.LALT)
HRGUI = KC.MT(KC.COMM, KC.LGUI)


#Macros 
Scnshot = KC.LGUI(KC.LSFT(KC.S))
TManager = KC.LCTL(KC.LSFT(KC.ESC))
    
NTab = KC.LCTL(KC.TAB)
PTab = KC.LCTL(KC.LSFT(KC.TAB))


keyboard.keymap = [
    [  #QWERTY
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,               KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,    \
        KC.A,    KC.S,    KC.D,    KC.F,    KC.G,               KC.H,    KC.J,    KC.K,    KC.L, KC.QUOT,   \
        HLCtrl,  HLAlt,   KC.C,    KC.V,    KC.B,               KC.N,    KC.M,   HRGUI,   HRAlt,  HRCtrl,   \
                        KC.LSFT,   KC.SPC,  LOWER,              RAISE,   KC.BSPC,  KC.ENT,
    ],
    [  #LOWER
        KC.ESC, KC.PGDOWN, KC.UP,   KC.PGUP,  KC.PERC,         KC.PLUS, KC.N7,  KC.N8, KC.N9,  KC.EQL, \
        KC.CAPS,  KC.LEFT, KC.DOWN, KC.RGHT,  KC.LPRN,         KC.MINS, KC.N4,  KC.N5, KC.N6,  KC.ASTR, \
        XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX,  KC.RPRN,         KC.N0,   KC.N1, KC.N2, KC.N3,  KC.PSLS, \
                             KC.LGUI, XXXXXXX,  LOWER,         COMBO,   KC.DEL,  KC.TAB,
    ],
    [  #RAISE
        KC.TILD, KC.EXLM,  KC.AT, KC.HASH,  KC.DLR,             KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, \
        KC.MUTE, KC.VOLU, NTab, KC.LBRC, KC.LCBR,            KC.COLN, KC.HOME, KC.END, KC.UNDS, KC.PIPE, \
        XXXXXXX, KC.VOLD, PTab, KC.RBRC, KC.RCBR,            KC.SCLN, XXXXXXX, XXXXXXX, XXXXXXX, KC.BSLS, \
                        XXXXXXX,   XXXXXXX,  COMBO,             RAISE,   XXXXXXX, XXXXXXX,
    ],
    
    [  #COMBO
        KC.GRV , KC.F1,   KC.F2,   KC.F3,   KC.F4,           KC.MB_MMB, KC.MB_LMB, KC.MS_UP,KC.MB_RMB,TManager, \
        KC.INS, KC.F5,   KC.F6,   KC.F7,   KC.F8,            KC.MW_UP, KC.MS_LT, KC.MS_DN, KC.MS_RT,Scnshot,   \
        KC.NLCK, KC.F9,   KC.F10,  KC.F11,  KC.F12,          KC.MW_DN,XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,         \
                        GAME,XXXXXXX,XXXXXXX,             XXXXXXX,XXXXXXX,XXXXXXX,
    ],
    
    [  #GAME
        KC.N1 , KC.Q , KC.W , KC.E , KC.R,     KC.MB_MMB, KC.MB_LMB, KC.MS_UP,KC.MB_RMB,XXXXXXX,
        KC.G  , KC.A, KC.S,  KC.D  , KC.F ,    KC.MW_UP, KC.MS_LT, KC.MS_DN, KC.MS_RT,XXXXXXX, 
        KC.LCTL, KC.Z, KC.X, KC.C, KC.V,       KC.MW_DN,XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,
                       KC.LSFT, KC.SPC, LOWER,    XXXXXXX,   XXXXXXX,  QWERTY, 
    ]   
]

class _LockStatus(LockStatus):
    def during_bootup(self, sandbox):
        self.caps_lock_led = blue
    def after_hid_send(self, sandbox):
        super().after_hid_send(sandbox)
        self.caps_lock_led.value = not(self.get_caps_lock())
    
keyboard.extensions.append(_LockStatus())




if __name__ == '__main__':
    keyboard.go()
