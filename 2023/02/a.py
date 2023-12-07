import sys
import re

red_max = 12
green_max = 13
blue_max = 14

def is_valid_game(game, color, cap):
    max_cube_count = max([int(x) for x in re.findall(f"(\d+) {color}", game)])
    return True if max_cube_count <= cap else False

valid_games = []
for line in sys.stdin:
    game_id, game_data = line.split(':')
    id = int(game_id.split(' ')[1])

    if not is_valid_game(line, 'red', red_max):
        continue

    if not is_valid_game(line, 'green', green_max):
        continue

    if not is_valid_game(line, 'blue', blue_max):
        continue

    valid_games.append(id)

print(sum(valid_games))