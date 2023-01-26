# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


# class Person:
#     def __init__(self):
#         self.planet = Planet()
#
#     def get_person_room(self):
#         return self.planet.get_contry().get_city().get_street().get_room().get_name()
#
#     def get_city_population(self):
#         return self.planet.get_contry().get_city().population()


class Person:
    def __init__(self, city, room, population, name):
        self.city = city
        self.room = room
        self.population = population
        self.name = name

    def get_city(self):
        return city
    def get_room(self):
        return self.room

    def get_population(self):
        return population

    def get_name(self):
        return name