/*
* motor speed control demo, using touch and ir
* (c) 2015 warefab
* author : muchiri john
*/

#include <SPI.h>
#include "scratch_n_sketch.h"

char ch[8];

scratch_n_sketch sns;

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
