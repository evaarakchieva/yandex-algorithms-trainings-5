n = int(input())
playlists = {}
for person in range(n):
    song_count = int(input())
    playlists[person] = list(map(str, input().split()))

intersection = set()
for key, value in playlists.items():
    if key == 0:
        intersection = set(value)
    else:
        intersection = intersection.intersection(set(value))

intersection = sorted(intersection)

print(len(intersection))
print(' '.join(intersection))
