class Temperature:
    def __init__(self):
        self._kelvin = None
        self._celsius = None
        self._fahrenheit = None

    @property
    def kelvin(self):
        return self._kelvin

    @kelvin.setter
    def kelvin(self, value):
        self._kelvin = value
        self._celsius = value - 273.15
        self._fahrenheit = value * 9/5 - 459.67

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value
        self._kelvin = value + 273.15
        self._fahrenheit = value * 9/5 + 32

    @property
    def fahrenheit(self):
        return self._fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._fahrenheit = value
        self._celsius = (value - 32) * 5/9
        self._kelvin = (value + 459.67) * 5/9

t1 = Temperature()
t1.kelvin = 0
print(t1.kelvin)
print(t1.celsius)
print(t1.fahrenheit)
t1.fahrenheit = 20
print(t1.kelvin)
print(t1.celsius)
print(t1.fahrenheit)
t1.celsius = 30
print(t1.kelvin)
print(t1.celsius)
print(t1.fahrenheit)