# 
#	  these files are created by
#		Aryaman Godara		
#

#
#	Any changes for better is accepted, cause these are made in the initial phase of my coding 
#
from math import sqrt

def check_prime(numb):
    prm = True
    for i in range(2, int(sqrt(numb)) + 1):
        if numb % i == 0:
            prm = False
            break
    return prm


print("Welcome to Godara PrimeTech.")

menu = 0

while True:
    print(
        "\nPress:\n1.To check a no. is prime or composite\n2.Enter a number , upto you want to list out all the prime numbers\n3.Exit to os\n"
    )
    try:
        menu = int(input())
    except ValueError:
        print("Invalid")

    if menu == 1:
        number = int(input("Enter the number: "))
        if check_prime(number):
            print("Prime no.")
        else:
            print("Composite no.")

    elif menu == 2:
        list = []
        n = int(input("Enter a number: "))
        if n < 1:
            print("invalid")
        else:
            for i in range(2, n + 1):
                if check_prime(i):
                    list.append(i)
        print(list)
        print("No. of primes are " + str(len(list)))

    elif menu == 3:
        print("Thanks for using our software!!!")
        break

    else:
        print("Atleast chose a options:)")