def find_y_start(line, line_h):
    y_start = 0
    for index in range(line):
        y_start += line_h[index]
    return y_start


def count_word_length(start_pos, word_len, c, new_fragment_start_list):
    word_length = c * word_len
    if start_pos[0] == 0 or start_pos[0] in new_fragment_start_list:
        pass
    else:
        word_length = c * (word_len + 1)
    return word_length


def find_blocked_x_pixels(line_y_start, blocked_pixels, current_line_height):
    set_of_blocked_x = set()
    end_x_of_block_elements = []
    for element in blocked_pixels:
        if (element[0] < (line_y_start + current_line_height)) and (element[1] > line_y_start):
            blocked_x_pixels_set_el = [i for i in range(element[2], element[3])]
            blocked_x_pixels_set_el = set(blocked_x_pixels_set_el)
            set_of_blocked_x = set_of_blocked_x.union(blocked_x_pixels_set_el)
            end_x_of_block_elements.append(element[3])
    end_x_of_block_elements.sort()
    return set_of_blocked_x, end_x_of_block_elements


def find_intersection(start_pos, word_length, set_of_blocked_x):
    word_takes_pixels = set(range(start_pos[0], start_pos[0] + word_length))
    if word_takes_pixels.intersection(set_of_blocked_x):
        return 1
    return 0


def check_fragment_placement(start_pos, word_length, w, set_of_blocked_x):
    if start_pos[0] + word_length > w or find_intersection(start_pos, word_length, set_of_blocked_x):
        return 0
    return 1


def put_word(word, start_pos, c, h, line, blocked_pixels, current_line_height, line_heights):
    while True:
        word_len = len(word)
        set_of_blocked_x, end_x_of_block_elements = find_blocked_x_pixels(start_pos[1], blocked_pixels, current_line_height)

        word_len = count_word_length(start_pos, word_len, c, end_x_of_block_elements)
        is_fit = check_fragment_placement(start_pos, word_len, w, set_of_blocked_x)

        if is_fit:
            next_position = [start_pos[0] + word_len, start_pos[1]]
            up_right_coordinates = next_position.copy()
            break

        if start_pos[0] + word_len > w:
            line_heights.append(current_line_height)
            current_line_height = h
            line += 1
            current_line_y = find_y_start(line, line_heights)
            start_pos = [0, current_line_y]
        else:
            for x in end_x_of_block_elements:
                if x > start_pos[0]:
                    start_pos[0] = x
                    break
    return line, current_line_height, next_position, up_right_coordinates


def put_picture(output, c, w, layout, width, height, dx, dy, start_pos, current_line, current_line_height,
                new_fragment_start_list, blocked_pixels, up_right_coordinates, line_heights):
    if layout == 'embedded':
        while True:
            set_of_blocked_x, end_x_of_block_elements = find_blocked_x_pixels(start_pos[1], blocked_pixels,
                                                                                      current_line_height)
            word_len = width
            if start_pos[0] == 0 or start_pos[0] in end_x_of_block_elements:
                pass
            else:
                word_len += c

            is_fit = check_fragment_placement(start_pos, word_len, w, set_of_blocked_x)

            if is_fit:
                next_position = [start_pos[0] + word_len, start_pos[1]]
                up_right_coordinates = next_position.copy()
                break

            if start_pos[0] + word_len > w:
                line_heights.append(current_line_height)
                current_line_height = h
                current_line += 1
                current_line_y = find_y_start(current_line, line_heights)
                start_pos = [0, current_line_y]
            else:
                for x in end_x_of_block_elements:
                    if x > start_pos[0]:
                        start_pos[0] = x
                        break

        if height > current_line_height:
            current_line_height = height

        output.append([next_position[0] - width, next_position[1]])
        return current_line, current_line_height, next_position, up_right_coordinates

    elif layout == 'floating':
        start_x = up_right_coordinates[0]
        start_y = up_right_coordinates[1]

        start_x += dx
        start_y += dy
        end_x = start_x + width

        if start_x < 0:
            shift_x = -start_x
            start_x = 0
            end_x += shift_x
        elif end_x > w:
            shift_x = end_x - w
            end_x = w
            start_x -= shift_x

        next_position = start_pos
        up_right_coordinates = [end_x, start_y]
        output.append([start_x, start_y])

        return current_line, current_line_height, next_position, up_right_coordinates

    elif layout == 'surrounded':
        while True:
            set_of_blocked_x, end_x_of_block_elements = find_blocked_x_pixels(start_pos[1], blocked_pixels, current_line_height)

            top = start_pos[1]
            bottom = start_pos[1] + height
            left = start_pos[0]
            right = start_pos[0] + width

            word_len = width
            is_fit = check_fragment_placement(start_pos, word_len, w, set_of_blocked_x)

            if is_fit:
                next_position = [start_pos[0] + word_len, start_pos[1]]
                up_right_coordinates = next_position.copy()
                break
            if start_pos[0] + word_len > w:
                line_heights.append(current_line_height)
                current_line_height = h
                current_line += 1
                current_line_y = find_y_start(current_line, line_heights)
                start_pos = [0, current_line_y]
            else:
                for x in end_x_of_block_elements:
                    if x > start_pos[0]:
                        start_pos[0] = x
                        break

        blocked_pixels.append([top, bottom, left, right])
        output.append([next_position[0] - width, next_position[1]])

        return current_line, current_line_height, next_position, up_right_coordinates


