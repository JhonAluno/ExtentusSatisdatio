#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        pass
