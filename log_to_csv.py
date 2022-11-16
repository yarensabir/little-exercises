import csv

date = [0]
data = [0]
counter = 0

try: 
    file =  "log.txt"
    lines = open(file).readlines()
    for text in lines:
        # log dosyamızı kaydettiğimiz örüntüye göre parçalamaya çalışıyoruz.
        # parçalama yapamıyorsak bu satır bir önceki satırın devamı olabilir
        # bu nedenle bir önceki satırın datası ile birleştiriyoruz
        try:
            date_, data_ = text.split("   ")
        except Exception:
            data_ = data[counter]
            data_ = data_ + text
        
        #bu satırı koyma nedenim:
        # csv ye yazılan datalarda alt satıra inme sorunu vardı
        # yani her bilgiden sonra boş bir alt satır bulunmaktaydı
        # fakat bu alt satır date'te oluşmadığı için sorunu data'nnın kendisi ile çözdüm
        data_, *_ = data_.split("\n") 
        
        date.append(date_)
        data.append(data_)
        counter +=1
    
    print("finito")

except Exception:
    print("exception at line " + str(counter))


with open("log.csv", 'w', newline='') as csvfile:
        fieldnames = ['Date','Data']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for x in range(len(date)):
            writer.writerow({'Date':date[x],'Data': data[x]})
        
        