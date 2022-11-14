import time
import matplotlib.pyplot as plt
import numpy as np

data1_array = [0]
data2_array = [0]
sayac = [0]
s_sayac = 0

while True:
    sayac.append(s_sayac)
    s_sayac +=1

    data1 = read_data() #temsili veri girişi
    data2 = read_data()
    
    data1_array.append(data1)
    data2_array.append(data2)
    
    plt.figure(1)
    plt.suptitle('graphic 1')
    plt.plot(sayac,data1_array)

    plt.figure(2)
    plt.suptitle('graphic 2')
    plt.plot(sayac,data2_array)

    plt.draw()
    plt.pause(0.01)

    
