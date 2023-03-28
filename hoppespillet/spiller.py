import pygame as pg

class Spiller:
    def __init__(self) -> None:
        self._x = 20
        self._y = 450
        
    def tegn(self, vindu, y):
        pg.draw.circle(vindu, (100,50,140), (self._x,self._y + y), 25)
        # pg.draw.circle(vindu, (r,g,b), (x,y), radius)
        return