# A or B

# cook your dish here
#    
T = int(input())  
for _ in range(T):
    X, Y = map(int, input().split())  
    max_points = max((500 - 2 * X) + (1000 - 4 * (X + Y)), (1000 - 4 * Y) + (500 - 2 * (X + Y)))
    print(max_points) 


# Second Largest

# cook your dish here
T = int(input())
for _ in range(T):
    
    A,B,C = map(int,input().split())
    max_minmn = A+B+C -max(A,B,C)-min(A,B,C)
    print(max_minmn)


# Pass or Fail

# cook your dish here
T = int(input())
for _ in range(T):
    N,X,P = map(int,input().split())
    SCORE = 3* X - (N-X)
    if SCORE >= P:
        print("PASS")
    else:
        print("FAIL")



# Cyclic Quadrilateral

# cook your dish here
T = int(input())
for _ in range(T):
    A,B,C,D = map(int,input().split())
    if A + C == 180:
        print("YES")
    else:
        print("NO")


# Too many items

# cook your dish here
import math
T = int(input())
for _ in range(T):
    N = int(input())
    chef_item = math.ceil(N/10)
    print(chef_item)


