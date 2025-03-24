# Chef Fantasy 11

# cook your dish here
T = int(input())
for _ in range(T):
    N =int(input())
    world_up = N * (N-1)
    print(world_up)

# Building Race

# cook your dish here
T = int(input())
for _ in range(T):
    A,B,X,Y = map(int,input().split())
    chef = A/X 
    chefina = B/Y 
    if chef < chefina:
        print("Chef")
    elif chef > chefina:
        print("chefina")
    else:
        print("Both")

# Chef and Races

# cook your dish here
T = int(input())
for _ in range(T):
    X,Y,A,B = map(int,input().split())
    wins = 0
    if X!=A and X!=B:
        wins+=1
    if Y !=A and Y !=B :
        wins+=1
    print(wins)
   

# Endless Appetizers

# cook your dish here
import math
T = int(input())
for _ in range(T):
    X,Y,R = map(int,input().split())
    total_stick = X+(R/30)
    sticks = math.ceil(total_stick/Y)  
    print(sticks)


# Presents for Cheffina

# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    gift_price = N -(N//5) 
    print(gift_price)
    

