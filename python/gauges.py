#Scratch_n_sketch scripting
from libs.board import *

board = scratch_n_sketch()

PI = 22/7
#gauge position x,y,radius
gaugePos1 = [64, 64, 63];
gaugePos2 = [gaugePos1[0] * 5 + 8 + 1, gaugePos1[1], gaugePos1[2]]
gaugePos3 = [gaugePos1[0] * 5 + 8 + 1, gaugePos1[1], gaugePos1[2]]

#Radians limit anglemin anglemax
gaugeLimits1 = [150, 390]
gaugeLimits2 = [150, 390]
gaugeLimits3 = [150, 390]

#value containers
gaugeVal1 = [0, -1]
gaugeVal2 = [0, -1]
gaugeVal3 = [0, -1]

def drawLineAngle(x, y, angle, length, cl, offset):
    board.penColor(cl[0], cl[1], cl[2])
    board.drawLine(
		x,
		y,
		int(x + (length * math.cos(angle + offset))),#_angle_offset
		int(y + (length * math.sin(angle + offset))),
		)

def  drawNeedle(val, pos, limits, cl):
    if (val[0] != val[1]):
        len = pos[2] / 1.35;
        angleMax = limits[1] - limits[0];
        drawLineAngle(pos[0], pos[1], map(val[1], 0, 1023, 0, angleMax), len, cl, limits[0]);
        drawLineAngle(pos[0], pos[1], map(val[0], 0, 1023, 0, angleMax), len, cl, limits[0]);
        val[1] = val[0];

    return val[1];


def roundGaugeTicker(vs):
    x = vs[0]
    y =  vs[1]
    r = vs[2]
    frm = vs[3]
    to = vs[4]
    dev = vs[5]
    while (frm <= to) :
        dsec = frm * (PI / 180);
        board.drawLine(
            int(x + (math.cos(dsec) * (r / dev)) + 1),
            int(y + (math.sin(dsec) * (r / dev)) + 1),
            int(x + (math.cos(dsec) * r) + 1),
            int(y + (math.sin(dsec) * r) + 1)
            )
        frm += 30


def drawGauge(pos, limits):
    board.penColor(255, 255, 255)
    board.drawCircle(pos[0], pos[1], pos[2]) #draw instrument container
    board.drawCircle(pos[0], pos[1], pos[2] + 1); #draw instrument container
    roundGaugeTicker([pos[0], pos[1], pos[2], limits[0], limits[1], 1.3]);
    if (pos[2] > 15) :
        #tft.roundGaugeTicker(pos[0], pos[1], pos[2], limits[0] + 15, limits[1] - 15, 1.1); #draw minor ticks
        #roundGaugeTicker(uint16_t x, uint16_t y, uint16_t r, int frm, int to, float dev,uint16_t color)
        roundGaugeTicker([pos[0], pos[1], pos[2], limits[0] + 15, limits[1] - 15, 1.1])


def main():
    #auto find and connect
    board.connect()
    board.backGroundColor(0, 0, 0)

    board.rotateDisplay(board.rotate_0)

    drawGauge(gaugePos1,gaugeLimits1);
    #drawGauge(gaugePos2, gaugeLimits2);
    #drawGauge(gaugePos3,gaugeLimits3);

    while true:
        board.penColor(0, 0, 0)
        board.fillCircle(64, 64, 50)

        gaugeVal1[0] = randomNumber(0, 1023);

        board.penColor(255, 255, 0)
        board.drawText('{:04d}'.format(gaugeVal1[0]), 45, 100)

        """
        gaugeVal2[0] = randomNumber(0, 1023);
        gaugeVal3[0] = randomNumber(0, 1023);
        """
        drawNeedle(gaugeVal1, gaugePos1, gaugeLimits1, [255, 0, 0]);
        """
        gaugeVal2[1] = drawNeedle(gaugeVal2, gaugePos2, gaugeLimits2, [0, 255, 0]);
        gaugeVal3[1] = drawNeedle(gaugeVal3, gaugePos3, gaugeLimits3, [0, 0, 255]);
        """
        wait(500)

if __name__ == "__main__":
  main()
