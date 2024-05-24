buah = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]

i = 0
while i < len(buah):
    if len(buah[i]) < 5:
        del buah[i]
    else:
        i += 1

buah.sort()

print(buah)