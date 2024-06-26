import numpy as np
import pandas as pd
from temperature import WeekTemperature

def main():
    # dt = pd.DataFrame(np.random.randint(20, 30, size=7),
    #                   ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])
    week_tempreture = WeekTemperature(20, 30)
    print(week_tempreture.week_temperature())

main()