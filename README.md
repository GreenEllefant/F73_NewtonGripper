# F73_NewtonGripper
<b>Description:</b> Code for testing the Blue Robotics Newton Gripper using micropython and arduino.

<b>Author:</b> Jack Ellsworth
<b>Contributors:</b> 
 

<b>Purpose:</b> Our senior project requires this linear actuator be controlled for testing of an acoustic mooring system. We need to understand the behavior of the Newton Gripper and implement it in our system's release mechanism.

<b>MicroPython:</b> This project contains code for testing the linear actuator using MicroPython on an STM32 board (Nucleo-64). This device will be used for initial testing and qualification.

<b>C++:</b> This project also contains code for testing the linear actuator using C++ on an Arduino Uno R3. This device will be used during mechanical testing including underwater testing.

## Device Specifications
The Newton Gripper has three wires: power, signal, and ground. These can be seen in Figure 1 below. The "guide" section of the device's webpage says to do the following steps, in order:
1. Connect the yellow signal wire to the microcontroller logic, which should be 3.3V. 5V is not accepted.
2. Connect the red power wire to a voltage source, from 9 to 18 volts. Connect the black wire to ground.

To control the device, apply the following pwm pulse sizes:
- \> 1530us - Extend.
- = 1500us - No movement.
- < 1470us - Retract.

<p align="center"> <img src = img/NewtonGripper_SideViewWithCables.jpg width = 400> </p>
<p align=center> <b> Figure 1: </b> Newton Gripper - Side View with Cables

Questions:
- How fast does the actuator move? Is this a function of the load applied?
  - 2 seconds unloaded at 2A current limit
- How much force is applied during extension/retraction?
  - ans
- Does the device have built in hard stops on the extension/retraction?
  - ans
- What is the best frequency for the pwm? What is the full wave period?
  - ans
- How does the device behave when there is no power? Does the load pull out the shaft?
  - ans
- How does the device behave when the signal wire is floating? Does the device still draw power?
  - ans
- How does the device behave when there is insufficient power supply voltage? Insufficient current?
  - ans
- How does the device behave when the load has a radial component on the shaft?
  - ans
    
## STM32 Testing Results (COMPLETE)
This section contains the details of the testing done using the STM32 in CalPoly's mechatronics lab using the lab hardware.

Materials:
- PSU
- Nucleo-64, USB-to-Micro cable
- PC running Thonny
- Newton Gripper

Device Setup:
1. Connect PSU power to Actuator
2. Connect Nucleo to computer
3. Connect PWM from Nucleo to yellow signal

Results:
 Actuator runs in expected pulse range. Disconnecting signal causes actuator to stop the motion.

## Arduino Testing Results (IN PROGRESS)
This section contains the details of the arduino code implementation. It also documents our setup including which pin the signal is applied to and how the actuator is connected to power.

Materials:
- Pulley test rig
- Actuator
- PSU
- Arduino Mega, voltage divider
- Computer
- Weights
- Current Sensor 
  - (https://www.pololu.com/product/2453/pictures)
  - Pololu 0J7387 cs02b white square with green X

Device Setup
1. Connect Arduino to voltage divider and computer
2. Mount Actuator
3. Connect actuator to power
4. Run tests
