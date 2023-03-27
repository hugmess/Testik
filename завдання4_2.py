x = int(input("Введіть х -> "))

if x < 0:
    y = x
elif x <= 1:
    y = x ** 2
else:  
    y = 2 * x
print(y)
