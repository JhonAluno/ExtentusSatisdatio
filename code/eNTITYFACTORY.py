#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH
from code.bACKGROUND import BACKGROUND


class ENTITYFACTORY:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(6):
                    list_bg.append(BACKGROUND(f'Level1Bg{i}', position=(0, 0)))
                    list_bg.append(BACKGROUND(f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg
