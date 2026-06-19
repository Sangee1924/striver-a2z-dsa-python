def Print_N_to_1(n):
    if n<1:
        return
    print(n)
    Print_N_to_1(n-1)

num = int(input("Enter an Number : "))
Print_N_to_1(num)