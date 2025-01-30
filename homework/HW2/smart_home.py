class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.status = False

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def __str__(self):
        return f"{self.name}: {'On' if self.status else 'OFF'}"


class Light(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.brightness = 100

    def adjust_brightness(self, level):
        if level > 1 and level < 100:
            self.brightness = level

    def __str__(self):
        return f"{self.name}: {'On' if self.status else 'OFF'}, Brightness {self.brightness}"


class Thermostat(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.temperature = 65

    def _check_temperature_limits(self, temp):
        if temp < 80 and temp > 55:
            return True
        else:
            return False

    def adjust_temperature(self, temp):
        if self._check_temperature_limits(temp):
            self.temperature = temp

    def __str__(self):
        return f"{self.name}: {'On' if self.status else 'OFF'}, Temperature: {self.temperature}"


class Speaker(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.volume = 3

    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 1:
            self.volume -= 1

    def __str__(self):
        return f"{self.name}: {'ON' if self.status else 'OFF'}, Volume: {self.volume}"


class SmartHome:
    def __init__(self):
        self.devices = []

    def __add__(self, other):
        if isinstance(other, SmartDevice):
            self.devices.append(other)
        return self

    def turn_off_all(self):
        for device in self.devices:
            device.turn_off()

    def __str__(self):
        return "\n".join(str(device) for device in self.devices)
