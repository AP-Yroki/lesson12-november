class Snow:

    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Snow(self.count + other)

    def __sub__(self, other):
        return Snow(self.count - other)

    def __mul__(self, other):
        return Snow(self.count * other)

    def __truediv__(self, other):
        if other != 0:
            return Snow(self.count / other)
        else:
            raise ValueError('Делить на 0 нельзя')

    def makeSnow(self, num_in_row):
        rows = self.count // num_in_row
        remainder = self.count % num_in_row
        snow_str = ('*' * num_in_row + '/n') * rows
        snow_str += '*' * remainder
        return snow_str


test1 = Snow(12)
test2 = Snow(34)

result_add = test1 + 5
res_sub = test2 - 7
res_mul = test1 * 2
res_tru = test2 / 2
print(res_tru.count)
print(res_mul.count)
print(res_sub.count)
print(result_add.count)

print(test1.makeSnow(10))
print(test2.makeSnow(3))

