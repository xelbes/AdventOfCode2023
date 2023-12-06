def data_cleaning(file, split_char):
    card_numbers = []
    lines = []
    for line in file.readlines():
        line = line.replace("\n", "")
        card_nr, line = line.split(split_char)
        card_numbers.append(card_nr)
        lines.append(line)
    return card_numbers, lines


def split_values_on_input(line):
    lotto_nr, your_nr = line.split("|")
    lotto_nr, your_nr = lotto_nr.strip(), your_nr.strip()
    lotto_nr, your_nr = lotto_nr.replace("  ", " "), your_nr.replace("  ", " ")
    lotto_nr, your_nr = lotto_nr.split(" "), your_nr.split(" ")
    return lotto_nr, your_nr


def part_01():
    file = open("input.txt", "r")
    result = 0
    card_numbers, lines = data_cleaning(file, ":")
    for line in lines:
        cnt = 0
        lotto_nr, your_nr = split_values_on_input(line)
        for number in your_nr:
            if number in lotto_nr:
                cnt += 1
        if cnt > 0:
            cnt = 2 ** (cnt - 1)
        result += cnt
    print(result)
    file.close()


def part_02():
    file = open("input.txt", "r")
    result = 0
    card_numbers, lines = data_cleaning(file, ":")
    array_of_split_values = []
    for line in lines:
        lotto_nr, your_nr = split_values_on_input(line)
        array_of_split_values.append([lotto_nr, your_nr])
    for index, game_round in enumerate(array_of_split_values):
        cnt = 0
        print(game_round)
        for number in game_round[1]:
            if number in game_round[0]:
                cnt += 1
        for i in range(cnt + 1):
            print(i)
            if (index + i + 1) > len(array_of_split_values) - 1:
                break
            array_of_split_values[index + i + 1][1] = array_of_split_values[index + i + 1][1] + array_of_split_values[index + i + 1][1][:26]
        result += cnt + 1
    print(result)
    file.close()


if __name__ == '__main__':
    part_01()
    part_02()
