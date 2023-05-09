from .InputPin import InputPin
from .OutputPin import OutputPin

try:
    # Try importing RPi GPIO package, define placeholder class if import fails.
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except ImportError:
    class GPIO:
        """
        Placeholder GPIO class to substitute for RPi class when not running on a RPi4B
        """
        IN = 0
        OUT = 1

        @staticmethod
        def setup(x, y):
            pass

        @staticmethod
        def input(x):
            return False

        @staticmethod
        def output(x, y):
            pass

        @staticmethod
        def cleanup():
            pass


class RPi4BOutPin(OutputPin):
    """
    Output pin implementation for RPi4B.
    """

    def _setup(self):
        GPIO.setup(self._pin, GPIO.OUT)

    def high(self):
        GPIO.output(self._pin, True)

    def low(self):
        GPIO.output(self._pin, False)


class RPi4BInPin(InputPin):
    """
    Input pin implementation for RPi4B.
    """

    def _setup(self):
        GPIO.setup(self._pin, GPIO.IN)

    def read(self) -> bool:
        return GPIO.input(self._pin)


class RPi4B:
    """
    GPIO Interface for Raspberry Pi 4B
    """

    @staticmethod
    def output_pin(pin: int) -> OutputPin:
        """
        :param pin: The pin number.
        :return: An output pin object for the RPi4B
        """
        return RPi4BOutPin(pin)

    @staticmethod
    def input_pin(pin: int) -> InputPin:
        """
        :param pin: The pin number.
        :return: An input pin object for the RPi4B
        """
        return RPi4BInPin(pin)

    @staticmethod
    def cleanup():
        GPIO.cleanup()

