import RPi.GPIO as GPIO

class Motor:
### GPIO.setmode(GPIO.BCM) must be called prior to this class being used ###

    def __init__(self, fwdPin, revPin):
# When initialted, provide pin numbers for forward and reverse logic on GPIO

        GPIO.setup(fwdPin, GPIO.OUT)
        GPIO.setup(revPin, GPIO.OUT)
        self.fwd = GPIO.PWM(fwdPin, 50) # sets pins to 50Hz
        self.rev = GPIO.PWM(revPin, 50) #
        self.fwd.start(0)
        self.rev.start(0)

    def drive(self, speed):
# Drives Motor at a given speed between -100 and 100

        if speed > 0 and speed <= 100:
            self.rev.ChangeDutyCycle(0)
            self.fwd.ChangeDutyCycle(speed)
            return "forward"

        elif speed < 0 and speed >= -100:
            self.fwd.ChangeDutyCycle(0)
            self.rev.ChangeDutyCycle(-speed)
            return "reverse"

        elif speed is 0:
            self.fwd.ChangeDutyCycle(0)
            self.rev.ChangeDutyCycle(0)
            return "stop"

        else:
            print "\nERROR: Invalid speed, must be between -100 and 100!"
            return "FAIL"


class servo:
### GPIO.setmode(GPIO.BCM) must be called prior to this class being used ###

        def __init__(self, pin):
# Set GPIO pin to appropriate value for servo control
            GPIO.setup(pin, GPIO.OUT)
            self.pwm = GPIO.PWM(pin, 100) # allocates GPIO pin and frequency
            self.pwm.start(5)   # starts pwm at duty of 5


        def setAngle(self, angle):
# Sets the servo to a given angle
            duty = float(angle) / 10.0 + 2.5
            self.pwm.ChangeDutyCycle(duty)
