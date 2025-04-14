import os
import sys
import pygame
from codes.Game import Game

dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

game = Game()
game.run()




