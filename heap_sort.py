import random
import pygame
from pygame.locals import *

scr_size = (width,height) = (900,600)
FPS = 80
screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)

pygame.display.set_caption('Heap Sort')

def generatearray(lowerlimit,upperlimit,length):
    arr = []
    for i in range(0,length):
        arr.append(2*i)

        #arr.append(random.randrange(lowerlimit,upperlimit))

    random.shuffle(arr)
    return arr
#    arr = []
#    for i in range(0,length):
#        arr.append(random.randrange(lowerlimit,upperlimit))
#
#    return arr

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]

        heapify(arr, n, largest)
    displayarray(arr)

def heapSort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

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
            heapSort(arr)
        else:
            displayarray(arr)

main()
