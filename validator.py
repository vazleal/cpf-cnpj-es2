import re

def validate_cpf(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calc_digit(cpf_slice, factor):
        total = sum(int(d) * (factor - i) for i, d in enumerate(cpf_slice))
        remainder = (total * 10) % 11
        return remainder if remainder < 10 else 0

    d1 = calc_digit(cpf[:9], 10)
    d2 = calc_digit(cpf[:10], 11)

    return cpf[-2:] == f"{d1}{d2}"

def validate_cnpj(cnpj: str) -> bool:
    cnpj = re.sub(r'\D', '', cnpj)
    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False

    def calc_digit(cnpj_slice, weights):
        total = sum(int(d) * w for d, w in zip(cnpj_slice, weights))
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder

    weights1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    weights2 = [6] + weights1

    d1 = calc_digit(cnpj[:12], weights1)
    d2 = calc_digit(cnpj[:12] + str(d1), weights2)

    return cnpj[-2:] == f"{d1}{d2}"
