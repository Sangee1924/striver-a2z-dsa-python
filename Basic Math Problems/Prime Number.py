n = int(input("Enter an number: "))
count=0

for i in range(2,n):
    if n%i==0:
        count +=1
        
if count==0:
    print(f"{n} is an prime number")
else:
    print(f"{n} is not an prime number")