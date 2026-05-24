import pytest
from praktikum.bun import Bun
from tests.data.ingredient_data import BUNS


class TestBun:

    @pytest.mark.parametrize("name, price", BUNS)
    def test_bun_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", BUNS)
    def test_bun_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
