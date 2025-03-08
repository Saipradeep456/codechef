# Bus Seat Numbering

T = int(input())
for _ in range(T):
    N = int(input())
    if 1 <=N<=10:
        print("Lower Double")
    elif 11<=N<=15:
        print("Lower Single")
    elif 16<=N<=25:
        print("Upper Double")
    else:
        print("Upper Single")

# Discus Throw

T = int(input())
for _ in range(T):
    A,B,C = map(int,input().split())
    final_score = max(A,B,C)
    print(final_score)


# Maximise the Tastiness

T = int(input())
for _ in range(T):
    a,b,c,d = map(int,input().split())
    max_test = max(a,b)+max(c,d)
    print(max_test)
