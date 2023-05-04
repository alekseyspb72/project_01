# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number):
    d_alpha = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    dig = list(range(10))
    dict_m = dict(zip(dig,d_alpha))
    print(dict_m[number])


try:
    switch_it_up(int(input()))
except KeyError:
    print('None')
