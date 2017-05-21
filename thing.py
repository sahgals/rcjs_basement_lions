 #include <Sweep.h>
#include <SPI.h>
#include <Pixy.h>
#include <servo.h>

Pixy pixy;
Servo first, Servo second, Servo third, Servo fourth;

int angle;
int reverseangle;

int set1 = 90;
int set2 = 90;
int set3 = 91;
int set4 = 91;

int setl1 = 9.8299;
int setl2 = 9.8229;
int setl3 = 9.83;
int setl4 = 9.83;

int anglea = 45;
int angleb = 45;
int anglec = 32;
int angled = 32;

int lengtha;
int lenghtb;
int lenghtc;
int lenghtd;

int anglee;
int anglef;
int angleg;
int angleh;

int zone;

int sindiv1;
int sindiv2;

int basehundred;
int finallenghts[3];

int speedA, speedB, speedC, speedD;

long lenToSpeed(int len) {
  int robotSpeed = (1660 * len) / 100
}
void setup()
{
  first.attach(2);
  second.attach(3);
  thied.attach(4);
  fourth.attach(5);
  Serial.begin(9600);
  Pixy.init;
  

}

void loop()
{
  //basecontrol
  if (angle > 180)
  {
    reversangle = angle - 180;
  }
  else if (angle < 180)
  {
    reversangle = angle + 180;
  }
  else if (angle == 180)
  {
    reversangle = 0;
  }


  if (angle >= 315 || angle <= 45)
  {
    zone = 1;
  }
  else if (angle >= 54 || angle <= angled)
  {
    zone = 2;
  }

  if (zone == 1)
  {
    anglea = set1 + angle;
    angleb = set2 - angle;
    angled = set3 - reversangle;
    anglec = set4 - reversanggle;
  }
  else if (zone == 2)
  {
    anglea = set1 - angle;
    angleb = set2 + angle;
    angled = set3 - reversangle;
    anglec = set4 - reversangle;
  }

  lengtha = setl1 * tan(anglea);
  
  lengthb = setl2 * tan(angleb);

  sindiv1 = sin(angleg) / setl3;
  lengthd = sin(angled) / sindiv1;

  sindiv2 = sin(angleh) / setl4;
  lenghtd = sin(angled) / sindiv2;

  finallenghts[0] = lengtha;
  finallenghts[1] = lenghtb;
  finallengths[2] = lengthc;
  finallengths[3] = lenghtd;

  first.writeMicroseconds(lenToSpeed(finallengths[0]));
  second.writeMicroseconds(lenToSpeed(finallengths[1]));
  third.writeMicroseconds(lenToSpeed(finallengths[2]));
  fourth.writeMicroseconds(lenToSpeed(finallengths[3]));

  
}
