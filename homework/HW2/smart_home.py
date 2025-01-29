class SmartDevice:
    def __init__(self, name, status = False):
        self.name = name
        self.status = status

    def turn_on(self):
        self.status = True
    def turn_off(self):
        self.status = False
    def __str__(self):
        return f"{self.name}: {self.status}"
    
class Light(SmartDevice):
    def __init__(self, name):
        self.name = name
        self.brightness = 100

    def adjust_brightness(self, level):
        level = int(input())
        if level > 1 and level < 100:
            self.brightness = level
    
    def __str__(self):
        return f"{self.name}: {'On' if self.status else 'OFF'}, Brightness {self.brightness}"
            
class Thermostat(SmartDevice):
    def __init__(self,name):
        self.name = name
        self.temperature = 65.0

    def _check_temperature_limits(self, temp):
        if temp < 80 and temp > 55:
            return True
        else:
            return False
        
    def adjust_temperature(self, temp):
        temp = float(input())
        if self._check_temperature_limits(temp):
            self.temperature = temp

    def __str__(self):
        return f"{self.name}: {'On' if self.status else 'OFF'}, Temperature: {self.temperature}"

class Speaker(SmartDevice):
    def __init__(self,name):
        self.name = name
        self.volume  = 3

    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1
    def decraese_volume(self):
        if self.volume > 1:
            self.volume -= 1
    def __str__(self):
        return f"{self.name}: {'ON' if self.status else 'OFF'}, Volume: {self.volume}"

class SmartHome(SmartDevice):
    devices = [Speaker, Thermostat, Light]

    def __add__(self, other):
        other = input()
        self.devices.append(other)

    def turn_off_all(self):
        Light.turn_off()
        Thermostat.turn_off()
        Speaker.turn_off()
    def __str__(self):
        return f"{Light.status()} {Speaker.status()} {Light.status()}"



    

        


