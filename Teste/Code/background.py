#!/usr/bin/python
# -*- coding: utf-8 -*-
from Code.Const import WIN_WIDHT, ENTITY_SPEED
from Code.entity import Entity


class Background(Entity):

    def __init__(self, name, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDHT

