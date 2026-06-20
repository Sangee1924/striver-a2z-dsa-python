def count_feq(arr):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i, 0) + 1
    for pairs in freq.items():
        print(f"Count of {pairs[0]} = {pairs[1]}")

n = int(input("Enter length of Arr: "))
arr =[]
for i in range(n):
    val = int(input("Enter Arr val :"))
    arr.append(val)
count_feq(arr)