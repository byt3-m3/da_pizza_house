class Item:
    def __init__(self, **kwargs):
        self.price = kwargs.get('price', float)
        self.name = kwargs.get('name', str)

    def __repr__(self):
        return f'<Item(name={self.name}, price={self.price}, {self.__class__})'


class Food(Item):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Drink(Item):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class InventoryItem:
    def __init__(self, **kwargs):
        self.quantity = kwargs.get("quantity")

        self._item = kwargs.get("item", None)

    @property
    def item(self):
        if isinstance(self._item, Item):
            return self._item

    @item.setter
    def item(self, item: Item):
        if isinstance(self._item, Item):
            self._item = item

    def __repr__(self):
        return f'<InventoryItem(quantity={self.quantity}, item={self.item})>'


class Inventory:
    def __init__(self, **kwargs):
        self.account = kwargs.get("account", float)
        self._items = []

    def __len__(self):
        return len(self.items)

    @property
    def balance(self):
        return round(self.account, 4)

    @property
    def stock(self):
        """

        :return: The current value of all items currently in the inventory
        """
        total = 0
        for item in self.items:
            total += item.item.price * item.quantity

        return total

    @property
    def size(self):
        """

        :return: Returns the current len for the self.items property.
        """
        return len(self)

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, item: InventoryItem):
        if isinstance(item, InventoryItem):
            self._deduct_from_account(item.item.price * item.quantity)
            self._items.append(item)

    def add_item(self, item: Item, quantity: int) -> bool:
        """
        Creates a new item in the items list. This method will take a basic Item
        convert to an InventoryItem for the system and append it to the self.items list.

        This function will automatically detect if exsisting items are present by querying the name,
        If there are common products, it will update the quantity to reflect


        :param item:
        :param quantity:
        :return:
        """
        if isinstance(item, Item):
            if self._query_item_by_name(item.name):
                inventory_item = self._query_item_by_name(item.name)
                inventory_item.quantity += quantity
                return True
            else:
                self.items = InventoryItem(quantity=quantity, item=item)
                return True
        else:
            return False

    def delete_item(self, item: InventoryItem):
        # TODO: Implement function to remove item from inventory
        raise NotImplementedError

    def add_items(self, items: list):
        """
        Takes a list of tulples structed as (item, quantity). Will iterate over the list tupples
        and add items to the inventory


        :param items:
        :return:
        """
        results = []
        for tuple_ in items:
            if isinstance(tuple_, tuple):
                item = tuple_[0]
                quantity = tuple_[1]
                if self.add_item(item, quantity):
                    results.append((item, True))
                else:
                    results.append((item, False))

        return results

    def get_item_from_inventory(self, name: str, quantity: int) -> InventoryItem:
        """
        Gets an IventoryItem from the current stock.

        :param name:
        :param quantity:
        :return:
        """
        inventory_item = self._query_item_by_name(name)
        if inventory_item:
            inventory_item.quantity = inventory_item.quantity - quantity
            self._add_to_account(quantity + inventory_item.item.price)
            return InventoryItem(item=inventory_item.item, quantity=quantity)

    def _query_item_by_name(self, name) -> InventoryItem:
        """
        Iterates the self.items list and searches for a specific item enclosed in the InventoryItem object.


        :param name:
        :return: InventoryItem object is match else None
        """
        for item in self.items:
            if item.item.name == name:
                return item

    def _deduct_from_account(self, amount: float):
        """
        Subtracts the amount from the account

        :param amount:
        :return:
        """
        temp = self.account - amount
        if temp < 0:
            raise Exception(f'Insufficient Funds: {self.balance}!')
        self.account = temp

        return True

    def _add_to_account(self, amount: float):
        temp = self.account + amount
        if temp < 0:
            raise Exception(f'Insufficient Funds: {self.balance}!')
        self.account = temp
        return True


# Helper functions

def new_item(name: str, price: float) -> Item:
    """
    Creates a new instance of Item.

    :param name: Name of item
    :param price: Price of the Item
    :return:
    """
    return Item(name=name, price=price)


def new_inventory_item(item: Item, quantity: int) -> InventoryItem:
    """
    Creates a new instance of InventoryItem

    :param item: instance of a Item
    :param quantity: Number of Items
    :return:
    """
    if isinstance(item, Item):
        return InventoryItem(item=item, quantity=quantity)


def build_inventory_item(name: str, price: float, quantity: int) -> InventoryItem:
    """
    Builds a new item instance and creates a instance of InventoryItem

    :param name: Name of item
    :param price: Price of the Item
    :param quantity: Number of Items
    :return:
    """
    return InventoryItem(item=Item(name=name, price=price), quantity=quantity)
