def Print_1_N_BT(n):
    if n<1:
        return
    Print_1_N_BT(n-1)
    print(n)

num = int(input("Enter an number: "))
Print_1_N_BT(num)