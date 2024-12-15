#Задача "Записать и запомнить":
# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи, strings - список строк для записи.
# Функция должна:
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
# Пример полученного словаря:
# {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
# Где:
# 1, 2 - номера записанных строк.
# 0, 16 - номера байт, на которых началась запись строк.
# 'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.
def custom_write(file_name, strings):
    strings_positions = dict() #создаем словарь
    file = open(file_name, 'w', encoding='utf-8')    # определяем начальные значения
    str_num = 0
    str_start_byte = file.seek(0)  # байт начала первой строки
    for string_ in strings:
        file.write(string_ + '\n')
        str_num += 1
        key = (str_num, str_start_byte)  # задаём ключи словаря
        strings_positions[key] = string_  # добавляем значения в словарь
        str_start_byte = file.tell()
    file.close()
    return strings_positions

file_name = 'newfile.txt'  # задаём имя нашего файла

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)