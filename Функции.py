# from random import randint
#
# def amallar():
#     menu()
#
#     tanlov = int(input('amalni tanlang = '))
#     umumiy_javoblar = []
#     while tanlov!= 6:
#         if tanlov == 1:
#             javob = qoshish()
#             umumiy_javoblar.append(javob)
#             menu()
#             tanlov = int(input('amalni tanlang = '))
#         elif tanlov == 2:
#             javob = ayirish()
#             umumiy_javoblar.append(javob)
#             menu()
#             tanlov = int(input('amalni tanlang = '))
#         elif tanlov == 3:
#             javob = kopaytirish()
#             umumiy_javoblar.append(javob)
#             menu()
#             tanlov = int(input('amalni tanlang = '))
#         elif tanlov == 4:
#             javob = bolish()
#             umumiy_javoblar.append(javob)
#             menu()
#             tanlov = int(input('amalni tanlang = '))
#         else:
#             tanlov = int(input('Bunday amal turi yoq'))
#     for javoblar in umumiy_javoblar:
#         for javob in javoblar:
#             print(javob)
#
# def menu():
#     print("""__MENU__
#     Qoshish == 1
#     Ayirish == 2
#     Kopaytirish == 3
#     Bolish = 4
#     Natija == 6""")
# def qoshish():
#     javoblar = []
#     for i in range(1,6):
#         son1 = randint(1, 100)
#         son2 = randint(1, 100)
#         print(son1, '+', son2, '=', end='')
#         yigindi = son1 + son2
#         javob = int(input())
#         if javob == yigindi:
#             s = f'{son1} + {son2} = {yigindi} ✅'
#             javoblar.append(s)
#         else:
#             s = f'{son1} + {son2} = {javob} 👎 {yigindi} ✅'
#             javoblar.append(s)
#     return javoblar
#
# def ayirish():
#     javoblar = []
#     for i in range(1, 6):
#         son1 = randint(1, 100)
#         son2 = randint(1, 100)
#         print(son1, '-', son2, '=', end='')
#         yigindi = son1 - son2
#         javob = int(input())
#         if javob == yigindi:
#             s = f'{son1} - {son2} = {yigindi} ✅'
#             javoblar.append(s)
#         else:
#             s = f'{son1} - {son2} = {javob} 👎 {yigindi} ✅'
#             javoblar.append(s)
#     return javoblar
# def kopaytirish():
#     javoblar = []
#     for i in range(1, 6):
#         son1 = randint(1, 10)
#         son2 = randint(1, 10)
#         print(son1, '*', son2, '=', end='')
#         yigindi = son1 * son2
#         javob = int(input())
#         if javob == yigindi:
#             s = f'{son1} * {son2} = {yigindi} ✅'
#             javoblar.append(s)
#         else:
#             s = f'{son1} * {son2} = {javob} 👎 {yigindi} ✅'
#             javoblar.append(s)
#     return javoblar
# def bolish():
#     javoblar = []
#     for i in range(1, 6):
#         son1 = randint(1, 10)
#         son2 = randint(1, 10)
#         print(son1, '/', son2, '=', end='')
#         yigindi = son1 * son2
#         javob = int(input())
#         if javob == yigindi:
#             s = f'{son1} / {son2} = {yigindi} ✅'
#             javoblar.append(s)
#         else:
#             s = f'{son1} / {son2} = {javob} 👎 {yigindi} ✅'
#             javoblar.append(s)
#     return javoblar

# amallar()
# ///////////////////////////
# a = int(input('Son kiriting = '))
# if a % 2 == 0:
#     print('sanaladigan son')
# else:
#     print('sanalmaydigan son')


# //////////////////////////////
matn = input('Matn kiriting')


def matn_uzunligi(matn: str) -> int:
    return len(matn)


print(matn_uzunligi(matn), 'ta harf bor')
