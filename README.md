# Pygame Space_Raiders 🚀

This is a  game that is controlled by the arduino. The game is writen in Python using libraries Pygame and pyserial.


Before running the codes check out the follwing:

# 1. Install the necesary libraries  :

To install pygame in your everonment 

    pip install pygame

Ton install pyserial in your everonment

    pip install pyserial


# 2.  Check the configuration serial 

Check this line:
    arduinoData = serial.Serial("/dev/ttyACM0", 9600)

** You can check the port in Windows by: **

_ Open the Arduino IDE._
_ Click on Tools in the menu bar and select Port from the drop-down menu. _
_ The port that the Arduino is using will be highlighted in the list. Take note of the port number (e.g., COM3). _

