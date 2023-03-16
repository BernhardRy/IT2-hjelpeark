import pygame as pg
from random import randint

class Hinder:
    def __init__(self) -> None:
        self._hoyde = randint(20, 100)
        self._bredde = 20
        self._x = 300
        self._y = 500 - self._hoyde

    def tegn(self, vindu):
        pg.draw.rect(vindu, (180, 40, 70), (self._x, self._y, self._bredde, self._hoyde))

    def flytt_venstre(self):
        self._x -= 1
        