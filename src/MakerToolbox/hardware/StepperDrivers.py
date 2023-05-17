from time import sleep
from abc import ABC, abstractmethod
from ..gpio import OutputPin


class StepperDriver(ABC):
    """
    Abstract base class for stepper motor drivers.
    """

    @abstractmethod
    def step(self, delay: float = None):
        """
        Performs a single step of the stepper motor.

        Args:
            delay (float): Delay in seconds between steps.
        """
        pass

    @abstractmethod
    def set_direction(self, value: bool):
        """
        Sets the direction of the stepper motor.

        Args:
            value (bool): True for forward direction, False for backward direction.
        """
        pass

    @abstractmethod
    def get_direction(self) -> bool:
        """
        Gets the current direction of the stepper motor.

        Returns:
            bool: True for forward direction, False for backward direction.
        """
        pass


class BasicStepperDriver(StepperDriver):
    """
    A basic stepper driver capable of pulsing a stp and dir pin.
    """

    def __init__(self, stp_pin: OutputPin, dir_pin: OutputPin, default_delay: float = 0.01):
        self._stp = stp_pin
        self._dir = dir_pin
        self._default_delay = default_delay
        self._direction = False

    def step(self, delay: float = None):
        if delay is None:
            delay = self._default_delay
        self._stp.low()
        sleep(delay)
        self._stp.high()
        sleep(delay)

    def set_direction(self, value: bool):
        self._direction = value
        if value:
            self._dir.high()
        else:
            self._dir.low()

    def get_direction(self) -> bool:
        return self._direction


class ULN2003(StepperDriver):
    """
    ULN2003 stepper driver.
    """

    def __init__(self, in1: OutputPin, in2: OutputPin, in3: OutputPin, in4: OutputPin, default_delay: float = 0.01):
        self._in1 = in1
        self._in2 = in2
        self._in3 = in3
        self._in4 = in4
        self._default_delay = default_delay
        self._direction = True
        self._in1.low()
        self._in2.low()
        self._in3.low()
        self._in4.low()
        self._sequence = [False, False, False, False, False, True, True, True]

    def step(self, delay: float = None):
        if delay is None:
            delay = self._default_delay
        for x in range(8) if self._direction else range(8, -1, -1):
            self._in1.set(self._sequence[x % 8])
            self._in2.set(self._sequence[(x + 3) % 8])
            self._in3.set(self._sequence[(x + 4) % 8])
            self._in4.set(self._sequence[(x + 6) % 8])
            sleep(delay)

    def set_direction(self, value: bool):
        self._direction = value

    def get_direction(self) -> bool:
        return self._direction
