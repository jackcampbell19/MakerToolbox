from abc import ABC, abstractmethod


class PWMPin(ABC):

    def __init__(self, pin: int, frequency: int):
        """
        Initializes the PWM pin.
        :param pin: The output pin.
        :param frequency: The initial frequency.
        """
        self._pin = pin

    @abstractmethod
    def start(self, duty_cycle: float):
        """
        Starts the PWM signal with the given duty cycle.
        :param duty_cycle: Desired duty cycle.
        """
        pass

    @abstractmethod
    def stop(self):
        """
        Stops the PWN signal.
        """
        pass

    @abstractmethod
    def change_duty_cycle(self, duty_cycle: float):
        """
        Abstract method to change the duty cycle of a device.

        This method should be implemented by subclasses to provide a specific implementation
        for changing the duty cycle of a device. The duty cycle determines the ratio of
        active time to the total time for a periodic signal or operation.

        Args:
            duty_cycle (float): The new duty cycle value to be set for the device.

        Raises:
            NotImplementedError: This exception should be raised by subclasses that do not
                provide an implementation for this method.
        """
        pass

    @abstractmethod
    def change_frequency(self, frequency: int):
        """
        Abstract method to change the frequency of a device.

        This method should be implemented by subclasses to provide a specific implementation
        for changing the frequency of a device. The frequency determines the number of cycles
        per unit of time for a periodic signal or operation.

        Args:
            frequency (int): The new frequency value to be set for the device.

        Raises:
            NotImplementedError: This exception should be raised by subclasses that do not
                provide an implementation for this method.
        """
        pass
