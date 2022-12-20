# alınan vize notuna göre final notunun min kaç olması gerektiğini hesaplama

# geçme notu 35
# açık öğretim için

import csv

def v1_3070():
    """ vize %30, final %70 """
    vize = [0]
    final = [0]

    for x in range(101):
        print(str(x) +" - "+ str((35-x*3/10)*(10/7)))
        vize.append(x)
        final.append(str((35-x*3/10)*(10/7)))
    vize.pop(0)
    final.pop(0)
    return vize, final

def v2_4060():
    """ vize %40, final %60 """
    vize = [0]
    final = [0]

    for x in range(101):
        print(str(x) +" - "+ str((35-x*4/10)*(10/6)))
        vize.append(x)
        final.append(str((35-x*4/10)*(10/6)))
    vize.pop(0)
    final.pop(0)
    return vize, final


if __name__ == "__main__":

    vize, final = v1_3070()
    #vize, final = v2_4060()

    with open('final_kac_olmali.csv', 'w', newline='') as csvfile:
        fieldnames = ['Vize','Final(min)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for x in range(len(vize)):            
            writer.writerow({'Vize':vize[x],'Final(min)':final[x]})
