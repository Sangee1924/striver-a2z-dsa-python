# Method 1
n = int(input("enter"))
count = 0
number = len(str(n))
for i in range(number):
    count=count+1
print(f"The number {n} has {count} digits.")

# Method 2
n_2 = int(input("enter"))
count_2= 0
while(n_2>0):
    count_2=count_2+1
    n_2=n_2//10
print(f"The number {n_2} has {count_2} digits.")