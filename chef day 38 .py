# Get Lowest Free

# cook your dish here
T = int(input())
for  _ in range(T):
    A,B,C = map(int,input().split())
    super_market = A+B+C - min(A,B,C)
    print(super_market)


# Minimum number of Flips

# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    total_flip = sum(A)
    if total_flip % 2 != 0:
        print(-1)
    else:
       num_flip = abs(total_flip)//2
       print(num_flip)
       
    

# Binary Battles

# cook your dish here
import math
T  = int(input())
for _ in range(T):
    N ,A,B =  map(int,input().split())
    rounds = int(math.log2(N))
    binary_battle = rounds *A + B* (rounds-1)
    print(binary_battle)


