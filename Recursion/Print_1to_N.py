def Print_1_to_N(count,n):
    if count>n:
        return
    print(count)
    Print_1_to_N(count+1,n)

num = int(input("Enter an number : "))
Print_1_to_N(1,num)