from src.models.ingredient import Ingredient, Restriction
import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501


# Req 2
def test_dish():
    dish = Dish('estrogonofe', 29.90)
    dish2 = Dish('estrogonofe', 29.90)
    dish3 = Dish('marmitex', 9.90)
    assert isinstance(dish, Dish)
    assert dish.name == 'estrogonofe'
    assert dish.price == 29.90

    assert dish == dish2

    assert hash(dish) == hash(dish)
    assert hash(dish) != hash(dish3)

    assert repr(dish) == "Dish('estrogonofe', R$29.90)"

    ingredient = Ingredient('ovo')

    dish.add_ingredient_dependency(ingredient, 1)

    assert dish.recipe.get(ingredient) == 1

    assert ingredient in dish.get_ingredients()

    assert Restriction.ANIMAL_DERIVED in dish.get_restrictions()

    with pytest.raises(TypeError):
        Dish('hot dog', 'one dolar')

    with pytest.raises(ValueError):
        Dish('hot dog', 0)
