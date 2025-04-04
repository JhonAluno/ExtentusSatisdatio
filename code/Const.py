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
    'Parado': 1,
    'Hurt': 1,
    'Scream': 3,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT',)

#P
PLAYER_KEY_UP = {'Parado': pygame.K_UP, 'Hurt': pygame.K_w}
PLAYER_KEY_DOWN = {'Parado': pygame.K_DOWN, 'Hurt': pygame.K_s}
PLAYER_KEY_LEFT = {'Parado': pygame.K_LEFT, 'Hurt': pygame.K_a}
PLAYER_KEY_RIGHT = {'Parado': pygame.K_RIGHT, 'Hurt': pygame.K_d}
PLAYER_KEY_SHOOT ={'Parado': pygame.K_RCTRL, 'Hurt': pygame.K_LCTRL}

# S
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
