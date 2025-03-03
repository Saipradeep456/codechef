# Problems in your to-do list

T = int(input())
for _ in range(T):
    N = int(input())
    different = list(map(int,input().split()))
    count = 0
    for i in different:
        if i >= 1000:
            count+=1
    print(count)
    