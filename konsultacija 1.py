# # 1. Duomenų tipai

# x = 5 #tai yra skaičius integer
# # print(x * 5)

# a = '5' #tai yra simbolis string
# # print(a * 5)

# x ir a skirtingi duomenų tipai. Paleisk programą. a yra simbolis o x yra skaicius
# parašyk: kuo skiriasi išvestis? kodėl taip yra? x*5 bus 25 o a * 5= 55555 nes kai skaiciu su skaicium sudaugina kai simbolis ju tiesiog padaro 5 kartus daugiau
# atsakymas: 

# # užkomenduok viršuj esantį kodą ir atkomentuok žemiau esantį kodą
# # -----------------------------------------------------------------
# # 2. Duomenų tipų keitimas

# b = int(a) #naujas kintamasis
# print(b * 5)
# # kokį atsakymą gavai? koks b duomenų tipas? 
# # atsakymas: b tampa integer tai tampa skacium atsakyma gausim 25
# print(a * 5)
# # ar kažkaip pasikeitė a? koks a duomenų tipas? 
# # atsakymas: enpasikeit4 ir string

# z = str(x)
# print(z * 5)
# # kokį atsakymą gavai? koks z duomenų tipas?
# # atsakymas: 55555 z yra string
# print(x * 5)
# # ar kažkaip pasikeitė x? koks a duomenų tipas?
# # atsakymas: nepasikite intreger

# # užkomenduok viršuj esantį kodą ir atkomentuok žemiau esantį kodą
# # -----------------------------------------------------------------
# 3. Duomenų tipų keitimas 2

# q = 0
# # print(type(q))
# # # kokį rezultatą gavai? Ką daro funkcija type()?
# # # atsakymas <class 'int'> pasako koks duomenu tipas yra q

# # q1 = str(q)
# # q2 = float(q)
# # print(q1, type(q1))
# # print(q2, type(q2))
# # # kokį rezultatą gavai?
# # # # atsakymas 0 <class 'str'>    
# # #             0.0 <class 'float'>

# q3 = bool(q) #paversk q į būliu (boolean)

# print(q3, type(q3))

# # užkomenduok viršuj esantį kodą ir atkomentuok žemiau esantį kodą
# # -----------------------------------------------------------------
# 4. Duomenų tipų keitimas 3

# t = True
# f = False

# print(t, f)

# # t1 = #paversk t į skaičių (integer)
# # f1 = #paversk f į skaičių (integer)
# t1=int(t)
# f1=int(f)
# print(t1, f1)

# # užkomenduok viršuj esantį kodą ir atkomentuok žemiau esantį kodą
# # -----------------------------------------------------------------
# # 5. Duomenų tipai ir input() funkcija
ivestis = input("Parašyk man kažką: ")
# paleisk šią programą kelis kartus.
# Vieną kartą įrašyk kokį nors žodį, antrą kartą tik skaičius, trečią kartą ir raides ir žodžius
print(type(ivestis))

# # koks kintamojo ivestis duomenų tipas pirmu, antru ir trečiu atveju?
# # atsakymas:  visais atvejais duomenu tipas yra string, visad input grazins string nebent para6ysi kad automati6kai pajkeitu i kazkoki kita duomenu tipa

# # užkomenduok viršuj esantį kodą ir atkomentuok žemiau esantį kodą
# # -----------------------------------------------------------------
# # 6. Duomenų tipų keitimas 4

zodis = input("Parašyk man žodį: ")
sveikas_skaicius = input("Parašyk man sveiką skaičių: ")
kablelio_skaicius = input("Parašyk man skaičių su kableliu: ")
bulius = input("Įvesk True ar False: ")

# pakeisk kiekvieno kintamojo duomenų tipą, kad atitiktų tai, ko prašo
zodis = str(zodis)
sveikas_skaicius = int(sveikas_skaicius)
kablelio_skaicius = float(kablelio_skaicius)
bulius = bool(bulius)

# čia tavo kodai


print(zodis, type(zodis))
print(sveikas_skaicius, type(sveikas_skaicius))
print(kablelio_skaicius, type(kablelio_skaicius))
print(bulius, type(bulius))