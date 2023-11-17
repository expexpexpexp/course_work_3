import pytest
from utils import load_datetime, mask_number


def test_transform_date():
    test_date = "2019-08-26T10:50:58.294041"
    test_date_2 = "2018-07-11T02:26:18.671407"
    test_date_3 = "2019-12-08T22:46:21.935582"
    test_date_4 = "2018-09-12T21:27:25.241689"
    assert load_datetime(test_date) == "26.08.2019"
    assert load_datetime(test_date_2) == "11.07.2018"
    assert load_datetime(test_date_3) == "08.12.2019"
    assert load_datetime(test_date_4) == "12.09.2018"


def test_mask_card_number():
    test_card = "Visa Classic 6831982476737658"
    test_card_2 = "Visa Platinum 1246377376343588"
    test_card_3 = "Maestro 3928549031574026"
    test_card_4 = "Visa Platinum 2256483756542539"
    assert mask_number(test_card) == "Visa Cla** **** 7658"
    assert mask_number(test_card_2) == "Visa Pla** **** 3588"
    assert mask_number(test_card_3) == "Maestro ** **** 4026"
    assert mask_number(test_card_4) == "Visa Pla** **** 2539"
