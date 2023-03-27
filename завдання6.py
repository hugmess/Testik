temperatura = float(input("Введіть температуру"))

if temperatura <=0:
    print("Вода перебуває в твердому стані")
elif temperatura >0 and temperatura <=100:
    print("Вода перебуває в рідкому стані")
else:
    print("Вода перебуває в газоподібному стані")
