import sys, pygame
from ship import *
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()

# set the width and height to the size of the screen
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 0, 0)
screen.fill(color)

player = Ship((20, height // 2))
numLevels = 4
level = 1
asteroidCount = 3


def main():
    global level

    # game loop
    while level <= numLevels:
        clock.tick(144)

        # event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    player.speed = (1, 0)
                if event.key == K_LEFT:
                    player.speed = (-1, 0)
                if event.key == K_UP:
                    player.speed =(0, -1)
                if event.key == K_DOWN:
                    player.speed = (0, 1)




        # update screen
        player.update()
        screen.fill(color)
        screen.blit(player.image, player.rect)
        pygame.display.flip()




if __name__ == "__main__":
    main()