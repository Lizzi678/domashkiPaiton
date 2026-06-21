from string_utils import StringUtils
import pytest

utils = StringUtils()

# тесты для метода capitalize
def test_capitalize_positive():
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("привет") == "Привет"

def test_capitalize_negative():
    assert utils.capitalize("") == ""
    assert utils.capitalize("123") == "123"

# тесты для методы trim
def test_trim_positive():
    assert utils.trim("") == ""
    assert utils.trim(" ") == ""

# тесты для метода contains
def test_contains_positive():
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("SkyPro", "Pro") is True

def test_contains_negative():
    assert utils.contains("SkyPro", "U") is False
    assert utils.contains("", "a") is False

# тесты для метода delete_symbol
def tset_delete_symbol_positive():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

def tset_delete_symbol_negative():
    assert utils.delete_symbol("SkyPro", "z") == "SkyPro"
    assert utils.delete_symbol("", "a") == ""

