atm = [500000,200000,100000,50000,20000,10000,5000,2000,1000]
a=[]
i = "co"
while(i == "co"):
    tien = int(input("nhap so tien can rut la: "))
    for i in atm:
        if(tien >= i):
            a.append([i,tien//i])
            tien = tien - (tien//i)*i
    for i in a:
        print(i)
    i = input("ban co muon rut tien tiep hay khong?\nNhap co hoac khong: ")