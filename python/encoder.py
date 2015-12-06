#Scratch_n_sketch scripting

board = scratch_n_sketch()
board.connect()
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
board.penColor(255, 255, 0)
board.rotateDisplay(board.rotate_0)
#loop checking sensor data
while True:
    #get sensor data
    board.getSensorData()
    #set led on/off according to luminance value
    if board.angleSensor < 512:
        board.ledWrite(Green, On)
    else:
        board.ledWrite(Green, Off)
    #format output
    asn = ''
    if board.angleSensor < 10: asn = '00'
    elif board.angleSensor < 100 : asn = '0'
    #show luminance in display
    board.drawText(
        join('Encoder Value : ', asn+str(board.angleSensor)), 30, 150)
    #wait for 100ms
    wait(100)

board.disconnect()