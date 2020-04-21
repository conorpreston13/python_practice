# MERGE SORT ===================================================================

def merge_sort(arr1, arr2):
    # print('Merge function called with lists below')
    # print(f"left: {arr1} and right: {arr2}")
    sorted_arr =[]
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        # print(f"Left list index i is {i} and has a value of {arr1[i]}")
        # print(f"Right list index j is {j} and has a value of {arr2[j]}")
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
        # print(sorted_arr)
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr

def divide_arr(arr):
    if len(arr) < 2:
        # print(f"Base condition reached with {arr[:]}")
        return arr[:]
    else:
        middle = len(arr)//2
        # print("Current list to work with:", arr)
        # print("Left split:", arr[:middle])
        # print("Right split:", arr[middle:])
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])
        return merge_sort(l1, l2)

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
print(divide_arr(l))
