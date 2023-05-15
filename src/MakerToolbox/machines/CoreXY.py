from hardware import BasicStepperDriver
from utility import XYPosition


class CoreXY:
    """
    Class representing a CoreXY utility system.

    Attributes:
        stepper_a (BasicStepperDriver): Stepper driver for motor A.
        stepper_b (BasicStepperDriver): Stepper driver for motor B.
        _current_position (XYPosition): Current position of the utility system.
    """

    def __init__(self, stepper_a: BasicStepperDriver, stepper_b: BasicStepperDriver):
        """
        Initializes a CoreXY utility system.

        Args:
            stepper_a (BasicStepperDriver): Stepper driver for motor A.
            stepper_b (BasicStepperDriver): Stepper driver for motor B.
        """
        self._stepper_a = stepper_a
        self._stepper_b = stepper_b
        self._current_position = XYPosition(0, 0)

    def step_together(self, steps: int, delay_func: callable = None):
        """
        Performs a specified number of steps on both motors simultaneously.

        Args:
            steps (int): Number of steps to perform.
            delay_func (callable, optional): Custom delay function. If provided,
                it should take two arguments: current step and total steps,
                and return the delay time in seconds for the current step.
        """
        for current in range(steps):
            if delay_func is not None:
                delay = delay_func(current, steps)
            else:
                delay = None
            self._stepper_a.step(delay)
            self._stepper_b.step(delay)

    @staticmethod
    def step_single(stepper: BasicStepperDriver, steps: int, delay_func: callable = None):
        """
        Performs a specified number of steps on a single motor.

        Args:
            stepper (BasicStepperDriver): Stepper driver to control.
            steps (int): Number of steps to perform.
            delay_func (callable, optional): Custom delay function. If provided,
                it should take two arguments: current step and total steps,
                and return the delay time in seconds for the current step.
        """
        for current in range(steps):
            if delay_func is not None:
                delay = delay_func(current, steps)
            else:
                delay = None
            stepper.step(delay)

    def north(self, steps: int, delay_func: callable = None):
        """
        Moves the utility system north by a specified number of steps.

        Args:
            steps (int): Number of steps to move north.
            delay_func (callable, optional): Custom delay function. If provided,
                it should take two arguments: current step and total steps,
                and return the delay time in seconds for the current step.
        """
        self._stepper_a.set_direction(True)
        self._stepper_b.set_direction(False)
        self.step_together(steps, delay_func)
        self._current_position.y -= steps

    def south(self, steps: int, delay_func: callable = None):
        """
        Moves the utility system south by a specified number of steps.

        Args:
            steps (int): Number of steps to move south.
            delay_func (callable, optional): Custom delay function. If provided,
                it should take two arguments: current step and total steps,
                and return the delay time in seconds for the current step.
        """
        self._stepper_a.set_direction(False)
        self._stepper_b.set_direction(True)
        self.step_together(steps, delay_func)
        self._current_position.y += steps

    def east(self, steps: int, delay_func: callable = None):
        """
        Moves the utility system east by a specified number of steps.

        Args:
            steps (int): Number of steps to move east.
            delay_func (callable, optional): Custom delay function. If provided,
                it should take two arguments: current step and total steps,
                and return the delay time in seconds for the current step.
        """
        self._stepper_a.set_direction(True)
        self._stepper_b.set_direction(True)
        self.step_together(steps, delay_func)
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
        self._stepper_a.set_direction(False)
        self._stepper_b.set_direction(False)
        self.step_together(steps, delay_func)
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
        self._stepper_a.set_direction(True)
        self.step_single(self._stepper_a, steps * 2, delay_func)
        self._current_position.x -= steps
        self._current_position.y -= steps

    def north_east(self, steps: int, delay_func: callable = None):
        """
        Moves the utility system north east by a specified number of steps.

        Args:
            steps (int): Number of steps to move north east.
            delay_func (callable, optional): Custom delay function. If provided,
                it should take two arguments: current step and total steps,
                and return the delay time in seconds for the current step.
        """
        self._stepper_b.set_direction(True)
        self.step_single(self._stepper_b, steps * 2, delay_func)
        self._current_position.x += steps
        self._current_position.y -= steps

    def south_west(self, steps: int, delay_func: callable = None):
        """
        Moves the utility system south west by a specified number of steps.

        Args:
            steps (int): Number of steps to move south west.
            delay_func (callable, optional): Custom delay function. If provided,
                it should take two arguments: current step and total steps,
                and return the delay time in seconds for the current step.
        """
        self._stepper_b.set_direction(False)
        self.step_single(self._stepper_b, steps * 2, delay_func)
        self._current_position.x -= steps
        self._current_position.y += steps

    def south_east(self, steps: int, delay_func: callable = None):
        """
        Moves the utility system south east by a specified number of steps.

        Args:
            steps (int): Number of steps to move south east.
            delay_func (callable, optional): Custom delay function. If provided,
                it should take two arguments: current step and total steps,
                and return the delay time in seconds for the current step.
        """
        self._stepper_a.set_direction(False)
        self.step_single(self._stepper_a, steps * 2, delay_func)
        self._current_position.x += steps
        self._current_position.y += steps
