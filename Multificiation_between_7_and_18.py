result=1
initial=7
while initial<=18:
    result=result*initial
    initial+=1
print("Multiplication of numbers between 7 and 18 is:", result)

result=1
for i in range(7,19):
    result *= i
print("Multiplication of numbers between 7 and 18 is:", result)