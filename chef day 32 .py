# Weights

# cook your dish here
T = int(input())
for _ in range(T):
    W,X,Y,Z = map(int,input().split())
    if W == X or W == Y or W == Z or W == X+Y or W == X+Z or W == Y+Z or W == X+Y+Z :
        print("YES")
    else:
        print("NO")
    
# Chef and his Apps

# cook your dish here
T = int(input())
for _ in range(T):
    S,X,Y,Z = map(int,input().split())
    if S - (X+Y)>=Z :
        print("0")
    elif S -Y-Z>=Z or S-X>=Z:
        print("1")
    else:
        print("2")

# Chef Eren

# cook your dish here
T = int(input())
for _ in range(T):
    N,A,B = map(int,input().split())
    count_odd = (N+1)//2
    count_even = N//2
    total_episode = count_odd*B + count_even*A
    print(total_episode)