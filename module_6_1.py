# Создаём класс родителя Animal (животные) с атрибутами name (название животного),
# alive (живой) и fed (накормленный):
class Animal():
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False
    def eat(self, food):
        if food.edible:
            print(f'{self.name}, съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name}, не стал есть {food.name}')
            self.alive = False
# Создаём класс родителя Plant (растения) с атрибутами name (название растения),
# и edible (съедобность)
class Plant():
    def __init__(self, name):
        self.name = name
        self.edible = False
# Создаем 4 класса наследника:
# Mammal, Predator для Animal.
# Flower, Fruit для Plant.
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
# Для каждого из объектов класса Mammal и Predator прописываем атрибуты и методы:
# где eat(self, food) - это метод, а food - это параметр принимающий объекты классов растений.
a1 = Predator('Волк')
a2 = Mammal('Кролик')
p1 = Flower('Цветок роза')
p2 = Fruit('Апельсин')
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
# Волк не стал есть цветы и он погибнет
# А если Кролик будет есть апельсины то он будет жить
print(a1.alive)
print(a2.fed)
