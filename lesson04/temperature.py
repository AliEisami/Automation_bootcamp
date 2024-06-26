import numpy as np
import pandas as pd

class WeekTemperature:
    def __init__(self, low, high):
        self._low = low
        self._high = high

    @property
    def low(self):
        return self._low

    @low.setter
    def low(self, low):
        self._low = low

    @property
    def high(self):
        return self._high

    @high.setter
    def high(self, high):
        self._high = high

    #function that generate temperature for every day in the week
    def week_temperature(self):
        days_temperature = pd.DataFrame(np.random.randint(self._low, self._high, size=7),
                          ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
        return days_temperature