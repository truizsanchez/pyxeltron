class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


def check_collision(rect1: Rectangle, rect2: Rectangle) -> bool:
    collision = bool(
            rect1.x < rect2.x + rect2.width
            and rect1.x + rect1.width > rect2.x
            and rect1.y < rect2.y + rect2.height
            and rect1.height + rect1.y > rect2.y
    )
    return collision
