Nomor = [8, 3, 12, 4, 7, 2]

for i in range(len(Nomor)):
    if Nomor[i] < 5:
        Nomor[i] = 0

Nomor.sort(reverse=True)

print(Nomor)
