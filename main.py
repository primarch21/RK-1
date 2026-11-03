"""РК №1. Вариант запросов Г, предметная область №2: Школьник — Класс."""

from operator import itemgetter


class Pupil:
    """Школьник; age — количественный признак, class_id — связь 1:М."""

    def __init__(self, id, surname, age, class_id):
        self.id = id
        self.surname = surname
        self.age = age
        self.class_id = class_id


class SchoolClass:
    """Школьный класс."""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class PupilClass:
    """Связь школьника с классом для отношения М:М."""

    def __init__(self, pupil_id, class_id):
        self.pupil_id = pupil_id
        self.class_id = class_id


# Условные названия классов позволяют проверить начало названия на «А».
classes = [
    SchoolClass(1, "Альфа"),
    SchoolClass(2, "Бета"),
    SchoolClass(3, "Альтаир"),
]

pupils = [
    Pupil(1, "Иванов", 14, 1),
    Pupil(2, "Петров", 15, 1),
    Pupil(3, "Сидорова", 16, 2),
    Pupil(4, "Алексеева", 15, 3),
    Pupil(5, "Смирнов", 17, 2),
]

# В модели М:М школьник может посещать несколько учебных классов.
pupils_classes = [
    PupilClass(1, 1),
    PupilClass(2, 1),
    PupilClass(3, 2),
    PupilClass(4, 3),
    PupilClass(5, 2),
    PupilClass(1, 3),
    PupilClass(4, 2),
]


def query_g1(pupils, classes):
    """Классы на букву «А» и их школьники; связь 1:М."""
    return {
        c.name: [p.surname for p in pupils if p.class_id == c.id]
        for c in classes
        if c.name.startswith("А")
    }


def query_g2(pupils, classes):
    """Максимальный возраст по классам, по убыванию; связь 1:М."""
    ages_by_class = {
        c.id: [p.age for p in pupils if p.class_id == c.id]
        for c in classes
    }
    # У пустого класса максимальный возраст не определён.
    result = [
        (c.name, max(ages_by_class[c.id]))
        for c in classes
        if ages_by_class[c.id]
    ]
    return sorted(result, key=itemgetter(1), reverse=True)


def query_g3(pupils, classes, links):
    """Все пары (школьник, класс), сортировка по классу; связь М:М."""
    many_to_many = [
        (p.surname, c.name)
        for c in classes
        for link in links
        for p in pupils
        if link.class_id == c.id and link.pupil_id == p.id
    ]
    return sorted(many_to_many, key=itemgetter(1))


def main():
    print("Задание Г1. Классы на букву «А» и их школьники:")
    for name, surnames in query_g1(pupils, classes).items():
        print(f"{name}: {', '.join(surnames) or 'нет школьников'}")

    print("\nЗадание Г2. Максимальный возраст (по убыванию):")
    for name, max_age in query_g2(pupils, classes):
        print(f"{name}: {max_age}")

    print("\nЗадание Г3. Школьники и классы (сортировка по классу):")
    for surname, name in query_g3(pupils, classes, pupils_classes):
        print(f"{surname} — {name}")


if __name__ == "__main__":
    main()
