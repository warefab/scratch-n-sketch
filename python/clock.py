from libs.board import *

board = scratch_n_sketch()

#ccenterx = ccentery = 0#center x,y of the clock
cradius = 80 #radius of the clock
scosConst = 0.0174532925

def drawClockFace():

    board.penColor(25, 255, 155)
    board.fillCircle(ccenterx, ccentery, cradius);
    board.penColor(0, 0, 0)
    board.fillCircle(ccenterx, ccentery, cradius-4);
    #Draw 12 lines
    #console([ccenterx, ccentery])
    board.penColor(0, 0, 255)
    i = 0
    while (i <= 360):
        #console(i)
        sx = math.cos((i-90)*scosConst);
        sy = math.sin((i-90)*scosConst);
        x0 = int(sx*(cradius-4)+ccenterx);
        yy0 = int(sy*(cradius-4)+ccentery);
        x1 = int(sx*(cradius-11)+ccenterx);
        yy1 = int(sy*(cradius-11)+ccentery);
        #console([x0, yy0, x1, yy1])
        board.drawLine(x0, yy0, x1, yy1);
        i+= 30

def main():
    #find and connect board
    board.connect()
    #setup
    board.backGroundColor(0, 0, 0)
    board.textBackColor(0, 0, 0)
    board.setFont(Font.terminal)
    board.rotateDisplay(board.rotate_0)

    global ccenterx
    global ccentery

    ccenterx = 120
    ccentery = 160

    osx = ccenterx;
    osy = ccentery;
    omx = ccenterx;
    omy = ccentery;
    ohx = ccenterx;
    ohy = ccentery;

    drawClockFace() #Draw clock face

    while true:

        hh = int(time.strftime('%H', time.localtime()));
        mm = int(time.strftime('%M', time.localtime()));
        ss = int(time.strftime('%S', time.localtime()));

        sdeg = ss * 6;                  # 0-59 -> 0-354
        mdeg = mm * 6 + sdeg * 0.01666667;  # 0-59 -> 0-360 - includes seconds
        hdeg = hh * 30 + mdeg * 0.0833333;  # 0-11 -> 0-360 - includes minutes and seconds

        hx = math.cos((hdeg-90)*scosConst)
        hy = math.sin((hdeg-90)*scosConst)
        mx = math.cos((mdeg-90)*scosConst)
        my = math.sin((mdeg-90)*scosConst)
        sx = math.cos((sdeg-90)*scosConst)
        sy = math.sin((sdeg-90)*scosConst)

        #Erase just old hand positions
        board.penColor(0, 0, 0)
        board.fillCircle(ccenterx, ccentery, cradius - 14)
        #Draw new hand positions
        board.penColor(255, 255, 255)
        board.drawLine(int(hx*(cradius-56)+ccenterx+1), int(hy*(cradius-28)+ccentery+1), ccenterx+1, ccentery+1);
        board.penColor(255, 0, 255)
        board.drawLine(int(mx*(cradius-34)+ccenterx+1), int(my*(cradius-17)+ccentery+1), ccenterx+1, ccentery+1);
        board.penColor(0, 255, 255)
        board.drawLine(int(sx*(cradius-16)+ccenterx+1), int(sy*(cradius-14)+ccentery+1), ccenterx+1, ccentery+1);
        board.penColor(255, 0, 0)
        board.fillCircle(ccenterx+1, ccentery+1, 3);

        #Update old x&y coords
        osx = sx*(cradius-14)+ccenterx+1
        osy = sy*(cradius-14)+ccentery+1
        omx = mx*(cradius-17)+ccenterx+1
        omy = my*(cradius-17)+ccentery+1
        ohx = hx*(cradius-28)+ccenterx+1
        ohy = hy*(cradius-28)+ccentery+1
        #print time
        board.penColor(255, 255, 0)
        cr = time.strftime('%H:%M:%S', time.localtime())
        board.drawText(cr, 70, 280)
        #wait
        wait(1000)

if __name__ == "__main__":
    main()
