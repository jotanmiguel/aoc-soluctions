#!/usr/bin/env python3
from utils import aoc_utils as utils
import re

def part1(input_file: str = "input.txt"):
    input = readFile()
    total = 0
    for line in input:
        line = re.sub('\D', '', line)
        total += int(line[0] + line[-1])
    return total
            
def readFile(input_file: str = "input.txt"):
    input = []
    with open(input_file) as file:
        input = [line.strip() for line in file.readlines()]
    return input

def transform_to_numbers(nums):
    numbers_mapping = {
        "zero": "0", "one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6", "seven": "7",
        "eight": "8", "nine": "9"
    }
    transformed_nums = ''
    current_word = ''

    for char in nums:
        current_word += char
        if current_word in numbers_mapping:
            transformed_nums += numbers_mapping[current_word]
            current_word = ''

    return transformed_nums

def get_number_name(number):
    numbers = {
        "zero": "0", "one": "1", "two": "2", "three": "3", 
        "four": "4", "five": "5", "six": "6", "seven": "7", 
        "eight": "8", "nine": "9"
    }
    
    for name, num in numbers.items():
        if num == number:
            return name

    return None  # If number is not found in the dictionary

def find_numbers(line: str):
    numbers = {
        "zero": "0", "one": "1", "two": "2", "three": "3", 
        "four": "4", "five": "5", "six": "6", "seven": "7", 
        "eight": "8", "nine": "9"
    }
    
    possible_nums = []
    clean_line = ''
    clean_line = ''.join([char for char in line if any(char in number for number in numbers.keys()) or char.isdigit()])

    i = 0
    while i < len(clean_line):
        if clean_line[i].isdigit():
            possible_nums.append(clean_line[i])
            i += 1
        else:
            number = transform_to_numbers(clean_line[i:i+5])
            number_name = get_number_name(transform_to_numbers(clean_line[i:i+5]))
            possible_nums.append(number)
            i += len([get_number_name(number_name)])
    return findFirstAndLastNumber([int(num) for num in possible_nums if num.isdigit()])

def findFirstAndLastNumber(nums: list[int]) -> int:
    return int(str(nums[0]) + str(nums[-1]))

def part2(input_file: str = "input.txt"):
    input = open(input_file, "r").readlines()
    total = 0
    for line in input:
        total += find_numbers(line)
    return total
   
def solve(input_file: str = "input.txt"):
    print("Solving part 1 for ", input_file)
    print(part1(input_file))
    print("Solving part 2 for ", input_file)
    print(part2(input_file))

solve("input.txt")