def merge(num,low,mid,high):
    temp= []
    left = low
    right = mid+1
    while (left <= mid and right <= high):
        if num[left]< num[right]:
            temp.append(num[left])
            left+=1
        else:
            temp.append(num[right])
            right+=1

    while (left <=mid):
        temp.append(num[left])
        left+=1

    while (right <= high):
        temp.append(num[right])
        right+=1
    for i in range(low,high+1):
        num[i]=temp[i-low] 


def mergeSort(num,low,high):
    if(low >= high):
        return
    mid = (low+high)//2
    mergeSort(num,low,mid)
    mergeSort(num,mid+1,high)
    merge(num,low,mid,high)
    return num


n= int(input("Length of Arr: "))
arr = []
for i in range(n):
    val = int(input("Enter val  : "))
    arr.append(val)
ans = mergeSort(arr,0,n-1)
print(ans)