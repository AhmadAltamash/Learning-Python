def select_sort(arr):
    n = len(arr)
    for i in range(n):
        min_ind = i
        for j in range(i+1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr

a = list(map(int, input("Enter the number: ").split()))
print(select_sort(a))