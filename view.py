cl = ''
def main_menu() -> str:
    global cl
    cl = input('Введите класс: ').upper() + '.txt'
    _ = cl.replace('.txt', '')
    print(f'Вы выбрали "{_}" класс')
    return cl


def no_class():
    print('Такого класса нет')


def enter_subject() -> str:
    subject = input('Введите название предмета: ').lower()
    return subject


def show_pupils(some_dict: dict):
    for k, v in some_dict.items():
        print(f'{k:20}\t{v}')


def get_pupil() -> str:
    pupil = input('Кого вызвать к доске: ').lower()
    return pupil


def which_mark() -> int:
    try:
        mark = int(input('Введите оценку: '))
        while mark < 1 or mark > 5:
            mark = int(input('Введите корректную оценку: '))
    except ValueError:
        mark = int(input('Введите число: '))
    return mark


def choise_program():
    inp = input('Вызвать ученика: введите 1, для выхода введите любую клавишу: ')
    return inp
