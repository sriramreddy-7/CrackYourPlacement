def matrix_multiply(A, B):
    rows_A = len(A)
    cols_B = len(B[0])
    cols_A = len(A[0])
    rows_B = len(B)

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

rows_A = int(input("Enter number of rows for Matrix A: "))
cols_A = int(input("Enter number of columns for Matrix A: "))

rows_B = int(input("Enter number of rows for Matrix B: "))
cols_B = int(input("Enter number of columns for Matrix B: "))

if cols_A != rows_B:
    print("Not Possible")
else:
    A = []
    for i in range(rows_A):
        x = []
        for j in range(cols_A):
            x.append(int(input("Enter : ")))
        A.append(x)
    B = []
    for i in range(rows_B):
        x = []
        for j in range(cols_B):
            x.append(int(input("Enter : ")))
        B.append(x)
    t=matrix_multiply(A, B)
    for i in t:
        print(i)
