def get_correct_lines(lines, line_index, index_leading_number, index_tailing_number):
    correct_lines = []
    for i in range(line_index-1, line_index+2):
        if i < 0:
            continue
        if i > len(lines) - 1:
            continue
        if index_leading_number == 0:
            correct_lines.append(lines[i][index_leading_number:index_tailing_number+2])
        elif index_tailing_number == len(lines[i])-1:
            correct_lines.append(lines[i][index_leading_number-1:index_tailing_number+1])
        else:
            correct_lines.append(lines[i][index_leading_number-1:index_tailing_number + 2])
        print(lines[i][index_leading_number-1:index_tailing_number+2])
    print()
    return correct_lines


def check_adjacent(lines):
    return_value = []
    for line in lines:
        for char in line:
            if char.isdigit() or char == '.':
                return_value.append(False)
            else:
                return_value.append(True)
    if True in return_value:
        return True
    else:
        return False


def part_1():
    file = open("input.txt", "r")
    result = 0
    lines_with_newline = file.readlines()
    lines = []
    for line in lines_with_newline:
        lines.append(line.replace('\n', ''))
    numbers_to_add = []
    for line_index, line in enumerate(lines):
        index_leading_number = 0
        index_tailing_number = 0
        on_number = False
        number_array = []
        for index, char in enumerate(line):

            # check if we hit number:
            if char != "." and not on_number and char.isdigit():
                on_number = True
                index_leading_number = index

            # check if number ends
            if (char == "." or not char.isdigit()) and on_number:
                on_number = False
                index_tailing_number = index - 1

                # form number from index
                for i in range(index_tailing_number-index_leading_number+1):
                    number_array.append(line[index_leading_number + i])
                number = int(str.join('', number_array))
                number_array = []
                has_adjacent = check_adjacent(get_correct_lines(lines, line_index, index_leading_number,
                                                                index_tailing_number))
                if has_adjacent:
                    numbers_to_add.append(number)
    for number in numbers_to_add:
        result += number
    file.close()
    return result


def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    # 516951 too low
    # 586856 too high
    part_2()
