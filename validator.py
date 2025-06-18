import re
from typing import List

def extract_digits(value: str) -> str:
    return re.sub(r'\D', '', value)

def has_all_identical_digits(digits: str) -> bool:
    return digits == digits[0] * len(digits)

def compute_check_digit(digits: str, weights: List[int]) -> int:
    total = sum(int(d) * w for d, w in zip(digits, weights))
    remainder = total % 11
    
    return 0 if remainder < 2 else 11 - remainder

def is_valid_cpf(cpf: str) -> bool:
    digits = extract_digits(cpf)
    
    if len(digits) != 11 or has_all_identical_digits(digits):
        return False

    base = digits[:9]
    weights_first = list(range(10, 1, -1))
    weights_second = list(range(11, 1, -1))

    first_check = compute_check_digit(base, weights_first)
    second_check = compute_check_digit(base + str(first_check), weights_second)

    return digits.endswith(f"{first_check}{second_check}")

def is_valid_cnpj(cnpj: str) -> bool:
    digits = extract_digits(cnpj)
    
    if len(digits) != 14 or has_all_identical_digits(digits):
        return False

    base = digits[:12]
    weights_first = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    weights_second = [6] + weights_first

    first_check = compute_check_digit(base, weights_first)
    second_check = compute_check_digit(base + str(first_check), weights_second)

    return digits.endswith(f"{first_check}{second_check}")
