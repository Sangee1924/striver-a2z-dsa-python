#Brute Force

def Median(matrix):
    n=len(matrix)
    m=len(matrix[0])
    temp=[]
    for i in range(n):
        for j in range(m):
            temp.append(matrix[i][j])
    temp.sort()
    return temp[(n*m)//2]

n = int(input("Enter no of Rows = "))
m = int(input("Enter no of Columns = "))
matrix=[]
for i in range(n):
    row=[]
    for j in range(m):
        val = int(input("Enter the Value :"))
        row.append(val)
    matrix.append(row)
print(Median(matrix))