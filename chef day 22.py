# Air Conditioner Temperature

T = int(input())
for _ in range(T):
    A,B,C = map(int,input().split())
    if max(A,C) <= B:
        
        print("YES")
    else:
        print("NO")



# Nearest Exit

T = int(input())
for _ in range(T):
    X = int(input())
    if X <= 50:
        print("LEFT")
    else:
        print("RIGHT")

# Reverse The Number

T = int(input())
for _ in range(T):
    N = int(input())
    reversed = int(str(N)[::-1])
    print(reversed)
    