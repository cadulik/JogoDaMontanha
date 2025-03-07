#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Code.Const import WIN_HEIGHT, WIN_WIDHT
from Code.menu import Menu


class Game:
    def __init__(self):
        self.window = None
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDHT, WIN_HEIGHT))

    def run(self, ):

        while True:
            menu =Menu(self.window)
            menu.run()
            pass





