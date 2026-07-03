def union_Map(arr,arr2):
    freq={}
    temp=[]
    for i in range(n):
        freq[arr[i]]=freq.get(arr[i],0)+1
    for j in range(n2):
        freq[arr2[j]]=freq.get(arr2[j],0)+1
    for key,value in freq.items():
        temp.append(key)
    print("union_Map",temp)

def union_set(arr,arr2):
    sets = set()
    for i in range(n):
        sets.add(arr[i])
    for j in range(n2):
        sets.add(arr2[j])
    print("union_set",list(sets))

def union_2Pointer(arr,arr2,n,n2):
    i=0
    j=0
    temp=[]
    while(i<n and j<n2):
        if arr[i]<=arr2[j]:
            for k in range(len(temp)):
                if arr[i]==temp[k]:
                    i+=1
                    break
            else:
                temp.append(arr[i])
                i+=1
        elif arr[i]>arr2[j]:
            for k in range(len(temp)):
                if temp[k]==arr2[j]:
                    j+=1
                    break
            else:
                temp.append(arr2[j])
                j+=1
    while (i<n):
        for k in range(len(temp)):
            if arr[i]==temp[k]:
                i+=1
                break
        else:
            temp.append(arr[i])
            i+=1
    while(j<n2):
        for k in range(len(temp)):
            if temp[k]==arr2[j]:
                j+=1
                break
        else:
            temp.append(arr2[j])
            j+=1
    print("union_2-Pointer",temp)

n = int(input("Enter Length of a Array 1 : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value array 1 : "))
    arr.append(val)
n2 = int(input("Enter Length of a Array 2 : "))
arr2 =[]
for i in range(n2):
    val = int(input("Enter the value for array 2 : "))
    arr2.append(val)
union_Map(arr,arr2)
union_set(arr,arr2)
union_2Pointer(arr,arr2,n,n2)