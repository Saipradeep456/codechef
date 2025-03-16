# Blackjack
T = int(input())
for _ in range(T):
    A,B = map(int,input().split())
    X = 21- (A+B)
    if 1<= X <=10:
        print(X)
    else:
        print(-1)
        

# Fill Candies
import math
T = int(input())
for _ in range(T):
    N,K,M = map(int,input().split())
    candies_birthday = K*M
    capicity = math .ceil(N/candies_birthday)
    print(capicity)