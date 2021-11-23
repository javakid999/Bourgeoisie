class Rope:
    def __init__(self, points, sticks, color, iterations = 8):
        self.points = points
        self.sticks = sticks
        self.iterations = iterations
        self.color = color
    def update(self, player):
        for i in range(self.iterations):
          for point in self.points:
            point.update(player)
          for stick in self.sticks:
            stick.update()
    def render(self, display):
        for stick in self.sticks:
            stick.render(display, self.color)