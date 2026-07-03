def appearsones(arr):
    xors=0
    for i in range(n):
        xors = xors^ arr[i]
    print("Find the number that appears ones:",xors)



n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
appearsones(arr)