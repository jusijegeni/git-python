def is_Power(x):
   while (x%2 == 0):
       x = x / 2
   return x == 1

print(is_Power(int(input("Jep nje numer : "))))

