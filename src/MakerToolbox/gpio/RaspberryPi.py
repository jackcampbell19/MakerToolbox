from .InputPin import InputPin
from .OutputPin import OutputPin
from .PWMPin import PWMPin

try:
    # Try importing RPi GPIO package, define placeholder class if import fails.
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except ImportError:

    class RPiPWM:

        def start(self, x):
            pass

        def stop(self):
            pass

        def ChangeDutyCycle(self, x):
            pass

        def ChangeFrequency(self, x):
            pass

    class GPIO:
        """
        Placeholder GPIO class to substitute for RPi class when not running on a RPi4B
        """
        IN = 0
        OUT = 1
        PUD_UP = 2
        PUD_DOWN = 3

        @staticmethod
        def setup(x, y, pull_up_down=None):
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

        @staticmethod
        def PWM(x, y) -> RPiPWM:
            return RPiPWM()


class GenericRPiOutPin(OutputPin):
    """
    Output pin implementation for generic RPi.
    """

    def __init__(self, pin: int):
        super().__init__(pin)
        GPIO.setup(pin, GPIO.OUT)

    def high(self):
        GPIO.output(self._pin, True)

    def low(self):
        GPIO.output(self._pin, False)

    def set(self, value: bool):
        GPIO.output(self._pin, value)


class GenericRPiInPin(InputPin):
    """
    Input pin implementation for generic RPi.
    """

    def __init__(self, pin: int, pull_up: bool = True):
        super().__init__(pin)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP if pull_up else GPIO.PUD_DOWN)

    def read(self) -> bool:
        return bool(GPIO.input(self._pin))


class GenericRPiPWMPin(PWMPin):
    """
    PWM pin implementation for generic RPi.
    """

    def __init__(self, pin: int, frequency: int):
        super().__init__(pin, frequency)
        GPIO.setup(pin, GPIO.OUT)
        self._pwm = GPIO.PWM(pin, frequency)

    def start(self, duty_cycle: float):
        self._pwm.start(duty_cycle)

    def change_duty_cycle(self, duty_cycle: float):
        self._pwm.ChangeDutyCycle(duty_cycle)

    def change_frequency(self, frequency: int):
        self._pwm.ChangeFrequency(frequency)

    def stop(self):
        self._pwm.stop()


class Generic40PinRPi:
    """
    GPIO Interface for 40 pin Raspberry Pi.
    """

    @staticmethod
    def output_pin(pin: int) -> OutputPin:
        """
        :param pin: The pin number.
        :return: An output pin.
        """
        return GenericRPiOutPin(pin)

    @staticmethod
    def input_pin(pin: int) -> InputPin:
        """
        :param pin: The pin number.
        :return: An input pin.
        """
        return GenericRPiInPin(pin)

    @staticmethod
    def pwm_pin(pin: int, frequency: int) -> PWMPin:
        """
        :param pin: The pin number.
        :param frequency: The initial frequency.
        :return: A PWM pin.
        """
        return GenericRPiPWMPin(pin, frequency)

    @staticmethod
    def cleanup():
        GPIO.cleanup()


class RPi4(Generic40PinRPi):
    pass


class RPi3(Generic40PinRPi):
    pass
