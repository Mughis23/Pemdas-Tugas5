tahun = int(input("Tahun berapa yang ingin anda input :"))

if tahun % 4 == 0 :
    status = ("Tahun Kabisat")
else : 
    status = ("Bukan tahun Kabisat")
print(tahun, "merupakan", status)