def diagonalDifference(arr,p):
    n= len(arr)
    addl=0
    addr=0
    for i in range(0,p):
        for j in range(0,p):
            if i==j:
                addl+=arr[i][j]
            if i+j == (p-1):
                addr+=arr[i][j]    
    print(max(addl,addr) - min(addl,addr))    

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split(" "))))

    result = diagonalDifference(arr,n)