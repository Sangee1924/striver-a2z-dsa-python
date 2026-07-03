"""Count Reverse Pairs
Problem Statement: 
Given an array of numbers, you need to return the count of reverse pairs.
Reverse Pairs are those pairs where i<j and arr[i]>2*arr[j]"""

def CountRev(arr,low,mid,high):
    right=mid+1
    cnt=0
    for i in range(low,mid+1):
        while (right<=high and arr[i]>2*(arr[right])):
            right+=1
        cnt+= (right-(mid+1))
    return cnt

def merge(arr,low,mid,high):
    left=low
    right= mid+1
    temp=[]
    while(left<=mid and right<=high):
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while(left<=mid):
        temp.append(arr[left])
        left+=1
    while(right<=high):
        temp.append(arr[right])
        right+=1

    for i in range(low,high+1):
        arr[i]=temp[i-low]
    
def mergeSort(arr,low,high):
    cnt=0
    if low>=high:
        return 0
    mid = (low+high)//2
    cnt += mergeSort(arr,low,mid)
    cnt += mergeSort(arr,mid+1,high)
    cnt += CountRev(arr,low,mid,high)
    merge(arr,low,mid,high)

    return cnt

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
print(mergeSort(arr,0,n-1))   