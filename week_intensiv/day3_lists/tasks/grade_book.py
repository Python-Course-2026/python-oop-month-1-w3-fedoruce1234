class GradeBook:
    """ЗАДАЧА: Найти имя студента с самым высоким средним баллом"""

    def __init__(self):
        self.students = {}

    def get_best_student(self):
        if not self.students:
            return None

        best_student = None
        best_average = -1

        for name, grades in self.students.items():  # Исправлено: students + убран пробел
            if grades:  # если есть оценки
                average = sum(grades) / len(grades)
                if average > best_average:
                    best_average = average
                    best_student = name

        return best_student




