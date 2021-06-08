import pygame
pygame.mixer.init()
pygame.mixer.music.load('Moonlight_Sonata_by_Beethoven.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass



