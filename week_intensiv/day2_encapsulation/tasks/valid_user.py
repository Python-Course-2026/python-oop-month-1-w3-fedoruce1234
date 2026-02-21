class ValidUser:
    """ЗАДАЧА: Сеттер пароля с проверкой длины >= 8 и наличия цифр"""
    def __init__(self, user, pwd):
        self.username = user
        self._password = pwd

    def password(self):
        return "********"

    def password(self, val):
        has_digit = False
        for c in val:
            if c.isdigit():
                has_digit = True
                break
        if len(val) >= 8 and has_digit:
            self._password = val