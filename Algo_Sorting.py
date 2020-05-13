# Bubble Sort, Time Complexity: O(n^2), Space Complexity: O(1)
def bubble_sort(input_list):
    for i in range(len(input_list)-1, 0, -1):
        for j in range(i):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
    return input_list

test_list = [11,15,1,3,9,4]
print bubble_sort(test_list)
test_list += [4,6,88,-3]
print bubble_sort(test_list)

# Selection Sort, Time Complexity: O(n^2), Space Complexity: O(1)
def selection_sort(input_list):
    import sys
    for i in range(len(input_list)-1, -1, -1):
        min_val = sys.maxsize
        min_idx = -1
        for j in range(i+1):
            if input_list[j] < min_val:
                min_val = input_list[j]
                min_idx = j
        input_list.append(input_list.pop(min_idx))
    return input_list

test_list = [11,15,1,3,9,4,2,8]
print selection_sort(test_list)

# Insertion Sort, Time Complexity: O(n^2), Space Complexity: O(1)
def insertion_sort(input_list):
    import sys
    n = len(input_list)
    for i in range(1,n):
        index = i
        value = input_list[i]
        for j in range(i-1,-1,-1):
            if input_list[j] > value:
                input_list[j+1] = input_list[j]
                index = j
        input_list[index] = value
    return input_list

test_list = [11,15,1,3,9,4,2,8]
print insertion_sort(test_list)       

# Merge Sort, Time Complexity: O(nlogn), Space Complexity: O(n)
def merge(left_sorted, right_sorted):
    left_n = len(left_sorted)
    right_n = len(right_sorted)
    i = 0
    j = 0
    merged = []
    while i <= left_n - 1 and j <= right_n - 1:
        if left_sorted[i] <= right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        elif left_sorted[i] >= right_sorted[j]:
            merged.append(right_sorted[j])
            j += 1
    if i <= left_n - 1:
        merged += left_sorted[i:]
    if j <= right_n - 1:
        merged += right_sorted[j:]
    return merged

def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    
    if len(input_list) > 1:
        start = 0
        end = len(input_list) - 1
        mid = end // 2
        left_sorted = merge_sort(input_list[start:mid+1])
        right_sorted = merge_sort(input_list[mid+1:end+1])
        return merge(left_sorted, right_sorted)

test_list = [11,15,1,3,9,4,2,8]
print merge_sort(test_list)

# Quick Sort, Time Complexity: O(nlogn), Space Complexity: O(1)
def partition(input_list, start, end):
    p_value = input_list[end]
    p_index = start
    for i in range(start, end):
        if input_list[i] < p_value:
            input_list[i], input_list[p_index] = input_list[p_index], input_list[i]
            p_index += 1
    input_list[p_index], input_list[end] = input_list[end], input_list[p_index]
    return p_index

def quick_sort_helper(input_list, start, end):
    if start < end:
        p_index = partition(input_list, start, end)
        quick_sort_helper(input_list, start, p_index - 1)
        quick_sort_helper(input_list, p_index + 1, end)

def quick_sort(input_list):
    quick_sort_helper(input_list, 0, len(input_list)-1)
    return input_list

test_list = [11,15,1,3,9,4,2,8]
print quick_sort(test_list)


