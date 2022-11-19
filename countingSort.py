def countingSort(arr):
    n = max(arr)

    x = [0] * (n+1)
    for i in range(0, len(arr)):
        x[arr[i]] += 1
    print(x)



arr = [99,10,60,5,7,8,8,8]
countingSort(arr)