from Secret_name import SecretNumber
attempts=0
while True:
    g=int(input("what is the secret number?")) 
    attempts+=1
    if g<SecretNumber:
        print("too low")    
    elif g>SecretNumber:
        print("too high")  
    else:
        print("You find it hooray")
        break
    if attempts>=5:
        break

if attempts>=5 and g !=SecretNumber:
    while True:
        print("no more attempts sorry buddy")