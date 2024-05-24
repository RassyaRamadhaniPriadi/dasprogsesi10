
nilai = [105, 20, 8, 150, 30, 5, 200]

i = 0
while i < len(nilai):

    if nilai[i] < 10 or nilai[i] > 100:
        del nilai[i]
    else:
        i += 1

nilai.sort()

print(nilai)
