import re

file_path = r"D:\repo\adventofcode\2023_1_data.txt"

# pt.1
sum = 0
calibration_value = 0

with open(file_path, 'r') as calibration_file:
    for line in calibration_file:
        numbers = re.findall(r'\d', line)
        for number in numbers:
            calibration_value = int(str(numbers[0]) + str(numbers[-1]))
        sum = sum + calibration_value

# pt.2
sum = 0
calibration_value = 0

word_to_number = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e',
}
# 1six15ninebgnzhtbmlxpnrqoneightfhp

with open(file_path, 'r') as calibration_file:
    for line in calibration_file:
        numbers = []
        transformed_line = re.sub(r'(one|two|three|four|five|six|seven|eight|nine)', lambda match: word_to_number.get(match.group(0).lower(), match.group(0)), line)
        transformed_line = re.sub(r'(one|two|three|four|five|six|seven|eight|nine)', lambda match: word_to_number.get(match.group(0).lower(), match.group(0)), transformed_line)
        print(line, transformed_line)
        numbers = re.findall(r'\d', transformed_line)
        calibration_value = int(str(numbers[0]) + str(numbers[-1]))
        sum += calibration_value
print(sum)
