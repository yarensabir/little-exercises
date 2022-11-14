#!/usr/bin/python3
# -*- coding: utf-8 -*-

def wh_finder(path,file_number):
    
    """
    bu fonksiyon, nesne tespiti için boyunun küçük olduğunu düşündüğümüz etiketleri elemek için kullanıldı.
    bu fonksiyon ile boyunun uygun olduğunu düşündüğümüz etiketin alanını buluyoruz.
    
    uygulandığı veri seti şu şekildedir: her resimde 1 adet trafik levhası bulunmaktadır ve düz bir yolda sırayla bu tabelaların görüntüleri toplanmıştır
    ayrıca dosya isimleri 1.txt, 2.txt, 3.txt şeklinde sıralıdır

    file number = etiket boyunun uygun olduğuna karar verdiğimiz resim
    path = resmin bulunduğu klasörün yolu
    """

    file =  path + str(file_number) + ".txt" #dosyanın uzantılı tam adı
    lines = open(file).readlines()
    for text in lines: #text dosyası içindeki saıtlarda dolaşıyoruz (bizim senaryomuzda her .txt dosyasında 1 satır bulunmakta)
        #dosyamızın içindeki veri şu şekilde: 1 0.692187 0.295833 0.053125 0.097222
        #bu veriyi boşluklarından ayırıyoruz ve ilgili değişkenlere atıyoruz
        id, x, y, w, h = text.split(" ") 
        #değerlerimiz çarpma işlemi sonucunda küçülmesin diye büyütüyoruz
        w = float(w)* 1000
        h = float(h) * 1000
        wh = int(w*h) #etiketin alanı (orijinal alan değil ama bizim işimize yarıyor)
    return wh