import threading
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
#for GPIO BCM mode and for warning deletion
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
################
#gpio pin for sensors

#temparature pin
DHT_PIN = 14

#ultrasonic pin
GPIO_TRIGGER = 18
GPIO_ECHO = 24

#keypad pins
# These are the four rows and columns
L1 = 25
L2 = 8
L3 = 7
L4 = 1

C1 = 5
C2 = 6
C3 = 13
C4 = 19
##################
#for tempsensor
SENSOR_PIN = 15
####################

#####GPIO Setup and pins for LED and buzzer


#for temperature sensor
#for temperature sensor
GPIO.setup(27,GPIO.OUT)
GPIO.output(27,GPIO.LOW)


 

GPIO.setup(SENSOR_PIN, GPIO.IN)


GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

GPIO.setup(26,GPIO.OUT)

DHT_SENSOR = Adafruit_DHT.DHT11




    
#for ultra sonic sensor

 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.setup(21,GPIO.OUT)
p = GPIO.PWM(21, 50) # GPIO 17 for PWM with 50Hz
p.start(6) # Initialization

###############################

#for pir sensor
def my_callback(channel):
    # Here, alternatively, an application / command etc. can be started.
    print('There was a movement!')
    GPIO.output(16,GPIO.HIGH)
    time.sleep(10)
    GPIO.output(16,GPIO.LOW)
#######################################

#for actuator fan
def fanon():
    time.sleep(2)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(26,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(26,GPIO.LOW)
###########################
####for servo motor
def rotateShutter():
 # GPIO 17 for PWM with 50Hz
     p.ChangeDutyCycle(6.5)
     time.sleep(0.1)
     p.ChangeDutyCycle(7)
     time.sleep(0.1)
     p.ChangeDutyCycle(7.5)
     time.sleep(0.1)
     p.ChangeDutyCycle(8)
     time.sleep(0.1)
     p.ChangeDutyCycle(8.5)
     time.sleep(0.1)
     p.ChangeDutyCycle(9)
     time.sleep(0.1)
     p.ChangeDutyCycle(9.5)
     time.sleep(0.1)
     p.ChangeDutyCycle(10)
     time.sleep(0.1)
     p.ChangeDutyCycle(10.5)
     time.sleep(0.1)
     p.ChangeDutyCycle(11)
     time.sleep(0.1)
     p.ChangeDutyCycle(11.5)
     time.sleep(0.1)
     p.ChangeDutyCycle(12)
     time.sleep(5)
     p.ChangeDutyCycle(6)
          
# for ultra sonic sensor ##########
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
####################################

#for keypad
# The GPIO pin of the column of the key that is currently
# being held down or -1 if no key is pressed
keypadPressed = -1
secretCode = "4789"
input = ""
# Setup GPIO

GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

# Use the internal pull-down resistors
GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# This callback registers the key that was pressed
# if no other key is currently pressed
def keypadCallback(channel):
    global keypadPressed
    if keypadPressed == -1:
        keypadPressed = channel

# Detect the rising edges on the column lines of the
# keypad. This way, we can detect if the user presses
# a button when we send a pulse.
GPIO.add_event_detect(C1, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C2, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C3, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C4, GPIO.RISING, callback=keypadCallback)

# Sets all lines to a specific state. This is a helper
# for detecting when the user releases a button
def setAllLines(state):
    GPIO.output(L1, state)
    GPIO.output(L2, state)
    GPIO.output(L3, state)
    GPIO.output(L4, state)

def checkSpecialKeys():
    global input
    pressed = False

    GPIO.output(L3, GPIO.HIGH)

    if (GPIO.input(C4) == 1):
        print("Input reset!");
        pressed = True

    GPIO.output(L3, GPIO.LOW)
    GPIO.output(L1, GPIO.HIGH)

    if (not pressed and GPIO.input(C4) == 1):
        if input == secretCode:
           GPIO.output(9, GPIO.HIGH)
           time.sleep(5)
           GPIO.output(9, GPIO.LOW)
        else:
            GPIO.output(10, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(10, GPIO.LOW)            
        pressed = True

    GPIO.output(L3, GPIO.LOW)

    if pressed:
        input = ""

    return pressed

# reads the columns and appends the value, that corresponds
# to the button, to a variable
def readLine(line, characters):
    global input
    # We have to send a pulse on each line to
    # detect button presses
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        input = input + characters[0]
    if(GPIO.input(C2) == 1):
        input = input + characters[1]
    if(GPIO.input(C3) == 1):
        input = input + characters[2]
    if(GPIO.input(C4) == 1):
        input = input + characters[3]
    GPIO.output(line, GPIO.LOW)
    

#functions for sensor running
def doorlock():
    global keypadPressed
    while True:    
        # If a button was previously pressed,
        # check, whether the user has released it yet
        if keypadPressed != -1:
            setAllLines(GPIO.HIGH)
            if GPIO.input(keypadPressed) == 0:
                keypadPressed = -1
            else:
                time.sleep(0.1)
        # Otherwise, just read the input
        else:
            if not checkSpecialKeys():
                readLine(L1, ["1","2","3","A"])
                readLine(L2, ["4","5","6","B"])
                readLine(L3, ["7","8","9","C"])
                readLine(L4, ["*","0","#","D"])
                time.sleep(0.1)
            else:
                time.sleep(0.1)
def shutterUp():
    while True:
        time.sleep(2)
        dist = distance()
        print ("Measured Distance = %.1f cm" % dist)
        if dist < 24.0:
            rotateShutter()
            time.sleep(0.5)

def ventilation():
    while True:
       #for temperature and humidity sensing
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
            if temperature < 26:
                fanon()
    
def homeLed():
  while True:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=my_callback)
###############################################################################

#methods for threading
x = threading.Thread(target = doorlock,args=())
x.start()
y = threading.Thread(target = shutterUp,args=())
y.start()
z = threading.Thread(target = ventilation,args=())
z.start()
f = threading.Thread(target = homeLed,args = ())
f.start()
########################################

#marging Threads for a single cpu
x.join()
y.join()
z.join()
f.join()
#################