class Event:
    """Класс-контейнер для данных о событии"""
    def __init__(self, title: str, date: str, participants: int):
        self.title = title
        self.date = date  # Формат "ГГГГ-ММ-ДД"
        self.participants = participants

class EventPlanner:
    """
    ЗАДАЧА: Аналитика событий.
    1. get_events_on_date(date): возвращает список НАЗВАНИЙ (str) событий на эту дату.
    2. get_total_participants(): возвращает общее число участников всех событий.
    """
    def __init__(self):
        self.events = []

    def add_event(self, event):
        # Добавляет объект Event в список
        self.events.append(event)

    def get_events_on_date(self, date):
        # ТВОЙ КОД ЗДЕСЬ
        result = []  # Создаем пустую коробку для названий

        for event in self.events:  # Берем каждое событие по очереди

            if event.date == date:  # Проверяем: "Это событие в нужную дату?"

                result.append(event.title)  # Если да, кладем его название в коробку

        return result  # Возвращаем коробку с названиями


    def get_total_participants(self):

        # ТВОЙ КОД ЗДЕСЬ
        total = 0  # Начинаем с нуля участников
        for event in self.events:  # Берем каждое событие
            total += event.participants  # Прибавляем участников этого события

        return total  # Возвращаем общую сумму

