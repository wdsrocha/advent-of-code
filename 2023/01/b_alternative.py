import sys

calibration_values = []
for line in sys.stdin:
    line = line.replace("one", "one1one")
    line = line.replace("two", "two2two")
    line = line.replace("three", "three3three")
    line = line.replace("four", "four4four")
    line = line.replace("five", "five5five")
    line = line.replace("six", "six6six")
    line = line.replace("seven", "seven7seven")
    line = line.replace("eight", "eight8eight")
    line = line.replace("nine", "nine9nine")

    digits = [c for c in line if c.isdigit()]
    value = 10 * int(digits[0]) + int(digits[-1])
    calibration_values.append(value)

print(sum(calibration_values))