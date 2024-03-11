uangAwal = int(input("Masukan uang anda : "))
pengeluaran = int(input("Berapa pengeluaran anda : "))

if pengeluaran > 60000:
    pengeluaran -= 10000
    
total = pengeluaran
kembalian = uangAwal - pengeluaran

print("Total belanjaan anda Rp%i dan kembaliannnya Rp.%i" %(total, kembalian))