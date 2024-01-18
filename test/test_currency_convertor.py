import pytest
from src.currency_convertor import CurrencyConvertor

@pytest.mark.parametrize("eur, chf", [
    (10,9.4),
    (20, 18.8),
    (30, 28.2), # test case
])
def test_Convert_Eur_To_Chf(eur, chf):

    # Appel la fonction qui converti les eur en chf
    convert = CurrencyConvertor.Convertor(eur)

    assert convert == chf


def test_Convert_Null_Value():
    eur = None
    chf = 0

    convert = CurrencyConvertor.Convertor(eur)

    assert convert == chf

def test_Convert_String_Number_Value():
    eur = '10'
    chf = 9.4

    convert = CurrencyConvertor.Convertor(eur)

    assert convert == chf

def test_Convert_Negative_Value():
    eur = -10
    chf = 0

    convert = CurrencyConvertor.Convertor(eur)

    assert convert == chf