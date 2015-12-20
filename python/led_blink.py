#led blinking
from libs.board import *
s = scratch_n_sketch()
s.connect()
s.clearDisplay()
s.setFont(Font.elephant)
s.penColor(255, 255, 0)
count = 0
for x in range(20):
    s.ledWrite(Red, On)
    wait(250)
    s.ledWrite(Red, Off)
    wait(250)
    s.drawText(count, 90, 120)
    count +=1
s.disconnect()
