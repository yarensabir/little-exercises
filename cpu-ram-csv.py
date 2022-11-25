import cv2, sys, time, psutil, csv
from time import sleep
from datetime import datetime

CPU = [0]
RAM_percent = [0]
raw_time = [0]
date_time = [0]

while True:
    print("while")
    date_time.append(datetime.now())
    raw_time.append(time.time())
    
    CPU.append(psutil.cpu_percent(percpu=False))
    RAM_percent.append(psutil.virtual_memory().percent)
    
    if time.time() - raw_time[1] > 120:
        break
    
    time.sleep(0.1)
CPU.pop(0)
RAM_percent.pop(0)
raw_time.pop(0)
date_time.pop(0)

with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Time','DateTime', 'CPU', 'RAM']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for x in range(len(date_time)):            
        writer.writerow({'Time': raw_time[x], 'DateTime':date_time[x], 'CPU':CPU[x], 'RAM':RAM_percent[x]})

print("csv yazıldı")

