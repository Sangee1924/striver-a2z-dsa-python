def char_freq(arr):
    freq={}

    for i in arr:
        freq[ord(i)-ord('a')] = freq.get((ord(i)-ord('a')), 0) + 1
    for pairs in freq.items():
        print(f"Freq of {chr(pairs[0]+97)} = {pairs[1]}")

n = int(input("Length of array : "))
arr=[]
for i in range(n):
    val = input("Enter val :")
    arr.append(val)
char_freq(arr)