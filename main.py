import sys
import random
import pygame

# Martyna
plik_obrazu = "C:/Marcy/Dev/Repo/projekcik/Projekt_ukladanka/blazenek_resized.jpg"
rozmiar_grafiki = (800, 600)
szerokosc_kafelka = 200
wysokosc_kafelka = 200
kolumny = 4
rzedy = 3

# w prawym dolnym rogu nie ma kafelka
pusty_kafelek = (kolumny-1, rzedy-1)

czarny = (0, 0, 0)

# poziome i pionowe granice dla kafelków
pozioma_granica = pygame.Surface((szerokosc_kafelka, 1))
pozioma_granica.fill(czarny)
pionowa_granica = pygame.Surface((1, wysokosc_kafelka))
pionowa_granica.fill(czarny)

obraz = pygame.image.load(plik_obrazu)
kafelki = {}
for k in range(kolumny) :
    for r in range(rzedy) :
        kafelek = obraz.subsurface (
            k*szerokosc_kafelka, r*wysokosc_kafelka,
            szerokosc_kafelka, wysokosc_kafelka)
        kafelki [(k, r)] = kafelek
        if (k, r) != pusty_kafelek:
            kafelek.blit(pozioma_granica, (0, 0))
            kafelek.blit(pozioma_granica, (0, wysokosc_kafelka-1))
            kafelek.blit(pionowa_granica, (0, 0))
            kafelek.blit(pionowa_granica, (szerokosc_kafelka-1, 0))
            # tutaj zaokrąglamy krawędzie
            kafelek.set_at((1, 1), czarny)
            kafelek.set_at((1, wysokosc_kafelka-2), czarny)
            kafelek.set_at((szerokosc_kafelka-2, 1), czarny)
            kafelek.set_at((szerokosc_kafelka-2, wysokosc_kafelka-2), czarny)
kafelki[pusty_kafelek].fill(czarny)

stan = {(kol, rzad): (kol, rzad)
            for kol in range(kolumny) for rzad in range(rzedy)}

(pusty_k, pusty_r) = pusty_kafelek

#Faustyna: ROBOT-PRZESZKADZACZ, na razie wyświetla się na jednym kafelku
class Robocik(pygame.sprite.Sprite):

    def __init__(self):
            super(Robocik, self).__init__()
            self.okienko = pygame.Surface((200, 200))
            self.okienko.fill((0, 0, 0))
            self.okienko = pygame.transform.smoothscale(pygame.image.load("robot.png"), (200, 200))
            self.rect = self.okienko.get_rect()

    def robot_go(self):
        # szerokosc = [12, 1, ]
        obraz.blit(self.okienko, (200, 400) )
        pygame.display.flip()

pygame.init()
display = pygame.display.set_mode(rozmiar_grafiki)
pygame.display.set_caption("shift-puzzle")
display.blit (obraz, (0, 0))
pygame.display.flip()

def zamiana_pozycji (k, r) :
    global pusty_k, pusty_r
    display.blit(
        kafelki[stan[(k, r)]],
        (pusty_k*szerokosc_kafelka, pusty_r*wysokosc_kafelka))
    display.blit(
        kafelki[pusty_kafelek],
        (k*szerokosc_kafelka, r*wysokosc_kafelka))
    stan[(pusty_k, pusty_r)] = stan[(k, r)]
    stan[(k, r)] = pusty_kafelek
    (pusty_k, pusty_r) = (k, r)
    pygame.display.flip()

def tasowanie() :
    global pusty_k, pusty_r
    ostatni_r = 0
    for i in range(75):
        pygame.time.delay(50)
        while True:
            r = random.randint(1, 4)
            if (ostatni_r + r == 5):
                continue
            if r == 1 and (pusty_k > 0):
                zamiana_pozycji(pusty_k - 1, pusty_r)
            elif r == 4 and (pusty_k < kolumny - 1):
                zamiana_pozycji(pusty_k + 1, pusty_r)
            elif r == 2 and (pusty_r > 0):
                zamiana_pozycji(pusty_k, pusty_r - 1)
            elif r == 3 and (pusty_r < rzedy - 1):
                zamiana_pozycji(pusty_k, pusty_r + 1)
            else:
                continue
            ostatni_r = r
            break
