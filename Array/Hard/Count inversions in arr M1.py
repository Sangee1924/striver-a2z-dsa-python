# Count inversions in an array

def inversionM1(arr):
    cnt=0
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                cnt+=1
    print("No Of Inversion :",cnt)

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
inversionM1(arr)