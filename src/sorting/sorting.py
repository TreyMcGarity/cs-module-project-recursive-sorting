# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    a = 0 # index arrA
    b = 0 # index arrB
    i = 0 # incrementing index

    # while both indexes are less than length of corresponding arrays
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            # a is smaller, its value should be added next
            merged_arr[i] = arrA[a]
            # increment arrA's index
            a += 1
        else:
            # b is smaller, its value should be added next
            merged_arr[i] = arrB[b]
            # increment arrB's index
            b += 1
        i += 1

    # while indexes are less than individual arrs
    while a < len(arrA):
        # set value at in LHS at index a to merged array at index i
        merged_arr[i] = arrA[a]
        # increment to accommodate more than one value insertion
        a += 1
        i += 1
    # continues process same as LHS but with RHS
    while b < len(arrB):
        # set value at in RHS at index a to merged array at index i
        merged_arr[i] = arrB[b]
        # increment to accommodate more than one value insertion
        b += 1
        i += 1 
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # reducing down by half until each list has 1 sorted item
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # recursive dividing on the subarrays until each only has 1 element remaining
    left = merge_sort(left)
    right = merge_sort(right)
    # compare/merge the 1 sorted item in each subarray
    arr = merge(left, right)

    return arr
"""
[4, 2, 8, 7, 1, 9, 5, 3, 6]     ORIGINAL

mid: 4          INDEX OF MIDDLE  
[4, 2, 8, 7]    LHS FROM ORIGINAL   
mid: 2          MID OF LHS
[4, 2]          LHS(2)
mid: 1          MID OF LHS AGAIN
[4]             LHS(3)
[2]             RHS
 arrA [4]
 arrB [2]

        MERGE A AND B MAKES NEW LHS
 merg [2, 4]
 ---------------------
[8, 7]          RHS FROM INDEX OF MID
mid: 1          MID OF RHS
[8]             LHS
[7]             RHS
 arrA [8]       
 arrB [7]

        MERGE A AND B MAKES NEW RHS
 merg [7, 8]
 ---------------------
 arrA [2, 4]
 arrB [7, 8]

    MERGED NEW LHS AND NEW RHS TO FINAL LHS
 merg [2, 4, 7, 8]
___________________________________________

[1, 9, 5, 3, 6] RHS FROM ORIGINAL
mid: 2          MID OF RHS
[1, 9]          LHS
mid: 1          MID OF LHS
[1]             LHS(2)
[9]             RHS
 arrA [1]
 arrB [9]

        MERGE A AND B MAKES NEW LHS
 merg [1, 9]

[5, 3, 6]       RHS FORM MID 
mid: 1          MID OF RHS
[5]             LHS
[3, 6]          RHS
mid: 1          MID OF RHS
[3]             LHS(2)
[6]             RHS(2)
 arrA [3]
 arrB [6]

        MERGE A AND B MAKES NEW B
 merg [3, 6]
  ---------------------
 arrA [5]
 arrB [3, 6]

        MERGE LHS AND RHS MAKES NEW RHS
 merg [3, 5, 6]

        MERGE arrA AND arrB
 arrA [1, 9]
 arrB [3, 5, 6]

    MERGED NEW LHS AND NEW RHS TO FINAL RHS
 merg [1, 3, 5, 6, 9]
___________________________________________

 arrA [2, 4, 7, 8]
 arrB [1, 3, 5, 6, 9]

    MERGED FINAL LHS AND FINAL RHS TO MAKE FINAL MERGED
 merg [1, 2, 3, 4, 5, 6, 7, 8, 9]

[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
data = [4, 2, 8, 7, 1, 9, 5, 3, 6]
print(merge_sort(data))
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
