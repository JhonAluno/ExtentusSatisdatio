# import pygame
#
#
# class SpriteSheet():
#     def __init__(self, image):
#         self.sheet = image
#
#     def get_image(self, frame, WIN_WIDTH, WIN_HEIGHT, scale, colour):
#         image = pygame.Surface((WIN_WIDTH, WIN_HEIGHT)).convert_alpha()
#         image.blit(self.sheet, (0, 0), ((frame * WIN_WIDTH), 0, WIN_WIDTH, WIN_HEIGHT))
#         image = pygame.transform.scale(image, (WIN_WIDTH * scale, WIN_HEIGHT * scale))
#         image.set_colorkey(colour)
#
#         return image
#
#
