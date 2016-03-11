#Scratch_n_sketch scripting
from libs.board import *


#size =  48*48 pixels
#length = 288 bytes
bulb = [
    0x00,0x00,0x7F,0xFE,0x00,0x00,0x00,0x01,0xFF,0xFF,0x80,0x00,0x00,0x01,0xFF,0xFF,0x80,0x00,0x00,0x07,0xFF,0xFF,0xE0,0x00,0x00,0x0F,0xFF,
    0xFF,0xF0,0x00,0x00,0x1F,0xF0,0x0F,0xF8,0x00,0x00,0x3F,0xC0,0x03,0xFC,0x00,0x00,0x3F,0x80,0x01,0xFC,0x00,0x00,0x7F,0x00,0x00,0xFE,0x00,
    0x00,0x7E,0x00,0x00,0x7E,0x00,0x00,0x7E,0x00,0x00,0x7E,0x00,0x00,0x7C,0x00,0xE0,0x3F,0x00,0x00,0xF8,0x00,0xE0,0x1F,0x00,0x00,0xF8,0x00,
    0xE0,0x1F,0x00,0x00,0xF8,0x1C,0xF8,0x1F,0x00,0x00,0xF8,0x7D,0xFE,0x1F,0x00,0x00,0xF8,0xF9,0xDF,0x1F,0x00,0x00,0xF9,0xFB,0xDF,0x9F,0x00,
    0x00,0x7D,0xFB,0xDF,0xBF,0x00,0x00,0x7C,0xFB,0x9F,0x3E,0x00,0x00,0x7E,0x7F,0xBE,0x7E,0x00,0x00,0x7E,0x3F,0xBC,0x7E,0x00,0x00,0x7E,0x07,
    0x00,0x7E,0x00,0x00,0x3F,0x07,0x00,0xFC,0x00,0x00,0x1F,0x87,0x01,0xF8,0x00,0x00,0x1F,0x80,0x01,0xF8,0x00,0x00,0x0F,0xC0,0x03,0xF0,0x00,
    0x00,0x0F,0xC0,0x03,0xF0,0x00,0x00,0x0F,0xC0,0x03,0xF0,0x00,0x00,0x07,0xC0,0x03,0xE0,0x00,0x00,0x07,0xE0,0x07,0xE0,0x00,0x00,0x03,0xE0,
    0x0F,0xC0,0x00,0x00,0x03,0xF0,0x0F,0xC0,0x00,0x00,0x01,0xF0,0x0F,0x80,0x00,0x00,0x01,0xF0,0x0F,0x80,0x00,0x00,0x01,0xF8,0x1F,0x80,0x00,
    0x00,0x01,0xFF,0xFF,0x80,0x00,0x00,0x01,0xFF,0xFF,0x80,0x00,0x00,0x01,0xFF,0xFF,0x80,0x00,0x00,0x00,0xFF,0xFF,0x00,0x00,0x00,0x00,0x7F,
    0xFE,0x00,0x00,0x00,0x00,0x7F,0xFE,0x00,0x00,0x00,0x00,0x7F,0xFE,0x00,0x00,0x00,0x00,0x7F,0xFE,0x00,0x00,0x00,0x00,0x7F,0xFE,0x00,0x00,
    0x00,0x00,0x7F,0xFE,0x00,0x00,0x00,0x00,0x7F,0xFE,0x00,0x00,0x00,0x00,0x7F,0xFE,0x00,0x00,
]

message = [
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x1F,0xFF,0xFF,0xFF,0xFF,0xF8,0x7F,0xFF,0xFF,0xFF,0xFF,0xFE,0xFF,0xFF,0xFF,0xFF,
    0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
    0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xDF,0xFB,0xFF,0xFF,0xFF,0xFF,0x03,0xC0,0xFF,0xFF,0xFF,0xFE,0x03,0x80,0x7F,0xFF,0xFF,0xFC,0x00,0x00,0x3F,0xFF,0xFF,0xF8,0x00,0x00,0x1F,0xFF,
    0xFF,0xF8,0x00,0x00,0x1F,0xFF,0xFF,0xF0,0x00,0x00,0x0F,0xFF,0xFF,0xF8,0x00,0x00,0x1F,0xFF,0xFF,0xF8,0x00,0x00,0x1F,0xFF,0xFF,0xF8,0x00,0x00,0x3F,0xFF,0xFF,0xFE,0x00,0x00,
    0x3F,0xFF,0xFF,0xFE,0x00,0x00,0x7F,0xFF,0xFF,0xFF,0x00,0x00,0xFF,0xFF,0xFF,0xFF,0xC0,0x01,0xFF,0xFF,0xFF,0xFF,0xC0,0x07,0xFF,0xFF,0xFF,0xFF,0xE0,0x0F,0xFF,0xFF,0xFF,0xFF,
    0xF8,0x1F,0xFF,0xFF,0xFF,0xFF,0xF8,0x3F,0xFF,0xFF,0xFF,0xFF,0xFC,0x7F,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
    0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0x7F,0xFF,0xFF,0xFF,0xFF,0xFE,0x3F,0xFF,0xFF,0xFF,0xFF,0xFC,0x07,0xFF,0xFF,0xFF,0xFF,0xE0,0x00,0x00,0x3F,0xFC,
    0x00,0x00,0x00,0x00,0x3F,0xF8,0x00,0x00,0x00,0x00,0x0F,0xF0,0x00,0x00,0x00,0x00,0x03,0xE0,0x00,0x00,0x00,0x00,0x03,0x80,0x00,0x00,0x00,0x00,0x01,0x80,0x00,0x00,0x00,0x00,
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
]
#init
board = scratch_n_sketch()
#connect board
board.connect()
board.backGroundColor(0, 0, 0)
board.penColor(255, 255, 0)
console('icon demo')
#begin image draw
console('image begin')
#upload image data
board.drawBitmap(20,20, bulb, 48, 48, 288)
board.penColor(255, 0, 255)
board.drawBitmap(20,120, message, 48, 48, 288)
#end
console('image end')
#disconnect
board.disconnect()
