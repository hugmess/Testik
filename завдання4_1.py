import math

a = int(input("Введіть a -> "))

if -1 < a < 1:
    y = 1 - math.sin(a)
else:
    y = 0
print(y)