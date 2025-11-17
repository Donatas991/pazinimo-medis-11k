# nesuprantau starto laustiniu skliausteliu vertes pagrindiniu

from random import*

n = int(input("kiek krepsinio zaideju? n="))

a = [randint(170,215) for a in range(n)] #randint funkcija gražina random (atsitiktinį) int (skaičių) rėžyje nuo 170 iki 215
print("krepsininku ugiai ", a)
# neprisimenu akmens sortinimo metodo
# for i in range(n-1):
#     if rik

# burbulo metodas
for i in range(n-1):
    for j in range(n-2, i-1, -1):
        if a[j] > a[j+1]:
            a[j], a[j+1] =  a[j+1], a[j]

#akmens metodas
for i in range(n-1, -1, -1):
    for j in range(i):
        if a[j] > a[j+1]:
            a[j], a[j+1] =  a[j+1], a[j]
            print("apsikeite", a[j], a[j+1])

#MK užbaik kodą ir išsiaiškink, kuo skiriasi burbulo ir akmens metodai

