print(type(float(123)))
print(type(123))

s="Aho54yuOsman42z.89tur"
print(s[7:12])
print((s[11:6:-1]))

x=float(input("what x to find the cube root of?: "))
g=float(input("what guess to start with?: "))
i=g-(g**3-x)/(3*g**2) 
print("your guess is ", i)