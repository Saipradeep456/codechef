# X Jumps....?

# cook your dish here
T = int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    jumps_stairs = X//Y
    big_jump = jumps_stairs+(X%Y)
    print(big_jump)


# Chessboard Distance.....?


# cook your dish here
T = int(input())
for _ in range(T):
    X1,Y1,X2,Y2 = map(int,input().split())
    chess_board = abs(X1-X2)
    board = abs(Y1-Y2)
    multi_board = max(chess_board, board)
    print(multi_board)


# Valentine is Coming
# cook your dish here
T = int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    valentine_day = (X//Y)
    print(valentine_day)


# It is My Serve

# cook your dish here
T = int(input())
for _ in range(T):
    P,Q = map(int,input().split())
    serve = P+Q
    tennis = serve//2
    if tennis % 2==0:
        print("Alice")
    else:
        print("Bob")
   

# Water Mixing

# cook your dish here
T = int(input())
for _ in range(T):
    A,B,X,Y = map(int,input().split())
    if  A == B:
        print("YES")
    elif B > A and (B - A) <= X:
        print("YES")
    elif A > B and (A - B) <=Y:
        print("YES")
    else:
        print("NO")
