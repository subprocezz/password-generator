#!usr/bin/env python3
# -*- encoding: utf-8 -*-

import argparse 
from random import choice
from string import *

def generate_password(lenght: int, character_set: str) -> str:
    if lenght <= 0 or not character_set:
        return "Invalid input!"

    password: str = "".join(choice(character_set) for _ in range(lenght))
    
    return password

def get_character_set(include_upper: bool, include_lower: bool, include_numbers: bool, include_special: bool) -> str:
    character_set: str = ''.join([
        ascii_uppercase if include_upper else '',
        ascii_lowercase if include_lower else '',
        digits if include_numbers else '',
        punctuation if include_special else ''
    ])

    return character_set

def main() -> None:
    parser = argparse.ArgumentParser(description="Secure Password generator.")
    parser.add_argument('-l', '--length', type=int, required=True, help="password lenght")
    parser.add_argument('-u', '--include_upper', action='store_true', help="include uppercase")
    parser.add_argument('-lc', '--include_lower', action='store_true', help="include lowecase")
    parser.add_argument('-n', '--include_numbers', action='store_true', help="include numbers")
    parser.add_argument('-s', '--include_special', action='store_true', help="Incluir special characters")
    
    args = parser.parse_args()
    character_set = get_character_set(args.include_upper, args.include_lower, args.include_numbers, args.include_special)
    password: str = generate_password(args.length, character_set)
    print(password)

if __name__=="__main__":
    main()

