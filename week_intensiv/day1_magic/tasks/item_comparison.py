class Item:
    """ЗАДАЧА: Сравнение товаров по цене через __lt__ и по всем полям через __eq__"""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        """Сравнение по цене (меньше)"""
        if not isinstance(other, Item):
            return NotImplemented
        return self.price < other.price

    def __eq__(self, other):
        """Сравнение по всем полям"""
        if not isinstance(other, Item):
            return NotImplemented
        return self.name == other.name and self.price == other.price