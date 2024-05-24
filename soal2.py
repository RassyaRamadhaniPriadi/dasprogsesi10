
Nomor = [7, 4, 9, 2, 5, 1]

i = 0
while i < len(Nomor):
    if Nomor[i] % 2 != 0:  
        del Nomor[i]     
    else:
        i += 1           

Nomor.sort()


print(Nomor)