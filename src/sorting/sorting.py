# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        m = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[m] = left[i]
                i += 1
            else:
                arr[m] = right[j]
                j += 1
            m += 1

        while i < len(left):
            arr[m] = left[i]
            i += 1
            m += 1
        while j < len(right):
            arr[m] = right[j]
            j += 1
            m += 1


arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(arr)
merge_sort(arr)
print(arr)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
# Your code here


# def merge_sort_in_place(arr, l, r):
# Your code here
