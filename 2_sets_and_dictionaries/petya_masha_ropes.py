def find_min_length_of_rope(rope_count, rope_lengths):
    max_length = rope_lengths[0]
    sum_of_lengths_left = sum(rope_lengths)
    for i in range(1, rope_count):
        if rope_lengths[i] > max_length:
            max_length = rope_lengths[i]
    rope_lengths.remove(max_length)
    if max_length > sum(rope_lengths):
        return max_length - sum(rope_lengths)
    else:
        return sum_of_lengths_left


n = int(input())
input_list = list(map(int, input().split()))
print(find_min_length_of_rope(n, input_list))
