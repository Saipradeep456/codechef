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



        