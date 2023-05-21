from ..gpio import PWMPin
from time import sleep


class ServoMotor:
    """
    Represents a servo motor.
    """

    DEFAULT_FREQUENCY = 50

    def __init__(self, pwm: PWMPin):
        """
        Initializes the ServoMotor instance.

        Args:
            pwm (PWMPin): The PWM pin object that controls the servo motor.
        """
        self._pwm = pwm
        self._has_started = False

    def set_angle(self, angle: float, delay: float = 1):
        """
        Sets the servo motor to a specified angle.

        Args:
            angle (float): The desired angle for the servo motor (0 to 180 degrees).
            delay (float, optional): The delay in seconds after setting the angle. Defaults to 1 second.
        """
        duty_cycle = angle / 18.0 + 2.5
        if not self._has_started:
            self._pwm.start(duty_cycle)
            self._has_started = True
        else:
            self._pwm.change_duty_cycle(duty_cycle)
        sleep(delay)
