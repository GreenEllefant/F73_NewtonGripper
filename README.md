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
- > 1530us - Extend.
- = 1500us - No movement.
- < 1470us - Retract.

<p align="center"> <img src = img/NewtonGripper_SideViewWithCables.jpg width = 400> </p>
<p align=center> <b> Figure 1: </b> Newton Gripper - Side View with Cables

Questions:
- How fast does the actuator move? Is this a function of the load applied?
- How much force is applied during extension/retraction?
- Does the device have built in hard stops on the extension/retraction?
- What is the best frequency for the pwm? What is the full wave period?
- How does the device behave when there is no power? Does the load pull out the shaft?
- How does the device behave when the signal wire is floating? Does the device still draw power?
- How does the device behave when there is insufficient power supply voltage? Insufficient current?
- How does the device behave when the load has a radial component on the shaft?
    
## STM32 Testing Results (IN PROGRESS)
This section contains the details of the testing done using the STM32 in CalPoly's mechatronics lab using the lab hardware.

Materials:
- PSU
- Nucleo-64, USB-to-Micro cable
- PC running Thonny
- Weights
- Pulley
- Rope

Device Setup:
1. Connect the purple wire to the yellow wire.
2. Press go.
3. Profit.

Test 1:
    This is the description of test 1.

Test 2: 
    This is the description of test 2.
 
etc....

## Arduino Testing Results (IN PROGRESS)
This section contains the details of the arduino code implementation. It also documents our setup including which pin the signal is applied to and how the actuator is connected to power.

...