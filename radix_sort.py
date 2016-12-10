import random
import pygame
from pygame.locals import *

scr_size = (width,height) = (900,600)
FPS = 40
screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)

pygame.display.set_caption('Radix Sort')

def generatearray(lowerlimit,upperlimit,length):
    arr = []
    for i in range(0,length):
        arr.append(random.randrange(lowerlimit,upperlimit))

    return arr

def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)

    count = [0] * (10)

    for i in range(0, n):
        index = (arr[i]/exp1)
        count[ (index)%10 ] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    i = n-1
    while i>=0:
        index = (arr[i]/exp1)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1

    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]
        displayarray(arr)

def radixSort(arr):

    max1 = max(arr)
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10

def displayarray(arr):
    image = pygame.Surface((width - width/5,height - height/5))
    rect = image.get_rect()
    rect.top = height/10
    rect.left =  width/10
    width_per_bar = rect.width/len(arr) - 2

    l = 0
    for k in range(0,rect.width,width_per_bar + 2):
        bar = pygame.Surface((width_per_bar,arr[l]))
        bar_rect = bar.get_rect()
        bar.fill(white)
        bar_rect.bottom = rect.height
        bar_rect.left = k

        image.blit(bar,bar_rect)
        l += 1


    screen.fill(black)
    screen.blit(image,rect)
    pygame.display.update()
    clock.tick(FPS)

def main():
    arr = generatearray(1,height - height/5 - 10,240)
    temparr = [0]*len(arr)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.KEYUP:
                pass

        if sorted(arr) != arr:
            radixSort(arr)
        else:
            displayarray(arr)

main()
