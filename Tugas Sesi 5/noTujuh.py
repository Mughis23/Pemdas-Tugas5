o = 1
p = 1
q = p
for i in range (10):
    print(o, end=" ")
    q = o + p
    o = p
    p = q