from sys import exit
import pygame

pygame.init()

tamanhoTela = (800,400)

screen = pygame.display.set_mode(tamanhoTela)

running = True
while running:
  # analisar eventos
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  # desenhar elementos
  # atualizar tudo
  pygame.display.update()
