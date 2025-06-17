import unittest
from validator import validate_cpf, validate_cnpj

class TestValidatorBehavior(unittest.TestCase):
    def test_should_accept_valid_cpf(self):
        assert validate_cpf("529.982.247-25") is True

    def test_should_reject_invalid_cpf(self):
        assert validate_cpf("123.456.789-00") is False

    def test_should_accept_valid_cnpj(self):
        assert validate_cnpj("45.723.174/0001-10") is True

    def test_should_reject_invalid_cnpj(self):
        assert validate_cnpj("00.000.000/0000-00") is False

    def test_should_reject_cpf_with_invalid_format(self):
        assert validate_cpf("abcdefghijk") is False

    def test_should_reject_cnpj_with_invalid_format(self):
        assert validate_cnpj("abcdefghijklmn") is False

if __name__ == "__main__":
    unittest.main()
