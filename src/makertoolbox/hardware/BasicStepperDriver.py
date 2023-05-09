from time import sleep
from makertoolbox.gpio import OutputPin


class BasicStepperDriver:
    """
    A basic stepper driver capable of pulsing a stp and dir pin.
    """

    def __init__(self, stp_pin: OutputPin, dir_pin: OutputPin):
        self._stp = stp_pin
        self._dir = dir_pin

    def step(self, delay=0.0005):
        """
        Moves the stepper one step in set direction.
        :param delay: The delay before and after pulling the stp pin high.
        """
        self._stp.low()
        sleep(delay)
        self._stp.high()
        sleep(delay)

    def direction(self, value: bool):
        """
        Sets the direction of the stepper.
        :param value: True for 'High', False for 'Low'
        """
        if value:
            self._dir.high()
        else:
            self._dir.low()
