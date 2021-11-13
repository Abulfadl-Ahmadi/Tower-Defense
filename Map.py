class Cell:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._content = []

    def add_content(self, obj):
        self._content.append(obj)

    def remove_content(self, obj):
        self._content.remove(obj)

    def __str__(self):
        return " | ".join([str(content) for content in self._content])


class Map:

    def __init__(self, width, length):
        self._width = width
        self._length = length
        self._matrix = None

    def initialize(self):
        self._matrix = []
        for x in range(self._width):
            row = []
            for y in range(self._length):
                cell = Cell(x, y)
                cell.add_content("^")
                row.append(cell)

            self._matrix.append(row)

    def show_map(self):
        global y
        for x in range(self._length):
            for y in range(self._width):
                print(self._matrix[y][x], end=" ")
            print(" ")


game_map = Map(5, 5)
game_map.initialize()
game_map.show_map()
