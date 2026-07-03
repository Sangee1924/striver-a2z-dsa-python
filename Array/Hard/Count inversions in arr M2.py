# Count inversions in an array

def inversionM2(arr,low,mid,high):
    cnt=0
    temp=[]
    left=low
    right=mid+1
    while (left<=mid and right<=high):
        if arr[left]>arr[right]:
            cnt+=(mid-left)+1
            temp.append(arr[right])
            right+=1
        else:
            temp.append(arr[left])
            left+=1
    while(left<=mid):
        temp.append(arr[left])
        left+=1
    while(right<=high):
        temp.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]
    return cnt

def MergeSort(arr,low,high):
    cnt=0
    if low>=high:
        return 0
    mid= (low+high)//2
    cnt += MergeSort(arr,low,mid)
    cnt += MergeSort(arr,mid+1,high)
    cnt += inversionM2(arr,low,mid,high)
    return cnt

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
print(MergeSort(arr,0,n-1))