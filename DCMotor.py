# Thomas Miles, 30/08/16
# tmiles@student.unimelb.edu.au
# 626263
from RPIO import PWM

class DCMotor:

    LOW = 0
    HIGH = 20000

    def __init__(self, fwdPin, revPin, name):
# When initialted, provide pin numbers for forward and reverse logic on GPIO


    self.name = name
    self.fwd = fwdPin
    self.rev = revPin
    self.current = self.fwd
    self.inactive = self.rev
    self.pulse = LOW

    self.output = PWM.Servo()
    self.output.set_servo(self.current, self.pulse)

    print "--> " + name "enabled"

    def accelerate(self, step, extent):
        """ Increases or decreases speed based on step variable """
        # +ve step accelerates, -ve deccelerates
        i = 0
        while i < extent:
            self.setSpeed(self.pulse/HIGH + step)
            i = i+1

    def setSpeed(self, speed):
# Speed is a % between -100 (reverse) and 100

        if speed > 0:
            if speed > 100:
                speed = 100
            self.forward(HIGH*speed/100)

        elif speed < 0:
            if speed < -100:
                speed = -100
            self.reverse(-HIGH*speed/100)

        else:
            self.stop()

    def stop(self):
        """ Stops the motor """
        output.stop_servo(self.current)
        output.stop_servo(self.inactive)
        print "--> " + self.name + "has been stopped"

    def forward(self, speed):
        """ Drives motor in forward direction at speed between 0 and 20000 """
        self.pulse = speed
        self.current = self.fwd
        self.inactive = self.rev
        self.output.set_servo(self.current, self.pulse)
        output.stop_servo(self.inactive)


    def reverse(self, speed):
        """ Drives motor in forward direction at speed between 0 and 20000 """
        self.pulse = speed
        self.current = self.rev
        self.inactive = self.fwd
        self.output.set_servo(self.current, self.pulse)
        output.stop_servo(self.inactive)
