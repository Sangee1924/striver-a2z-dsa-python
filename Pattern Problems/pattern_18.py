n = int(input())

start = ord('A') +n

for i in range(1,n+1):
    start=start-i
    for j in range(i):
        print(chr(start),end=" ")
        start = start+1
    print()