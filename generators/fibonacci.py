def fib(num):
    a = 0
    b = 1

    for i in range(num):
        yield a # Return current number and than recalculate a and b for next number
        temp = a
        a = b
        b = temp + b

for x in fib(10):
    print(x)