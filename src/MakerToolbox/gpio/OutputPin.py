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

    @abstractmethod
    def set(self, value: bool):
        """
        Pulls the pin given the value.
        :param value: The desired state.
        """
        pass
