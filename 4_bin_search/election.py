def bin_search(value, length, array):
    left, right = -1, length
    while right - left > 1:
        mid = (left + right) // 2
        if array[mid][0] >= value:
            right = mid
        else:
            left = mid
    return right


def sort_by_votes(item):
    return item[0]


def sort_by_index(item):
    return item[2]


def get_input():
    n = int(input())
    parties = []
    for i in range(n):
        votes, popularity = map(int, input().split())
        parties.append([votes, popularity, i])
    return n, parties


def calculate_suffix_sum(n, parties):
    suffix_sum = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + parties[i][0]
    return suffix_sum


def find_best_party(n, parties, suffix_sum):
    min_popularity = suffix_sum[0] + max(item[1] for item in parties) + 1
    best_party = -1
    max_popularity = max(item[1] for item in parties)
    for i in range(n):
        if parties[i][1] < 0 or parties[i][1] >= min_popularity:
            continue
        left = parties[i][0]
        right = suffix_sum[0] + max_popularity + 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            index = bin_search(mid, n, parties)
            if index < n and mid == parties[i][0]:
                index += 1
            diff_votes = mid - parties[i][0]
            diff_prefix = suffix_sum[index] - (n - index) * (mid - 1)
            if index == n or diff_votes >= diff_prefix:
                right = mid - 1
                result = mid
            else:
                left = mid + 1
        popularity = result - parties[i][0] + parties[i][1]
        if popularity < min_popularity:
            best_party = i
            min_popularity = popularity
    return best_party, min_popularity


def update_votes(best_party, parties, vote, n):
    index = bin_search(parties[best_party][0] + vote, n, parties)
    parties[best_party][0] += vote
    for i in range(index, n):
        if best_party != i:
            extra_votes = parties[i][0] - parties[best_party][0] + 1
            parties[i][0] = parties[best_party][0] - 1
            vote -= extra_votes
    index = n
    while vote > 0:
        index -= 1
        if index != best_party:
            if parties[index][0] > vote:
                parties[index][0] -= vote
                vote = 0
            else:
                vote -= parties[index][0]
                parties[index][0] = 0


def solve():
    n, parties = get_input()
    parties.sort(key=sort_by_votes)
    suffix_sum = calculate_suffix_sum(n, parties)
    best_party, min_popularity = find_best_party(n, parties, suffix_sum)
    vote = min_popularity - parties[best_party][1]
    update_votes(best_party, parties, vote, n)
    print(min_popularity)
    print(parties[best_party][2] + 1)
    parties.sort(key=sort_by_index)
    for party in parties:
        print(party[0], end=" ")

solve()
