# ism = input('Ismni kiriting = ')
# fam = input('Familiya_kiriting = ')
# yosh = input('Yoshni kiriting = ')
# print('Salom',ism,fam,'Siz',yosh,'yoshdasiz')

#//////////////////////////

# raqam = int(input('Raqamni kiriting = '))
#
# print('Siz kiritgan raqam',raqam)

#////////////////////////////
# nmetro = {"Ленинская": ["Заельцовская", "Гагаринская", "Красный проспект", "Площадь Ленина", "Октябрьская",
#                         "Речной Вокзал", "Студенческая", "Площадь Маркса"],
#           "Дзержинская": ["Площадь Гарина-Михайловского", "Сибирская", "Маршала Покрышкина", "Березовая Роща",
#                           "Золотая Нива"]}
#
# station = input('Введите название текущей станции: ')
# route = input('Выберите направление движения \
# #(1 - с севера на юг или с запада на восток, \
# #2 - с юга на север или с востока на запад): ')
#
# for k, v in nmetro.items():
#     if not station in v:
#         print('Такой станции нет')
#     else:
#         idx = v.index(station)
#         if route == '1':
#             print(nmetro[k][idx + 1])
#         elif route == '2':
#             print(nmetro[k][idx - 1])