class Flower:
    def __init__(self, name, color, length, stoimost, life_time):
        self.color = color
        self.length = length
        self.stoimost = stoimost
        self.life_time = life_time


class Romashka(Flower):
    def __init__(self, color, length, stoimost, life_time):
        super().__init__('Ромашка', color, length, stoimost, life_time)
        self.name = "Ромашка"

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


class Tylpan(Flower):
    def __init__(self, color, length, stoimost, life_time):
        super().__init__('Тюльпан', color, length, stoimost, life_time)
        self.name = "Тюльпан"

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        return self.flowers.append(flower)

    def calc_avg_lifetime(self):
        total_lifetime = sum(flower.life_time for flower in self.flowers)
        avg_fresh = total_lifetime / len(self.flowers)
        return avg_fresh

    def sort_by_params(self, attribute):
        return sorted(self.flowers, key=lambda flower: getattr(flower, attribute))

    def search_by_lifetime(self, life_time):
        return [flower for flower in self.flowers if flower.life_time == life_time]


romashka = Romashka('white', 23, 20, 12)
tylpan = Tylpan('red', 10, 120, 15)

bouquet = Bouquet()
bouquet.add_flower(romashka)
bouquet.add_flower(tylpan)

print(bouquet.sort_by_params('length'))
print(bouquet.search_by_lifetime(12))
