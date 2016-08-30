from RPIO import PWM

class Servo:
        MIN = 1000
        INIT = 2000 # initial frequency 2µs
        MAX = 3000

        def __init__(self, pin, name):
#======= *MIN & MAX may need adjusting, just guessed


            self.name = name
            self.pulse = INIT
            self.pin = pin
            self.servo = PWM.Servo()
            self.servo.set_servo(self.pin, self.pulse)

            print self.name + "has been initialised"

        def turn(self, step):
        # +ve step turns clockwise, -ve counter-clockwise
            if (self.pulse + step) >= MAX:
                self.pulse = MIN
                if self.pulse + step <= MAX:
                    self.pulse = MIN
            else:
                self.pulse = self.pulse + step

            self.output.set_servo(self.pin, self.pulse)

        def deactivate (self):
            self.servo.stop_servo(self.pin)
            print self.name + "has been deactivated"
