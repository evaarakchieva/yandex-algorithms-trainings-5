def manual_bin_search(data, x):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return right + 1


def find(data, left, right):
    if not data:
        return -1
    bs_l = manual_bin_search(data, left)
    bs_r = manual_bin_search(data, right + 1)
    return bs_r - bs_l


def main():
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()
    k = int(input())
    answer = []
    for _ in range(k):
        l, r = map(int, input().split())
        answer.append(find(data, l, r))
    print(*answer)


if __name__ == "__main__":
    main()
