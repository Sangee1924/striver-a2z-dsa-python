n = int(input())

for i in range((n*2)-1):
    for j in range((n*2)-1):
        top=i
        botton=(2*n-2)-i
        left = j
        right = (2*n - 2)-j
        min_dist=min(top,botton,left,right)

        print(n-min_dist,end=" ")
    print()