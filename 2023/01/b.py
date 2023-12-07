import sys
import re

word_to_digit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5, 
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def to_numeric_digit(s):
    if s.isdigit():
        return int(s)
    else:
        return word_to_digit[s]

valid_digits = [str(i) for i in range(10)] + list(word_to_digit.keys())

calibration_values = []
for line in sys.stdin:
    pattern = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    groups = re.findall(pattern, line)
    if groups:
        first_digit = to_numeric_digit(groups[0])
        last_digit = to_numeric_digit(groups[-1])
        value = 10 * first_digit + last_digit
        print(groups)
        print(value)
        calibration_values.append(value)

print(sum(calibration_values))