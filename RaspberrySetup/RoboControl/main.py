#!/usr/bin/env python3
from __future__ import division
import serial
import paho.mqtt.client as mqtt
from subprocess import call
import time
import Adafruit_PCA9685
import RPi.GPIO as GPIO

SERIAL_PORT = '/dev/ttyUSB0'
SERIAL_BAUDRATE = 9600

USERNAME = "samor"
PASSWORD = "haw"
TOPIC_MECANUM = "mecanum"
TOPIC_MANIPULATOR = "manipulator"
BROKER_ADDRESS = "192.168.0.1"
PORT = 1883

# Initialisierung mit alternativer Adresse
pwm = Adafruit_PCA9685.PCA9685(address=0x41)
 
# Frequenz auf 50Hz setzen
pwm.set_pwm_freq(50)

# Startposition definieren
Motor1Start = 1.6
Motor2Start = 1.7
Motor3Start = 1.7
Motor4Start = 1.5
Motor5Start = 1.4
Motor6Start = 1.5

# Schlafposition
Motor1Sleep = 2.4
Motor2Sleep = 2.2
Motor3Sleep = 1.2
Motor4Sleep = 0.8
Motor5Sleep = 1.4
Motor6Sleep = 2.0

#Minimum und maximum der Servos 
Motor1Minimum = 0.5
Motor2Minimum = 1.1
Motor3Minimum = 0.8
Motor4Minimum = 0.8
Motor5Minimum = 0.5
Motor6Minimum = 1.1

Motor1Maximum = 2.4
Motor2Maximum = 2.2
Motor3Maximum = 1.7
Motor4Maximum = 2.2
Motor5Maximum = 2.5
Motor6Maximum = 2.2

#Motor Initialisierungswerte
Motor1 = 0
Motor2 = 1
Motor3 = 2
Motor4 = 3
Motor5 = 4
Motor6 = 5

Motor1Pulse = Motor1Start
Motor2Pulse = Motor2Start
Motor3Pulse = Motor3Start
Motor4Pulse = Motor4Start
Motor5Pulse = Motor5Start
Motor6Pulse = Motor6Start

# Hilfsfunktion
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000
    pulse_length /= 50
    pulse_length /= 4096
    pulse *= 1000
    pulse /= pulse_length
    pulse = round(pulse)
    pulse = int(pulse)
    pwm.set_pwm(channel, 0, pulse)

# Wertbegrenzung einer Variable zwischen min und max
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def StartPosition():
    global Motor1Pulse
    global Motor2Pulse
    global Motor3Pulse
    global Motor4Pulse
    global Motor5Pulse
    global Motor6Pulse
    print(" manipulator: moving to the start position...")
    #Setze Roboter auf Startposition
    set_servo_pulse(Motor2,Motor2Start)
    time.sleep(0.5)
    set_servo_pulse(Motor3,Motor3Start)
    time.sleep(0.5)
    set_servo_pulse(Motor4,Motor4Start)
    time.sleep(0.5)
    set_servo_pulse(Motor5,Motor5Start)
    time.sleep(0.25)
    set_servo_pulse(Motor1,Motor1Start)
    set_servo_pulse(Motor6,Motor6Start)
    Motor1Pulse = Motor1Start
    Motor2Pulse = Motor2Start
    Motor3Pulse = Motor3Start
    Motor4Pulse = Motor4Start
    Motor5Pulse = Motor5Start
    Motor6Pulse = Motor6Start
    print(" manipulator: reached start position")
    

def Servo1_Links():
    global Motor1Pulse
    NewMotor1 = constrain(Motor1Pulse + 0.1, Motor1Minimum, Motor1Maximum)
    if NewMotor1 != Motor1Pulse:
        set_servo_pulse(Motor1, NewMotor1)
        Motor1Pulse = NewMotor1
        print(" Servo1 position: " + str("%.1f" % Motor1Pulse))
    else:
        print(" Servo1 at max position")

