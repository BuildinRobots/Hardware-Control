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
SPEED = 50 # %
start_time = time.time()

print "--> 0-1: Driving forward"
alfie.drive_esc.setSpeed(SPEED)
time.sleep(0.5)
print "--> 1-2: Turning out of the gate"
alfie.steering_servo.setAngle(30)
time.sleep(1)
print "--> 2-3: going straight again"
alfie.steering_servo.setAngle(0)
print "--> 3-4: turning to align with pipe, setting grabber to holding position"
alfie.arm_motor.setSpeed(100)
alfie.steering_servo.setAngle(30)
time.sleep(0.1)
alfie.arm_motor.stop()
print "--> 4-5: straightening up"
alfie.steering_servo.setAngle(0)
time.sleep(0.1)
print "--> 5: lifting over the bumps"
alfie.lift()
print "--> 5-6: driving over the pipe"
alfie.drive_esc.setSpeed(SPEED/2)
time.sleep(1)
print "--> 6: releasing"
alfie.drive_esc.setSpeed(SPEED)
alfie.release()
print "--> 6-7: turning towards finish zone"
alfie.steering_servo.setAngle(-30)
time.sleep(1)
alfie.steering_servo.setAngle(0)
print "7-8: hit the breaks!"
alfie.drive_esc.setspeed(-50)
time.sleep(1)

elapsed_time = time.time - start_time
print "run completed in " + elapsed_time + " seconds!"

alfie.terminate()
