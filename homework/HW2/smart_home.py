class SmartDevice:
    """
    A base class for representing a smart device.
    """

    def __init__(self, name):
        """
        Initializes a new smart device.

        Args:
            name (str): The name of the smart device.
        """
        self.name = name
        self.status = False

    def turn_on(self):
        """
        Turns the smart device on.
        """
        self.status = True

    def turn_off(self):
        """
        Turns the smart device off.
        """
        self.status = False

    def __str__(self):
        """
        Returns a string representation of the smart device's current status.

        Returns:
            str: The name and status of the device.
        """
        return f"{self.name}: {'On' if self.status else 'OFF'}"


class Light(SmartDevice):
    """
    A class for representing a light, inheriting from SmartDevice.
    Allows adjusting brightness in addition to basic on/off functionality.
    """

    def __init__(self, name):
        """
        Initializes a new light device.

        Args:
            name (str): The name of the light.
        """
        super().__init__(name)
        self.brightness = 100

    def adjust_brightness(self, level):
        """
        Adjusts the brightness of the light.

        Args:
            level (int): The brightness level, between 1 and 100.
        """
        if level > 1 and level < 100:
            self.brightness = level

    def __str__(self):
        """
        Returns a string representation of the light's current status and brightness.

        Returns:
            str: The name, status, and brightness level of the light.
        """
        return f"{self.name}: {'On' if self.status else 'OFF'}, Brightness {self.brightness}"


class Thermostat(SmartDevice):
    """
    A class for representing a thermostat, inheriting from SmartDevice.
    Allows adjusting the temperature within a specified range.
    """

    def __init__(self, name):
        """
        Initializes a new thermostat device.

        Args:
            name (str): The name of the thermostat.
        """
        super().__init__(name)
        self.temperature = 65

    def _check_temperature_limits(self, temp):
        """
        Checks if the given temperature is within the allowed range (55 to 80 degrees).

        Args:
            temp (int): The temperature to check.

        Returns:
            bool: True if the temperature is within the range, False otherwise.
        """
        if temp < 80 and temp > 55:
            return True
        else:
            return False

    def adjust_temperature(self, temp):
        """
        Adjusts the temperature if it is within the allowed range.

        Args:
            temp (int): The temperature to set.
        """
        if self._check_temperature_limits(temp):
            self.temperature = temp

    def __str__(self):
        """
        Returns a string representation of the thermostat's current status and temperature.

        Returns:
            str: The name, status, and temperature of the thermostat.
        """
        return f"{self.name}: {'On' if self.status else 'OFF'}, Temperature: {self.temperature}"


class Speaker(SmartDevice):
    """
    A class for representing a speaker, inheriting from SmartDevice.
    Allows adjusting the volume in addition to basic on/off functionality.
    """

    def __init__(self, name):
        """
        Initializes a new speaker device.

        Args:
            name (str): The name of the speaker.
        """
        super().__init__(name)
        self.volume = 3

    def increase_volume(self):
        """
        Increases the volume of the speaker, up to a maximum of 10.
        """
        if self.volume < 10:
            self.volume += 1

    def decrease_volume(self):
        """
        Decreases the volume of the speaker, down to a minimum of 1.
        """
        if self.volume > 1:
            self.volume -= 1

    def __str__(self):
        """
        Returns a string representation of the speaker's current status and volume.

        Returns:
            str: The name, status, and volume of the speaker.
        """
        return f"{self.name}: {'ON' if self.status else 'OFF'}, Volume: {self.volume}"


class SmartHome:
    """
    A class for representing a smart home that manages multiple smart devices.
    """

    def __init__(self):
        """
        Initializes a new smart home with an empty list of devices.
        """
        self.devices = []

    def __add__(self, other):
        """
        Adds a smart device to the smart home.

        Args:
            other (SmartDevice): A smart device to add to the smart home.

        Returns:
            SmartHome: The updated smart home instance.
        """
        if isinstance(other, SmartDevice):
            self.devices.append(other)
        return self

    def turn_off_all(self):
        """
        Turns off all devices in the smart home.
        """
        for device in self.devices:
            device.turn_off()

    def __str__(self):
        """
        Returns a string representation of all devices in the smart home.

        Returns:
            str: A list of the devices and their statuses.
        """
        return "\n".join(str(device) for device in self.devices)

