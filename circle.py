#!/usr/bin/python3

import arcade

class Circle:
    def __init__(self, x, y, r, change_x, change_y):
        self.x = x
        self.y = y
        self.r = r
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, arcade.color.AMAZON)

    def update(self):
        pass

