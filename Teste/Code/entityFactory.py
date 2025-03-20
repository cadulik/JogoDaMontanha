#!/usr/bin/python
# -*- coding: utf-8 -*
import random

from Code.Const import WIN_WIDHT, WIN_HEIGHT
from Code.background import Background
from Code.enemy import Enemy
from Code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg=[]
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}',(0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDHT, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1',(10,WIN_HEIGHT/2 - 30))

            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30 ))

            case 'Enemy1':
                return Enemy('Enemy1',(WIN_WIDHT + 10 , random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDHT + 10, random.randint(40, WIN_HEIGHT -40)))



