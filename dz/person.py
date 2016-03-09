# -*- coding: utf8 -*-

u"""
Задание 1: классный Человек.
УСЛОВИЕ:
Реализовать класс Person, который отображает запись в книге контактов.
Класс имеет 4 атрибута:
- surname - строка - фамилия контакта (обязательный)
- first_name - строка - имя контакта (обязательный)
- nickname - строка - псевдоним (опциональный)
- birth_date - объект datetime.date (обязательный), формат: YYYY-MM-DD
Каждый вызов класса должен создавать экземпляр (инстанс) класса с указанными
атрибутами.
Также класс имеет 2 метода:
- get_age() - считает возраст контакта в полных годах на дату вызова и
возвращает строку вида: "27";
- get_fullname() - возвращает строку, отражающую полное имя (фамилия + имя)
контакта;
"""

from datetime import datetime, date


class Person(object):
    def __init__(self, surname, fist_name, birth_date, nickname=""):
        self.surname = surname
        self.fist_name = fist_name
        self.birth_date = birth_date
        if nickname is not None:
            self.nickname = nickname
        try:
            date_format = "%Y-%m-%d"
            datetime_object = datetime.strptime(birth_date, date_format)
            self.birth_date_alternative = datetime_object.date()
        except ValueError:
            raise ValueError("You must provide birth date in correct format "
                             "(YYYY-MM-DD)!")

    def get_age_alternative(self):
        today = date.today()
        delta_in_days = today - self.birth_date_alternative
        return str(int(delta_in_days.days // 365.25))

    def get_age(self):
        birth_date = [int(a) for a in self.birth_date.split("-")]
        now_date = datetime.now()
        now_date = list(now_date.timetuple())[0:3]
        res = now_date[0] - birth_date[0]
        if (now_date[1] - birth_date[1]) < 0 or (now_date[2] - birth_date[2]) < 0:
            res -= 1
        return res

    def get_fullname(self):
        return "%s %s" % (self.surname, self.fist_name)


person = Person("Ivan", "Ivanov", "1988-03-10", "Script")
print person.get_age()
print person.get_age_alternative()
print person.get_fullname()
