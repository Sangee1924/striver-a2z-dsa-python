# Brute Force
def BruteForce(arr,low,high):
    print("Brute Force")
    def merge(arr,low,mid,high):
        temp= []
        left = low
        right = mid+1
        while (left <= mid and right <= high):
            if arr[left]< arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1

        while (left <=mid):
            temp.append(arr[left])
            left+=1

        while (right <= high):
            temp.append(arr[right])
            right+=1
        for i in range(low,high+1):
            arr[i]=temp[i-low]

    def mergeSort(arr,low,high):
        if low>=high:
            return
        mid = (low+high)//2
        mergeSort(arr,low,mid)
        mergeSort(arr,mid+1,high)
        merge(arr,low,mid,high)

    for i in range(n):
        if arr[n-1-i]!=arr[n-2-i]:
            print("Second largest Number :",arr[n-2-i])
            break
    for j in range(n-1):
        if arr[j]!=arr[j+1]:
            print("Second Smallest Number :",arr[j+1])
            break
   
# Better
def Better(arr):
    print("Better")
    if n<2:
        print("No Values")
    else:
        largest= arr[0]
        smallest = arr[0]
        for i in range(n):
            if arr[i]>largest:
                largest=arr[i]
            if arr[i]<smallest:
                smallest=arr[i]

        second_Largest = -1
        second_Smallest = largest
        for k in range(n):
            if arr[k]<largest and arr[k]>second_Largest:
                second_Largest=arr[k]
            if arr[k]>smallest and arr[k]<second_Smallest:
                second_Smallest=arr[k]
        print("Second largest =",second_Largest)
        print("Second Smallest =",second_Smallest)

# Optimal Approach
def Optimal(arr):
    print("Optimal Approach")
    def SecondLargest(arr):
        largest = arr[0] 
        s_Largest=-1
        for i in range(n):
            if arr[i]>largest:
                s_Largest=largest
                largest=arr[i]
            elif arr[i]<largest and arr[i]>s_Largest:
                s_Largest=arr[i]
        if s_Largest == -1:
            print("There is no second largest")
        else:
            print("second Largest Number = ",s_Largest)

    def SecondSmallest(arr):
        smallest=arr[0]
        s_smallest = float('inf')
        for i in range(n):
            if arr[i]<smallest:
                s_smallest=smallest
                smallest=arr[i]
            elif arr[i]!=smallest and arr[i]<s_smallest:
                s_smallest=arr[i]
        if s_smallest == float('inf'):
            print("There is no second smallest")
        else:
            print("Second Smallest number =",s_smallest)
    SecondLargest(arr)
    SecondSmallest(arr)

n = int(input("Enter length:"))
arr=[]
for i in range(n):
    val = int(input("Enter the Value : "))
    arr.append(val)
BruteForce(arr,0,n-1)
Better(arr)
Optimal(arr)
