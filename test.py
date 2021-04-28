import pygame
from pathlib import os
pygame.init()

# player_img = pygame.image.load(r'Assests\advisor_black.png')
img_path = os.path.join('Assests/advisor_black.png')
player_img = pygame.image.load(img_path).convert()