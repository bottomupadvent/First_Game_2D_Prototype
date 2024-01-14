#!/usr/bin/python3

from circle import Circle
import arcade

class Train(Circle):
    def __init__(self, x, y, r, change_x, change_y):
        super().__init__(x, y, r, change_x, change_y)

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, arcade.color.CADMIUM_ORANGE)

    def update(self):
        self.y += self.change_y


