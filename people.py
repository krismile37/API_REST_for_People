"""
Это модуль людей, который поддерживает все действия ReST для
коллекции PEOPLE
"""

# Системные модули
from datetime import datetime

# Сторонние модули
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Данные для обслуживания с API
PEOPLE = {
    "Farrell": {
        "fname": "Матвей",
        "lname": "Соколов",
        "timestamp": get_timestamp(),
    },
    "Brockman": {
        "fname": "Павел",
        "lname": "Морозов",
        "timestamp": get_timestamp(),
    },
    "Easter": {
        "fname": "Роман",
        "lname": "Лебедев",
        "timestamp": get_timestamp(),
    },
}


def read_all():
    """
    Эта функция отвечает на запрос для /api/people
    с полными списками людей

    :return:        json строка списка людей
    """
    # Создание списока людей из наших данных
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


def read_one(lname):
    """
    Эта функция отвечает на запрос /api/people/{named}
    с одним подходящим человеком из людей

    :param lname:   фамилия человека, которого нужно найти
    :return:        человек, соответствующий фамилии
    """
    # Существует ли личность в людях?
    if lname in PEOPLE:
        person = PEOPLE.get(lname)

    # в противном случае, нет, не найдено
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )

    return person


def create(person):
    """
    Эта функция создает нового человека в структуре людей
    на основании переданных личных данных

    :param person:  человек для создания в людях структуры
    :return:        201 - удачно, 406 - человек существует
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    # Существует ли уже этот человек?
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return PEOPLE[lname], 201

    # В противном случае, они существуют, это ошибка
    else:
        abort(
            406,
            "Person with last name {lname} already exists".format(lname=lname),
        )


def update(lname, person):
    """
    Эта функция обновляет существующего человека в структуре людей

    :param lname:   фамилия человека для обновления в структуре людей
    :param person:  человек для обновления
    :return:        обновленная структура людей
    """
    # Существует ли личность в людях?
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["timestamp"] = get_timestamp()

        return PEOPLE[lname]

    # в противном случае, нет, это ошибка
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )


def delete(lname):
    """
    Эта функция удаляет человека из структуры людей

    :param lname:   фамилия человека, подлежащего удалению
    :return:        200 при успешном удалении, 404 если не найдено
    """
    # Существует ли человек, которого нужно удалить?
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            "{lname} successfully deleted".format(lname=lname), 200
        )

    # В противном случае, нет, человек для удаления не найден
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )