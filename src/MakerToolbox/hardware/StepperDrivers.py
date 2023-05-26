from time import sleep
from abc import ABC, abstractmethod
from typing import List

from ..gpio import OutputPin


class StepperDriver(ABC):
    """
    Abstract base class for stepper motor drivers.
    """

    def __init__(self, delay_func: callable = lambda current, total: 0.003):
        self._delay_func = delay_func
        self._step_phases = []

    def step(self, num_steps: int = 1, delay_func: callable = None, direction: bool = None):
        """
        Performs a specified number of steps in the stepper motor.

        Args:
            num_steps (int, optional): The number of steps to perform. Defaults to 1.
            delay_func (callable, optional): A function that calculates the delay between steps. Defaults to None.
            direction (bool, optional): The direction of the steps, uses the currently set direction if set to None.
            True for forward, False for backward. Defaults to None.
        """
        if delay_func is None:
            delay_func = self._delay_func
        if direction is not None:
            self.set_direction(direction)
        for x in range(num_steps):
            delay = delay_func(x, num_steps)
            for phase in self._step_phases:
                phase()
                sleep(delay)

    @staticmethod
    def move(steppers: List['StepperDriver'], num_steps: int = 1, delay_func: callable = None):
        """
        Moves multiple stepper motors simultaneously.

        Args:
            steppers (List['StepperDriver']): A list of stepper motor drivers.
            num_steps (int, optional): The number of steps to perform. Defaults to 1.
            delay_func (callable, optional): A function that calculates the delay between steps.
        """
        phase_counts = [len(stepper._step_phases) for stepper in steppers]
        assert max(phase_counts) == min(phase_counts)
        num_phases = max(phase_counts)
        for current_step in range(num_steps):
            delay = delay_func(current_step, num_steps) if delay_func is not None else 0.003
            for x in range(num_phases):
                for stepper in steppers:
                    stepper._step_phases[x]()
                sleep(delay)

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

    def __init__(
            self,
            stp_pin: OutputPin,
            dir_pin: OutputPin,
            delay_func: callable = lambda current, total: 0.003
    ):
        super().__init__(delay_func)
        self._stp = stp_pin
        self._dir = dir_pin
        self._direction = False
        self._step_phases = [
            self._stp.low,
            self._stp.high
        ]

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

    def __init__(
            self,
            in1: OutputPin,
            in2: OutputPin,
            in3: OutputPin,
            in4: OutputPin,
            delay_func: callable = lambda current, total: 0.01
    ):
        super().__init__(delay_func)
        self._in1 = in1
        self._in2 = in2
        self._in3 = in3
        self._in4 = in4
        self._direction = True
        self._forward_sequence = [
            (lambda: self._sequence_component(x)) for x in range(8)
        ]
        self._backwards_sequence = [
            (lambda: self._sequence_component(x)) for x in range(8, -1, -1)
        ]
        self._in1.low()
        self._in2.low()
        self._in3.low()
        self._in4.low()

    def _sequence_component(self, x):
        sequence = [False, False, False, False, False, True, True, True]
        self._in1.set(sequence[x % 8])
        self._in2.set(sequence[(x + 3) % 8])
        self._in3.set(sequence[(x + 4) % 8])
        self._in4.set(sequence[(x + 6) % 8])

    def set_direction(self, value: bool):
        self._direction = value
        if value:
            self._step_phases = self._forward_sequence
        else:
            self._step_phases = self._backwards_sequence

    def get_direction(self) -> bool:
        return self._direction
