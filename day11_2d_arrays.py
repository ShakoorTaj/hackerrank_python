# a = []
# for arr_i in range(6):
#     arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#     a.append(arr_t)
#
# sum_of_hourglass = []
#
#
# def calculate_sum(i, j):
#     return a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j + 1] + a[i + 2][j] + a[i + 2][j + 1] + a[i + 2][j + 2]
#
#
# for row in range(0, 4):
#     for col in range(0, 4):
#         sum = calculate_sum(row, col)
#         sum_of_hourglass.append(sum)
# print(max(sum_of_hourglass))


arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

sum_of_hourglass = []

for i in range(len(arr) - 2):  # range(0, 4) - loop for row
    for j in range(len(arr) - 2):  # range(0, 4) - loop for column
        sum_of_hourglass.append(
                    arr[i][j] +     # [1st row][1st col]
                   arr[i][j + 1] +  # [1st row][2nd col]
                   arr[i][j + 2] +  # [1st row][3rd col]

                   arr[i + 1][j + 1] +  # [2nd row][2nd col]

                   arr[i + 2][j] +      # [3rd row][1st col]
                   arr[i + 2][j + 1] +  # [3rd row][2nd col]
                   arr[i + 2][j + 2]    # [3rd row][3rd col]
                   )

max_sum_of_hourglass = max(sum_of_hourglass)
print(max_sum_of_hourglass)





