from algorithms import *
from hardware import *
from gpio import *
from machines import *
from utility import *

# Move a stepper motor forward and then backwards.
stepper: BasicStepperDriver = BasicStepperDriver(RPi4.output_pin(2), RPi4.output_pin(3), default_delay=0.003)
stepper.set_direction(True)
for _ in range(200):
    stepper.step()
stepper.set_direction(False)
for _ in range(200):
    stepper.step()

corexy: CoreXY = CoreXY(stepper, stepper)
corexy.north(1)

servo = ServoMotor(RPi4.pwm_pin(18, ServoMotor.DEFAULT_FREQUENCY))
servo.set_angle(45)

motor = DCMotorDriver(
    RPi4.pwm_pin(18, DCMotorDriver.DEFAULT_FREQUENCY),
    RPi4.output_pin(13),
    RPi4.output_pin(4)
)
motor.set_speed(1)

RPi4.cleanup()
