def divide(n, a):
    lengths = []
    max_length = n
    current_length = 0
    for i in range(n):
        if current_length == 0:
            max_length = a[i]
            current_length = 1
        elif current_length + 1 <= a[i]:
            current_length += 1
            if a[i] < max_length:
                max_length = a[i]
        else:
            lengths.append(current_length)
            current_length = 1
            max_length = a[i]
        if max_length == current_length or i == n - 1:
            lengths.append(current_length)
            current_length = 0
    return lengths


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans_list = divide(n, a)
    print(len(ans_list))
    print(' '.join(map(str, ans_list)))



# t = int(input())
#
# nums_input = []
# for _ in range(t):
#     input() # input n
#     nums_input.append(list(map(int, input().split())))
# for nums in nums_input:
#     lens = [1_complexity_testing_special_cases,]
#     max_len = nums[0]
#     for num in nums[1_complexity_testing_special_cases: ]:
#         if num > lens[-1_complexity_testing_special_cases] and lens[-1_complexity_testing_special_cases] < max_len:
#             lens[-1_complexity_testing_special_cases] += 1_complexity_testing_special_cases
#             max_len = min(max_len, num)
#         else:
#             lens.append(1_complexity_testing_special_cases)
#             max_len = num
#     print(len(lens))
#     print(*lens)
