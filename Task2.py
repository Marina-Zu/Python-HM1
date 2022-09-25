# Проверка истинности выражения


print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not (x or y or z)) == (not x and not y and not z): # не нашла, как ставиться знак обычного равенства
                print(x, y, z)