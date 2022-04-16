# # my_set = {'bishkek','osh','bishkek'}
#
# # my_list = ['bishkek','osh','bishkek']
#
# # my_tuple = ('osh',100,True,'false') # можно и без скобки
# # print(my_tuple)
#
#
# # capital_slovar = {
# #     'Russia': 'Moskow',
# #     'Kyrgyzstan': 'Bishkek',
# #     'France': 'Paris'
# # }
#
#
# # try:
# #     number1 = int(input('введите первое число: '))
# #     number2 = int(input('введите второе число: '))
# #     summ = number1 + number2
# #     print(summ)
# # except:
# #     print('введите число пожалуйста...')
# #     number1 = int(input('введите первое число: '))
# #     number2 = int(input('введите второе число: '))
# #     summ = number1 + number2
# #     print(summ)
# # else:
# #     summ = number1 + number2
# #     print(summ)
#
# # a = int(input('15'))
# # a = 15
# # b = '15'
# # print(a + b)
#
# months = {
#     1: 'январь',
#     2: 'февраль',
#     3: 'март',
#     4: 'апрель',
#     5: 'май',
#     6: 'июнь',
#     7: 'июль',
#     8: 'август',
#     9: 'сентябрь',
#     10: 'октябрь',
#     11: 'ноябрь',
#     12: 'декабрь',
# }
# try:
#     date = int(input('введите порядок месяца: '))
#     print(months[date])
#     if date > 12:
#         print('у нас есть только 12 месяцев')
# except:
#     print('найдена ошибка... ')
#     date = int(input('введите порядок месяца: '))
#     print(months[date])
#
# # сделать и если что попросить извинений
# # try:
# #     print(months[date])
# # except KeyError:
# #     print('net takogo month number')
#
# # # попросить разрешение
# # if date <=12 and date > 0:
# #     print(months[date])
# # else:
# #     print('net takogo')

def elem(lion,tiger):
    if lion>tiger:
        print(lion)

    else:
        print(tiger)

