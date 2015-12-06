#include <SPI.h>
#include "scratch_n_sketch.h"

char ch[8];

scratch_n_sketch sns;
/*
void setup() {
Serial.begin(115200);

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
*/

uint16_t xpos, ypos, count, pc;

void setup(){
  sns.begin(4);
  delay(1000);
  //Serial.begin(115200);
  //colors
  sns.fillScreen(0, 0, 0);
  sns.textBackColor(250, 250, 250);
  sns.penColor(250, 250, 250);
  //oi
  sns.setFont(sns.font.terminal );
  //rotate 0
  sns.rotateDisplay(sns.rotate.rotate_0);
  //buttons
  sns.fillRectangle(10, 250, 115, 300, 1);
  sns.fillRectangle(120, 250, 230, 300, 1);
  //headers
  sns.penColor(255, 0, 0);
  sns.drawText("UP",  50 , 270);
  sns.penColor(0, 255, 0);
  sns.drawText("DOWM", 150 , 270);
  sns.penColor(255, 255, 0);
  sns.textBackColor(0, 0, 0);
  xpos = 0;
  ypos = 0;
  sns.drawText("FAN SPEED", 60, 90);
  sns.penColor(0, 255, 255);
  sns.drawText("%", 165, 130);
  //font
  sns.setFont(sns.font.elephant);
  //loop
  count = 0;
}


void loop(){
  //get sensor data
  sns.getSensorData();
  //get touch x && y pos
  xpos = sns.sensor.TouchX;
  ypos = sns.sensor.TouchY;

  //draw coordinates
  pc = (int)(map(count, 0, 255, 0, 100));
  sprintf(ch, "%03d", pc);
  sns.drawText(ch, 65, 120);
  //increase fan speed
  if (((xpos>169 && xpos<488) && (ypos>746 && ypos<875)) ||
  sns.sensor.irCode == 0x4BB0){
    if(count < 255){
      count+=5;
      sns.doutWrite (sns.io.Do3, count);
    }
  }
  //decrease fan speed
  if (((xpos>532 && xpos<875) && (ypos>746 && ypos<875)) ||
  sns.sensor.irCode == 0x5BA0){
    if(count > 0){
      count-=5;
      //analogWrite(6, count);
      sns.doutWrite(sns.io.Do3, count);
    }
  }
  delay(50);
  if(pc >= 0 && pc<35){
    //sns.ledWrite(sns.led.red, HIGH);
    //sns.ledWrite(sns.led.green, LOW);
    sns.rgbLed(0, 255, 0, 150);
  }else if(pc>=35 && pc<65) 
    sns.rgbLed(0, 0, 255, 150);
  else{
    //sns.ledWrite(sns.led.red, LOW);
    //sns.ledWrite(sns.led.green, HIGH);
    sns.rgbLed(255, 0, 0, 150);
  }
  delay(50);
}
/*
//draw graph : using A0 analog noise
void setup()
{
sns.begin(5);
delay(1000);
Serial.begin(115200);
// position of the line on screen
xpos = 10;
// clear the screen with a pretty color
sns.fillScreen(0, 0, 0);
sns.rotateDisplay(sns.rotate.rotate_90);
sns.penColor(250, 180, 10);
sns.setFont(sns.font.terminal);
sns.drawText("LIGHT SENSOR", 90, 20);
}
int drawHeight;
void loop()
{
// read the sensor and map it to the screen height
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
*/
