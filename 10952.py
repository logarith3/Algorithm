while True:
    t = list(map(int,input().split()))
    if bool(t):
        print("break out")
        break
    else:
        print(t[0] + t[1])
