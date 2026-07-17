N = int(input("Enter a Number: "))
ans=1
for i in range(1,N):
    if i*i <= N:
        ans=i
    else:
        break
print("Sqrt of a number without using Binary Search :",ans)