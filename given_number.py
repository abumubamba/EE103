given_number=int(input("Enter a number: "))
if given_number < 0:
    print("Please enter a non-negative integer.")
else:
    guess=1
    while guess**2 < given_number:
        guess += 1
    if guess**2 == given_number:
        print("The square root of", given_number, "is", guess)
    else:
        print(given_number, "is not a perfect square.")