def fibonacci(num) :
    a = 0
    b = 1
    
    i = 0
    while i < num :
        print(a, end=" , ")
        c = a + b
        a = b
        b = c
        
        i += 1
n = int(input("Enter the number: "))
fib = fibonacci(n)
print(fib)
fibonacci(n)
