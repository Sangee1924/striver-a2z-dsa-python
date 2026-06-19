def Print_N_1_BT(i,num):
    if i>num:
        return
    Print_N_1_BT(i+1,num)
    print(i)


num = int(input("Enter an Number: "))
Print_N_1_BT(1,num)