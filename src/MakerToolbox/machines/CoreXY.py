from typing import List

from ..hardware import BasicStepperDriver, StepperDriver


class CoreXY:
    """
    Class representing a CoreXY utility system.

    Attributes:
        stepper_a (BasicStepperDriver): Stepper driver for motor A.
        stepper_b (BasicStepperDriver): Stepper driver for motor B.
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
        self._xy_delta_to_stepper_movement = {
            (0, 0): (0, 0),
            (0, 1): (1, -1),
            (0, -1): (-1, 1),
            (1, 0): (-1, -1),
            (-1, 0): (1, 1),
            (1, 1): (0, -2),
            (1, -1): (-2, 0),
            (-1, 1): (2, 0),
            (-1, -1): (0, 2)
        }

    def move_y(self, steps: int, delay_func: callable = None):
        """
        Moves the machine along the y axis.

        Args:
            steps (int): Number of steps to move north.
            delay_func (callable, optional): Custom delay function. If provided,
                it should take two arguments: current step and total steps,
                and return the delay time in seconds for the current step.
        """
        if steps == 0:
            return
        if steps > 0:
            self._stepper_a.set_direction(True)
            self._stepper_b.set_direction(False)
        else:
            self._stepper_a.set_direction(False)
            self._stepper_b.set_direction(True)
        StepperDriver.move([self._stepper_a, self._stepper_b], abs(steps), delay_func)

    def move_x(self, steps: int, delay_func: callable = None):
        """
        Moves the machine along the x axis.

        Args:
            steps (int): Number of steps to move.
            delay_func (callable, optional): Custom delay function. If provided,
                it should take two arguments: current step and total steps,
                and return the delay time in seconds for the current step.
        """
        if steps == 0:
            return
        if steps > 0:
            self._stepper_a.set_direction(False)
            self._stepper_b.set_direction(False)
        else:
            self._stepper_a.set_direction(True)
            self._stepper_b.set_direction(True)
        StepperDriver.move([self._stepper_a, self._stepper_b], abs(steps), delay_func)

    def move_diagonally(self, steps: int, x_direction: int, y_direction: int, delay_func: callable = None):
        if steps == 0 or x_direction == 0 or y_direction == 0:
            return
        stepper: StepperDriver
        if x_direction > 0:
            if y_direction > 0:
                stepper = self._stepper_b
                self._stepper_b.set_direction(False)
            else:
                stepper = self._stepper_a
                self._stepper_a.set_direction(False)
        else:
            if y_direction > 0:
                stepper = self._stepper_a
                self._stepper_a.set_direction(True)
            else:
                stepper = self._stepper_b
                self._stepper_b.set_direction(True)
        stepper.step(2 * steps, delay_func)

