def pal(i,string):
    length = len(string)
    if ( i >= length/2):
        return True
    if (string[i] != string[length-i-1]):
        return False
    return pal(i+1,string)

string = input("Enter: ")
print(pal(0,string))