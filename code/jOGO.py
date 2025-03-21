#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.mENU import MENU


class JOGO:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(576, 324))
        self.itens_pegos = None
        self.vida_inimigo = None

    def pegarItem(self, ):
        pass

    def atacarInimigo(self, ):
        pass

    def verificarVitoria(self, ):
        pass

    def run(self):
        while True:
            menu = MENU(self.window)
            menu.run()



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()  # End
