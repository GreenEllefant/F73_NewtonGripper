'''! @NewtonGripper.py
    This file contains the class for controlling the Blue Robotics Newton Gripper's linear actuator.
    
    @author Jack Ellsworth
    @date 2023.03.23
'''

import pyb

class NewtonGripper:
    '''! This class controls a Blue Robotics Newton Gripper.'''
    def __init__ (self, pwmPin, timer):
        '''! Creates a NewtonGripper object to control the actuator.
            @param pwmPin The pin object set up for timer channel output, aka the pwm logic
            @param timer  An uninitialized timer object for handling the pwm timing. Timer number must be specified before passing to NewtonGripper. Will use channel 1 (make sure pwmPin is ok for use with channel 1 on this timer)
        '''
        # Store given parameters
        self.pin = pwmPin
        self.timer = timer
        
        # Save these values for use in functions
        self.status = 0         # Reports which mode the actuator is in
        self.prescaler = 9      # Value for the timer's prescaler
        self.period = 12000     # Value for the timer's AR (auto reload)
                
        # Initialize timer to use channel 1 with PWM centered
        self.timer.deinit()
        self.timer.init(prescaler=self.prescaler, period=self.period, mode=pyb.Timer.CENTER)
        self.ch1 = self.timer.channel(1, mode=pyb.Timer.PWM, pin=self.pin)
        
        
    def extend(self):
        '''! Runs the pwm signal to cause the actuator to extend.'''
        self.status = 1
        self.ch1.pulse_width(7000)   # 7000 ticks = 1.7510ms on oscilloscope
        print( "newt.extend()" )
        
    def retract(self):
        '''! Runs the pwm signal to cause the actuator to retract.'''
        self.status = -1
        self.ch1.pulse_width(5000)   # 5000 ticks = 1.2507ms on oscilloscope
        print( "newt.retract()" )
        
    def stop(self):
        '''! Runs the pwm signal to cause the actuator to stop moving.'''
        self.status = 0
        self.ch1.pulse_width(6000)   # 6000 ticks = 1.5008ms on oscilloscope
        print( "newt.stop()" )
        
    def get_status(self):
        '''! Gives the status of the NewtonGripper. 1 for extending, 0 for stopped, -1 for retracting.'''
        return self.status
        
    
if __name__ == "__main__":
    '''! 
    Testing Code: 
        Connect Newton gripper power and gnd to psu.
        Connect yellow logic line to pin PB4.
    '''
    # Create but do not initialize a timer object for timer channel 3, which uses pin PB4 for channel 1 output.
    timer4 = pyb.Timer(4)
    
    # Set up the pin PB6 for timer 4 channel 1 output
    pin_PB6 = pyb.Pin(pyb.Pin.board.PB6, pyb.Pin.OUT_PP)
        # identifier = pyb.Pin.board.PB6
        # mode = pyb.Pin.ALT to use alternate functions (see STM32L476xx Alternate Function table)
        # pull = pyb.Pin.PULL_NONE to disable pullup resistors. Not needed for this application, just use push pull
        # alt = 2 sets alternate function to 2 (see STM32L476xx Alternate Function table)
        
    # Create NewtonGripper object
    newt = NewtonGripper(pin_PB6, timer4)
    
    # Run tests
    print("TEST START")
    newt.retract()
    prevTime = pyb.millis()
    while True:
        if pyb.millis() > (prevTime + 1000):
            newt.stop()
            break
    print("TEST FINISHED")
    
    
    