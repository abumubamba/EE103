a=int(input("give a number: ")) 
i=1
sum=0
while i<=a:
    sum=sum+i
    i+=1

b=a*(a+1)/2

if sum==b:
    print("code works perfectly and the sum of numbers from 1 to",a,"is",sum)
elif sum!=b:
        print("code failes")

