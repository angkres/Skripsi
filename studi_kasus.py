a = 0.9144
b = 0.9020
c = 0.8760
d = 0.8850
e = 0.8940

rata = (a+b+c+d+e)/5
print("Hasil rata-rata akurasi: ")
print(rata)
x= 0

if a > x:
    x = a
elif b > a:
    x = b
elif c > b:
    x = c
elif d > e:
    x = d
else:
    x = e
print("Akurasi tertinggi: ")
print(x)

y = 0
if a < b:
    y = a
elif b < c:
    y = b
elif c < d:
    y = c
elif d < e:
    y = d
else:
    y = e
print("Akurasi terendah: ")
print(y)