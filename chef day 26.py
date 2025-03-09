# Watching Movies at 2x

X,Y = map(int,input().split())
total_minutes = (Y//2)+(X-Y)
print(total_minutes)



# Police and Thief
# cook your dish here
T = int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    distance = abs(X-Y)//1
    print(int(distance))


# Flip the cards

T = int(input())
for _ in range(T):
    N,X = map(int,input().split())
    fac_card = min(X,N-X)
    print(fac_card)


# Bath in Winters

# cook your dish here
T = int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    buckets_li = X //(2*Y)
    print(buckets_li)


# Finding Shoes

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    shoes_pairs = max(N,2*N- M)
    print(shoes_pairs)
