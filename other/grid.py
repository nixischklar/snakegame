Window_Height = 700
Window_Width = 800


class SmartGrid:
    def __init__(self):
        self.grid = [[False for i in range(Window_Height)]
                     for j in range(Window_Width)]

    def __getitem__(self, coords):
        return self.grid[coords[0]][coords[1]]

    def __setitem__(self, coords, value):
        self.grid[coords[0]][coords[1]] = value

