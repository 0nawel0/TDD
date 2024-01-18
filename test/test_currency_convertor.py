import pytest
from src.currency_convertor import CurrencyConvertor

def test_Convert_Eur_To_Chf():
    eur = 10
    eur_To_Chf = 9.4

    # Appel la fonction qui converti les eur en chf
    convert = CurrencyConvertor.Convertor(eur)

    assert convert == eur_To_Chf