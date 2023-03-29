list_sets: list[set] = []

help_message: str = """
`1` - Создать подмножество
`2` - Удалить подмножество
`3` - Посмотреть содержимое существующих подмножеств
`4` - Добавить элементы в подмножество
`5` - Удалить элементы из множества
`6` - Добавить элементы из второго множества в первое
`7` - Удалить элементы из второго множества в первом
`help` - Вывести это сообщение
`exit` - Выйти из программы"""


def add(set_elements: set, element):
    """Метод добавления элемента во множество"""
    set_elements.add(element)


def add_elements(set_elements: set, *elements):
    """Метод добавления нескольких элементов во множество"""
    for element in elements:
        if isinstance(element, set):
            for set_element in element:
                add(set_elements, set_element)
        else:
            add(set_elements, element)


def add_set(set_elements: set, elements: set):
    """Метод добавления элементов во множество, содержащиеся в другом множестве"""
    set_elements.update(elements)


def remove(set_elements: set, element):
    """Метод удаления элемента из множества"""
    if element in set_elements:
        set_elements.remove(element)


def remove_elements(set_elements: set, *elements):
    """Метод удаления нескольких элементов из множества"""
    for element in elements:
        if isinstance(element, set):
            for set_element in element:
                remove(set_elements, set_element)
        else:
            remove(set_elements, element)


def remove_set(set_elements: set, elements: set) -> set:
    """Метод удаления элементов из множества, содержащихся в другом множестве"""
    return set_elements.difference(elements)


def print_set(set_elements: set, comment: str = ''):
    """Метод вывода множества"""
    print(comment + '{ ', end='')
    print(', '.join(str(s) for s in set_elements), end=' ')
    print('}')


def tests():
    # Создаем множество чисел
    set_numbers = set()
    # Добавляем туда значения
    add_elements(set_numbers, 1, 2, 3, 4, 5, 6, 7, 8)
    # Выводим значения множества
    print_set(set_numbers, 'Первое подмножество:\t')

    # Удалим оттуда цифру '5'
    remove(set_numbers, 5)
    # Выводим значения множества
    print_set(set_numbers, 'Первое подмножество после удаления числа 5:\t')

    # Создадим второе подмножество
    set_numbers_2 = {1, 5, 7, 8}
    # Выводим значения второго множества
    print()
    print_set(set_numbers_2, 'Второе подмножество:\t')
    # Удалим из первого подмножества элементы второго
    set_numbers = remove_set(set_numbers, set_numbers_2)
    # Выводим значения множества
    print_set(
        set_numbers,
        'Первое подмножество после удаления элементов из второго подмножества:\t'
    )

    # Создадим третье подмножество
    set_numbers_3 = {1, 7, 8, 9, 10, 11}
    # Выводим значения третьего множества
    print()
    print_set(set_numbers_3, 'Третье подмножество:\t')
    # Добавим значения третьего подмножества в первое
    add_set(set_numbers, set_numbers_3)
    # Выводим значения множества
    print_set(
        set_numbers,
        'Первое подмножество после добавления элементов из третьего подмножества:\t'
    )


def get_elements(prefix: str = '') -> set | None:
    func_command: str = input(f'{prefix} Введите элементы черех пробел: ')
    func_command.strip()
    if func_command == '':
        return None
    return_set = set()
    for i in func_command.split():
        if i.isdigit():
            return_set.add(int(i))
        else:
            return_set.add(i)
    return return_set


def add_elements_in_set():
    while True:
        func_set = select_set('[add]')
        if func_set is None:
            return
        set_elements: set | None = get_elements('[add]')
        if set_elements is None:
            continue
        add_elements(func_set, set_elements)
        print('Элементы успешно добавлены')


def remove_elements_in_set():
    while True:
        func_set = select_set('[remove]')
        if func_set is None:
            return
        set_elements: set | None = get_elements('[remove]')
        if set_elements is None:
            continue
        remove_elements(func_set, set_elements)
        print('Элементы успешно удалены')


def extend_set():
    while True:
        func_set1 = select_set(
            '[extend(Подмножество, в которое добавятся элементы)]')
        if func_set1 is None:
            return
        func_set2 = select_set(
            '[extend(Подмножество, из которого возьмутся элементы)]')
        if func_set2 is None:
            return
        add_set(func_set1, func_set2)
        print('Элементы из второго множества успешно добавлено в первое')


def substract_set():
    while True:
        func_set1 = select_set(
            '[substract(Подмножество, из которого удалятся элементы)]')
        if func_set1 is None:
            return
        func_set2 = select_set(
            '[extend(Подмножество, из которого возьмутся элементы)]')
        if func_set2 is None:
            return
        func_set1 = remove_set(func_set1, func_set2)
        print('Элементы из второго множества успешно удалены в первом')


def select_set(prefix: str = '') -> set | None:
    len_sets = len(list_sets)
    if len_sets == 0:
        print('Подмножества отсутствуют')
        return None

    print('Существующие подмножества:', end=' ')
    for i in range(len_sets):
        print(i+1, end=' ')
    while True:
        func_command: str = input(
            f'\n{prefix} Введите число множества либо введите `back` для возврата в меню: '
        )
        if func_command == 'back':
            return None
        elif not func_command.isdigit():
            print('Введеная команда не является числом')
            continue
        number = int(func_command)
        if not 0 < number <= len_sets:
            print('Нет такого номера подмножества')
        else:
            return list_sets[number-1]


def show_sets():
    while True:
        func_set = select_set('[show]')
        if func_set is None:
            return
        print_set(func_set)


def delete_set():
    print("""
    Внимание, при удалении любого подмножества посередине, остальные смещаются влево
    Например: Множества 1,2,3 вы удалили 2, остались подмножества 1,2""")
    while True:
        func_set = select_set('[delete]')
        if func_set is None:
            return
        list_sets.remove(func_set)
        print('Множество успешно удалено')


if __name__ == '__main__':
    tests()

    print(help_message)
    while True:
        command = input('\nВвод: ')
        match command:
            case '1':
                list_sets.append(set())
                print(
                    f'Было успешно создано подмножество под номером {len(list_sets)}')
            case '2':
                delete_set()
            case '3':
                show_sets()
            case '4':
                add_elements_in_set()
            case '5':
                remove_elements_in_set()
            case '6':
                extend_set()
            case '7':
                substract_set()
            case 'exit':
                break
            case 'help':
                print(help_message)
            case _:
                print('Неизвестная команда, `help` - помощь, `exit` - выход')
