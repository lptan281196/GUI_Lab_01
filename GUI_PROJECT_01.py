#GUI_PROJECT_01
import itertools
import pygame as pg


pg.init()
pg.font.init()

BLACK = pg.Color('black')
WHITE = pg.Color('white')

screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

colors = itertools.cycle((WHITE))
tile_size = 40
width, height = 8*tile_size, 8*tile_size
background = pg.Surface((width, height))

pg.display.set_caption('GUI_PROJECT_01')
    
#circle = (0,GREY,0,,tile_size,tile_size)
for y in range(0, height, tile_size):
    for x in range(0, width, tile_size):
        rect = (x, y, tile_size, tile_size)
        pg.draw.rect(background, next(colors), rect)
        pg.draw.circle(background,WHITE,[40,40],tile_size)
        pg.draw.circle(background,pg.Color('red'),[7*40,7*40],tile_size)
    next(colors)

game_exit = False
while not game_exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_exit = True

    screen.fill((60, 70, 90))
    screen.blit(background, (100, 100))

    pg.display.flip()
    clock.tick(30)

pg.quit()
