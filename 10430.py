i = input().split()
i = list(map(int,i))
print((i[0]+i[1])%i[2])
print(((i[0]%i[2])+(i[1]%i[2]))%i[2])
print((i[0]*i[1])%i[2])
print(((i[0]%i[2])*(i[1]%i[2]))%i[2])
    
