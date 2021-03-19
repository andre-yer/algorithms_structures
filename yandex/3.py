class PearsBasket:
    
    def __init__(self, amount):
        self.amount = amount


    def __floordiv__(self, other):
        pears_list = []
        pear_mod = self.amount % other
        pear_div = self.amount // other
        for i in range(other):
            pears_list.append(__class__(pear_div))
        pears_list.append(__class__(pear_mod))
        return pears_list

    def __mod__(self, other):
        return self.amount % other

    def __add__(self, other):
        return __class__(self.amount + other.amount)

    def __sub__(self, other):
        if other >= self.amount:
            return __class__(0)
        else:
            self.amount -= other
            return __class__

    def __str__(self):
        return str(self.amount)

    def __repr__(self):
        return '{}({})'.format(__class__.__name__, self.amount)








pb = PearsBasket(17)
array = pb // 4
print(array)
pb_2 = PearsBasket(13)
pb_3 = pb + pb_2
print(pb_3)
print(pb_3 % 7)
pb - 2
print([pb])
