
s = scratch_n_sketch()
s.connect()
for x in range(20):
    s.ledWrite(Red, On)
    wait(250)
    s.ledWrite(Red, Off)
    wait(250)
s.disconnect()
