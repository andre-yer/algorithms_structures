class AbstractCat:

    def __init__(self):
        self.weight = 0
        self.food = 0

    def eat(self, food):
        self.food += food
        next_weight = self.weight + self.food // 10
        if next_weight > 100:
            self.food -= (100 - self.weight) * 10
            self.weight = 100
        else:
            self.weight = next_weight
            self.food = self.food % 10

    def __str__(self):
        return '{} ({})'.format(self.__class__.__name__, self.weight)


class Kitten(AbstractCat):

    def __init__(self, weight):
        super().__init__()
        self.weight = weight

    def meow(self):
        return 'meow...'

    def sleep(self):
        return 'Snore' * int(self.weight // 5)


class Cat(Kitten):

    def __init__(self, weight, name):
        super().__init__(weight)
        self.name = name

    def meow(self):
        return 'MEOW...'

    def get_name(self):
        return self.name

    def catch_mice(self):
        return 'Got it!'


def main():
    abscat = AbstractCat()
    abscat.eat(125)
    abscat.eat(17)
    print(abscat)
    kit = Kitten(21)
    print(kit.sleep())
    cat = Cat(83, 'Molly')
    print(cat.meow())
    print(cat.get_name())


if __name__ == '__main__':
    main()
