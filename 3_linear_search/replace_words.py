def get_words_from_line(line):
    return line.split()

dictionary = set()

line = input()
text = get_words_from_line(line)

for word in text:
    dictionary.add(word)

text.clear()

line = input()
text = get_words_from_line(line)

for word in text:
    prefix_is_found = False
    for i in range(1, len(word)):
        prefix = word[:i]
        if prefix in dictionary:
            print(prefix, end=" ")
            prefix_is_found = True
            break
    if not prefix_is_found:
        print(word, end=" ")
