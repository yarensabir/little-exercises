#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
from time import sleep
from datetime import datetime

   
def data_logging(self, path):
    now = datetime.now() #YYYY-AA-GG Saat:Dakika:Saniye.Salise formatında tarih bilgisi
    file_name, *_ = self.now.split(' ') #dosyaları tarihleri ile kaydedeceğim için sadece baştaki tarih bilgisini alıyorum
    file_path = path + file_name + ".csv" #oluşturulacak dosya tam yolu
    file = open(file_path, "a") #dosyayı append modunda açıyoruz
    #deneme amaçlı dosyaların içine kendi oluşturduğumuz değişkene bağlı veri atıyoruz
    i=0
    if os.stat(file_path).st_size == 0:
        file.write("Time,Sensor1,Sensor2,Sensor3,Sensor4,Sensor5\n")
    while True:
        i = i + 1
        #tarih bilgisi + sensörler için anlamsız değerlerin yazılması
        file.write(str(self.now) + "," + str(i) + "," + str(-i) + "," + str(i-10) + "," +str (i+5) + "," + str(i*i) + "\n")
        file.flush()
        time.sleep(5) 
    file.close()