def Servo1_Rechts():
    global Motor1Pulse
    NewMotor1 = constrain(Motor1Pulse - 0.1, Motor1Minimum, Motor1Maximum)
    if NewMotor1 != Motor1Pulse:
        set_servo_pulse(Motor1, NewMotor1)
        Motor1Pulse = NewMotor1
        print(" Servo1 position: " + str("%.1f" % Motor1Pulse))
    else:
        print(" Servo1 at min position")
        
def Servo2_Runter():
    global Motor2Pulse
    NewMotor2 = constrain(Motor2Pulse + 0.1, Motor2Minimum, Motor2Maximum)
    if NewMotor2 != Motor2Pulse:
        set_servo_pulse(Motor2, NewMotor2)
        Motor2Pulse = NewMotor2
        print(" Servo2 position: " + str("%.1f" % Motor2Pulse))
    else:
        print(" Servo2 at max position")
        
def Servo2_Hoch():
    global Motor2Pulse
    NewMotor2 = constrain(Motor2Pulse - 0.1, Motor2Minimum, Motor2Maximum)
    if NewMotor2 != Motor2Pulse:
        set_servo_pulse(Motor2, NewMotor2)
        Motor2Pulse = NewMotor2
        print(" Servo2 position: " + str("%.1f" % Motor2Pulse))
    else:
        print(" Servo2 at min position")
    
def Servo3_Runter():
    global Motor3Pulse
    NewMotor3 = constrain(Motor3Pulse - 0.1, Motor3Minimum, Motor3Maximum)
    if NewMotor3 != Motor3Pulse:
        set_servo_pulse(Motor3, NewMotor3)
        Motor3Pulse = NewMotor3
        print(" Servo3 position: " + str("%.1f" % Motor3Pulse))
    else:
        print(" Servo3 at min position")
        
def Servo3_Hoch():
    global Motor3Pulse
    NewMotor3 = constrain(Motor3Pulse + 0.1, Motor3Minimum, Motor3Maximum)
    if NewMotor3 != Motor3Pulse:
        set_servo_pulse(Motor3, NewMotor3)
        Motor3Pulse = NewMotor3
        print(" Servo3 position: " + str("%.1f" % Motor3Pulse))
    else:
        print(" Servo3 at max position")
        
def Servo4_Runter():
    global Motor4Pulse
    NewMotor4 = constrain(Motor4Pulse - 0.1, Motor4Minimum, Motor4Maximum)
    if NewMotor4 != Motor4Pulse:
        set_servo_pulse(Motor4, NewMotor4)
        Motor4Pulse = NewMotor4
        print(" Servo4 position: " + str("%.1f" % Motor4Pulse))
    else:
        print(" Servo4 at min position")
        
def Servo4_Hoch():
    global Motor4Pulse
    NewMotor4 = constrain(Motor4Pulse + 0.1, Motor4Minimum, Motor4Maximum)
    if NewMotor4 != Motor4Pulse:
        set_servo_pulse(Motor4, NewMotor4)
        Motor4Pulse = NewMotor4
        print(" Servo4 position: " + str("%.1f" % Motor4Pulse))
    else:
        print(" Servo4 at max position")
    
def Servo5_Runter():
    global Motor5Pulse
    NewMotor5 = constrain(Motor5Pulse - 0.1, Motor5Minimum, Motor5Maximum)
    if NewMotor5 != Motor5Pulse:
        set_servo_pulse(Motor5, NewMotor5)
        Motor5Pulse = NewMotor5
        print(" Servo5 position: " + str("%.1f" % Motor5Pulse))
    else:
        print(" Servo5 at min position")
        
def Servo5_Hoch():
    global Motor5Pulse
    NewMotor5 = constrain(Motor5Pulse + 0.1, Motor5Minimum, Motor5Maximum)
    if NewMotor5 != Motor5Pulse:
        set_servo_pulse(Motor5, NewMotor5)
        Motor5Pulse = NewMotor5
        print(" Servo5 position: " + str("%.1f" % Motor5Pulse))
    else:
        print(" Servo5 at max position")
        
