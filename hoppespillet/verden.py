import pygame as pg
from spiller import Spiller
from hinder import Hinder
import time

spiller1 = Spiller()
hindere = []

for i in range(3):
    nytt_hinder = Hinder()
    hindere.append(nytt_hinder)

pg.init()
clock = pg.time.Clock()

VINDU_BREDDE = 500
VINDU_HOYDE = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

y = 0
fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    vindu.fill((255, 255, 255)) # farge (rgb)

    for hinder in hindere:
        hinder.flytt_venstre()
        hinder.tegn(vindu)
    spiller1.tegn(vindu, y)
    # pg.draw.rect(vindu, (r,g,b), (x,y,bredde,hoyde))
    
    # if event.type == pg.KEYDOWN:
    #     if event.key==pg.K_SPACE:
    #         y -= 0.1
    #         print("hei")

    keys = pg.key.get_pressed()
    tast = False

    if keys[pg.K_UP]:
        tast = True
        while tast:
            if event.type == pg.KEYUP:
                print("hei")
                tast = False
                
    # if keys[pg.K_LEFT]:
    #     player_x -= 300 * dt
    # if keys[pg.K_RIGHT]:
    #     player_x += 300 * dt

    pg.display.flip() # Oppdaterer pygame-vinduet - denne må være med

    dt = clock.tick(60)
    dt

pg.quit()
print("ferdig")