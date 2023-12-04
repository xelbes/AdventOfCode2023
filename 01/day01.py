file = open("input.txt", "r")

numbersAsStrings = {
    'one':      '1',
    'two':      '2',
    'three':    '3',
    'four':     '4',
    'five':     '5',
    'six':      '6',
    'seven':    '7',
    'eight':    '8',
    'nine':     '9'}


def convert_strings_into_numbers(line):
    string_array = [*line]
    empty = []
    new_string = ""
    for char in string_array:
        empty.append(char)
        new_string = str.join('', empty)
        for number in numbersAsStrings.keys():
            new_string = new_string.replace(number, numbersAsStrings[number])
            empty = [*new_string]
    return new_string


def main():
    result = 0
    for line in file.readlines():
        line = line.replace('\n', '')
        print(line)
        line = convert_strings_into_numbers(line)
        print(line)
        line_number = []
        for char in [*line]:
            if char.isdigit():
                line_number.append(char)

        coords = [line_number[0], line_number[-1]]
        print(str(coords) + "\n")
        result += int(str.join('', coords))

    # 53794 too low
    print(result)


if __name__ == '__main__':
    main()

file.close()
