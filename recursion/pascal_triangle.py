def pascal_triangle(n):
    answer_row = []
    if n == 1:
        return [1]
    elif n > 1:
        new_row = [1]
        prev_row = pascal_triangle(n - 1)
        for i in range(1, n - 1):
            new_row.append(prev_row[i - 1] + prev_row[i])
        new_row.append(1)
        answer_row += new_row
    return answer_row

print(pascal_triangle(8))