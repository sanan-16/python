def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inversions = merge_sort(arr[:mid])
    right, right_inversions = merge_sort(arr[mid:])

    merged, split_inversions = merge(left, right)
    total_inversions = left_inversions + right_inversions + split_inversions

    return merged, total_inversions

def merge(left, right):
    merged = []
    inversions = 0
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions

arr = [1, 3, 5, 2, 4, 6]
sorted_arr, inversions = merge_sort(arr)
print("Sorted array:", sorted_arr)
print("Number of inversions:", inversions)
