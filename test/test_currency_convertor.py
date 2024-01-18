import pytest
from src.currency_convertor import CurrencyConvertor

def test_Convert_Eur_To_Chf():
    eur = 20
    eur_To_Chf = 18.8

    # Appel la fonction qui converti les eur en chf
    convert = CurrencyConvertor.Convertor(eur)

    assert convert == eur_To_Chf