r = 1
s = 2
t = 3

print(r, end=" ")
print(s, end =" ")
print(t, end =" ")
for i in range(7):
    u = r + s + t
    print(u, end = " ")
    r = s
    s = t
    t = u