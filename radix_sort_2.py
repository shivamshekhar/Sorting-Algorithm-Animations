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
        arr.append(17*2*i)

        #arr.append(random.randrange(lowerlimit,upperlimit))

    random.shuffle(arr)
    return arr
#    arr = []
#    for i in range(0,length):
#        arr.append(random.randrange(lowerlimit,upperlimit))
#
#    return arr

def calcdigits(n):
    count=0
    while(n!=0):
        count+=1
        n=n/10
    return count

def radixsort(vec):
    tmpvec = list(vec)
    sz = len(vec)
    div = 10
    mx = max(vec)
    n_pass = calcdigits(mx)
    digits = [[],[],[],[],[],[],[],[],[],[]]
    for i in range(0,n_pass):
        for j in range(0,sz):
            digits[tmpvec[j]%10].append(vec[j])

        index=0
        for j in range(0,10):
            while(len(digits[j]) > 0):
                displayarray(vec)
                vec[index] = digits[j].pop(0)
                index+=1
            displayarray(vec)

        for j in range(0,sz):
            tmpvec[j] = vec[j]/div
        div = div*10

    return vec

def displayarray(arr):
    image = pygame.Surface((width - width/5,height - height/5))
    rect = image.get_rect()
    rect.top = height/10
    rect.left =  width/10
    width_per_bar = rect.width/len(arr) - 2

    l = 0
    for k in range(0,rect.width,width_per_bar + 2):
        bar = pygame.Surface((width_per_bar,arr[l]/17))
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
    arr = generatearray(1,(height - height/5 - 10),240)
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
            radixsort(arr)
        else:
            displayarray(arr)

main()
