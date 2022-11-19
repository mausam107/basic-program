def findMedian(arr):
    arr2 = sorted(arr)
    half= len(arr)//2 
    print(arr2[half])

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split(" ")))
    findMedian(arr)