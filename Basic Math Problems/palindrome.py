n = int(input("Enter an number: "))
temp = n
length = len(str(n))
num_check=""
for i in range(length):
    num_check += str(temp%10)
    temp=temp//10

if str(n) == num_check:
    print("palindrome number")
else:
    print("Not palindrome number")