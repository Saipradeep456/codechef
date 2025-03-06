
# Sasta Shark Tank

# cook your dish here
T = int(input())
for _ in range(T):
    A,B = map(int,input().split())
    if A*10 >B*5:
        print("FIRST")
    elif A*10<B*5:
        print("SECOND")
    else:
        print("ANY")



# Good Program

# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    if N%4 == 0:
        print("Good")
    else:
        print("Not Good")


# Qualify the round

# cook your dish here
T = int(input())
for _ in range(T):
    X,A,B = map(int,input().split())
    total_Score = (A*1)+(B*2)
    if total_Score>=X:
        print("Qualify")
    else:
        print("NotQualify")