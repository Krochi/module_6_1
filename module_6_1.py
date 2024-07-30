# Задача "Съедобное, несъедобное":
# Разнообразие животного мира давно будоражит умы человечества.
# Царства, классы, виды... Почему бы и нам не попробовать выстроить
# что-то подобное используя наследования классов?
# Необходимо описать пример иерархии животного мира,
# используя классы и принцип наследования.

# Создайте:
# 2 класса родителя: Animal, Plant
# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
# Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения

# 4 класса наследника:
# Mammal, Predator для Animal.
# Flower, Fruit для Plant.

# У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
# eat(food) - метод, где food - это параметр, принимающий объекты классов растений.

# Метод eat должен работать следующим образом:
# Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>",
# меняется атрибут fed на True.
# Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>",
# меняется атрибут alive на False.
# Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.

# У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)

# Создайте объекты классов и проделайте действия затронутые в примере результата работы программы.

# Пункты задачи:
# Создайте классы Animal и Plant с соответствующими атрибутами и методами
# Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами.
# При необходимости переопределите значения атрибутов.
# Создайте объекты этих классов.


class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

# Создаем объекты классов
a1 = Predator('Волк')
a2 = Mammal('Слон')
p1 = Flower('ромашку')
p2 = Fruit('банан')

# Проверка результата
print(a1.name)  # Вывод: Волк
print(p1.name)  # Вывод: ромашку

print(a1.alive)  # Вывод: True
print(a2.fed)    # Вывод: False
a1.eat(p1)       # Вывод: Волк не стал есть рамашку
a2.eat(p2)       # Вывод: Слон съел банан
print(a1.alive)  # Вывод: False
print(a2.fed)    # Вывод: True
