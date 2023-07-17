def column_sum(matrix):
    rows=len(matrix)
    columns=len(matrix[0])
    sums=[0]*columns
    for i in range(rows):
        for j in range(columns):
            sums[j]+=matrix[i][j]
    return sums
rows=int(input())
columns=int(input())
matrix=[]
for i in range(rows):
    row=[]
    for j in range(columns):
        element=int(input(f"{i},{j}:"))
        row.append(element)
    matrix.append(row)
result=column_sum(matrix)
print(result)

