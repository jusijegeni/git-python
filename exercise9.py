num = int(input("enter number of digits you want in series (minimum 2): "))

first = 0
second = 1

print("\nfibonacci series is:")
print(first, ",", second, end=", ")

for i in range(2, num):
    next = first + second
    print(next, end=", ")

    first = second
    second = next
    
"""""
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

n = int(input("Enter number of terms:"))

print("Fibonacci sequence:")
for i in range(n):
    print (fibonacci(i))

