# Bisection Search =============================================================


# Iterative approach ===============================

def bisection_iter(num, arr):
    start = 0
    stop = len(arr)-1
    while start <= stop:
        mid = (start + stop)//2
        if num == arr[mid]:
            return f"{num} found at index: {mid}"
        elif num > arr[mid]:
            start = mid +1
        else:
            stop = mid - 1
    return f"{num} not found in list"

def create_list(max_val):
    arr = []
    for num in range(1, max_val+1):
        arr.append(num)
    return arr

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num_to_search = -1

l = create_list(10)
# for num in range(16):
#     print(bisection_iter(num, l))

# Recursive approach ===============================

def bisection_recur(num, arr, start, stop):
    if start > stop:
        return f"{num} not found in list"
    else:
        mid = (start + stop)//2
        if num == arr[mid]:
            return f"{num} found at index: {mid}"
        elif num > arr[mid]:
            return bisection_recur(num, arr, mid+1, stop)
        else:
            return bisection_recur(num, arr, start, mid-1)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in range(16):
    print(bisection_recur(num, l, 0, len(l)-1))
