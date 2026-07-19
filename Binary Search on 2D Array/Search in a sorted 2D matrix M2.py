def Search(matrix,target):
    n=len(matrix)
    m=len(matrix[0])
    i=0
    j=m-1
    while(i<n and j>=0):
        if matrix[i][j]==target:
            return True
        elif matrix[i][j]>target:
            i+=1
        else:
            j-=1
    return False

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