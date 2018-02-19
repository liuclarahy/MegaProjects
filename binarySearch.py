"""
Given a sorted array of integers, return the index of the given key. Return -1 if not found.
"""
def binary_search_logic (arr, key, low, high):
    if low > high:
        return -1

    mid = low + int( high - low ) / 2

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search_logic (arr, key, low, mid-1)
    else:
        return binary_search_logic (arr, key, mid+1, high)
   

def binary_search (arr, key):
    return binary_search_logic( arr, key, 0, len(arr)-1 )


arr = [1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 162, 176, 188, 199, 200, 210, 222]
key = 120 

print binary_search(arr, key)

