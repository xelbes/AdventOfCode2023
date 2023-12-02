def check_color(colors):
    match colors[1]:
        case "blue":
            if int(colors[0]) <= 14:
                return True
            else:
                return False
        case "red":
            if int(colors[0]) <= 12:
                return True
            else:
                return False
        case "green":
            if int(colors[0]) <= 13:
                return True
            else:
                return False


def is_game_valid(game):
    validity_of_game = []
    for color in game:
        is_color_ok = check_color(color.strip().split(" "))
        validity_of_game.append(is_color_ok)
    if False in validity_of_game:
        return False
    else:
        return True


def part_1():
    result = 0
    file = open("input.txt", "r")
    for line in file.readlines():
        line = line.replace('\n', '')
        line = str.split(line, ": ")
        index, value = [str.replace(line[0], "Game ", ""), line[1]]
        games = str.split(value, ";")
        validity = []
        for game in games:
            game = str.split(game, ",")
            validity.append(is_game_valid(game))
        if False in validity:
            is_round_possible = False
        else:
            is_round_possible = True
        if is_round_possible:
            result += int(index)
    file.close()
    return result


def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
    # 4494 too high
    # 4682 too high
    # 368 too low


