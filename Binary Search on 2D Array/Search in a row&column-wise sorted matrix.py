def Search(matrix,target):
    n=len(matrix)
    m=len(matrix[0])
    row=n-1
    col=0
    while(row>=0 and col<m):
        if matrix[row][col]==target:
            return (row,col)
        elif matrix[row][col]<target:
            col+=1
        else:
            row-=1
    return (-1,-1)

n = int(input("Enter no of Rows = "))
m = int(input("Enter no of Columns = "))
matrix=[]
for i in range(n):
    row=[]
    for j in range(m):
        val = int(input("Enter the Value :"))
        row.append(val)
    matrix.append(row)
target = int(input("Enter the num to find : "))
print(Search(matrix,target))