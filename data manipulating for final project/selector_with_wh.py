#!/usr/bin/python3
# -*- coding: utf-8 -*-

def selector_with_wh(path1, path2,  fileCount, filter):
    """
    wh_filter_finder ile istediğimiz etiketin alanını bulduk. 
    Bu fonksiyon ile bulduğumuz alana eşit ve büyük olacak şekilde etikete sahip olan resimleri ayıklıyoruz.

    filter = wh_filter_finder ile return ettiğimiz wh
    path1 = kaynak dosya yolu
    path2 = hedef dosya yolu
    fileCount = klasördeki text dosyası sayısı
    """
    filter = int(filter) 
    for i in range(1,fileCount+1):
        try: 
            file =  path1 + str(i) + ".txt" 
            lines = open(file).readlines()
            for text in lines:
                id, x, y, w, h = text.split(" ") 
                w = float(w) * 1000
                h = float(h) * 1000
                wh = int(w*h)
                if wh >= filter:
                    dosya = path2 + str(i) + ".txt"
                    with open(dosya, 'a') as f:
                        f.write(text)           
        except Exception:
            pass