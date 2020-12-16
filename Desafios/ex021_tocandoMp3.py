import pygame
pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('D:\Arquivos de Programas\Xampp\htdocs\meusAplicativos\scriptsPython\Desafios\Camp_in_the_Woods.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()