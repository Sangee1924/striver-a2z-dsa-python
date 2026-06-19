n = int(input())

start = ord('A')

for i in range(n):
    for j in range(start,start+n-i):
        print(chr(j),end=" ")
    print()
