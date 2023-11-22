import numbers
from random import randint
class NumList:
    def __init__(self, size):
        self.size = size
        self.data = []

    def input_data(self, data):
        self.data = data

    def fill_random(self):
        for i in range(0, self.size):
            self.data.append(randint(0, 10))

    def find(self, number):
        indexes = []
        if isinstance(number, numbers.Number):
            for i in range(0, self.size - 1):
                if self.data[i] == number:
                    indexes.append(i)
            return indexes
        else: return []

    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return self.__str__()

    def remove(self, value):
        if self.data.count(value) > 0:
            self.data.remove(value)
        return self.data

    def max(self):
        mx = -1
        for i in range(0, self.size - 1):
            if self.data[i] > mx: mx = self.data[i]
        return mx

    def add(self, other):
        result = []
        if isinstance(other, NumList) and other.size == self.size:
            for i in range(0, self.size):
                a = self.data[i]
                b = other.data[i]
                result.append(a + b)
        return result



n = NumList(13)
m = NumList(13)

m.fill_random()
n.fill_random()
to_find = 7
to_remove = 7
print(f"list n: {n}")
print(f"list m: {m}")
print(f"n add m:{n.add(m)}")
print(f"n.find {to_find}: {n.find(to_find)}")
print(f"n.remove {to_remove}: {n.remove(to_remove)}")
print(f"n.max: {n.max()}")

print(f"m.find {to_find}: {m.find(7)}")
print(f"m.remove {to_remove}: {m.remove(7)}")
print(f"m.max: {m.max()}")

