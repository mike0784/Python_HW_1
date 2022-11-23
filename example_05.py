print("2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат")

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            text = "~(" + str(x) + " or " + str(y) + " or " + str(z) + ") = " + str(not(x or y or z)) + "   ~" + str(x) + " and ~" + str(y) + " and ~" + str(z) + " = " + str((not x) and (not y) and (not z))
            if not(x or y or z) == ((not x) and (not y) and (not z)):
                print(text + "    Обе части равны")
            else:
                print(text + "    Части не равны")
                