def Array_rev(i,result):
    if i < 0:
        print(result)
        return
    result.append(numbers[i])
    return Array_rev(i-1,result)


n = int(input("Enter: "))
numbers=[]
result =[]
for i in range(n):
    num = int(input("Enter List num: "))
    numbers.append(num)

Array_rev(n-1,result)