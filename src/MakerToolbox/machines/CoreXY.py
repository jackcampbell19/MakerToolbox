from ..hardware import BasicStepperDriver, StepperDriver
from ..utility import Discrete2DPosition


class CoreXY:
    """
    Class representing a CoreXY utility system.

    Attributes:
        stepper_a (BasicStepperDriver): Stepper driver for motor A.
        stepper_b (BasicStepperDriver): Stepper driver for motor B.
        _current_position (Discrete2DPosition): Current position of the utility system.
    """

    def __init__(self, stepper_a: BasicStepperDriver, stepper_b: BasicStepperDriver, delay_func: callable = lambda c, t: 0.006):
        """
        Initializes a CoreXY utility system.

        Args:
            stepper_a (BasicStepperDriver): Stepper driver for motor A.
            stepper_b (BasicStepperDriver): Stepper driver for motor B.
        """
        self._stepper_a = stepper_a
        self._stepper_b = stepper_b
        self._current_position = Discrete2DPosition(0, 0)
        self._delay_func = delay_func

    def north(self, steps: int, delay_func: callable = None):
        """
        Moves the utility system north by a specified number of steps.

        Args:
            steps (int): Number of steps to move north.
            delay_func (callable, optional): Custom delay function. If provided,
                it should take two arguments: current step and total steps,
                and return the delay time in seconds for the current step.
        """
        if delay_func is None:
            delay_func = self._delay_func
        self._stepper_a.set_direction(True)
        self._stepper_b.set_direction(False)
        StepperDriver.move([self._stepper_a, self._stepper_b], steps, delay_func)
        self._current_position.y += steps

    def south(self, steps: int, delay_func: callable = None):
        """
        Moves the utility system south by a specified number of steps.

        Args:
            steps (int): Number of steps to move south.
            delay_func (callable, optional): Custom delay function. If provided,
                it should take two arguments: current step and total steps,
                and return the delay time in seconds for the current step.
        """
        if delay_func is None:
            delay_func = self._delay_func
        self._stepper_a.set_direction(False)
        self._stepper_b.set_direction(True)
        StepperDriver.move([self._stepper_a, self._stepper_b], steps, delay_func)
        self._current_position.y -= steps

    def east(self, steps: int, delay_func: callable = None):
        """
        Moves the utility system east by a specified number of steps.

        Args:
            steps (int): Number of steps to move east.
            delay_func (callable, optional): Custom delay function. If provided,
                it should take two arguments: current step and total steps,
                and return the delay time in seconds for the current step.
        """
        if delay_func is None:
            delay_func = self._delay_func
        self._stepper_a.set_direction(False)
        self._stepper_b.set_direction(False)
        StepperDriver.move([self._stepper_a, self._stepper_b], steps, delay_func)
        self._current_position.x += steps

    def west(self, steps: int, delay_func: callable = None):
        """
        Moves the utility system west by a specified number of steps.

        Args:
            steps (int): Number of steps to move west.
            delay_func (callable, optional): Custom delay function. If provided,
                it should take two arguments: current step and total steps,
                and return the delay time in seconds for the current step.
        """
        if delay_func is None:
            delay_func = self._delay_func
        self._stepper_a.set_direction(True)
        self._stepper_b.set_direction(True)
        StepperDriver.move([self._stepper_a, self._stepper_b], steps, delay_func)
        self._current_position.x -= steps

    def north_west(self, steps: int, delay_func: callable = None):
        """
        Moves the utility system north west by a specified number of steps.

        Args:
            steps (int): Number of steps to move north west.
            delay_func (callable, optional): Custom delay function. If provided,
                it should take two arguments: current step and total steps,
                and return the delay time in seconds for the current step.
        """
        if delay_func is None:
            delay_func = self._delay_func
        self._stepper_a.step(steps * 2, delay_func, direction=True)
        self._current_position.x -= steps
        self._current_position.y += steps

    def north_east(self, steps: int, delay_func: callable = None):
        """
        Moves the utility system north east by a specified number of steps.

        Args:
            steps (int): Number of steps to move north east.
            delay_func (callable, optional): Custom delay function. If provided,
                it should take two arguments: current step and total steps,
                and return the delay time in seconds for the current step.
        """
        if delay_func is None:
            delay_func = self._delay_func
        self._stepper_b.step(steps * 2, delay_func, direction=False)
        self._current_position.x += steps
        self._current_position.y += steps

    def south_west(self, steps: int, delay_func: callable = None):
        """
        Moves the utility system south west by a specified number of steps.

        Args:
            steps (int): Number of steps to move south west.
            delay_func (callable, optional): Custom delay function. If provided,
                it should take two arguments: current step and total steps,
                and return the delay time in seconds for the current step.
        """
        if delay_func is None:
            delay_func = self._delay_func
        self._stepper_b.step(steps * 2, delay_func, direction=True)
        self._current_position.x -= steps
        self._current_position.y -= steps

    def south_east(self, steps: int, delay_func: callable = None):
        """
        Moves the utility system south east by a specified number of steps.

        Args:
            steps (int): Number of steps to move south east.
            delay_func (callable, optional): Custom delay function. If provided,
                it should take two arguments: current step and total steps,
                and return the delay time in seconds for the current step.
        """
        if delay_func is None:
            delay_func = self._delay_func
        self._stepper_a.step(steps * 2, delay_func, direction=False)
        self._current_position.x += steps
        self._current_position.y -= steps
