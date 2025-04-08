# B
import pygame

BG = (50, 50, 50)
BLACK = (0, 0, 0)

# C
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)


# E
EVENT_INIME = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 0,
    'Level1Bg3': 2,
    'Level1Bg4': -1,
    'Level1Bg5': 3,
    'player1Run': 8,
    'Hurt': 8,
    'Scream': 2,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT',)

#P
PLAYER_KEY_UP = {'player1Run': pygame.K_UP, 'player2Run': pygame.K_w}
PLAYER_KEY_DOWN = {'player1Run': pygame.K_DOWN, 'player2Run': pygame.K_s}
PLAYER_KEY_LEFT = {'player1Run': pygame.K_LEFT, 'player2Run': pygame.K_a}
PLAYER_KEY_RIGHT = {'player1Run': pygame.K_RIGHT, 'player2Run': pygame.K_d}
PLAYER_KEY_SHOOT ={'player1Run': pygame.K_RCTRL, 'player2Run': pygame.K_LCTRL}

# S
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
