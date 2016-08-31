# Thomas Miles, 30/08/16
# tmiles@student.unimelb.edu.au
# 626263
import Motor.py
import Servo.py
import ESC.py

    class Alfie:
        """ Class used to impliment the entire robot """

        def __init__(self):
            self.steering_servo = Servo(14, "Steering Servo")   #GPIO pin 14
            self.arm_servo = Servo(15, "Arm Servo")             #GPIO pin 15
            self.release_servo = Servo(18, "Release Servo")     #GPIO pin 18
            self.arm_motor = DCMotor(22, 24, "Arm Motor")       #GPIO pin 22,24
            self.drive_esc = ESC(26, "Drive ESC")               #GPIO pin 26
            self.resetServos()

        def resetServos(self):
            self.steering_servo.reset()
            self.arm_servo.reset()
            self.release_servo.reset()

        def release(self):
            """ Actuates the release mechanism """

            self.release_servo.turn(1,1000)

        def lift(self):
            """ Actuates the arm shortening mechanism """

            self.arm_servo.turn(1,1000)

        def rotateArm(self, direction, t=1):
            """ Moves arm in a given direction (left/right)
                for t seconds (defult 1)                    """

            if direction is "left":
                self.arm_motor.setSpeed(-100)
                time.sleep(t)
                self.arm_motor.stop()
            elif direction is "right":
                self.arm_motor.setSpeed(100)
                time.sleep(t)
                self.arm_motor.stop()
            else:
                sys.exit("ERROR: direction error in arm_motor call")

        def terminate(self):
            self.steering_servo.deactivate()
            self.arm_servo.deactivate()
            self.release_servo.deactivate()
            self.arm_motor.stop()
            self.drive_esc.deactivate()
            sys.exit("--> All objects deactivated, goodbye!")
