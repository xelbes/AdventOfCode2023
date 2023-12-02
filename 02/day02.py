

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
    file = open("input.txt", "r")
    result = 0
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
    file = open("input.txt", "r")
    result = 0
    for line in file.readlines():
        colors = {
            "red":      0,
            "blue":     0,
            "green":    0
        }
        row_result = 1
        line = line.replace('\n', '')
        line = str.split(line, ": ")
        value = line[1]
        games = str.split(value, ";")
        for game in games:
            game = str.split(game, ",")
            for color in game:
                amount, color = color.strip().split(" ")
                if int(amount) > int(colors[color]):
                    colors[color] = amount
        for i in colors:
            row_result *= int(colors[i])
        result += row_result
    file.close()
    return result


if __name__ == '__main__':
    print(part_1())
    print(part_2())


