
buah1 = ["apel", "jeruk", "mangga"]
buah2 = ["apel", "anggur", "nanas"]

buah_mix = buah1 + buah2


buah_sama = []

for fruit in buah_mix:
    if fruit not in buah_sama:
        buah_sama.append(fruit)

buah_sama.sort()

print(buah_sama)
print(buah_mix)