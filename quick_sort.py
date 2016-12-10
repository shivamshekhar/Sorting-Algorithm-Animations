import random
import pygame
from pygame.locals import *

scr_size = (width,height) = (900,600)
FPS = 40
screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)

pygame.display.set_caption('Quick Sort')

def generatearray(lowerlimit,upperlimit,length):
    arr = []
    for i in range(0,length):
        arr.append(random.randrange(lowerlimit,upperlimit))

    return arr

def partition(arr,low,high):
    i = low-1
    pivot = arr[high]
    for j in range(low , high):
        if   arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
            displayarray(arr)
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quicksort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)



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
            quicksort(arr,0,len(arr) - 1)
        else:
            displayarray(arr)

main()
