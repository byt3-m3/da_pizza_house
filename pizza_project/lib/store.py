from enum import Enum
from queue import Queue

from pizza_project.lib.inventory import Inventory, Item


class JobRole(Enum):
    PREP = 1
    COOK = 2
    EXPEDITER = 3
    DEFAULT = 99


class Order:
    pass


class Job:
    pass


class MenuItem:
    def __init__(self, **kwargs):
        self._item = None
        self._ingredients = []

        self.item = kwargs.get("item", None)
        self.price = kwargs.get("price", float)

    def add_ingredient(self, item: Item):
        raise NotImplementedError

    def add_ingredients(self, items: list):
        raise NotImplementedError

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, item: Item):
        if isinstance(item, Item):
            self._ingredients.append(item)

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item: Item):
        if isinstance(item, Item):
            self._item = item


class Menu:
    pass


class Worker:

    def __init__(self, **kwargs):
        self._que = kwargs.get("que", Queue(maxsize=8))
        self.role = kwargs.get("role", JobRole.DEFAULT)
        self.name = kwargs.get("name")

    @property
    def que(self):
        return self._que

    @que.setter
    def que(self, job: Job):
        if isinstance(job, Job):
            self._que.put(job)

    def __len__(self):
        return len(self._que)

    def work(self):
        raise NotImplementedError


class Store:

    def __init__(self, **kwargs):
        self.inventory = kwargs.get("inventory", Inventory(account=10000))
        self.menu = kwargs.get("menu", Menu())
        self.name = kwargs.get("name")
        self.workers = kwargs.get("workers", [])
        self.orders = kwargs.get("orders", [])
        self.jobs = kwargs.get("jobs", [])

        self.id = id(self)

    def hire_worker(self, worker: Worker):
        raise NotImplementedError

    def fire_worker(self, worker: Worker):
        raise NotImplementedError

    def check_inventory(self, item: MenuItem):
        raise NotImplementedError

    def open(self):
        raise NotImplementedError

    def take_order(self, order: Order):
        raise NotImplementedError

    def stock_up(self):
        raise NotImplementedError


# Helper Functions

def make_worker(name: str, role: JobRole):
    if role in JobRole:
        return Worker(name=name, role=role)
    else:
        raise Exception(f"Invalid Job Role Options: {[val.name for val in JobRole]}")
