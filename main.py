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