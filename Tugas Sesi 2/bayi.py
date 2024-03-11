bayi = int(input("Berapa umur anda: "))

if bayi <=2 :
    panggilan = ("Bayi")
elif bayi <=5 :
    panggilan = ("Balita")
elif bayi <=12 :
    panggilan = ("Anak - Anak")
elif bayi <=17 :
    panggilan = ("Remaja")
elif bayi > 17 and bayi <=30 :
    panggilan = ("Dewasa")
else :
    panggilan = ("Orang Tua")
print("Panggilan untuk manusia berumur", bayi, "tahun adalah", panggilan)