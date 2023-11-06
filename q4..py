def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid1 = len(arr) // 3
    mid2 = 2 * len(arr) // 3

    left = merge_sort(arr[:mid1])
    middle = merge_sort(arr[mid1:mid2])
    right = merge_sort(arr[mid2:])

    return merge(left, middle, right)


def merge(left, middle, right):
    merged = []
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(middle) and k < len(right):
        min_val = min(left[i], middle[j], right[k])
        if min_val == left[i]:
            merged.append(left[i])
            i += 1
        elif min_val == middle[j]:
            merged.append(middle[j])
            j += 1
        else:
            merged.append(right[k])
            k += 1

    merged.extend(left[i:])
    merged.extend(middle[j:])
    merged.extend(right[k:])

    return merged

arr = [6, 3, 9, 1, 5, 2, 8, 7, 4]
sorted_arr = merge_sort(arr)
print("Sorted array using three-way merge sort:", sorted_arr)
