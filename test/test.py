import pytest
import lib

lists = [[2, 5, 7, 7, 8, 2], [2, 5, 7, 10], [2, 7]]

# Тест функции на упорядоченных от мин к макс значениях
def test_CountElements_good():
    assert lib.count_elements(lists) == 2

def test_CountElements_bad():
    assert lib.count_elements(lists) == 5

