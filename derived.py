#!/usr/bin/python3

import arcade
import math
import settings as se
from circle import Circle

class Player(Circle):
    def __init__(self, x, y, r, change_x, change_y):
        super().__init__(x, y, r, change_x, change_y)
        self.view_bottom = 0
        self.changed = False

    def draw(self):
        super().draw()

    def update(self, train):
        self.y += self.change_y
        self.x += self.change_x

    # Stop player go beyond the max and min window width 
        if self.x > se.WIN_WIDTH - 33 - self.r and self.y != train.y:
            self.x = se.WIN_WIDTH - 33 - self.r
        elif self.x < self.r:
            self.x = self.r
    # Player can get on train if following
        elif self.y == train.y and train.x - self.x < 25:
            self.x = se.WIN_WIDTH - self.r - 2
            self.y = 0
            self.x = 0
            view = arcade.get_viewport()
            arcade.draw_text("Yo Bro", view[0] + 100, view[2] + 200, arcade.color.WHITE,
                            12, 40)

        # Scroll up (ViewPort)
        top_bndry = self.view_bottom + se.WIN_HEIGHT - se.VIEWPORT_MARGIN
        if self.y > top_bndry:
            self.view_bottom += self.y - top_bndry
            self.changed = True

        if self.changed:
            arcade.set_viewport(0, se.WIN_WIDTH, self.view_bottom,
                                se.WIN_HEIGHT + self.view_bottom)


    def on_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.change_y = se.SPEED
        elif key == arcade.key.DOWN:
            self.change_y = -se.SPEED
        elif key == arcade.key.LEFT:
            self.change_x = -se.SPEED
        elif key == arcade.key.RIGHT:
            self.change_x = se.SPEED

    def on_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.change_y = 0
        elif key == arcade.key.DOWN:
            self.change_y = 0
        elif key == arcade.key.LEFT:
            self.change_x = 0
        elif key == arcade.key.RIGHT:
            self.change_x = 0
