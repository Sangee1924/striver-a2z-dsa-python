def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while(i<j):
        while(arr[i]<=pivot and i<high):
            i+=1
        while(arr[j]>pivot and j>low):
            j-=1
        if(i<j):
            arr[i],arr[j] =arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j


def QuickSort(arr,low,high):
    if(low<high):
        pIndex = partition(arr,low,high)
        QuickSort(arr,low,pIndex-1)
        QuickSort(arr,pIndex+1,high)    


n= int(input("Length of Arr: "))
arr = []
for i in range(n):
    val = int(input("Enter val  : "))
    arr.append(val)
QuickSort(arr,0,len(arr)-1)
print(arr)