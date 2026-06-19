n = int(input())

start = ord('A')

for i in range(n):
    for j in range(i+1):
        print(chr(start+i),end=" ")
    print()