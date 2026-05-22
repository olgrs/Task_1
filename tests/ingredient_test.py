import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (INGREDIENT_TYPE_SAUCE,
                                        INGREDIENT_TYPE_FILLING)


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price, expected_type", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0, INGREDIENT_TYPE_SAUCE),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100.0, INGREDIENT_TYPE_FILLING),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200.0, INGREDIENT_TYPE_SAUCE),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200.0, INGREDIENT_TYPE_FILLING),
    ])
    def test_ingredient_creation_and_getters(self, ingredient_type, name,
                                             price, expected_type):
        ingredient = Ingredient(ingredient_type, name, price)
        assert (ingredient.get_type() == expected_type
                and ingredient.get_name() == name
                and ingredient.get_price() == price)
