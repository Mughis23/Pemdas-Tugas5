nilai = int(input("Masukan nilai anda = "))
if nilai < 50 :
    predikat = "E"
elif nilai >=50 and nilai <60 :
    predikat = "D"
elif nilai >=60 and nilai <70 :
    predikat = "C"
elif nilai >=70 and nilai <80  :
    predikat = "B"
else :
    predikat = "A"

print ("Anda mendapat predikat", predikat, "dengan nilai", nilai)