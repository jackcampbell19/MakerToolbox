from ..gpio import PWMPin, OutputPin


def _convert_speed_to_duty_cycle(speed: float) -> float:
    """
    Converts the speed value to a duty cycle value in the range of 0 to 100.

    Args:
        speed (float): The speed value as a float between -1 and 1.

    Returns:
        float: The corresponding duty cycle value in the range of 0 to 100.
    """
    return max(min(abs(speed), 1), 0) * 100


class DCMotorDriver:
    DEFAULT_FREQUENCY = 100

    def __init__(self, pwm: PWMPin, dir_a: OutputPin, dir_b: OutputPin, initial_speed: float = 0.5):
        """
        Initializes the DC motor driver instance.

        Args:
            pwm (PWMPin): The PWM pin object used for controlling the motor speed.
            dir_a (OutputPin): The GPIO pin object connected to the A input of the motor driver for direction control.
            dir_b (OutputPin): The GPIO pin object connected to the B input of the motor driver for direction control.
            initial_speed (float, optional): The initial speed of the motor as a float between -1 and 1.
                                             Defaults to 0.5.
        """
        self._pwm = pwm
        self._dir_a = dir_a
        self._dir_b = dir_b
        self.set_speed(0)  # Stop the motor initially
        self._pwm.start(_convert_speed_to_duty_cycle(initial_speed))

    def set_speed(self, speed: float):
        """
        Sets the speed of the DC motor.

        Args:
            speed (float): The speed of the motor as a float between -1 and 1.
                           A value of -1 represents maximum speed in reverse direction,
                           0 stops the motor, and 1 represents maximum speed in forward direction.
        """
        if speed > 0:
            self._dir_a.low()
            self._dir_b.high()
        elif speed < 0:
            self._dir_a.high()
            self._dir_b.low()
        else:
            self._dir_a.low()
            self._dir_b.low()

        duty_cycle = _convert_speed_to_duty_cycle(speed)
        self._pwm.change_duty_cycle(duty_cycle)

    def stop(self):
        """
        Stops the motor by setting the speed to 0.
        """
        self.set_speed(0)
