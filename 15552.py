import sys
c = int(sys.stdin.readline().rstrip())
for i in range(0,c):
    t = list(map(int,sys.stdin.readline().rstrip().split()))
    print(t[0] + t[1])
