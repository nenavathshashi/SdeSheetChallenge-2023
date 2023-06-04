def setZeros(matrix: List[List[int]]) -> None:
    n=len(matrix)
    m=len(matrix[0])
    rows_with_zero=set()
    columns_with_zero=set()
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                rows_with_zero.add(i)
                columns_with_zero.add(j)
    for i in range(n):
        for j in range(m):
            if (i in rows_with_zero) or (j in columns_with_zero):
                matrix[i][j]=0
