def Print_N_times(i):
    if i>num:
        return
    
    print(Name,end=" ")
    Print_N_times(i+1)


Name = input("Enter your Name: ")
num = int(input("Enter an number: "))

Print_N_times(1)