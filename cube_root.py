a=int(input("Enter a number: "))
if a<0:
    b= -(-a)**(1/3)
else:
    b= a**(1/3)
print("The cube root of", a, "is", b)