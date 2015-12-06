/*
 * scratch_n_sketch.h
 *
 * Created: 10/16/2015 05:23:53
 *  Author: Muchiri Mercy
 */ 


#ifndef SCRATCH_N_SKETCH_H_
#define SCRATCH_N_SKETCH_H_

typedef struct {
  uint16_t AngleSensor = 0;
  uint16_t LightSensor = 0;
  uint16_t A1 = 0;
  uint16_t A2 = 0;
  uint8_t Button = 0;
  uint8_t Di1 = 0;
  uint8_t Di2 = 0;
  uint8_t Di3 = 0;
  uint16_t irCode = 0;
  uint16_t TouchX = 0;
  uint16_t TouchY = 0;
  uint8_t TempSensor = 0;
}Sensors;

//swap
#define swap(a,b) ((uint16_t n = b); b = a; a = n;)
//fonts struct
typedef struct {
  char terminal = 'i';
  char ocr      = 'c';
  char peanut   = 'd';
  char comic    = 'o';
  char calibri  = 'f';
  char consolas = 'g';
  char droid    = 's';
  char elephant = 'h';
  char atomic   = 'a';
  char icon_s   = 'p';
}Font;
//rotation struct
typedef struct {
  char rotate_0   = 'p';
  char rotate_90  = 'i';
  char rotate_180 = 'q';
  char rotate_270 = 'n';
}Rotate;

typedef struct {
  char red   = 'r';
  char green  = 'g';
  char blue = 'b';
  char all = 'a';
  char Do1 = '1';
  char Do2 = '2';
  char Do3 = '3';
}Led;

class scratch_n_sketch
{ 
public:
  scratch_n_sketch();
  void begin(uint8_t pin, uint8_t ts=SPI_CLOCK_DIV64);
  void drawText(char *s, uint16_t x, uint16_t y);
  void fillCircle(uint16_t x1, uint16_t y1, uint16_t r);
  void penColor(uint8_t r, uint8_t g, uint8_t b);
  void textBackColor(uint8_t r, uint8_t g, uint8_t b);
  void fillScreen(uint8_t r, uint8_t g, uint8_t b);
  void clearScreen();
  void fillRectangle(uint16_t x1, uint16_t y1, uint16_t x2, uint16_t y2, uint8_t type=0);
  void drawLine(uint16_t x1, uint16_t y1, uint16_t x2, uint16_t y2);
  uint8_t * getSensorData();
  void showImage(uint16_t x, uint16_t y, uint16_t h, uint16_t w, int *image);
  void rgbLed(uint8_t r, uint8_t g, uint8_t b, uint8_t brightness=255);
  void setBrightness(uint8_t b);
  void setFont(char fnt='i');
  void rotateDisplay(char rt='p');
  void ledWrite(char l, uint8_t val);
  void doutWrite(char d, uint8_t val);
  
  Sensors sensor;
  Font font;
  Rotate rotate;
  Led led;
  Led io;
  
  uint16_t height;
  uint16_t width;
  
  private:
  char rot;
  uint8_t sensor_data[50];
  char cmd[50], *p;
  inline void sensorEval();
  float getTemp(uint16_t tp);
  inline void sendHelper();
  /*
  uint16_t AngleSensor;
  uint16_t LightSensor;
  uint16_t DA1;
  uint16_t DA2;
  uint8_t Button;
  uint8_t Di1;
  uint8_t Di2;
  uint8_t Di3;
  uint16_t irCode;
  uint16_t TouchX;
  uint16_t TouchY;
  float TempSensor;*/
};

#endif /* SCRATCH_N_SKETCH_H_ */
