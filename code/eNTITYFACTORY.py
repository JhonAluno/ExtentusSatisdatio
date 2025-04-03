import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.bACKGROUND import BACKGROUND
from code.jOGADOR import JOGADOR


class ENTITYFACTORY:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0), spritesheet=None):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(6):
                    list_bg.append(BACKGROUND(f'Level1Bg{i}', position=(0, 0)))
                    list_bg.append(BACKGROUND(f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Parado':
                return JOGADOR('Parado', (50, WIN_HEIGHT / 2))
            case 'Hurt':
                return JOGADOR('Hurt', (60, WIN_HEIGHT / 2))

                


