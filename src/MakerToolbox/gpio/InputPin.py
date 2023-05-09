from abc import ABC, abstractmethod


class InputPin(ABC):
    """
    Abstract class that models a GPIO pin designated for input.
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
    def read(self) -> bool:
        """
        Reads the current value of the pin.
        :return: True if 'High', False if 'Low'
        """
        pass
