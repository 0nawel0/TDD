import pytest
from src.convertor import StringCalculator

def testConvertEurToChf():
    eur = 10
    eurToChf = 9.4

    convert = StringCalculator.Convertor(eur)

    assert convert == eurToChf