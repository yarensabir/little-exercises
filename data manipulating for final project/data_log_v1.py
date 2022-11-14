#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
from time import sleep
from datetime import datetime

file = open("/home/yaren/data_log.csv", "a") #dosya append modunda açılıyor
i=0 #dosyaya yazmak için bir değer

#dosyanın boyu sıfırsa yani hiç oluşturulmamışsa header ekleyerek dosyanın açılışını yapıyoruz
if os.stat("/home/yaren/data_log.csv").st_size == 0: 
    file.write("Time,Sensor1,Sensor2,Sensor3,Sensor4,Sensor5\n")

#dosyaya 5 saniyede bir i'ye bağlı olarak veri yazıyoruz
while True:
    i = i + 1
    now = datetime.now() #YYYY-AA-GG Saat:Dakika:Saniye.Salise formatında tarih bilgisi
    file.write(str(now) + "," + str(i) + "," + str(-i) + "," + str(i-10) + "," +str (i+5) + "," + str(i*i) + "\n")
    file.flush()
    time.sleep(5)
file.close()
