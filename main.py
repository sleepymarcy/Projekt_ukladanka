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