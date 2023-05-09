# MakerToolbox
The MakerToolbox module provides a collection of tools for working with various electronic hardware. The goal of this module is to simplify setting up and interfacing with hardware while developing maker projects.

## Imports
`from makertoolbox import *`

## GPIO Interfaces
The following classes can be used to interface with GPIO. Each class manages the logic for setting up GPIO depending on the hardware it represents.

### `RPi4B` - _Raspberry Pi 4B_
- `output_pin(pin: int) -> OutputPin`
- `input(pin: int) -> InputPin`

## Hardware
The following classes provide interfaces for controlling various pieces of hardware.

### `BasicStepperDriver`
A stepper driver that uses only a `stp` and `dir` pin.
- `__init__(self, stp_pin: OutputPin, dir_pin: OutputPin)`
- `step(self, delay=0.0005)`
- `direction(self, value: bool)`

## Examples
```python
from makertoolbox import BasicStepperDriver, RPi4B

# Move a stepper motor one direction and then the opposite direction.
stepper: BasicStepperDriver = BasicStepperDriver(RPi4B.output_pin(1), RPi4B.output_pin(2))
stepper.direction(True)
for _ in range(200):
    stepper.step()
stepper.direction(False)
for _ in range(200):
    stepper.step()

```
