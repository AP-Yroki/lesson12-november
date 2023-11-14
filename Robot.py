class Robot:

    def __init__(self, x, y):
        if not (0 <= 100) or not (0 <= y <= 100):
            raise ValueError('введите корректные координаты от 0 до 100')
        self.x = x
        self.y = y
        self.path_history = [(x, y)]

    def move(self, commands):
        for command in commands:
            if command == 'N' and self.y < 100:
                self.y += 1
            elif command == 'S' and self.y > 0:
                self.y -= 1
            elif command == 'E' and self.x < 100:
                self.x += 1
            elif command == 'W' and self.x > 0:
                self.x -= 1

            self.path_history.append((self.x, self.y))

        return (self.x, self.y)

    def path(self):
        return self.path_history


robot = Robot(10, 10)
print(robot.move("N"))
print(robot.move("EE"))
print(robot.path())