class SnowFlake:

        def __init__(self, count):
            if count % 2 == 0:
                raise ValueError('Число должно быть нечётным')

            self.count = count
            self.flake = ['*' if i == count // 2 else '-' for i in range(count)]

        def thaw(self, steps):
            for i in range(steps):
                self.flake = self.flake[1:-1]

        def freeze(self, n):
            self.count += 2 * n
            self.flake = ['-' for i in range(n)] + self.flake + ['-' for i in range(n)]

        def thicken(self):
            self.count += 2
            self.flake = ['*' if i == 0 or i == self.count - 1 else '*' + char + '*' for i, char in enumerate(self.flake)]

        def show(self):
            print(''.join(self.flake))


snowflake = SnowFlake(7)
snowflake.show()

snowflake.thaw(1)
snowflake.show()

snowflake.freeze(2)
snowflake.show()

snowflake.thicken()
snowflake.show()
