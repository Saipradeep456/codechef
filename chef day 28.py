# Chess Ratings
# cook your dish here
import math
T = int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    if X >=Y:
        print(0)
    else:
        sai =(Y-X)/8
        print(math.ceil(sai))
        

# Complementary Strand in a DNA

T = int(input())
for _ in range(T):
    N = int(input().strip())
    S = input().strip()
    complement = {'A':'T','T':'A','C':'G','G':'C'}
    sai = ''.join(complement[base] for base in S) 
    print(sai)

# chef  and water bottle
T = int(input())
for _ in range(T):
    N,X,K = map(int,input().split())
    bottle = min(N,k//x)
    print(bottle)

# Candy Distribution
T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    if (N/M)%2==0:
        print("YES")
    else:
        print("No")
