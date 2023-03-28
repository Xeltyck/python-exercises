from re import L


List  = []
Number  = int(input("Ingrese el número: "))
Factorial = 1

for Y in range(1,(Number+1)):
    Factorial  = Factorial * Y
    
print(Factorial)

