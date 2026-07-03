def Rotate90degree(matrix):
    ans=[[0]*m for _ in range(n)]
    for i in range(n):
        x=0
        for j in range(m-1,-1,-1):    
            ans[i][x]= matrix[j][i]
            x+=1
    print(matrix)
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
Rotate90degree(matrix)