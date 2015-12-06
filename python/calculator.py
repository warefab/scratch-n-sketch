"""
" Scratch_n_sketch scripting
"
" calculator example
" (c) 2015 warefab.com
"
"""

from libs.board import *

#create board instance
board = scratch_n_sketch()
#auto find and connect
board.connect()
#colors
board.backGroundColor(10, 150, 150)
board.textBackColor(10, 150, 150)
board.penColor(0, 255, 255)
#rotate 0
board.rotateDisplay(board.rotate_0)
xpos = ypos = t_index = 0;
#font
board.setFont(board.ocr_extended)
#ans panel
board.penColor(5, 250, 5)
board.drawText('scratch_n_sketch', 12, 5)
board.penColor(255, 255, 255)
board.fillRectangle(0, 20, 239, 70)
#font
board.setFont(board.comic_sans)
#button create start #######################################
buttons = ['%', '^', 'C', '/',
           '7', '8', '9', '*',
           '4', '5', '6', '-',
           '1', '2', '3', '+',
           '0', '.', '=']
index = 0
#draw buttons and register touch boundaries
for y in range(4):
    for x in range(4):
        #draw button
        board.drawRoundRectangle(58*x+4, 75+50*y+4, 58*x+58-2, 75+50*y+50-2);
        board.drawText(buttons[index], 58*x+24, 75+50*y+17)
        #register touch coordinates and index
        if (index == 0): t_index = [[58*x+4, 75+50*y+4, 58*x+58-2, 75+50*y+50-2, buttons[index]]]
        else: t_index.append([58*x+4, 75+50*y+4, 58*x+58-2, 75+50*y+50-2, buttons[index]])
        #increment index
        index+=1
#button 0

board.drawRoundRectangle(4, 280, 80, 316)
board.drawText(buttons[index], 35, 292)
t_index.append([4, 280, 80, 316, buttons[index]])
#button .
board.drawRoundRectangle(84, 280, 150, 316)
board.drawText(buttons[index+1], 112, 288)
t_index.append([84, 280, 150, 316, buttons[index+1]])
#button =
board.drawRoundRectangle(154, 280, 230, 316)
board.drawText(buttons[index+2], 185, 292)
t_index.append([154, 280, 230, 316, buttons[index+2]])
#calc panel
board.penColor(5, 5, 5)
board.textBackColor(255, 255, 255)
board.setFont(board.font_big)
nums = ['0', '0']
prevnum = num = ''
mp = ' '
num_index = index = af = ans = err = dec_set= 0
while True:
    board.getSensorData()
    #check button touch coordinates
    if board.TouchX == 0 and board.TouchY == 0:
        xpos = ypos = 0
        prevnum = num = ''
    else:
        #map touch xpos to lcd(0-239)
        xpos = int(map(board.TouchX, 117, 900, 0, 239))
        #map touch ypos to lcd(0-319)
        ypos = int(map(board.TouchY, 87, 890, 0, 319))
    #check button touch
    for button in range(19):
        if(xpos >= t_index[button][0] and  xpos <= t_index[button][2] and
           ypos >= t_index[button][1] and  ypos <= t_index[button][3]):
          num = t_index[button][4]
          break;
    #avoid long press
    if num != prevnum:
        try:
            board.textBackColor(0, 0, 0)
            board.penColor(0, 0, 0)
            board.fillRectangle(0, 20, 239, 70)
            board.penColor(255,255, 5)
            #reject symbol inputs
            if not num in '*/-+%=^C':
                index+=1
                if not (dec_set and num == '.'):
                    if nums[num_index] == '0' and num != '.':
                        nums[num_index] = num
                    else:
                        nums[num_index] += num
                if num == '.':
                    dec_set = 1
            #set symbol
            elif num in '*/-+%^':
                mp = num
                num_index = 1
                if num == '^' : dec_set = 1
                else: dec_set = 0
            #clear everything
            elif num == 'C':
                nums = ['0', '0']
                index = num_index = dec_set = 0
                mp = ' '
            #get answer
            elif num == '=':
                #power sign
                if mp == '^':
                    eqt = 'ans = pow(' + nums[0] + ',' + nums[1] + ')'
                #division check error
                elif mp == '/' and nums[1] == '0':
                    err = 1
                #percent
                elif mp == '%':
                    eqt = 'ans = ' + nums[0] + ' / 100 * ' + nums[1]
                #normal equation
                else:
                    eqt = 'ans = ' + nums[0] + mp + nums[1]
                #show ans
                board.drawText('Ans', 5, 25)
                #show error if found
                if err:
                    board.drawText('Error', 5, 50)
                #show ans if successful
                else:
                    #execute equation
                    exec(eqt)
                    #print to console
                    console('{} = {:.3f}'.format(eqt[6:],ans))
                    #show ans
                    board.drawText('%.3f'%ans, 5, 50)
                #init values
                mp = ' '
                index = num_index = 0
                nums = ['0', '0']
                af = 1;
                err = dec_set = 0
            if af == 0:
                board.drawText(nums[0], 5, 25)
                board.drawText(nums[1], 5, 50)
            af = 0
            board.drawText(mp, 220, 25)
        except:
            pass
        #avoid long press
        prevnum = num
    #wait a bit to process sensor info
    wait(100)
#button create end #######################################
board.disconnect()
