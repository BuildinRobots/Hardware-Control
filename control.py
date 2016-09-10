# Thomas Miles, 30/08/16
# tmiles@student.unimelb.edu.au
# 626263

"""   Contains basic control classes for basic robotics components:
       Servo __init__(self, pin, name, init = 2000)
       ESC __init__(self, pin, name)
       DCMotor __init__(self, fwdPin, revPin, name)

       An IO class is provided for neater GPIO control:
       IO __init__(self)
       Creating an object of this class by defult will activate the GPIO; This
       must be done before component classes are created

"""

import RPi.GPIO as GPIO
import time

class IO:
    """ simplifys GPIO control """
    active = True
    warnings = False

    def __init__ (self):
        """ sets up the GPIO to defult settings """

        GPIO.setwarnings(warnings)
        GPIO.setmode(GPIO.BCM)

    def activate (self, yn):
        """ yn is a boolean input to activate/deactivate the GPIO """
        if active == yn:
            print "--> IO.active is already " + yn
        else:
            active = yn
            if active is True:
                GPIO.setwarnings(warnings)
                GPIO.setmode(GPIO.BCM)
                return
            elif active is False:
                GPIO.cleanup()
                print "--> IO has been disabled"
                return
            else:
                print "--> WARNING: IO.activate() requires a boolean input"
                return
#==============================================================================#


class Servo:
    """ for controling servo components """

    def __init__(self, pin, name, init):
        """ initialises servo """
        # init = defult angle

        GPIO.setup(pin, GPIO.OUT)
        self.channel = GPIO.PWM(pin, 100)# allocates GPIO channel, sets to 100Hz
        duty = float(init) / 10.0 + 2.5 # duty cycle for a given angle
        self.channel.start(duty)

        self.init = duty # saves defult duty cycle
        self.name = name
        print name + "has been initialised"


    def reset(self):
        """ resets servo to defult position """

        self.channel.ChangeDutyCycle(self.init)
        print "--> "+ self.name + " has been reset"


    def setAngle(self, angle):
# Sets the servo to a given angle
        duty = float(angle) / 10.0 + 2.5
        self.channel.ChangeDutyCycle(duty)


    def deactivate (self):
        self.channel.stop()
        print "--> " + self.name + "has been deactivated"
#==============================================================================#


class DCMotor:

    LOW = 0
    HIGH = 20000

    def __init__ (self, fwdPin, revPin, name):
# When initialted, provide pin numbers for forward and reverse logic on GPIO

        self.name = name
        GPIO.setup(fwdPin, GPIO.OUT)
        GPIO.setup(revPin, GPIO.OUT)
        self.fwd = GPIO.PWM(fwdPin, 100) # sets output channels to 100Hz
        self.rev = GPIO.PWM(revPin, 100) #
        self.fwd.start(0)
        self.rev.start(0)

    print "--> " + name + "enabled"


    def setSpeed (self, speed):
""" Speed is a percentage between -100 (reverse) and 100 """

        if speed > 0:
            if speed > 100:
                speed = 100
            self.rev.ChangeDutyCycle(0)
            self.fwd.ChangeDutyCycle(speed)

        elif speed < 0:
            if speed < -100:
                speed = -100
            self.fwd.ChangeDutyCycle(0)
            self.rev.ChangeDutyCycle(-speed)

        else:
            self.rev.ChangeDutyCycle(0)
            self.fwd.ChangeDutyCycle(0)

    def deactivate (self):
        self.rev.stop()
        self.fwd.stop()
        print "--> " + self.name + "has been deactivated"
#==============================================================================#


class ESC:
    """Sends signals to an electronic speed controler (ESC) in order to control
        a brushless DC motor
        __init__(self, pin, name):"""
    freq = 50 #Hz
    # duty values
    LOW = 5         # ~4000us
    NEUTURAL = 7.5  # ~6000us
    HIGH = 10       # ~8000us

    def __init__(self, pin, name):
        """ Sets up the ESC with a given GPIO pin """
        keypress = input (
                              "--> Please ensure ESC is OFF.",
                              "    \nHit enter to continue..."
                              )
        GPIO.setup(pin, GPIO.OUT)
        self.channel = GPIO.PWM(pin, freq)
        self.name = name
        self.duty = LOW
        self.channel.start(self.duty)


    def calibrate(self):
        """ calibrates the ESC """

        keypress = input (
                              "--> Initialising " + name + " on GPIO pin" + pin,
                              "    \nPlease ensure ESC is connected to GPIO.",
                              "    \nConnect the ESC to power and switch it on",
                              "    \nHit enter to continue..."
                              )

        print "--> Please hold the Set button on the ESC.",
        keypress = input ("--> When orange LED becomes solid, release Set and",
                          " hit enter (should take ~4s)"
                          )
        self.duty = HIGH
        self.channel.ChangeDutyCycle(self.duty)
        keypress = input ("--> Red LED should flash and become solid,",
        " when motor beeps, hit enter")

        self.duty = LOW
        self.channel.ChangeDutyCycle(self.duty)
        keypress = input ("--> Orange LED should flash and become solid,",
        " when motor beeps, hit enter")

        self.duty = NEUTURAL
        self.channel.ChangeDutyCycle(self.duty)

        keypress = input ( "--> Both LEDs should blink and become solid,\n ",
                           "   motor should then beep and the LEDs should wink",
                           "\n--> varify sucess (y/n): ")

        x = True
        while x
            keypress = raw_input(
                            "--> Calibration complete, varify sucess (y/n)" )
            if keypress is "n":
                sys.exit("--> Terminating")

            if keypress is "y":
                Print "--> Sucess confirmed, please restart ESC"
                x = False
#==============================================================================#


    def setSpeed(self, speed):
# Speed is a % between -100 (reverse) and 100
        self.duty = NEUTURAL + 5.0/speed

        if (speed > 100) or (speed < -100):
            print "--> ERROR: Invalid speed, must be between -100 and 100!"

        else:
            self.channel.ChangeDutyCycle(self.duty)
            print "--> " + self.name + " speed set to " + speed + "%"
#==============================================================================#


    def deactivate (self):
        self.channel.stop()
        print "--> " + self.name + "has been deactivated"
