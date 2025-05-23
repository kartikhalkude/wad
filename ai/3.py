def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Get user input for array
input_str = input("Enter space-separated integers for the array: ")
arr = list(map(int, input_str.split()))

# Get user input for sorting method
sorting_method = input("Enter sorting method (bubble/selection/merge): ").lower()

# Perform the selected sorting method
if sorting_method == 'bubble':
    bubble_sorted_arr = list(arr)
    bubble_sort(bubble_sorted_arr)
    print("Bubble Sorted Array:", bubble_sorted_arr)
elif sorting_method == 'selection':
    selection_sorted_arr = list(arr)
    selection_sort(selection_sorted_arr)
    print("Selection Sorted Array:", selection_sorted_arr)
elif sorting_method == 'merge':
    merge_sorted_arr = list(arr)
    merge_sort(merge_sorted_arr)
    print("Merge Sorted Array:", merge_sorted_arr)
else:
    print("Invalid sorting method. Please enter 'bubble', 'selection', or 'merge'.")