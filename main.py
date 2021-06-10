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

#Faustyna: ROBOT-PRZESZKADZACZ
class Robocik(pygame.sprite.Sprite):

    def __init__(self):
            super(Robocik, self).__init__()
            self.start = 0
            self.okienko = pygame.Surface((200, 200))
            self.okienko.fill((0, 0, 0))
            self.okienko = pygame.transform.smoothscale(pygame.image.load("C:/Marcy/Dev/Repo/projekcik/Projekt_ukladanka/robot.png"), (200, 200))
            self.rect = self.okienko.get_rect()

    def robot_go(self, szerokosc_robota, wysokosc_robota):
        obraz.blit(self.okienko, (szerokosc_robota, wysokosc_robota) )
        pygame.display.flip()


pygame.init()
display = pygame.display.set_mode(rozmiar_grafiki)
pygame.display.set_caption("Morskie puzzlowanie")
display.blit (obraz, (0, 0))
pygame.display.flip()

robot = Robocik()

lista_szerokosci = [1, 200, 400]
lista_dlugosci = [1, 200, 400]


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

na_start = True
pokazanie_rozwiazania = False
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN :
        if na_start:
            tasowanie()
            na_start = False
        elif event.dict['button'] == 1:
            pozycja_myszki = pygame.mouse.get_pos()
            k = pozycja_myszki[0] // szerokosc_kafelka
            r = pozycja_myszki[1] // wysokosc_kafelka
            if ((abs(k - pusty_k) == 1 and r == pusty_r) or
                    (abs(r - pusty_r) == 1 and k == pusty_k)):
                zamiana_pozycji (k, r)
        elif event.dict['button'] == 3:
            zapisany_obraz = display.copy()
            display.blit(obraz, (0, 0))
            pygame.display.flip()

            pygame.time.wait(1000)
            szerokosc_robota = random.choice(lista_szerokosci)
            wysokosc_robota = random.choice(lista_dlugosci)
            robot.robot_go(szerokosc_robota, wysokosc_robota)

            pokazanie_rozwiazania = True
    elif pokazanie_rozwiazania and (event.type == pygame.MOUSEBUTTONUP):
        display.blit (zapisany_obraz, (0, 0))
        pygame.display.flip()
        pokazanie_rozwiazania = False
