import math

def count(n,k):
    if n < k:
        return 0
    

    # C(n, k) = (n + k - 1)! / k! * (n - 1)!
    return math.factorial(n + k - 1) // math.factorial(k) * math.factorial(n - 1)





