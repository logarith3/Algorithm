c = int(input())

for i in range(0,c):
    t = input().split()
    t = list(map(int,t))
    print("Case #"+str(i+1)+":",t[0],"+",t[1],"=",t[0] + t[1])
