n = int(input("Enter the size of the square matrix: "))
values = list(map(int, input(f"Enter all {n * n} elements, space-separated (matrix 1): ").split()))
matrix1 = [values[i * n:(i + 1) * n] for i in range(n)]
values = list(map(int, input(f"Enter all {n * n} elements, space-separated (matrix 2): ").split()))
matrix2 = [values[i * n:(i + 1) * n] for i in range(n)]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
print("The resulting matrix is:")
for row in result:
    print(row)
