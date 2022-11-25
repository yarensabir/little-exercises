import csv
import matplotlib.pyplot as plt

counter = 1
time = [0]
date_time = [0]
RAM = [0]
CPU = [0]

try: 
    file =  "/file.csv"
    lines = open(file).readlines()
    for text in lines:
        Time, DateTime, cpu, ram = text.split(",")         
        try:
            ram, *_ = ram.split("\n")
        except Exception as e:
            pass

        time.append(Time)
        date_time.append(DateTime)
        RAM.append(float(ram))
        CPU.append(float(cpu))
    counter +=1
except Exception as e:
    print("exception at line " + str(counter))
    print(e)


#MEANS
RAM.pop(0)
CPU.pop(0)
ram_ort = 0
cpu_ort = 0

for x in range(len(RAM)):
    ram_ort = RAM[x] + ram_ort
    cpu_ort = CPU[x] + cpu_ort

print("ram ort: " + str(ram_ort/len(RAM)))
print("cpu ort: " + str(cpu_ort/len(RAM)))

print("\n")
print("max_ram: " + str(max(RAM)))
print("min_ram: " + str(min(RAM)))
print("max_cpu: " + str(max(CPU)))
print("min_cpu: " + str(min(CPU)))

#---------------------------------------
PLOTTING
plt.figure(figsize=(10,10))
plt.figure(1)
plt.suptitle('cpu usage')
plt.xlabel("time")
plt.ylabel("cpu%")
plt.plot(time, CPU, color = "lime")

plt.figure(figsize=(10,10))
plt.figure(2)
plt.suptitle('ram usage')
plt.xlabel("time")
plt.ylabel("ram%")
plt.plot(time, RAM, color = "blueviolet")

plt.draw()
plt.pause(0.01)
