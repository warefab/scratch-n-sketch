/*
 * scratch_n_sketch::cpp
 *
 * Created: 10/16/2015 05:23:37
 *  Author: Muchiri Mercy
 */
#include <Arduino.h>
#include <SPI.h>

#include "scratch_n_sketch.h"

//////////////////////////////////////////////////////////////////////////
//init
//////////////////////////////////////////////////////////////////////////
scratch_n_sketch::scratch_n_sketch() :height(320), width(240), rot('p')
{
}
//init/begin
void scratch_n_sketch::begin(uint8_t pin, uint8_t ts)
{
  pinMode(pin, OUTPUT);
  digitalWrite(pin, HIGH);
  SPI.setClockDivider(ts);
  SPI.begin();
  for (int x = 0; x < 3; x++) SPI.transfer(0);
  delay(20);
  digitalWrite(pin, LOW);
  delay(20);
  digitalWrite(pin, HIGH);
  delay(500);
}
//////////////////////////////////////////////////////////////////////////
//send to tft helper
inline void scratch_n_sketch::sendHelper()
{
  p = &cmd[0];
  while (*p)
    SPI.transfer(*p++);
  memset(cmd, 0, sizeof(cmd));
}
//fill rectangle, normal and round
void scratch_n_sketch::drawLine(uint16_t x1, uint16_t y1, uint16_t x2, uint16_t y2)
{
  //(type == 0) ? type = 0xB5 : type = 0xB3;
  sprintf(cmd, "<B5|%d|%d|%d|%d>", x1, y1, x2, y2);
  sendHelper();
}
//////////////////////////////////////////////////////////////////////////
//draw text
void scratch_n_sketch::drawText(char *s, uint16_t x, uint16_t y)
{
  sprintf(cmd, "<A6|%s|%d|%d>", s, x, y);
  p = &cmd[0];
  while (*p)
    SPI.transfer(*p++);
}

//fill circle
void scratch_n_sketch::fillCircle(uint16_t x1, uint16_t y1, uint16_t r)
{
  sprintf(cmd, "<B7|%d|%d|%d>", x1, y1, r);
  p = &cmd[0];
  while (*p)
    SPI.transfer(*p++);
}

//pen color
void scratch_n_sketch::penColor(uint8_t r, uint8_t g, uint8_t b)
{
  sprintf(cmd, "<A7|%d|%d|%d>", r, g, b);
  p = &cmd[0];
  while (*p)
    SPI.transfer(*p++);
}

//text back  color
void scratch_n_sketch::textBackColor(uint8_t r, uint8_t g, uint8_t b)
{
  sprintf(cmd, "<A8|%d|%d|%d>", r, g, b);
  p = &cmd[0];
  while (*p)
  SPI.transfer(*p++);
}

//pen color
void scratch_n_sketch::fillScreen(uint8_t r, uint8_t g, uint8_t b)
{
  sprintf(cmd, "<A9|%d|%d|%d>", r, g, b);
  p = &cmd[0];
  while (*p)
    SPI.transfer(*p++);
}

//clear screen
void scratch_n_sketch::clearScreen()
{
  char *p = &cmd[0];
  while (*p)
    SPI.transfer(*p++);
}

//fill rectangle, normal and round
void scratch_n_sketch::fillRectangle(uint16_t x1, uint16_t y1, uint16_t x2, uint16_t y2, uint8_t type)
{
  (type == 0) ? type = 0xB1 : type = 0xB3;
  sprintf(cmd, "<%X|%d|%d|%d|%d>", type, x1, y1, x2, y2);
  p = &cmd[0];
  while (*p)
    SPI.transfer(*p++);
}

uint8_t *scratch_n_sketch::getSensorData()
{
  uint8_t data;
   
  SPI.transfer(0x02);
  delay(1);
  int index = 0;
  memset(sensor_data, 0, 50);
  while(1) {
    if(index > 50) return 0;
    data = (uint8_t)SPI.transfer(0x01);
    if(data != 'a' && index == 0) continue;
  if(data == '\n') break;
    sensor_data[index++] = data;
  };

  sensorEval();
  return sensor_data;
}

inline void scratch_n_sketch::sensorEval()
{
  uint8_t b_io = 0;
    uint8_t info[50];
  
  memcpy(info, sensor_data, 50); 
    
  strtok((char *)info, ",");

  sensor.AngleSensor = atoi(strtok(NULL, ","));
  sensor.LightSensor = atoi(strtok(NULL, ","));
  sensor.A1 = atoi(strtok(NULL, ","));
  sensor.A2 = atoi(strtok(NULL, ","));
    
  b_io = uint8_t(atoi(strtok(NULL, ",")));
  sensor.Button = ((b_io >> 3) & 1);
  sensor.Di1 = (b_io & 1);
  sensor.Di2 = ((b_io >> 1) & 1);
  sensor.Di3 = ((b_io >> 2) & 1);
    
  sensor.irCode = strtol(strtok(NULL, ","), NULL, 16);
  sensor.TouchX = atoi(strtok(NULL, ","));
  sensor.TouchY = atoi(strtok(NULL, ","));
  sensor.TempSensor = getTemp(atoi(strtok(NULL, ",")));
}

float scratch_n_sketch::getTemp(uint16_t tp)
{
  return ((tp * 0.80566406) - 500) / 10;
}


void scratch_n_sketch::showImage(uint16_t x, uint16_t y, uint16_t h, uint16_t w, int *image)
{
  sprintf(cmd, "<A1|c><A0|%d|%d|%d|%d>", x, y, h, w);
  p = &cmd[0];
  while (*p)
    SPI.transfer(*p++);
  delay(10);
  int *pp = &image[0];
  while (*pp) {
    sprintf(cmd, "<%X>", *pp++);
    p = &cmd[0];
    while (*p)
      SPI.transfer(*p++);
  }
  delay(10);
  sprintf(cmd, "<%X|s>", 0xA1);
  p = &cmd[0];
  while (*p)
    SPI.transfer(*p++);
}

void scratch_n_sketch::rgbLed(uint8_t r, uint8_t g, uint8_t b, uint8_t brightness)
{
  r = (r * brightness) >> 8;
  g = (g * brightness) >> 8;
  b = (b * brightness) >> 8;
  sprintf(cmd, "<E3|%d|%d|%d>", r, g, b);
  p = &cmd[0];
  while (*p)
    SPI.transfer(*p++);
  //delay(5);
}
//change font
void scratch_n_sketch::setFont(char fnt)
{
  sprintf(cmd, "<C1|%c>", fnt);
  sendHelper();
}
//set brightness
void scratch_n_sketch::setBrightness( uint8_t b)
{
  sprintf(cmd, "<E5|%d>", b);
  sendHelper();
}
//set display rotation
void scratch_n_sketch::rotateDisplay(char rt)
{
  if (rt == 'p' || rt == 'q') {
    width = 240; height = 320;
  } else
  {
    width = 320; height = 240;
  }
  rot = rt;
  sprintf(cmd, "<A5|%c>", rt);
  sendHelper();
}

void scratch_n_sketch::ledWrite(char l, uint8_t val)
{
  sprintf(cmd, "<E1|%c|%d>", l, val);
  sendHelper(); 
}

void scratch_n_sketch::doutWrite(char d, uint8_t val)
{
  sprintf(cmd, "<E2|%c|%d>", d, val);
  sendHelper(); 
}

