# Too many Floors

# cook your dish here
T = int(input())
for _ in range(T):
    X ,Y = map(int,input().split())
    floor_rom =(X-1)//10
    floor_y = (Y-1)//10 
    chef_chefina = abs (floor_rom - floor_y) 
    print(chef_chefina)


# Speed Limit Test


# cook your dish here
T = int(input())
for _ in range(T):
    A,X,B,Y = map(int,input().split())
    if A * Y > B * X :
        print("Alice")
    elif A * Y < B * X:
        print("Bob")
    else:
        print("Equal")


# Decrement OR Increment

N = int(input())
if N % 4 == 0:
    N = N + 1
else:
    N = N - 1
print(N)
