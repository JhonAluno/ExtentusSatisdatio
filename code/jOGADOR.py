#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.entity import Entity



class JOGADOR(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.itens = None
        self.vida = None

    def pegarItem(self, ITEM):
        pass

    def atacarInimigo(self, INIMIGO):
        pass

    def receberDano(self, int):
        pass

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT]: #and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        pass


