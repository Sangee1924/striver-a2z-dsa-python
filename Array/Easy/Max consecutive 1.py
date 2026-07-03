def maxConsecutive_1(arr):
    max_1 = 1
    count = 0
    for i in range(n):
        if arr[i]==1:
            count+=1
            max_1= max(count,max_1)
            
        else:
            count=0 
    print("Max consicutive ones:",max_1)

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
maxConsecutive_1(arr)