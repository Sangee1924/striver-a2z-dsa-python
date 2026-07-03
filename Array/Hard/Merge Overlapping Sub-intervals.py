# Merge Overlapping Sub-intervals

def mergeOverlapping(arr):
    ans=[]
    arr.sort()
    for i in arr:
        if not ans or i[0] > ans[-1][1]:
            ans.append(i)
        else:
            ans[-1][1] = max(i[1],ans[-1][1])
    print(ans)


n = int(input("Enter No.of Rows : "))
m = int(input("Enter No.of Col : "))
matrix=[]
for i in range(n):
    row=[]
    for j in range(m):
        val = int(input("Enter val : "))
        row.append(val)
    matrix.append(row)
mergeOverlapping(matrix)