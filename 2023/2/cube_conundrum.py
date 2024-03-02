#!/usr/bin/env python3
import aoc_utils as utils
import re

def solve(input_file: str = "input.txt"):
    file_input = utils.readInputFile(input_file)
    print("Solving part 1 for ", input_file)
    print(part1(file_input))
    print("Solving part 2 for ", input_file)
    print(part2(file_input))
    

def process_game_sets(set: list[str]) -> dict[str, int]:
    cubes = {'red': 0, 'green': 0, 'blue': 0}  # Initialize all colors with count 0
    for cube in set:
        color = cube[3:].strip()
        cubes[color] += int(cube[1:3])# Update count with the actual number of cubes    
    return dict(reversed(sorted(cubes.items())))

def part1(input: list[str]) -> int:
    def process_input(input: list[str]) -> int:
        ids = [process_line(int(re.split(r'[:;]', line)[0].split(" ")[1]),re.split(r'[:;]', line)[1:]) for line in input]
        return sum(sum(ids, []))
    
    def process_line(game_id:int, line: list[str]) -> dict[str, dict[str, list[str]]]:
        game = {} # dict indexes represent a set of cubes
        lines = []
        for i in range(len(line)):
            game[i] = process_game_sets(line[i].split(','))
        lines.append(game_possible((game_id, game)))
        return lines

    def game_possible(game: tuple[int, dict], max_r: int = 12, max_g: int = 13, max_b: int = 14) -> int:
        game_id:int = game[0]
        sets = game[1].values()
        possible = []
        for set in sets:
            possible.append(set['red'] <= max_r and set['green'] <= max_g and set['blue'] <= max_b)
        return game_id if all(possible) else 0
    
    return process_input(input)

def part2(input: list[str]) -> int:
    def process_input(input: list[str]) -> int:
        powers = [process_line(int(re.split(r'[:;]', line)[0].split(" ")[1]),re.split(r'[:;]', line)[1:]) for line in input]
        return sum(sum(powers, []))
    
    def process_line(game_id:int, line: list[str]) -> dict[str, dict[str, list[str]]]:
        game = {} # dict indexes represent a set of cubes
        lines = []
        for i in range(len(line)):
            game[i] = process_game_sets(line[i].split(','))
        lines.append(game_possible((game_id, game)))
        return lines

    def game_possible(game: tuple[int, dict], max_r: int = 12, max_g: int = 13, max_b: int = 14) -> int:
        game_id:int = game[0]
        sets = game[1].values()
        possible = []
        power_max_r = max([s['red'] if s['red'] != 0 else 1 for s in sets])
        power_max_g = max([s['green'] if s['green'] != 0 else 1 for s in sets])
        power_max_b = max([s['blue'] if s['blue'] != 0 else 1 for s in sets])
        return power_max_r * power_max_g * power_max_b
    
    return process_input(input)
solve("input.txt")