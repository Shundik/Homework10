from dataclasses import dataclass


@dataclass
class Person:
    age = 15

    @staticmethod
    def Age(age):
        if age > 18:
            print("Больше 18-ти")
        else:
            print('Меньше 18-ти')

    @classmethod
    def total_objects(cls):
        print("Возраст: ", cls.age)


Person.Age(15)
Person.total_objects()
