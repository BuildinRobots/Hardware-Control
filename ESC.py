# Thomas Miles, 30/08/16
# tmiles@student.unimelb.edu.au
# 626263

from RPIO import PWM
import time


class ESC:
    """Sends signals to an electronic speed controler (ESC) in order to control
        a brushless DC motor
        __init__(self, pin, name):"""

    # pulse values
    LOW = 1000
    NEUTURAL = 1500
    HIGH = 2000

    def __init__(self, pin, name):
        """Sets up and calibrates the ESC with a given GPIO pin,
            takes about 15 seconds"""
        self.name = name
        self.pin = pin
        self.pulse = NEUTURAL
        self.output = PWM.Servo()
        self.output.set_servo(pin, self.pulse)
#==============================================================================#
#                                  Calibration
#==============================================================================#
        keypress = raw_input(
                              "--> Initialising " + name + " on GPIO pin" + pin,
                              "    \nPlease turn on the ESC",
                              "    \nHit enter to continue..."
                            )

        print "--> Calibrating ESC, please Wait..."
        self.pulse = LOW
        self.output.set_servo(self.pin, self.pulse)
        time.sleep(5)

        print "--> Please Wait..."
        self.pulse = HIGH
        self.output.set_servo(self.pin, self.pulse)
        time.sleep(5)

        print "--> Please Wait..."
        self.pulse = NEUTURAL
        self.output.set_servo(self.pin, self.pulse)
        time.sleep(5)

        x = True
        while x
            keypress = raw_input(
                            "--> Calibration complete, varify sucess (y/n)" )
            if keypress is "n":
                print "Terminating"
                return False

            if keypress is "y":
                Print "Sucess!"
                return True

#==============================================================================#
#                                  Methods
#==============================================================================#
    def accelerate(self, step, extent):
        """ Increases or decreases speed based on step variable  """
        # +ve step accelerates, -ve deccelerates
        # extent is percent speed change (0.0 ~ 1.0)
        i = 0
        while i < extent*500:
            if (self.pulse + step) >= HIGH:
                self.pulse = HIGH
                if self.pulse + step <= LOW:
                    self.pulse = LOW
                else:
                    self.pulse = self.pulse + step

            self.output.set_servo(self.pin, self.pulse)
            i = i+1



    def stop(self):
        """ Stops the motor.
            NOTE if stopped for 2 sec the motor will be in reverse """
        self.pulse = NEUTURAL
        self.output.set_servo(self.pin, self.pulse)



    def setSpeed(self, speed):
# Speed is a % between -100 (reverse) and 100
        self.pulse = 1500 + speed*5

        if (speed > 100) or (speed < -100):
            print "--> ERROR: Invalid speed, must be between -100 and 100!"
            return False

        else:
            self.output.set_servo(self.pin, self.pulse)
            print "--> Speed set to "+ speed+"%"

    def deactivate (self):
        self.output.stop_servo(self.pin)
        print "--> " + self.name + "has been deactivated"
