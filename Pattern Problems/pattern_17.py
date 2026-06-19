n = int(input())

for i in range(1,n+1):
    start=ord('A')-1
    print(" "* (n-i),end="")
    for j in range(i*2-1):
        break_point = i
        if j<break_point:
            start=start+1
            print(chr(start),end="")
        else:
            start=start-1
            print(chr(start),end="")
    print()