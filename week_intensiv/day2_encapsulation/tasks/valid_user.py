class ValidUser:
    """ЗАДАЧА: Сеттер пароля с проверкой длины >= 8 и наличия цифр"""

    def __init__(self, user, pwd):
        self.username = user
        self._password = None
        # Используем setter для установки начального пароля
        self.password = pwd

    @property
    def password(self):
        # Getter: возвращает маскированный пароль
        return "********"

    @password.setter
    def password(self, val):
        # Setter: проверяет и устанавливает пароль
        has_digit = False
        for c in val:
            if c.isdigit():
                has_digit = True
                break

        # Если пароль соответствует требованиям — сохраняем
        if len(val) >= 8 and has_digit:
            self._password = val
        # Если нет — можно либо молча игнорировать, либо raise ValueError