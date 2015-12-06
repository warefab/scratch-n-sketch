/*
* touch draw demo
* (c) 2015 warefab
* author : muchiri john
*/
#include <SPI.h>
#include "scratch_n_sketch.h"

char ch[8];

scratch_n_sketch sns;

void setup() {
	sns.begin(5);
	delay(1000);

	sns.fillScreen(15, 167, 255);
	sns.penColor(255, 255, 255);
	sns.fillRectangle(0, 0 , 239, 249);
	sns.textBackColor(15, 167, 255);
	sns.setFont();
	sns.drawText("Temperature", 50, 260);
	delay(10);
}

void loop() {

	sns.penColor(random(10, 255), random(10, 255), random(10, 255));

	sns.getSensorData();

	int tsx = map(sns.sensor.TouchX, 173, 904, 0, 239);
	int tsy = map(sns.sensor.TouchY, 53, 964, 0, 319);

	if(tsx > 0  && tsy > 0)
		sns.fillCircle(tsx, tsy, 2);

	delay(50);

	sns.penColor(255, 255, 0);
	float tp = sns.sensor.TempSensor;
	sprintf(ch, "%03d", (int)tp);
	sns.drawText(ch, 100, 290);
	delay(50);
}
