"""Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
это порядковый номер строки в списке. Использовать генератор списков."""

str_list = ['sdfg jk jh', 'qwe 5r', 'sdf']
str_list = [f'{ind} - {st}' for ind, st in enumerate(str_list)]
print(str_list)
