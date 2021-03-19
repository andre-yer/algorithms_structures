class Robot:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.dirs_dict = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        self.pathes = [
            (self.x, self.y),
        ]

    def move(self, direction):
        dirs = list(direction)
        for item in dirs:
            next_x = self.x + self.dirs_dict[item][0]
            next_y = self.y + self.dirs_dict[item][1]
            if 0 <= next_x <= 100 and 0 <= next_y <= 100:
                self.x += self.dirs_dict[item][0]
                self.y += self.dirs_dict[item][1]
                self.pathes.append((self.x, self.y))
        return (self.x, self.y)

    def path(self):
        return self.pathes


r = Robot((0, 0))
print(r.move('SSSSS'))
print(*r.path())
