# Python Object Programming Reference

#### @property
Try to avoid getter and setter, but to use @property. For example, 
```python
class Parrot:
    def __init__(self,):
        self._voltage = 100000
    @property
    def voltage(self):
        return self._voltage
    @voltage.setter
    def voltage(self, value):
        self._voltage = value
    @voltage.deleter
    def voltage(self):
        del self._voltage

parrot = Parrot()
print(parrot.voltage)
parrot.voltage = 999
print(parrot.voltage)
```
