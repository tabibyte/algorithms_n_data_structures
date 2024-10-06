import re

file_path = r"D:\repo\adventofcode\2023_2_data.txt"


# pt.1
sum_id = 0

with open(file_path, 'r') as bag:
    for game in bag:
        game_id = int(re.findall(r"Game (\d+):", game)[0])
        blue_all = re.findall(r"(\d+) blue", game)
        blue = int(max(int(x) for x in blue_all))
        red_all = re.findall(r"(\d+) red", game)
        red = int(max(int(x) for x in red_all))
        green_all = re.findall(r"(\d+) green", game)
        green = int(max(int(x) for x in green_all))

        if blue > 14 or red > 12 or green > 13:
            continue
        else:
            sum_id += game_id

# print(sum_id)

# pt.2

power_sum = 0

with open(file_path, 'r') as bag:
    for game in bag:
        blue_all = re.findall(r"(\d+) blue", game)
        blue = int(max(int(x) for x in blue_all))
        red_all = re.findall(r"(\d+) red", game)
        red = int(max(int(x) for x in red_all))
        green_all = re.findall(r"(\d+) green", game)
        green = int(max(int(x) for x in green_all))

        power = red*blue*green
        power_sum += power
print(power_sum)
