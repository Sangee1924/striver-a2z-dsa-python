def RowMaxOnes(matrix):
    n=len(matrix)
    m=len(matrix[0])
    maxAns=float('-inf')
    ind=-1
    for i in range(n):
        low=0
        high=len(matrix[i])-1
        maxones=0
        while(low<=high):
            mid=(low+high)//2
            if matrix[i][mid]==1:
                maxones = m - mid
                high=mid-1
            else:
                low=mid+1
        if maxones>maxAns:
            maxAns=maxones
            ind=i
    return ind+1

n = int(input("Enter No.of Rows : "))
m = int(input("Enter No.of Col : "))
matrix=[]
for i in range(n):
    row=[]
    for j in range(m):
        val = int(input("Enter val : "))
        row.append(val)
    matrix.append(row)
print("Row with maximum number of 1's :",RowMaxOnes(matrix))