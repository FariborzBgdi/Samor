from __future__ import division
import time
import Adafruit_PCA9685

#Aktiviert den Spannungsumsetzer vor dem PCA9685
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.OUT, initial=GPIO.HIGH)


# Standardadresse: (0x40).
#pwm = Adafruit_PCA9685.PCA9685()

# Initalisierung mit alternativer Adresse
pwm = Adafruit_PCA9685.PCA9685(address=0x41)

# Einstellen der Minimal- und Maximal-Pulslaengen
servo_min = 150  # Minimale Pulslaenge
servo_max = 600  # Maximale Pulslaenge

# Hilfsfunktion
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000 
    pulse_length /= 50     
    print('{0}us per period'.format(pulse_length))
    pulse_length /= 4096     
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    print(pulse_length)
    pulse /= pulse_length
    print(pulse)
    pulse = round(pulse)
    print(pulse)
    pulse = int(pulse)
    print (pulse)
    pwm.set_pwm(channel, 0, pulse)

# Frequenz auf 50Hz setzen
pwm.set_pwm_freq(50)

print('Bewege Servo auf Kanal 0. Druecke Ctrl+C zum abbrechen...')
while True:
  #  Bewege Servo auf Kanal 0
    start_position = 0.771
    end_position = 1.8
    set_servo_pulse(0,start_position)
    time.sleep(1.5)
    set_servo_pulse(0,end_position)
    time.sleep(1.5)


