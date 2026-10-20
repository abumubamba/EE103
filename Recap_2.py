Student_id=int(input("your student ID: "))
f"{Student_id} is your student ID"

Name_lower="osman"
Name_upper=Name_lower.upper() 
print(Name_upper)
print(Name_lower[::-1])

this_year="2026"
First_two=float(this_year[0:2])
Last_two=float(this_year[2:4])
sum=First_two+Last_two
print(f"{sum:.2f}")
if sum==46:
    print("correct")
else:
    print("wrong")