#!/usr/bin/python3

from circle import Circle
import random as rand
import settings as se
import math
import arcade

class ManyC(Circle):
    def __init__(self, x, y, r, change_x, change_y):
        super().__init__(x, y, r, change_x, change_y)

    def update(self, player):
        viewport_height = arcade.get_viewport()     # Returns tuple for current Viewport

        # Change People's "y" location to top of viewport when they get below 0
        if self.y < viewport_height[2]:
            self.y = rand.randrange(viewport_height[3], viewport_height[3] + 200)
            self.x = rand.randrange(30, 250)

        # Next two lines doesn't let the people go beyond the line drawn 
        if self.x > se.WIN_WIDTH - 33 - self.r:
            self.x = se.WIN_WIDTH - 33 - self.r
        # Doesn't let people go beyond left side of Window
        if self.x <= self.r:
            self.x = self.r

        # Next 4 lines Collision detection with Player object
        dx = player.x - self.x
        dy = player.y - self.y
        distance = math.sqrt(dx * dx + dy * dy)
        if (distance < player.r + self.r):
            player.y = viewport_height[2] + 12
            player.x = 150

        self.y += -self.change_y
        self.x += -self.change_x


    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, arcade.color.WHITE)



