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
        self._is_stopped = True

    def set_angle(self, angle: float, delay: float = 1, stop_after_change: bool = True):
        """
        Sets the servo motor to a specified angle.

        Args:
            angle (float): The desired angle for the servo motor (0 to 180 degrees).
            delay (float, optional): The delay in seconds after setting the angle. Defaults to 1 second.
            stop_after_change (bool, optional): Flag to indicate whether to stop the PWM signal
                after each angle change. If set to True, the PWM signal will be stopped. If set to False,
                only the duty cycle will be changed. Defaults to True.
        """
        duty_cycle = angle / 18.0 + 2.5
        if self._is_stopped:
            self._pwm.start(duty_cycle)
            self._is_stopped = False
        else:
            self._pwm.change_duty_cycle(duty_cycle)
        sleep(delay)
        if stop_after_change:
            self._pwm.stop()
            self._is_stopped = True
