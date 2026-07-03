def longestSequence(arr):
    sets = set()
    for i in arr:
        sets.add(i)
    length=1
    for j in sets:
        if j-1 not in sets:
            count=1
            x = j
            while(x+1 in sets):
                x+=1
                count+=1
            length= max(length,count)
    print(length)

n= int(input("Length of Arr: "))
arr = []
for i in range(n):
    val = int(input("Enter val  : "))
    arr.append(val)
longestSequence(arr)