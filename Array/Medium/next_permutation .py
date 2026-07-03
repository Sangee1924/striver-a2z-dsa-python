# next_permutation : find next lexicographically greater permutation

def Permutation(arr):
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            breakpoint=i
            break
    else:
        arr.reverse()
        print(arr)
    for j in range(n-1,-1,-1):
        if arr[j]>arr[breakpoint]:
            arr[j],arr[breakpoint]=arr[breakpoint],arr[j]
            break
    left=breakpoint+1
    right=n-1
    while(left<=right):
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1

    print(arr)

n= int(input("Length of Arr: "))
arr = []
for i in range(n):
    val = int(input("Enter val  : "))
    arr.append(val)
Permutation(arr)