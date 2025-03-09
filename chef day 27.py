# Small factorials
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

t = int(input())
for _ in range(t):
    n = int(input())
    print(factorial(n)) 

# Mario and Transformation


# cook your dish here
T = int(input())
for _ in range(T):
    X = int(input())
    if X%3 == 0:
        print("Normal")
    elif X%3 == 1:
        print("HUGE")
    else:
        print("SMALL")

# Mario and Bullet

T = int(input())
for _ in range(T):
    X,Y,Z = map(int,input().split())
    mario_bull = max(0,Z-(Y//X))
    print(mario_bull)
    