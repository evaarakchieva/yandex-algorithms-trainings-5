def count_presses_in_one_line(input_a):
    presses = 0
    presses += input_a // 4
    input_a %= 4
    presses += 2 * (input_a // 3)
    input_a %= 3
    presses += 2 * (input_a // 2)
    input_a %= 2
    presses += input_a
    return presses


n = int(input())
sum_of_presses = 0
for i in range(n):
    a = int(input())
    sum_of_presses += count_presses_in_one_line(a)
print(sum_of_presses)
