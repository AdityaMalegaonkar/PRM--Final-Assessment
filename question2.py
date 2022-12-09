n = int(input("Enter a number : "))
a = 0
b = 1
if n <= 0:
    print("Incorrect input")
elif n == 1:
    print(b)
else:
    for i in range(3,n+1):
        c = a + b
        a = b
        b = c
    print(b)