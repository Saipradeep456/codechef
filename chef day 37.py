# Small Factorial

# cook your dish here
def small_factorial (n):
    count = 1
    for i in range(1,n+1):
        count *= i
    return count
T = int(input())
for _ in range(T):
    N = int(input())
    print(small_factorial(N))



# Dracula Eats


# cook your dish here
# import math
T  = int(input())
for _ in range(T):
    N = int(input())
    Dracula_eats = 1+(N-2)//7
    print(Dracula_eats)


# Single-use Attack
# cook your dish here
import math
T = int(input())
for _ in range(T):
    H,X,Y = map(int,input().split())
    Attacks = 1+math.ceil(max(0,H-Y)/X)
    print(Attacks)


# Reach fast


# cook your dish here
import math
T = int(input())
for _ in range(T):
    A,B,K = map(int,input().split())
    steps = abs(A - B)
    disyances = math.ceil(steps / K)
    print(int(disyances))

