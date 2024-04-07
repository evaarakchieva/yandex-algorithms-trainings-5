def count_max_height(n):
    sum_of_pos_diff = 0
    pos_indices = []
    neg_indices = []
    min_pos = 0
    min_pos_index = 0
    min_pos_index_among_pos = -1
    max_neg = 0
    max_neg_index = 0
    max_neg_index_among_neg = -1

    for i in range(n):
        up, down = list(map(int, input().split()))
        diff = up - down
        if diff > 0:
            index = i + 1
            pos_indices.append(index)
            sum_of_pos_diff += diff
            if min_pos < down:
                min_pos_index = i + 1
                min_pos = down
                min_pos_index_among_pos = len(pos_indices) - 1
        else:
            index = i + 1
            neg_indices.append(index)
            if max_neg < up:
                max_neg_index = i + 1
                max_neg = up
                max_neg_index_among_neg = len(neg_indices) - 1

    if max_neg > min_pos:
        print(sum_of_pos_diff + max_neg)
        print(' '.join(map(str, pos_indices + [max_neg_index] + neg_indices[: max_neg_index_among_neg] + neg_indices[max_neg_index_among_neg + 1:])))
    else:
        print(sum_of_pos_diff + min_pos)
        print(' '.join(map(str, pos_indices[: min_pos_index_among_pos] + pos_indices[min_pos_index_among_pos + 1:] + [min_pos_index] + neg_indices)))


input_n = int(input())
count_max_height(input_n)
