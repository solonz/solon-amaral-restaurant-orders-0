from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("Tomato")
    assert isinstance(ingredient, Ingredient)

    assert ingredient.restrictions == set()

    assert repr(ingredient) == "Ingredient('Tomato')"

    ingredient1 = Ingredient("Tomato")
    ingredient2 = Ingredient("Tomato")
    ingredient3 = Ingredient("Potato")

    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3

    assert hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) != hash(ingredient3)

    assert ingredient.name == "Tomato"