def Servo6_Zu():
    global Motor6Pulse
    NewMotor6 = constrain(Motor6Pulse - 0.1, Motor6Minimum, Motor6Maximum)
    if NewMotor6 != Motor6Pulse:
        set_servo_pulse(Motor6, NewMotor6)
        Motor6Pulse = NewMotor6
        print(" Servo6 position: " + str("%.1f" % Motor6Pulse))
    else:
        print(" Servo6 at min position")
        
def Servo6_Auf():
    global Motor6Pulse
    NewMotor6 = constrain(Motor6Pulse + 0.1, Motor6Minimum, Motor6Maximum)
    if NewMotor6 != Motor6Pulse:
        set_servo_pulse(Motor6, NewMotor6)
        Motor6Pulse = NewMotor6
        print(" Servo6 position: " + str("%.1f" % Motor6Pulse))
    else:
        print(" Servo6 at max position")

def AlleServosAus():
    global Motor1Sleep
    global Motor2Sleep
    global Motor3Sleep
    global Motor4Sleep
    global Motor5Sleep
    global Motor6Sleep
    global Motor1Pulse
    global Motor2Pulse
    global Motor3Pulse
    global Motor4Pulse
    global Motor5Pulse
    global Motor6Pulse
    print(" manipulator: moving to sleep position...")
    set_servo_pulse(Motor6,Motor6Sleep)
    time.sleep(1)
    set_servo_pulse(Motor5,Motor5Sleep)
    time.sleep(1)
    set_servo_pulse(Motor4,Motor4Sleep)
    time.sleep(1)
    set_servo_pulse(Motor3,Motor3Sleep)
    time.sleep(1)
    set_servo_pulse(Motor1,Motor1Sleep)
    time.sleep(1)
    set_servo_pulse(Motor2,Motor2Sleep)
    time.sleep(1)
    set_servo_pulse(Motor6,0)
    set_servo_pulse(Motor5,0)
    set_servo_pulse(Motor4,0)
    set_servo_pulse(Motor3,0)
    set_servo_pulse(Motor2,0)
    set_servo_pulse(Motor1,0)

    Motor1Pulse = Motor1Sleep
    Motor2Pulse = Motor2Sleep
    Motor3Pulse = Motor3Sleep
    Motor4Pulse = Motor4Sleep
    Motor5Pulse = Motor5Sleep
    Motor6Pulse = Motor6Sleep

    print(" manipulator: reached sleep position")

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker: " + BROKER_ADDRESS)
    client.subscribe(TOPIC_MECANUM)
    client.subscribe(TOPIC_MANIPULATOR)
    StartPosition()

def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    print("message received: ", msg)
    print("message topic: ", message.topic)

    # beim herunterfahren, soll sichergestellt werden, dass die Platform anhält
    if msg == "shutdown":
        ser.write(("ST" + '\n').encode('utf-8'))
        print(" shutdown system..")
        call("sudo shutdown -h now", shell=True)

    if message.topic == TOPIC_MECANUM:
        ser.write((msg + '\n').encode('utf-8'))
        line = ser.readline().decode('utf-8').rstrip()
        print(" mecanum: " + line)
    if message.topic == TOPIC_MANIPULATOR:
        if msg == "StartPos":
            StartPosition()
        if msg == "S1+":
            Servo1_Links()
        if msg == "S1-":
            Servo1_Rechts()
        if msg == "S2+":
            Servo2_Hoch()
        if msg == "S2-":
            Servo2_Runter()
        if msg == "S3+":
            Servo3_Hoch()
        if msg == "S3-":
            Servo3_Runter()
        if msg == "S4+":
            Servo4_Hoch()
        if msg == "S4-":
            Servo4_Runter()
        if msg == "S5+":
            Servo5_Hoch()
        if msg == "S5-":
            Servo5_Runter()
        if msg == "S6+":
            Servo6_Auf()
        if msg == "S6-":
            Servo6_Zu()
        if msg == "Saus":
            AlleServosAus()

if __name__ == '__main__':
    # connect to the serial port
    ser = serial.Serial(SERIAL_PORT, SERIAL_BAUDRATE)
    ser.reset_input_buffer()
    # connect to a mqtt broker and subscribe for a topic
    client = mqtt.Client()
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER_ADDRESS, PORT)
    client.loop_forever()