# # massyvo gretimu elementu sukeitimas vietomis
# from random input randint
# n = int(input('Kiek elementu turi masyvas? n ='))
# a = [radiant(-40, 40)for i in range(n)]
# print(a)
# for i in range(0, n - 1,2):
#     a[i], a[i+1] = a[i+1], a[i]
# print(a)

# while i<n-1
#     a[1], a[i+1] = a[i+1], a[i]
#     i+=2

from random import randint
n = int(input('Kiek žaidėjų komandoje? '))
a = [randint(170, 210) for i in range(n)]
print('Pradinis žaidėjų ūgių masyvas:', a)
for i in range(n - 1):
    pakeista = False
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            pakeista = True
    if not pakeista:
        break

print('Surikiuotas masyvas (ūgiai didėjimo tvarka):', a)
skirtumas = a[-1] - a[0]
print('Skirtumas tarp aukščiausio ir žemiausio žaidėjo ūgių:', skirtumas, 'cm')

# from random import randint


# n = int(input("Kiek elementų turi masyvas? "))
# a = [randint(1, 50) for i in range(n)]

# print("Pradinis masyvas:", a)
# for i in range(n - 1):
#     keitimas = False
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             keitimas = True
#     if not keitimas:
#         break

# print("Surikiuotas masyvas:", a)