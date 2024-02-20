gajiBulanan = int(input("Gaji bulanan : "))
masukKerja = int(input("Berapa hari anda masuk kerja : "))
uangTransport = 100000 * masukKerja
uangMakan = 50000 * masukKerja
uangLembur = int(input("Berapa jam kerja lembur anda : "))
if uangLembur <= 2:
    totalLembur = uangLembur * 100000
else : 
    totalLembur = 2 * 100000 + (uangLembur - 2 ) * 150000
honor = gajiBulanan+uangTransport+uangMakan+totalLembur
print("Uang honor yang didapat Rp.%i"%honor)