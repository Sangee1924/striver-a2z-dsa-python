def check(arr,mid):
    boardPainted=0
    painter=1
    for i in arr:
        if boardPainted+i <= mid:
            boardPainted+=i
        else:
            painter+=1
            boardPainted=i
    return painter

def painter(arr,k):
    low=max(arr)
    high=sum(arr)
    while(low<=high):
        mid=(low+high)//2
        if check(arr,mid) <= k:
            high=mid-1
        else:
            low=mid+1
    return low

n = int(input("Enter the length of Array: "))
arr=[]
for i in range(n):
    val= int(input("Enter Array value :"))
    arr.append(val)
k= int(input("Enter no of Painters : "))
print(painter(arr,k))