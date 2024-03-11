ipa = int(input("Masukan nilai Ipa anda : "))
matematika = int(input("Masukan nilai Matematika anda :"))
indo = int(input("Masukan nilai Indonesia anda : "))
inggris = int(input("Masukan nilai Inggris anda : "))
ips = int(input("Masukan nilai IPS anda : "))

rataIngMatIndo = (inggris + matematika + indo) / 3
rataSemua = (ipa + matematika + indo + inggris + ips) / 5


if rataIngMatIndo >= 75:
    kelulusan = "Lulus"
elif rataSemua >= 70:
    kelulusan = "Lulus"
elif matematika > 90 and inggris > 90:
    kelulusan = "Lulus"
else: 
    kelulusan = "Tidak Lulus"

print ("Anda dinyatakan", kelulusan) 