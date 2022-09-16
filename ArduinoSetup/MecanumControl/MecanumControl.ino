
#define MAX_SPEED 70    // max speed in ticks per second
#define DEFAULT_SPEED 30
#define MIN_DUTY 25     // minimal duty cicle for speed
#define ACCEL 1         // acceleration

// PID
#define PID_P 1.0
#define PID_I 0.4
#define PID_D 0.01

// encoder pins
#define OPTO_FL 2  // Front Left
#define OPTO_FR 3  // Front Right
#define OPTO_BL 12  // Back Left
#define OPTO_BR 13  // Back Right

// motor driver pins
// front right motor
#define MOTOR1_A 4
#define MOTOR1_B 5  // pwm
// front left motor
#define MOTOR2_A 7
#define MOTOR2_B 6  // pwm
// back right motor
#define MOTOR3_A 11
#define MOTOR3_B 10  // pwm
// back left motor
#define MOTOR4_A 8
#define MOTOR4_B 9  // pwm

//// motor driver pins
//// front right motor
//#define MOTOR1_A 2
//#define MOTOR1_B 3  // pwm
//// front left motor
//#define MOTOR2_A 4
//#define MOTOR2_B 5  // pwm
//// back right motor
//#define MOTOR3_A 7
//#define MOTOR3_B 6  // pwm
//// back left motor
//#define MOTOR4_A 8
//#define MOTOR4_B 9  // pwm

#include <AccelMotor.h>
AccelMotor motorFL(DRIVER2WIRE, MOTOR2_A, MOTOR2_B, HIGH);
AccelMotor motorBL(DRIVER2WIRE, MOTOR4_A, MOTOR4_B, HIGH);
AccelMotor motorFR(DRIVER2WIRE, MOTOR1_A, MOTOR1_B, HIGH);
AccelMotor motorBR(DRIVER2WIRE, MOTOR3_A, MOTOR3_B, HIGH);

#include "encoder.h"  // mini-class for simple encoder without direction detection
encCounter encFL(OPTO_FL);
encCounter encFR(OPTO_FR);
encCounter encBL(OPTO_BL);
encCounter encBR(OPTO_BR);

//#define MOTOR_TEST

void setup() {
  
  Serial.begin(115200); // Übertragungsgeschwindigkeit 115200 Baud
  
  attachPCINT(OPTO_FL);
  attachPCINT(OPTO_FR);
  attachPCINT(OPTO_BL);
  attachPCINT(OPTO_BR);

//  // pins D3 and D11 - 980 Hz
//  TCCR2B = 0b00000100;  // x64
//  TCCR2A = 0b00000011;  // fast pwm
//
//  // pins D9 and D10 - 976 Hz
//  TCCR1A = 0b00000001;  // 8bit
//  TCCR1B = 0b00001011;  // x64 fast pwm
//
//  TCCR1B=TCCR1B&0xf8|0x01; // Pin9,Pin10 PWM 31250Hz 
//  TCCR2B=TCCR2B&0xf8|0x01; // Pin3,Pin11 PWM 31250Hz 

  motorFR.setMinDuty(MIN_DUTY);
  motorBR.setMinDuty(MIN_DUTY);
  motorFL.setMinDuty(MIN_DUTY);
  motorBL.setMinDuty(MIN_DUTY);

  // FORWARD, BACKWARD, AUTO, STOP, BRAKE
  motorFR.setMode(AUTO);
  motorBR.setMode(AUTO);
  motorFL.setMode(AUTO);
  motorBL.setMode(AUTO);

  // motor controll mode PID_SPEED
  motorFR.setRunMode(PID_SPEED);
  motorBR.setRunMode(PID_SPEED);
  motorFL.setRunMode(PID_SPEED);
  motorBL.setRunMode(PID_SPEED);

  // reverse motor direction
  motorFL.setDirection(REVERSE);
  motorBL.setDirection(REVERSE);
  
  // PID
  motorFR.kp = PID_P;
  motorFL.kp = PID_P;
  motorBR.kp = PID_P;
  motorBL.kp = PID_P;

  motorFR.ki = PID_I;
  motorFL.ki = PID_I;
  motorBR.ki = PID_I;
  motorBL.ki = PID_I;

  motorFR.kd = PID_D;
  motorFL.kd = PID_D;
  motorBR.kd = PID_D;
  motorBL.kd = PID_D;

  // integration period
  motorFR.setDt(30);
  motorBR.setDt(30);
  motorFL.setDt(30);
  motorBL.setDt(30);

    // motor test
#ifdef MOTOR_TEST
  Serial.println("front left");
  motorFL.setSpeed(30);
  delay(2000);
  motorFL.setSpeed(0);
  delay(1000);
  Serial.println("front right");
  motorFR.setSpeed(30);
  delay(2000);
  motorFR.setSpeed(0);
  delay(1000);
  Serial.println("back left");
  motorBL.setSpeed(30);
  delay(2000);
  motorBL.setSpeed(0);
  delay(1000);
  Serial.println("back right");
  motorBR.setSpeed(30);
  delay(2000);
  motorBR.setSpeed(0);
#endif
}

