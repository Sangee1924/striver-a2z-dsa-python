n = int(input("Enter a number: "))
temp = n
length = len(str(n))
sum=0

for i in range(length):
    num = n%10
    sum = sum + num**length
    n=n//10

if sum == temp:
    print ("True")
else:
    print("False")