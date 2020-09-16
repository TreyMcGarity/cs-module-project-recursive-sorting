# TO-DO: Implement a recursive implementation of binary search

data1 = [9, 8, 7, 5, 3, 2, 1, 0, -2, -3, -4, -6, -8, -9]
data2 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
target = -8

def binary_search(arr, target, start, end):
    # start value is index 0 and end is index of end
    if start > end:
        return -1
    else:
        # middle of list is start + end divided by two
        mid = (start + end) // 2
        # if target is middle value, it's True
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            # go to top of function at new index values
            return binary_search(arr, target, start , mid - 1)
        else:
            # go to top of function at new index values
            return binary_search(arr, target, mid + 1 , end)

print(binary_search(data1, target, 0, len(data1) - 1))
print(binary_search(data2, target, 0, len(data2) - 1))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
