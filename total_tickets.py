for Alyssa in range(11):
    for Ben in range(11):
        for Cindy in range(11):

            a=(Ben==Alyssa-2)
            b=(Cindy==Alyssa*2)
            c=(Alyssa+Cindy+Ben==10)
            if a and b and c:
                print("Alyssa has ",Alyssa,"tickets")