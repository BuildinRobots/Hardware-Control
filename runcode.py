# Thomas Miles, 31/08/16
# tmiles@student.unimelb.edu.au
# 626263
import Alfie.py
import time

""" This is the application to run the pre-planned path """

keypress = raw_input("--> Please ensure Alfie has been correctly wired!\n",
                     "    Steering      - GPIO 14\n",
                     "    Arm Servo     - GPIO 15\n",
                     "    Release Servo - GPIO 18\n",
                     "    Arm Motor     - GPIO 22/24\n",
                     "    ESC           - GPIO 26\n",
                     "    Hit enter to confirm...")
alfie = Alfie()

start_time = time.time()

print "--> Driving forward"
alfie.drive_esc.accelerate(1, 0.25)
time.sleep(0.5)
print "--> Turning out of the gate"
alfie.steering_servo.turn(-1, 0.5)
time.sleep(1)
print "--> going straight again"
alfie.steering_servo.turn(1, 0.5)
print "--> turning to align with pipe, setting grabber to holding position"
alfie.arm_motor.setSpeed(100)
alfie.steering_servo.turn(-2, 0.8)
time.sleep(0.1)
alfie.arm_motor.stop()
print "--> straightening up"
alfie.steering_servo.turn(2, 0.8)
time.sleep(0.1)
print "--> lifting over the bumps"
alfie.lift()
alfie.drive_esc.accelerate(1, 0.25)
time.sleep(1)
print "releasing from the beam"
alfie.drive_esc.accelerate(-1, 0.25)
alfie.release()
print "turning towards finish zone"
alfie.steering_servo.turn(1, 1)
time.sleep(1)
alfie.steering_servo.turn(-1, 1)
print "hit the breaks"
alfie.drive_esc.setspeed(-50)
time.sleep(1)

elapsed_time = time.time - start_time
print "run completed in " + elapsed_time + " seconds!"

alfie.terminate()
