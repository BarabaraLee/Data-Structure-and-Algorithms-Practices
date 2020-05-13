"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

# iterative solution
def binary_search(input_array, value):
    left = 0
    right = len(input_array)-1
    
    while left <= right:
        mid = left + (right - left)//2
        
        if value == input_array[mid]:
            return mid
        elif value < input_array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)

# recursive solution
def binary_search_helper(input_array, left, right, value):
    mid = left + (right - left) // 2
    if left <= right:
        if value == input_array[mid]:
            return mid
        elif value < input_array[mid]:
            return binary_search_helper(input_array, left, mid - 1, value)
        else:
            return binary_search_helper(input_array, mid + 1, right, value)
    return -1
    

def binary_search_recursive(input_array, value):
    left = 0
    right = len(input_array) - 1
    return binary_search_helper(input_array, left, right, value)
    

print binary_search_recursive(test_list, test_val1)
print binary_search_recursive(test_list, test_val2)

















