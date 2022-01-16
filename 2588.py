a = input()
b = input()
for i in range(len(b),0,-1):
    print(i-1)
    print(int(a) * int(b[i-1]))
print(int(a)*int(b))
