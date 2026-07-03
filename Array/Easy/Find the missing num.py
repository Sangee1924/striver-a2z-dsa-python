def Find_Missing_num(arr):
    check=0
    sums=0
    for i in range(1,n+2):
        check +=i
    for j in arr:
        sums+=j
    missing = check - sums
    print("Missing Number :",missing)

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
Find_Missing_num(arr)