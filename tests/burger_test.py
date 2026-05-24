import pytest
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (INGREDIENT_TYPE_SAUCE,
                                        INGREDIENT_TYPE_FILLING)


class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient_sauce):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
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

    def test_price_with_only_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.get_price() == mock_bun.get_price() * 2

    def test_price_with_ingredients(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        ingredient = Ingredient("sauce", "test", 50)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == mock_bun.get_price() * 2 + 50

    def test_receipt_contains_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        assert mock_bun.get_name() in receipt

    def test_receipt_contains_ingredients(self, mock_bun, mock_ingredient_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        receipt = burger.get_receipt()
        assert mock_ingredient_sauce.get_name() in receipt

    def test_receipt_contains_price(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        assert str(mock_bun.get_price() * 2) in receipt

    def test_get_receipt_structure(self, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        receipt = burger.get_receipt()
        lines = [line for line in receipt.split("\n") if line]
        assert lines[0] == f"(==== {mock_bun.get_name()} ====)"
        assert lines[-2] == f"(==== {mock_bun.get_name()} ====)"
        assert lines[-1].startswith("Price:")
        assert any(
            f"= {mock_ingredient_sauce.get_type().lower()} {mock_ingredient_sauce.get_name()} =" == line
            for line in lines
        )
        assert any(
            f"= {mock_ingredient_filling.get_type().lower()} {mock_ingredient_filling.get_name()} =" == line
            for line in lines
        )
