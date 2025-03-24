#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code import lEVEL
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.lEVEL import LEVEL
from code.mENU import MENU


class JOGO:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
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
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = LEVEL(self.window, 'Level1', menu_return)
                level_return = level.run()

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass
