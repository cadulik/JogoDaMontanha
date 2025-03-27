#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Code.Const import WIN_HEIGHT, WIN_WIDHT, MENU_OPTION
from Code.level import Level
from Code.menu import Menu


class Game:
    def __init__(self):
        self.window = None
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDHT, WIN_HEIGHT))

    def run(self, ):

        while True:
            menu =Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0],MENU_OPTION[1],MENU_OPTION[2]]:
                player_score = [0,0] #[Player 1, Player 2 ]
                level = Level(self.window,'Level1',menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                pass





