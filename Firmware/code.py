#
# ███████  ██████  ██████   █████  ██████  ██████      ███████ ██     ██ 
# ██      ██    ██ ██   ██ ██   ██ ██   ██ ██   ██     ██      ██     ██ 
# █████   ██    ██ ██████  ███████ ██████  ██   ██     █████   ██  █  ██ 
# ██      ██    ██ ██   ██ ██   ██ ██   ██ ██   ██     ██      ██ ███ ██ 
# ███████  ██████  ██████  ██   ██ ██   ██ ██████      ██       ███ ███  
#                         
## Written by viniciusbrit
## Firmware v1.2

print("Starting")
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

split = Split(split_type=SplitType.UART, split_side=None, data_pin=board.GP9, data_pin2=board.GP8, uart_flip=True, use_pio=True)
keyboard.modules.append(split)

keyboard.modules.append(Layers())

### Key Matrix and Diodes
keyboard.col_pins = (board.GP10,board.GP11,board.GP12,board.GP13,board.GP14) 
keyboard.row_pins = (board.GP2,board.GP3,board.GP4,board.GP5)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

### Home Row Hold-Taps
ATAP = KC.HT(KC.A,KC.LGUI)
STAP = KC.HT(KC.S,KC.LALT)
DTAP = KC.HT(KC.D,KC.LCTL)
FTAP = KC.HT(KC.F,KC.LSFT)
JTAP = KC.HT(KC.J,KC.LSFT)
KTAP = KC.HT(KC.K,KC.LCTL)
LTAP = KC.HT(KC.L,KC.LALT)
SCOLTAP = KC.HT(KC.SCLN,KC.LGUI)

### Keymap
keyboard.keymap = [
    # QWERTY LAYER
    [
    KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P,
    ATAP, STAP, DTAP, FTAP, KC.G, KC.H, JTAP, KTAP, LTAP, SCOLTAP,
    KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.END, KC.HOME, KC.DEL,
    KC.MO(1), KC.SPC, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.BSPC, KC.ENTER,
    ],
    # NUMBERS & SYMBOLS LAYER
    [
    KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6,KC.N7, KC.N8, KC.N9, KC.N0,
    KC.DLR, KC.PLUS, KC.LPRN, KC.RPRN, KC.AT, KC.PIPE, KC.MINUS, KC.PEQL, KC.UNDS, KC.ASTR,
    KC.EXLM, KC.HASH, KC.LCBR, KC.RCBR, KC.TILD, KC.AMPR, KC.LBRC, KC.RBRC, KC.PERC, KC.CIRC,
    KC.MO(1), KC.TRNS, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.TRNS, KC.TRNS,
    ],
]

if __name__ == '__main__':
    keyboard.go()
