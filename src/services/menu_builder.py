import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        menu = {
            "dish_name": [],
            "price": [],
            "ingredients": [],
            "restrictions": [],
        }
        for dish in self.menu_data.dishes:
            if self.check_inventory(dish.recipe):
                if restriction not in dish.get_restrictions():
                    menu['dish_name'].append(dish.name)
                    menu['ingredients'].append(dish.get_ingredients())
                    menu['price'].append(dish.price)
                    menu['restrictions'].append(dish.get_restrictions())

        return pd.DataFrame(menu)

    # Req 6
    def check_inventory(self, recipe):
        for ingredient, amount in recipe.items():
            if ingredient not in self.inventory.inventory:
                return False
            elif self.inventory.inventory[ingredient] < amount:
                return False
        return True
