# look at each endpoint in arr [0, len(arr)-1]
# find midpoint idx
# compare target to value at midpoint
# divide in half (look at right or left side) - based upon comparison

def binSearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        potential_match = arr[mid]
        if target == potential_match:
            return mid
        elif target < potential_match:
            right = mid - 1
        else:
            left = mid + 1
    return "There is no target in this array"
