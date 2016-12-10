import random
import pygame
from pygame.locals import *

scr_size = (width,height) = (900,600)
FPS = 20
screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)

pygame.display.set_caption('Insertion Sort')

def generatearray(lowerlimit,upperlimit,length):
    arr = []
    for i in range(0,length):
        arr.append(random.randrange(lowerlimit,upperlimit))

    return arr


class sort():
    def __init__(self,arr):
        self.arr = arr
        self.n = len(arr)
        self.i = 2
        self.image = pygame.Surface((width - width/5,height - height/5))
        self.rect = self.image.get_rect()
        self.rect.left = width/10
        self.rect.top = height/10
        self.width_per_bar = self.rect.width / self.n - 2

    def update(self):
        if self.i < self.n:
            self.image.fill(black)
            #################Sorting Algorithm here#############################
            for j in range(self.i,0,-1):
                if self.arr[j] < self.arr[j-1]:
                    self.arr[j],self.arr[j - 1] = self.arr[j - 1],self.arr[j]
            self.i += 1
            ####################################################################
            l = 0
            for k in range(0,self.rect.width,self.width_per_bar + 2):
                bar = pygame.Surface((self.width_per_bar,self.arr[l]))
                bar_rect = bar.get_rect()
                bar.fill(white)
                bar_rect.bottom = self.rect.height
                bar_rect.left = k

                self.image.blit(bar,bar_rect)
                l += 1

        else:
            pass


    def draw(self):
        screen.blit(self.image,self.rect)


def main():
    arr = generatearray(1,height - height/5 - 10,240)
    insertion_sort = sort(arr)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.KEYUP:
                pass
        insertion_sort.update()
        screen.fill(black)
        print insertion_sort.arr
        insertion_sort.draw()
        pygame.display.update()
        clock.tick(FPS)

main()
