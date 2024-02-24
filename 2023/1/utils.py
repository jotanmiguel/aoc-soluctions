# Imports

# Functions
def first_and_last(list: list[str]) -> list[str]:
    """
    Created originally for the trebuchet problem, this function takes a list of strings and returns the first and last elements of the list.
    
    Example:
    first_and_last(['a', 'b', 'c', 'd']) -> ['a', 'd']
    
    Author: @jotanmiguel

    Args:
        list (list[str]): list of strings

    Returns:
        list[str]: first and last string of the given list 'list'
    """
    return [list[0], list[-1]]      

def common_letters(string1: str, string2: str) -> bool:
    """
    Created originally for the trebuchet problem, this function takes two strings and returns a list of common letters between the two strings.
    
    Example:
    common_letters('seven', 'nine') -> true
    """
    return True if string1[-1] == string2[0] else False

def transform_to_numbers(string):
    numbers_mapping = {
        "zero": "0", "one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6", "seven": "7",
        "eight": "8", "nine": "9"
    }
    transformed_string = ''
    current_word = ''

    for char in string:
        current_word += char
        if current_word in numbers_mapping:
            transformed_string += numbers_mapping[current_word]
            current_word = ''

    return transformed_string