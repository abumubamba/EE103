first_number=int(input("Bir sayı giriniz: "))
Last__number=int(input("Bir sayı daha giriniz: "))
result_for=1
while first_number<=Last__number:
    result_for*=first_number
    first_number+=1
print(result_for)

for David in range(29):
    for Emma in range(29):
        for Frank in range(29):
            a=(Emma==David+3)
            b=(Frank==3*David)
            c=(Frank+David+Emma==28)
            if a and b and c:
                print("David has " ,David, "tickets")