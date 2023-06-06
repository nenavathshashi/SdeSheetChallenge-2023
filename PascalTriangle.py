def printPascal(n:int):
    array=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        array[i][0]=1
    for i in range(1,n):
        for j in range(1,n):
            array[i][j]=array[i-1][j-1]+array[i-1][j]
    # print(array)
    ans=[]
    for i in range(n):
        ans.append(array[i][:i+1])
    return ans
