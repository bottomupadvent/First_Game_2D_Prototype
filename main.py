#!/usr/bin/python3

'''
Circle class is the Base class
Player class "is a" Circle # Player
ManyC class "is a" Circle  # People
Train class "is a" Circle # Train
settings include "globals"
'''

import arcade
import random as rand
import settings as se
from derived import Player
from circle import Circle
from many import ManyC
from train import Train

class Main(arcade.Window):

    def __init__(self):
        super().__init__(se.WIN_WIDTH, se.WIN_HEIGHT, se.WIN_TITLE) # Set Window Dimensions
        arcade.set_background_color(arcade.color.BLACK)     # Set Window Background Color
        self.player = Player(100, 10, 10, 0, 0)                     # Player Object
        self.train = Train(285, 200, 10, 4, 4)                       # Train Object
        self.manylist = list()

        for i in range(10):                                         # Creates People Object 10 of em 
            self.many = ManyC(rand.randrange(30, 250), rand.randrange(500, 700),
                            rand.randrange(6, 11), rand.randrange(-2, 2),
                            rand.randrange(3, 11))
            self.manylist.append(self.many)

    def on_draw(self):
        arcade.start_render()                                       # Drawing Commands go below this 
        arcade.draw_line(270, 0, 270, 10000, arcade.color.WHITE, 1)
        self.player.draw()
        self.train.draw()
        for i in range(10):
            self.manylist[i].draw()

    def update(self, delta_time):                                   # Update's All Objects
        self.player.update(self.train)
        self.train.update()
        for i in range(10):
            self.manylist[i].update(self.player)

    def on_key_press(self, key, modifiers):                         # Key Press Event
        self.player.on_press(key, modifiers)

    def on_key_release(self, key, modifiers):                       # Key Release Event 
        self.player.on_release(key, modifiers)

def main():                                                         # Main Method
    se.init()                                                       # Initializes Globals stored in settings
    window = Main()
    arcade.run()                                                    # Keeps the Window running

if __name__ == "__main__":
    main()

