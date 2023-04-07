ph = float (input("Ingrese acidez: "))
ca = float (input("Ingrese CA: "))

if ph >= 5.6 and ph <= 6.5:
    va1 = 1
elif (ph > 6.5 and ph <= 7) or (ph < 5.6 and ph >= 5.1):
    va1 = 2
elif (ph > 7 and ph <= 8) or (ph < 5.1 and ph >= 4.5):
    va1 = 3
else:
    va1 = 4

if ca >= 2 and ca <= 4:
    va2 = 1
elif ca >4 and ca <= 8:
    va2 = 2
elif ca > 8 and ca <= 12:
    va2 = 3
else:
    va2 = 4

if va1 == va2:
    impr = va1
    if impr == 1:
        print ("Sumamente Apto")
    elif impr == 2:
        print ("Moderadamente apto")
    elif impr == 3:
        print ("Marginalmente apto")
    else:
        print ("No apto")
elif va1 > va2:
    impr = va2
    if impr == 1:
        print ("Sumamente Apto")
    elif impr == 2:
        print ("Moderadamente apto")
    elif impr == 3:
        print ("Marginalmente apto")
    else:
        print ("No apto")
else:
    impr = va2
    if impr == 1:
        print ("Sumamente Apto")
    elif impr == 2:
        print ("Moderadamente apto")
    elif impr == 3:
        print ("Marginalmente apto")
    else:
        print ("No apto")
