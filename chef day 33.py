# Minimum number of coins

# cook your dish here
T = int(input())
for _ in range(T):
    X = int(input())
    if X % 5 == 0:
        if X % 10 == 0:
            print(X//10)
        else:
            print(X//10+1)
    else:
        print(-1)
        
               
            
# Airlines


# cook your dish here
import math
T = int(input())
for _ in range(T):
    X,N = map(int,input().split())
    planes_mood = math.ceil(N/100)
    travel_extract = max(0,planes_mood-X)
    print(travel_extract)


# Self Defence Training

# cook your dish here
T = int(input())
for _ in range(T):
    N =  int(input())
    Ai =  list(map(int,input().split()))
    count = 0
    for selfdef in Ai:
        if 10 <= selfdef <= 60:
            count+=1
    print(count)
  

# Cup Finals

# cook your dish here
T = int(input())
for _ in range(T):
    X,Y,D = map(int,input().split())
    if abs(X-Y )<= D:
        print("YES")
    else:
        print("NO")


