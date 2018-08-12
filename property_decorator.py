
# coding=utf-8


class Celsius1:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

class Celsius2:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # new update
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

class Celsius3:
    def __init__(self, temperature = 0):
        self._temperature = temperature


    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    def to_fahrenheit(self):
        print(self._temperature)
        return (self.temperature * 1.8) + 32

if __name__ == '__main__':
	# man = Celsius1()
	# man.temperature = 37
	# print(man.to_fahrenheit())
	
	# c = Celsius2(-10)
	# print(c.to_fahrenheit())
	c = Celsius3(37)
	print(c)
	print(c.temperature)
	# print(c.to_fahrenheit())

