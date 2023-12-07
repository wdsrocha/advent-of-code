import sys

calibration_values = []
for line in sys.stdin:
    digits = [c for c in line if c.isdigit()]
    value = 10 * int(digits[0]) + int(digits[-1])
    calibration_values.append(value)

print(sum(calibration_values))