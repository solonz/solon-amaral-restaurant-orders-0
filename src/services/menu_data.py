import pandas as pd
from src.models.ingredient import Ingredient
from src.models.dish import Dish


# Req 3
class MenuData:
    def __init__(self, source_path: str):
        data = pd.read_csv(source_path)
        menu = {}
        # https://www.w3schools.com/python/pandas/ref_df_itertuples.asp
        for dish, price, ing, amount in data.itertuples(
            index=False
        ):
            if dish not in menu:
                menu[dish] = Dish(dish, price)
            menu[dish].add_ingredient_dependency(Ingredient(ing), amount)
        self.dishes = set(menu.values())
