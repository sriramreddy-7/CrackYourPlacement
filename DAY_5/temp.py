# def matrix_multiply(A, B):
#     rows_A = len(A)
#     cols_B = len(B[0])
#     cols_A = len(A[0])
#     rows_B = len(B)
#
#     result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
#
#     for i in range(rows_A):
#         for j in range(cols_B):
#             for k in range(cols_A):
#                 result[i][j] += A[i][k] * B[k][j]
#
#     return result
#
# def get_matrix(rows, cols):
#     matrix = []
#     print(f"Enter the elements for a {rows}x{cols} matrix:")
#     for i in range(rows):
#         row = list(map(int, input().split()))
#         if len(row) != cols:
#             raise ValueError("Number of elements does not match the specified number of columns.")
#         matrix.append(row)
#     return matrix
#
# # Input dimensions for Matrix A
# rows_A = int(input("Enter number of rows for Matrix A: "))
# cols_A = int(input("Enter number of columns for Matrix A: "))
#
# # Input dimensions for Matrix B
# rows_B = int(input("Enter number of rows for Matrix B: "))
# cols_B = int(input("Enter number of columns for Matrix B: "))
#
# if cols_A != rows_B:
#     raise ValueError("Number of columns in Matrix A must be equal to the number of rows in Matrix B for multiplication.")
#
# # Get matrices from user
# A = get_matrix(rows_A, cols_A)
# B = get_matrix(rows_B, cols_B)
#
# # Multiply matrices
# result = matrix_multiply(A, B)
# print("Resultant Matrix:")
# for row in result:
#     print(' '.join(map(str, row)))
result = [[0 for _ in range(3)] for _ in range(2)]
print("op-1",result)
t=[]
for i in range(2):
    s=[]
    for j in range(3):
        s.append(0)
    t.append(s)
print("op-2",t)
