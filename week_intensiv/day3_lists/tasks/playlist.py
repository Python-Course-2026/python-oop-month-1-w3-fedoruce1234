class Playlist:
    """ЗАДАЧА: Подсчет общей длительности песен (track_list - список секунд)"""

    def __init__(self):
        self.tracks = []

    def get_duration(self):
        total = 0  # Начинаем с нуля
        for track in self.tracks:  # Проходим по каждой песне
            total += track  # Добавляем её длительность к общей
        return total  # Возвращаем результат