def miniMaxSum(arr):
    # Write your code here
    arr2= arr.sort()
    max=0
    min=0
    for i in range(0,len(arr)-1):
        min+=arr[i]
    for i in range(1,len(arr)):
        max+=arr[i]
    print(min,max)
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split(" ")))
    print(arr)

    miniMaxSum(arr)