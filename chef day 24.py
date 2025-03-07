# Elections in Chefland
# cook your dish here
T = int(input())
for _ in range(T):
    N,X = map(int,input().split())
    ages= list(map(int,input().split()))
    count = 0
    for i in ages:
        if i >= X:
            count+=1
    print(count)



# Minimum Cars required

# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    car_required =(N+3)//4
    print(car_required)



  # Test Score

# cook your dish here
T = int(input())
for _ in range(T):
    N,X,Y = map(int,input().split())
    if Y % X == 0 and Y <= N*X:
        print("YES")
    else:
        print("NO")



# Jenga Night

# cook your dish here
T = int(input())
for _ in range(T):
    N,X = map(int,input().split())
    if X%N == 0 :
        print("YES")
    else:
        print("NO")
      