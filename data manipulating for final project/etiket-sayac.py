#!/usr/bin/python3
# -*- coding: utf-8 -*-

#liste döndürmek için gerekli kütüphaneyi import ediyoruz
from array import *
from cgi import test
from logging.config import valid_ident 

def readTXT(path, fileCount, classCount):
    #sahip olduğumuz sınıf sayısı büyüklüğünde liste oluşturuyoruz
    #her index classes.txt dosyasının bir fazla numaralı satırında olan etiketin sayısını tutacak
    #yani sıfırıncı indexte classes.txt dosyasındaki birinci satırda bulunan etiketin sayısı tutulacak
    counters = [0]*classCount
    #etiketli fotoğraf sayısı = fileCount
    #dosyaları kolay okuyabilmek adına aritmetik artan biçimde yeniden isimlendirme yaptım
    #yani resimler ve .txt dosya isimlendirmesi 1.jpg 1.txt, 2.jpg, 2.txt,  ... şeklinde
    for i in range(1,fileCount+1):
        try: 
            #klasörden tek tek .txt dosyalarını alıyoruz
            file =  path + str(i) + ".txt" 
            #aldığımız dosyayı alıp açıyoruz
            lines = open(file).readlines()
            #bir dosyada birden fazla satır var, bu satırları aşağıdaki for ile dolaşıyoruz
            for text in lines:
                #dosyalarda ilk parça hangi etiket olduğunu belirtiyor
                #bu yüzden split ile parçalayıp sadece ilk parçayı kullanabileceğimiz bir değişkene atıyoruz
                text, *_ = text.split(" ") 
                #etiketleri saydırdığımız döngü
                for j in range(0,classCount): 
                    if text == (str(j)):
                        counters[j] = counters[j] + 1
        except Exception:
            pass
    return counters


tests = readTXT("/home/yaren/rb2022/dataset/test/", 200000, 28)
valid = readTXT("/home/yaren/rb2022/dataset/valid/", 200000, 28)
train = readTXT("/home/yaren/rb2022/dataset/train/", 200000, 28)
toplam = [0]*28 
for x in range(28):
    toplam[x] = tests[x] + valid[x] + train[x]

print(toplam)
