import random
import pygame
from pygame.locals import *

scr_size = (width,height) = (900,600)
FPS = 40
screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)

pygame.display.set_caption('Merge Sort')

def generatearray(lowerlimit,upperlimit,length):
    arr = []
    for i in range(0,length):
        arr.append(random.randrange(lowerlimit,upperlimit))

    return arr

def mergesort(arr,temparr,left,right):
    if left < right:
        mid = int((left + right)/2)
        mergesort(arr,temparr,left,mid)
        mergesort(arr,temparr,mid+1,right)
        merge(arr,temparr,left,mid + 1,right)

    else:
        pass

def merge(arr,temp,left,mid,right):
    left_end = mid - 1
    temp_pos = left
    size = right - left + 1

    while left <= left_end and mid<=right:
        if arr[left] <= arr[mid]:
            temp[temp_pos] = arr[left]
            temp_pos = temp_pos + 1
            left = left + 1
        else:
            temp[temp_pos] = arr[mid]
            temp_pos = temp_pos + 1
            mid = mid + 1

    while left<=left_end:
        temp[temp_pos] = arr[left]
        left = left + 1
        temp_pos = temp_pos + 1

    while mid <= right:
        temp[temp_pos] = arr[mid]
        mid = mid + 1
        temp_pos = temp_pos + 1

    for i in range(0,size):
        arr[right] = temp[right]
        right = right - 1
        displayarray(arr)



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
            mergesort(arr,temparr,0,len(arr) - 1)
        else:
            displayarray(arr)

main()
