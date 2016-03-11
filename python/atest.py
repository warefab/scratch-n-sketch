
from libs.board import *

s = scratch_n_sketch()
s.connect()

for x in range(1020):
    s.ledWrite(All, On)
    wait(250)
    s.ledWrite(All, Off)
    wait(250)
s.disconnect()
