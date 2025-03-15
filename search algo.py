# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i  
#     return -1  

arr = [12,3,4,5,6,642,22]
target = 6 



result1 = linear_search(arr, target)

if result1 == -1:
    print("Element not found in the array")
else:
    print(f"Element found at index {result}")



def binary(arr,target):
    n = len(arr)
    high = n-1
    low = 0
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] <= target:
            low = mid+1
        else:
            high = mid-1
    return -1


result = binary(arr,target)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")