def binary_search(list1,n):
    low=0
    high=len(list1)-1
    mid=0
    while low <= high:
        mid = (high + low)//2
        if list1[mid]<n:
            low = mid + 1
        elif list1[mid]>n:
            high =mid-1
        else:
            return mid
    return -1
list = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]
n = 66
result = binary_search(list,n)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list")
