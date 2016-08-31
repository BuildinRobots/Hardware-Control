# Thomas Miles, 30/08/16
# tmiles@student.unimelb.edu.au
# 626263
from RPIO import PWM

class Servo:
        MIN = 1000
        MAX = 3000

        def __init__(self, pin, name, init = 2000):
            """ initialises servo """

            self.name = name
            self.init = init
            self.pulse = self.init
            self.pin = pin
            self.servo = PWM.Servo()
            self.servo.set_servo(self.pin, self.pulse)

            print self.name + "has been initialised"


        def reset(self):
            """ resets servo to defult position """

            self.pulse = self.init
            print "--> "+ self.name + " has been reset"

        def turn(self, step, extent):
        # +ve step turns clockwise, -ve counter-clockwise
        # extent is overall percent angle change (0.0 ~ 1.0)
            i = 0
            while i < extent*1000:
                if (self.pulse + step) >= MAX:
                    self.pulse = MIN
                    if self.pulse + step <= MAX:
                        self.pulse = MIN
                    else:
                        self.pulse = self.pulse + step

                    self.output.set_servo(self.pin, self.pulse)

        def deactivate (self):
            self.servo.stop_servo(self.pin)
            print "--> " + self.name + "has been deactivated"
