# Pygame Space_Raiders 🚀

This is a  game that is controlled by the arduino with a ***JOYSTICK***. The game is writen in Python using libraries Pygame and pyserial.

Before running the codes check out the follwing:

# 1. Setting up the Arduino & Check the Configuration

Connect the Arduino to your computer using a USB cable 

Connect the **Joystick** to the arduino 

The **+5V** and **GND** on the joystick are connected to the Arduino respectively the same way

Open the **Joystick.ino** file in the Arduino IDE and check out if:

    int JSx = A0; // VRx value on the Jostick is connected to A0 on the Arduino
    int JSy = A2; // VRy value on the Jostick is connected to A2 on the Arduino
    int JSpin = 9; // Sw value on the Jostick is connected to 9 on the Arduino


After customizing the File ***Upload*** it to the Arduino Uno and exit.

# 2. Install the necesary libraries:

To install pygame in your everonment 

    pip install pygame

Ton install pyserial in your everonment

    pip install pyserial


# 3.  Check the configuration serial 

Check this line:

    arduinoData = serial.Serial("/dev/ttyACM0", 9600)

**You can check the port by:**

1.Open the Arduino IDE.

2.Click on Tools in the menu bar and select Port from the drop-down menu.

3.The port that the Arduino is using will be highlighted in the list. Take note of the port number (e.g., COM3).

**Alternatively in linux  you can check the port number by:**

1.Open a terminal window.

2.Run the following command to list all the serial ports:

    ls /dev/tty*

3.Look for a port name that starts with ***/dev/ttyUSB*** or ***/dev/ttyACM***. The number at the end may vary depending on your system and the number of connected devices.

4.Take note of the port name (e.g., /dev/ttyUSB0 or /dev/ttyACM1) that the Arduino is using.



# Running the Project  🥳

After making sure that all the Files and settings are well configured, you can run the project by running the **main.py** file using the following command:

    python main.py

Or use your Text Editor to run the project if it is capable of doig so! 😂



# Check out how it looks 😱

![The sample output of the awesome game ](https://github.com/Chiesa14/Pygame_Space-Raiders/blob/main/output.png)