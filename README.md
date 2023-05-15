# MakerToolbox
The MakerToolbox module provides a collection of tools for working with various electronic hardware. The goal of this module is to simplify setting up and interfacing with hardware while developing maker projects.

## Imports
`from MakerToolbox import *`

## GPIO Interfaces
> The following classes can be used to interface with GPIO. Each class manages the logic for setting up GPIO depending on the hardware it represents.

### `RPi4` - _Raspberry Pi Model 4 (B)_

The `RPi4` class provides a simple interface for configuring GPIO inputs and outputs for a Raspberry Pi 4 board.

```python
class RPi4:
    @staticmethod def output_pin(pin: int) -> OutputPin
    @staticmethod def input_pin(pin: int) -> InputPin
    @staticmethod def pwm_pin(pin: int, frequency: int) -> PWMPin
    @staticmethod def cleanup()
```

### `RPi3` - _Raspberry Pi Model 3 (A/B/B+)_

The `RPi3` class provides a simple interface for configuring GPIO inputs and outputs for a Raspberry Pi 3 board.

```python
class RPi3:
    @staticmethod def output_pin(pin: int) -> OutputPin
    @staticmethod def input_pin(pin: int) -> InputPin
    @staticmethod def pwm_pin(pin: int, frequency: int) -> PWMPin
    @staticmethod def cleanup()
```

## Hardware
> The following classes provide interfaces for controlling various pieces of hardware.

### `BasicStepperDriver`
The `BasicStepperDriver` provides a simple interface for controlling a stepper motor using only a `stp` and `dir` pin.

```python
class BasicStepperDriver:
    def __init__(self, stp_pin: OutputPin, dir_pin: OutputPin)
    def step(self, delay: float)
    def set_direction(self, value: bool)
    def get_direction(self) -> bool:
```

### `ULN2003`
The `ULN2003` class provides a simple interface for controlling a ULN2003 stepper motor driver.

```python
class ULN2003:
    def __init__(self, in1: OutputPin, in2: OutputPin, in3: OutputPin, in4: OutputPin, default_delay: float = 0.003)
    def step(self, delay: float)
    def set_direction(self, value: bool)
    def get_direction(self) -> bool:
```

### `DCMotorDriver`

The `DCMotorDriver` class provides a simple interface for controlling a DC motor using a motor driver module.

```python
class DCMotorDriver:
    def __init__(self, pwm: PWMPin, dir_a: OutputPin, dir_b: OutputPin, initial_speed: float = 0.5)
    def set_speed(self, speed: float)
    def stop(self)
```

## Machines
> The following classes represent 'machines' (collections of hardware) and provide methods for controlling them.
Hardware

### `CoreXY`
The `CoreXY` class provides a high-level interface for controlling a CoreXY motion system. See: https://en.wikipedia.org/wiki/CoreXY

```python
class CoreXY:
    def __init__(self, stepper_a: BasicStepperDriver, stepper_b: BasicStepperDriver)
    def step_together(self, steps: int, delay_func: callable = None)
    @staticmethod def step_single(stepper: BasicStepperDriver, steps: int, delay_func: callable = None)
    def north(self, steps: int, delay_func: callable = None)
    def south(self, steps: int, delay_func: callable = None)
    def east(self, steps: int, delay_func: callable = None)
    def west(self, steps: int, delay_func: callable = None)
    def north_west(self, steps: int, delay_func: callable = None)
    def north_east(self, steps: int, delay_func: callable = None)
    def south_west(self, steps: int, delay_func: callable = None)
    def south_east(self, steps: int, delay_func: callable = None)

```

## Utility
> The following classes provide generic utility.

### `XYPosition`

The `XYPosition` class defines a coordinate in space. Modeled as a vector.

```python
class XYPosition:
    def __init__(self, x: int, y: int)
```

## Algorithms
> The following are implementations of different algorithms.

### Paths

#### `compute_discrete_xy_path_differentials`
Computes a discrete path between two positions relative to the start position.
```python
compute_discrete_xy_path_differentials(start: XYPosition, end: XYPosition) -> List[XYPosition]
```

## Examples
```python
from MakerToolbox import BasicStepperDriver, RPi4

# Move a stepper motor one direction and then the opposite direction.
stepper: BasicStepperDriver = BasicStepperDriver(RPi4.output_pin(1), RPi4.output_pin(2))
stepper.set_direction(True)
for _ in range(200):
    stepper.step()
stepper.set_direction(False)
for _ in range(200):
    stepper.step()

```
