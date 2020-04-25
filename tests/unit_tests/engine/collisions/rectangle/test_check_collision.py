import unittest

from engine.collisions.rectangle import Rectangle, check_collision


class CheckCollisionTest(unittest.TestCase):

    def test_collision_1(self):
        rect1 = Rectangle(x=1, y=1, width=3, height=2)
        rect2 = Rectangle(x=3, y=2, width=2, height=3)
        result = check_collision(rect1, rect2)
        self.assertTrue(result)

    def test_collision_2(self):
        rect1 = Rectangle(x=2, y=3, width=3, height=2)
        rect2 = Rectangle(x=1, y=1, width=2, height=3)
        result = check_collision(rect1, rect2)
        self.assertTrue(result)

    def test_collision_3(self):
        rect1 = Rectangle(x=1, y=2, width=3, height=2)
        rect2 = Rectangle(x=2, y=3, width=2, height=3)
        result = check_collision(rect1, rect2)
        self.assertTrue(result)

    def test_no_collision_1(self):
        rect1 = Rectangle(x=1, y=2, width=3, height=2)
        rect2 = Rectangle(x=0, y=5, width=2, height=3)
        result = check_collision(rect1, rect2)
        self.assertFalse(result)

    def test_no_collision_2(self):
        rect1 = Rectangle(x=3, y=2, width=3, height=2)
        rect2 = Rectangle(x=0, y=1, width=2, height=3)
        result = check_collision(rect1, rect2)
        self.assertFalse(result)

    def test_no_collision_3(self):
        rect1 = Rectangle(x=1, y=1, width=3, height=2)
        rect2 = Rectangle(x=2, y=4, width=2, height=3)
        result = check_collision(rect1, rect2)
        self.assertFalse(result)