lines = []

with open('input.txt') as f:
    w, h, c = map(int, f.readline().split())
    content = f.readlines()

for i in range(len(content)):
    line_trimmed = content[i].split('\n')
    lines.append(line_trimmed[0])

layout, width, height, dx, dy = '', 0, 0, 0, 0
last_up_right_dot = [0, 0]
current_line_y = 0
current_line = 0
current_line_height = h
line_heights = []
blocked_x_pixels_in_lines = [0 for line in lines]
output = []
now_is_picture = False
new_fragment_start_list = []
blocked_pixels = []
up_right_coordinates = [0, 0]

for line in lines:
    words = line.split()
    if line == '':
        line_heights.append(current_line_height)
        current_line_height = h
        current_line += 1
        current_line_y = find_y_start(current_line, line_heights)
        last_up_right_dot = [0, current_line_y]
        up_right_coordinates = [0, current_line_y]

    for word in words:
        if '(' in word:
            now_is_picture = True

        if now_is_picture:
            if 'layout=' in word:
                layout = word[7:]
                if ')' in word:
                    layout = layout.strip(')')
                    now_is_picture = False
                    current_line, current_line_height, last_up_right_dot, up_right_coordinates = put_picture(
                        output, c, w, layout, width, height, dx, dy, last_up_right_dot, current_line,
                        current_line_height, new_fragment_start_list, blocked_pixels, up_right_coordinates,
                        line_heights)
                    layout, width, height, dx, dy = '', 0, 0, 0, 0
            elif 'width=' in word:
                width = word[6:]
                if ')' in word:
                    width = width.strip(')')
                    width = int(width)
                    now_is_picture = False
                    current_line, current_line_height, last_up_right_dot, up_right_coordinates = put_picture(
                        output, c, w, layout, width, height, dx, dy, last_up_right_dot, current_line,
                        current_line_height, new_fragment_start_list, blocked_pixels, up_right_coordinates,
                        line_heights)
                    layout, width, height, dx, dy = '', 0, 0, 0, 0
                width = int(width)
            elif 'height=' in word:
                height = word[7:]
                if ')' in word:
                    height = height.strip(')')
                    height = int(height)
                    now_is_picture = False
                    current_line, current_line_height, last_up_right_dot, up_right_coordinates = put_picture(
                        output, c, w, layout, width, height, dx, dy, last_up_right_dot, current_line,
                        current_line_height, new_fragment_start_list, blocked_pixels, up_right_coordinates,
                        line_heights)
                    layout, width, height, dx, dy = '', 0, 0, 0, 0
                height = int(height)

            elif 'dx=' in word:
                dx = word[3:]
                if ')' in word:
                    dx = dx.strip(')')
                    dx = int(dx)
                    now_is_picture = False
                    current_line, current_line_height, last_up_right_dot, up_right_coordinates = put_picture(
                        output, c, w, layout, width, height, dx, dy, last_up_right_dot, current_line,
                        current_line_height, new_fragment_start_list, blocked_pixels, up_right_coordinates,
                        line_heights)
                    layout, width, height, dx, dy = '', 0, 0, 0, 0
                dx = int(dx)
            elif 'dy=' in word:
                dy = word[3:]
                if ')' in word:
                    dy = dy.strip(')')
                    dy = int(dy)
                    now_is_picture = False
                    current_line, current_line_height, last_up_right_dot, up_right_coordinates = put_picture(
                        output, c, w, layout, width, height, dx, dy, last_up_right_dot, current_line,
                        current_line_height, new_fragment_start_list, blocked_pixels, up_right_coordinates,
                        line_heights)
                    layout, width, height, dx, dy = '', 0, 0, 0, 0
                dy = int(dy)
        else:
            current_line, current_line_height, last_up_right_dot, up_right_coordinates = put_word(word,
                                                                                                  last_up_right_dot, c,
                                                                                                  h, current_line,
                                                                                                  blocked_pixels,
                                                                                                  current_line_height,
                                                                                                  line_heights)

for item in output:
    print(' '.join(str(x) for x in item))
