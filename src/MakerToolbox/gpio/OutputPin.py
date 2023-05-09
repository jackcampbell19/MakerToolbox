from abc import ABC, abstractmethod


class OutputPin(ABC):
    """
    Abstract class that models a GPIO pin designated for output.
    """

    def __init__(self, pin: int):
        """
        Initializes the output pin.
        :param pin: The pin number.
        """
        self._pin = pin
        self._setup()

    @abstractmethod
    def _setup(self):
        """
        Sets up the pin depending on the hardware.
        """
        pass

    @abstractmethod
    def high(self):
        """
        Pulls the pin high.
        """
        pass

    @abstractmethod
    def low(self):
        """
        Pulls the pin high.
        """
        pass
