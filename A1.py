import math

def count(n,k):
    if n < k:
        return 0
    
    # C(n, k) = (n + k - 1)! / k! * (n - 1)!
    return math.factorial(n + k - 1) // math.factorial(k) * math.factorial(n - 1)

while True:
    #input of data
    k = input("Enter k: ")
    n = input("Enter n: ")

    # basic check for input
    if k.isdigit() and n.isdigit():
        k = int(k)
        n = int(n)
    else:
        print("You must enter digits to continue!!!")
        continue
    
    # printing result
    print("Number of ways rabbit can jump ladder is: " + str(count(n, k)))