bool currentMode = false; // false -> speed, true -> position

void moveDirection(int _speed = 25, String dir = "ST"){
  if(dir.equals("ST")){       // stop
    motorFL.setTargetSpeed(0);
    motorFR.setTargetSpeed(0);
    motorBL.setTargetSpeed(0);
    motorBR.setTargetSpeed(0);
    Serial.println("stop moving");
  }
  else if(dir.equals("FW")){  // forward
    motorFL.setTargetSpeed(_speed);
    motorFR.setTargetSpeed(_speed);
    motorBL.setTargetSpeed(_speed);
    motorBR.setTargetSpeed(_speed);
    Serial.println("moving forward");
  }
  else if(dir.equals("BW")){  // backward
    motorFL.setTargetSpeed(-_speed);
    motorFR.setTargetSpeed(-_speed);
    motorBL.setTargetSpeed(-_speed);
    motorBR.setTargetSpeed(-_speed);
    Serial.println("moving backward");
  }
  else if(dir.equals("L")){   // left
    motorFL.setTargetSpeed(-_speed);
    motorFR.setTargetSpeed(_speed);
    motorBL.setTargetSpeed(_speed);
    motorBR.setTargetSpeed(-_speed);
    Serial.println("moving left");
  }
  else if(dir.equals("R")){   // right
    motorFL.setTargetSpeed(_speed);
    motorFR.setTargetSpeed(-_speed);
    motorBL.setTargetSpeed(-_speed);
    motorBR.setTargetSpeed(_speed);
    Serial.println("moving right");
  }
  else if(dir.equals("FL")){  // forward-left
    motorFL.setTargetSpeed(0);
    motorFR.setTargetSpeed(_speed);
    motorBL.setTargetSpeed(_speed);
    motorBR.setTargetSpeed(0);
    Serial.println("moving forward-left");
  }
  else if(dir.equals("FR")){  // forward-right
    motorFL.setTargetSpeed(_speed);
    motorFR.setTargetSpeed(0);
    motorBL.setTargetSpeed(0);
    motorBR.setTargetSpeed(_speed);
    Serial.println("moving forward-right");
  }
  else if(dir.equals("BL")){  // backward-left
    motorFL.setTargetSpeed(-_speed);
    motorFR.setTargetSpeed(0);
    motorBL.setTargetSpeed(0);
    motorBR.setTargetSpeed(-_speed);
    Serial.println("moving backward-left");
  }
  else if(dir.equals("BR")){  // backward-right
    motorFL.setTargetSpeed(0);
    motorFR.setTargetSpeed(-_speed);
    motorBL.setTargetSpeed(-_speed);
    motorBR.setTargetSpeed(0);
    Serial.println("moving backward-right");
  }
  else if(dir.equals("RL")){  // rotate left
    motorFL.setTargetSpeed(-_speed);
    motorFR.setTargetSpeed(_speed);
    motorBL.setTargetSpeed(-_speed);
    motorBR.setTargetSpeed(_speed);
    Serial.println("rotating left");
  }
  else if(dir.equals("RR")){  // rotate right
    motorFL.setTargetSpeed(_speed);
    motorFR.setTargetSpeed(-_speed);
    motorBL.setTargetSpeed(_speed);
    motorBR.setTargetSpeed(-_speed);
    Serial.println("rotating right");
  }
  else{                       // unknown command -> stop
    motorFL.setTargetSpeed(0);
    motorFR.setTargetSpeed(0);
    motorBL.setTargetSpeed(0);
    motorBR.setTargetSpeed(0);
    Serial.println("unknown command: stop moving");
  }
}

void updateMotors(){
  motorFR.tick(encFR.update(motorFR.getState()));
  motorBR.tick(encBR.update(motorBR.getState()));
  motorFL.tick(encFL.update(motorFL.getState()));
  motorBL.tick(encBL.update(motorBL.getState()));
}

String inputString = "";

void loop() {

  while(Serial.available() > 0){
    char inChar = (char)Serial.read(); 
    if(inChar != '\n'){
      inputString += inChar;
    }
    
    else 
    {
      moveDirection(DEFAULT_SPEED, inputString);
      inputString = "";
    }  
  }
  updateMotors();
}

// vector PCint
ISR(PCINT0_vect) {  // pins 8-13
  encBR.update(motorBR.getState());
  encBL.update(motorBL.getState());
}
ISR(PCINT2_vect) {  // pins 0-7
  encFR.update(motorFR.getState());
  encFL.update(motorFL.getState());
}

// setup PCINT
uint8_t attachPCINT(uint8_t pin) {
  if (pin < 8) {            // D0-D7 (PCINT2)
    PCICR |= (1 << PCIE2);
    PCMSK2 |= (1 << pin);
    return 2;
  } else if (pin > 13) {    //A0-A5 (PCINT1)
    PCICR |= (1 << PCIE1);
    PCMSK1 |= (1 << pin - 14);
    return 1;
  } else {                  // D8-D13 (PCINT0)
    PCICR |= (1 << PCIE0);
    PCMSK0 |= (1 << pin - 8);
    return 0;
  }
}
