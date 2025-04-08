import random

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.bACKGROUND import BACKGROUND
from code.iNIMIGO import INIMIGO
from code.jOGADOR import JOGADOR


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
            case 'player1Run':
                return JOGADOR('player1Run', (8, 243))
            case 'player2Run':
                return JOGADOR('player2Run', (50, 242))
            case 'Scream':
                return INIMIGO('Scream', (WIN_WIDTH + 10, random.randint(0, WIN_WIDTH)))
            # case 'INIMIGO2':
            #     return INIMIGO('INIMIGO2', (WIN_WIDTH + 10, random.randint(0,0)))
        print('player1Run')


