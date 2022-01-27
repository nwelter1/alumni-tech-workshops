# Step 1: Split everything into its own group
# Step 2: From left to right merge two groups together
# Step 3: While merging, place each item in the correct position within the merged group
# Step 4: Continue Steps 3-4 until one group is left



def mergeSort(arr):

    # reference print
    print(f'Splitting... {arr}')

    # Step 1:
    if len(arr) > 1:
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        # recursively call mergeSprt to perform splits
        # merge when done
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0 # left
        j = 0 # right
        k = 0 # merging
        # step 2
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
            k += 1
        # Step 3
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1
        print(f'Merging {arr}')
        return arr

            




