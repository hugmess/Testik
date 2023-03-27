#для примера я решила взять простой калькулятор

a = int(input("Введи первое число "))
b = int(input("Введи второе число "))

znak = input("Знак? ")


if znak == "+":
 print(a+b)
elif znak == "-":
 print(a-b)
elif znak == "*":
 print(a*b)
elif znak == "/":
  print (a/b)
else:
  print("Не тот знак")

if b == 0:
 print("НОООЛЬ НЕЛЬЗЯ")
else:
 print(a/b)

if a == 0:
 print("НОООЛЬ НЕЛЬЗЯ")
else:
 print(a/b)

