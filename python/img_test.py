#Scratch_n_sketch scripting
from libs.board import *
from image_data import *
#init
board = scratch_n_sketch()
#connect board
board.connect()
board.backGroundColor(0, 0, 0)
board.rotateDisplay(board.rotate_0)
console('image demo')

image = studio_7_png
#begin image drawing
#x, y location; image width and height
board.imageBegin(0, 0, 240, 320);
wait(10)
console('image begin')
#upload image data
for x in image:
    #console(hex(x))
    board.imageData(hex(x))
#end
board.imageEnd()

console('image end')
#disconnect
board.disconnect()
