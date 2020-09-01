import unittest
from copy import deepcopy

from lib import Inventory, Food, Item, InventoryItem


class InventoryTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.inventory = Inventory(account=1000)

    def test_inventory_base(self):
        my_inventory = deepcopy(self.inventory)

        self.assertEqual(my_inventory.balance, 1000)

        self.assertEqual(my_inventory.size, 0)
        self.assertEqual(my_inventory.balance, 1000)

    def test_inventory_add_item(self):
        """
        Tests the functionality of add single Items

        :return:
        """
        my_inventory = deepcopy(self.inventory)

        cheese = Food(price=2.15, name="cheese")
        pizza_sauce = Food(price=1.25, name="pizza_sauce")

        self.assertIsInstance(cheese, Item)
        self.assertTrue(my_inventory.add_item(item=cheese, quantity=100))
        self.assertTrue(my_inventory.add_item(item=pizza_sauce, quantity=15))

        self.assertEqual(len(my_inventory), 2)

    def test_inventory_add_items(self):
        """
        Tests the functionality of add multiple Items

        :return:
        """
        my_inventory = deepcopy(self.inventory)

        cheese = Food(price=2.15, name="cheese")
        pizza_sauce = Food(price=1.25, name="pizza_sauce")

        self.assertIsInstance(my_inventory.add_items([(cheese, 100), (pizza_sauce, 15)]), list)
        self.assertEqual(my_inventory.balance, 766.25)

        self.assertEqual(len(my_inventory), 2)

    def test_inventory_get_item(self):
        my_inventory = deepcopy(self.inventory)

        cheese = Food(price=2.15, name="cheese")
        my_inventory.add_item(item=cheese, quantity=100)

        self.assertEqual(my_inventory.stock, 215.0)
        i_item = my_inventory.get_item_from_inventory('cheese', 50)
        self.assertIsInstance(i_item, InventoryItem)
        self.assertEqual(my_inventory.stock, 107.5)


if __name__ == '__main__':
    unittest.main()