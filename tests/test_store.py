import unittest

from pizza_project.lib import Store, make_worker, JobRole


class StoreTestCase(unittest.TestCase):
    def test_store_base(self):
        store_a = Store(name='store_a')
        print(store_a.inventory)

        w1 = make_worker("c baxter", JobRole.COOK)


if __name__ == '__main__':
    unittest.main()
