from ..gpio import InputPin
from time import sleep


class Button:

    def __init__(self, pin: InputPin, pressed_value: bool = True):
        """
        Initializes a Button instance.

        Args:
            pin (InputPin): The GPIO input pin connected to the button.
            pressed_value (bool, optional): The value indicating the pressed state of the button.
                                            Defaults to True.
        """
        self._pin = pin
        self._pressed_value = pressed_value

    def is_pressed(self) -> bool:
        """
        Checks if the button is currently pressed.

        Returns:
            bool: True if the button is pressed, False otherwise.
        """
        return self._pin.read() == self._pressed_value

    def wait_for_press(self, delay: float = 0.01):
        """
        Waits until the button is pressed.

        Args:
            delay (float, optional): The delay in seconds between each check for button press. Defaults to 0.01.
        """
        while not self.is_pressed():
            sleep(delay)

    def do_until_pressed(self, action: callable):
        """
        Performs the given action repeatedly until the button is pressed.

        Args:
            action (callable): The action to perform until the button is pressed.
        """
        while not self.is_pressed():
            action()

