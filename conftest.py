import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (INGREDIENT_TYPE_SAUCE,
                                        INGREDIENT_TYPE_FILLING)


@pytest.fixture
def mock_bun():
    """Создаёт мок-объект булочки с именем и ценой."""
    bun = Bun("test bun", 100.0)
    return bun


@pytest.fixture
def mock_ingredient_sauce():
    """Создаёт мок-объект соуса."""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 50.0)


@pytest.fixture
def mock_ingredient_filling():
    """Создаёт мок-объект начинки."""
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150.0)
