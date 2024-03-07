kilogram = int(input("Anda ingin membeli mangga berapa kg : "))

if kilogram <= 2:
    harga = 20_000
elif kilogram <= 5:
    harga = 18_000
else : 
    harga = 16_000

totalHarga = kilogram * harga
print(totalHarga)



