rows=int(input("enter no. of rows:"))
cols=int(input("enter no. of columns:"))
matrix=[]
print("enter row wise:\n")
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)
print("MATRIX")
for row in matrix:
    print(row)
diagonal_sum = 0
if rows==cols:
    for i in range(rows):
        diagonal_sum += matrix[i][i]
    print("Sum of diagonal elements:", diagonal_sum)
else:
    print("Matrix is not square matrix")
transposed=[]
for i in range(rows):
    nrow=[]
    for j in range(cols):
        nrow.append(matrix[j][i])
    transposed.append(nrow)
print("Transposed of matrix")
for row in transposed:
    print(row)