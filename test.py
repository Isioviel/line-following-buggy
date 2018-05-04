'''
Line-following robot code for microbit with L9110s motor driver
Created by Science Oxford

Thanks to MultiWingSpan, whose code for the Bit:Bot was a great starting point.
http://www.multiwingspan.co.uk/micro.php?page=botline
'''

from microbit import *

LF = pin14
LB = pin13
RF = pin12
RB = pin15

time = 0


# 1023 turns the motors off; 0 turns them on at full speed
def stop():
    LF.write_analog(1023)
    LB.write_analog(1023)
    RF.write_analog(1023)
    RB.write_analog(1023)
    display.show(Image.ANGRY)


# Inputs between 0-1023 to control both motors
def drive(l, r):
    display.clear()
    # Below code controls the left wheel - forward, backward, stop at given speed
    if l > 0 and l <= 1023:
        LF.write_analog(abs(l-1023)) # go forwards at speed given
        LB.write_analog(1023) # don't go backwards
    elif l < 0 and l >= -1023:
        LF.write_analog(1023) # don't go forwards
        LB.write_analog(abs(l+1023)) # go backwards at speed given
    else:
        LF.write_analog(1023) # stop the left wheel
        LB.write_analog(1023)
    # Below code controls the right wheel - forward, backward, stop at given speed
    if r > 0 and r <= 1023:
        RF.write_analog(abs(r-1023)) # go forwards at speed given
        RB.write_analog(1023) # don't go backwards
    elif r < 0 and r >= -1023:
        RF.write_analog(1023) # don't go forwards
        RB.write_analog(abs(r+1023)) # go backwards at speed given
    else:
        RF.write_analog(1023) # stop the right wheel
        RB.write_analog(1023)


# THIS CODE NOT GIVEN - TO BE WRITTEN DURING THE SESSION
def followLine():
    lft_opt = pin1.read_digital()
    rgt_opt = pin2.read_digital()
    print(lft_opt)
    print(rgt_opt)
    if lft_opt == 1 and rgt_opt == 0:
        drive(-300, 300)
        sleep(100)
    elif lft_opt == 0 and rgt_opt == 1:
        drive(300, -300)
        sleep(100)
    elif lft_opt == 0 and rgt_opt == 0:
        stop()
    else:
        drive(300, 300)
        sleep(100)
# Delay, so you have time to put the buggy on the ground!
stop()
sleep(1000)

# Forever, run the followLine() function i.e. follow the black line
while True:
    followLine()
    '''
    line1_a = pin1.read_analog()
    line2_a = pin2.read_analog()
    print("Line1, analog = " + str(line1_a))
    print("Line2, analog = " + str(line2_a))
    sleep(100)
    line1_d = pin1.read_digital()
    line2_d = pin2.read_digital()
    print("Line1, digital = " + str(line1_d))
    print("Line2, digital = " + str(line2_d))
    print()
    sleep(500)
    '''

'''
# TEST DRIVE CODE - if any of these don't work, it's probably a wiring problem!
stop()
drive(1023,1023)
display.show(Image.ARROW_N)
sleep(2000)
drive(0,0)
display.show(Image.SQUARE_SMALL)
sleep(2000)
drive(-1023,-1023)
display.show(Image.ARROW_S)
sleep(2000)
drive(511,511)
display.show(Image.ARROW_N)
sleep(2000)
drive(-511,-511)
display.show(Image.ARROW_S)
sleep(2000)
drive(511,-511)
display.show(Image.ARROW_E)
sleep(2000)
drive(-511,511)
display.show(Image.ARROW_W)
sleep(2000)
stop()
display.clear()
sleep(2000)
'''
