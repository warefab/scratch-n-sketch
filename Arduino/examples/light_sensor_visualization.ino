#include <SPI.h>
#include "scratch_n_sketch.h"

char ch[8];

scratch_n_sketch sns;

uint16_t xpos, ypos, drawHeight;

//draw graph : using A0 analog noise
void setup()
{
	sns.begin(5);
	delay(1000);
	// position of the line on screen
	xpos = 10;
	// clear the screen with a pretty color
	sns.fillScreen(0, 0, 0);
	sns.rotateDisplay(sns.rotate.rotate_90);
	sns.penColor(250, 180, 10);
	sns.setFont(sns.font.terminal);
	sns.drawText("LIGHT SENSOR", 90, 20);
}

void loop()
{
	// read sensors
	sns.getSensorData();
	delay(10);
	drawHeight = (int)(map(sns.sensor.LightSensor, 0, 1023, 10, sns.height-60));
	// draw a line in a nice color
	sns.drawLine(xpos, sns.height - 10, xpos, sns.height - drawHeight);
	sprintf(ch, "%04d", sns.sensor.LightSensor);
	sns.penColor(10, 180, 250);
	sns.drawText(ch, 140, 40);
	sns.penColor(250, 180, 10);
	// if the graph has reached the screen edge
	// erase the screen and start again
	if (xpos >= sns.width) {
		xpos = 10;
		sns.fillScreen(0, 0, 0);
		sns.drawText("LIGHT SENSOR", 90, 20);
	}
	else {
	// increment the horizontal position:
		xpos++;
	}
	delay(100);
}
