#led blinking
from libs.board import *
s = scratch_n_sketch()
s.connect()
while(True):
    s.ledWrite(Red, On)
    wait(1000)
    s.ledWrite(Red, Off)
    wait(1000)
s.disconnect()
