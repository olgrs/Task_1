import pytest
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient_sauce):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_sauce

    def test_remove_ingredient(self, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_filling

    def test_move_ingredient(self, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient_filling
        assert burger.ingredients[1] == mock_ingredient_sauce

    @pytest.mark.parametrize("sauce_price, filling_price, expected_total", [
        (50.0, 150.0, 400.0),  # 100*2 + 50 + 150 = 400
        (10.0, 10.0, 220.0),   # 100*2 + 10 + 10 = 220
    ])
    def test_get_price_parametrized(self, mock_bun, sauce_price, filling_price, expected_total):
        burger = Burger()
        burger.set_buns(mock_bun)  # mock_bun.price = 100.0
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "sauce1", sauce_price)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "filling1", filling_price)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert burger.get_price() == expected_total

    def test_get_receipt(self, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        receipt = burger.get_receipt()
        expected_lines = [
            f'(==== {mock_bun.get_name()} ====)',
            f'= {str(mock_ingredient_sauce.get_type()).lower()} {mock_ingredient_sauce.get_name()} =',
            f'= {str(mock_ingredient_filling.get_type()).lower()} {mock_ingredient_filling.get_name()} =',
            f'(==== {mock_bun.get_name()} ====)',
            '',
            f'Price: {burger.get_price()}'
        ]
        expected_receipt = '\n'.join(expected_lines)
        assert receipt == expected_receipt
