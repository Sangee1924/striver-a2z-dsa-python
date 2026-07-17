def totalHours(arr,mid):
    total=0
    for i in arr:
        total+= (i+mid-1)//mid
    return total

def koko(arr,h):
    low=1
    high=max(arr)
    while(low<=high):
        mid=(low+high)//2
        if totalHours(arr,mid)<=h:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans          # You can return ans or low

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
h = int(input("Enter Max Hours: "))
print(koko(arr,h))