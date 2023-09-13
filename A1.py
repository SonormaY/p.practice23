import math

def count(n,k):
    # checkig for correct data
    if n < k:
        return 0
    
    # creating array and sarting value
    dp = [0] * (n + 1)
    dp[0] = 1 

    # outer cycle for counting path to every step
    for i in range(1, n + 1):
        # inner cycle for counting paths to specific step
        for j in range(1, min(i, k) + 1):
            dp[i] += dp[i - j]

    return dp[n]

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






