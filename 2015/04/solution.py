import hashlib
from pathlib import Path

f = Path(__file__).with_name("input.txt")
key = f.read_text()

found_five_zeroes = False
found_six_zeroes = False
number = 1
n_found_five_zeroes = number
n_found_six_zeroes = number
while not found_five_zeroes or not found_six_zeroes:
    input = f'{key}{number}'
    hash = hashlib.md5(input.encode()).hexdigest()

    if not found_five_zeroes and hash.startswith('00000'):
        found_five_zeroes = True
        n_found_five_zeroes = number
    if not found_six_zeroes and hash.startswith('000000'):
        found_six_zeroes = True
        n_found_six_zeroes = number

    number += 1

print(f'Lowest positive number that generates hash with five leading zeroes: {n_found_five_zeroes}')
print(f'Lowest positive number that generates hash with six leading zeroes: {n_found_six_zeroes}')
