n = int(input())
start = ord('A')
for i in range(1,n+1):
    for j in range(start,start+i):
        print(chr(j),end=" ")
    print()