#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from Code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDHT, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT
from Code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name,position)


    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0 :
            self.rect.centery -= ENTITY_SPEED[self.name]

        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0 :
            self.rect.centerx -= ENTITY_SPEED[self.name]

        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDHT:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass
