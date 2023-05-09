from makertoolbox import *

# Move a stepper motor forward and then backwards.
stepper: BasicStepperDriver = BasicStepperDriver(RPi4B.output_pin(1), RPi4B.output_pin(2))
stepper.direction(True)
for _ in range(200):
    stepper.step()
stepper.direction(False)
for _ in range(200):
    stepper.step()



