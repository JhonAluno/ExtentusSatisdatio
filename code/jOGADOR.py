#!/usr/bin/python
# -*- coding: utf-8 -*-

from Entity import Entity


class JOGADOR(Entity):
    def __init__(self):
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
