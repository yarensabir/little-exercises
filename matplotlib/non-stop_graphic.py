import time
import matplotlib.pyplot as plt
import numpy as np

data_array = [0]
sayac = [0]
s_sayac = 0

while True:
    data = read_data() #temsili veri girişi
    data_array.append(data)
    sayac.append(s_sayac)
    s_sayac +=1
    plt.plot(sayac,data_array)
    plt.draw()
    plt.pause(0.01)