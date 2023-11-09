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

For mostly windows users the port in commonly COM5 port.
You can also check the port your arduino is using by opening the Arduino IDE

