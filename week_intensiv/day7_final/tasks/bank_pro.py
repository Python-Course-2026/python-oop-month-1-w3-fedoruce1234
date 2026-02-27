class Account:
    """Базовый класс счета"""

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


class BusinessAccount(Account):
    """Бизнес-счет с комиссией 5% и овердрафтом до -1000"""

    def __init__(self, owner, balance):
        super().__init__(owner, balance)
        self.commission_rate = 0.05  # 5% комиссия
        self.overdraft_limit = -1000  # Лимит овердрафта


class SavingsAccount(Account):
    """Накопительный счет без комиссии и овердрафта"""

    def __init__(self, owner, balance):
        super().__init__(owner, balance)
        self.commission_rate = 0  # Нет комиссии
        self.overdraft_limit = 0  # Нельзя уйти в минус


class BankPro:
    """
    ЗАДАЧА: Реализовать перевод с учетом комиссии и лимитов.
    1. Рассчитать комиссию: amount * commission_rate
    2. Проверить, хватает ли средств (с учетом комиссии и лимита овердрафта)
    3. Если хватает:
       - Списать с отправителя: amount + комиссия
       - Зачислить получателю: amount
       - Вернуть "Успех"
    4. Если не хватает: вернуть "Ошибка"
    """

    def transfer(self, from_acc, to_acc, amount):
        # Рассчитываем комиссию
        commission = amount * from_acc.commission_rate

        # Общая сумма списания (сумма перевода + комиссия)
        total_deduction = amount + commission

        # Проверяем, не превысит ли новый баланс лимит овердрафта
        new_balance = from_acc.balance - total_deduction

        if new_balance < from_acc.overdraft_limit:
            return "Ошибка"

        # Проводим перевод
        from_acc.balance -= total_deduction
        to_acc.balance += amount

        return "Успех"