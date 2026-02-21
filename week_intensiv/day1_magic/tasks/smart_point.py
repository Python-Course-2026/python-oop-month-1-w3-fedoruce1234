class SmartPoint:
    """ЗАДАЧА: Реализовать __str__ (Точка(x, y)) и __repr__ (SmartPoint(x=x, y=y))"""
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        # Возвращает строку для пользователя: "Точка(10, 20)"
        return f"Точка({self.x}, {self.y})"

    def __repr__(self):
        # Возвращает строку для разработчика: "SmartPoint(x=5, y=-5)"
        return f"SmartPoint(x={self.x}, y={self.y})"