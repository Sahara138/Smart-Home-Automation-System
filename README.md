# Smart-Home-Automation-System
Smart Home Automation is to explore the technical challenges of setting up a cost-effective home automation system and assess its effectiveness in operating household utilities and security devices. This project evaluates the setting up of a smart home automation system employing Python Webserver and a Raspberry Pi. The Raspberry Pi with its powerful CPU allows connection of multiple sensors simultaneously.

SOFTWARE & HARDWARE COMPONENTS:
The various components employed in the home automation system for a cost effective and opensource structure are: 
Raspberry Pi 4
    Raspberry Pi is a low cost, small size computer that runs on Linux OS. Raspberry Pi is used as the local webserver and its General-Purpose Input/Output (GPIO) pins are controlled through a simple webpage.
    
Python Programmer
    Python also has a large collection of libraries, which speeds up the development process. There are libraries for everything you can think of – game programming, rendering graphics, GUI interfaces,webframeworks,and scientific computing. We'll use the RPi.GPIO module as the driving force behind our Python examples. This set of Python files and source is included with Raspbian.
    
Other Hardware Components
  Sensor:
    1. Ultrasonic Sensor
    2. Keypad
    3. PIR Sensor
    4. Temperature Sensor(DHT11)
      
  Switch:
    5v Relay Module
    
  Actuator:
    1. LED/Light
    2. Fan
    3. Buzzer
    4. Servo Motor
    
BLOCK DIAGRAM:
    The block diagram of the proposed architecture as given below depicts the integration of hardware sensors in to the Raspberry Pi computer. The sensors based on environmental inputs send the data to Raspberry Pi which further processes the data. Corresponding values are then fed to the Relay Panel which changes the state of the devices as per the received input.
![image](https://github.com/Sahara138/Smart-Home-Automation-System/assets/117471587/8aee214f-83fd-46ed-81d2-5954f276066b)

System Design:
    For Garage, Ultrasonic sensor which sense the distance of object and Rotate the servo motor. Keypad which sensor input the secret code and turns on the Green/Red LED and Buzzer Which acts as right/wrong password for door lock system. PIR Sensor which sense the motion and turns on the light. For Ventilation, Temperature Sensor which checks the temperature of the house/room and turns on the fan in that house/room.

Conclusion
    Smart home automation system which is the most commercial application which has experimentally verified satisfactorily we have connected the small appliance to it and we were able to control them remotely. This will help the users of any age to control and monitor their home. The smart home automation system was accomplished and functioned smoothly as described in this paper. The structure enabled seamless control of sensors and appliances from a Python based user interface.

