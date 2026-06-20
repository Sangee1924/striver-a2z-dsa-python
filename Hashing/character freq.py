def char_freq(arr):
    freq = [0]*26

    for i in arr:
        freq[ord(i)-97] += 1
    
    val = input("enter char to get freq: ")
    print(freq[ord(val)-97])

n = int(input("Length of array: "))
arr=[]
for i in range(n):
    val = input("Enter arr Element : ")
    arr.append(val)

char_freq(arr)