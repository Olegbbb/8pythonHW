import controller
import os
import view

main_class_list = []
help_dict = {}
jornal = {}
pupil = ''
subject = ''


def exit_program():
    print('Завершение программы.')
    exit()


def start():
    global main_class_list
    controller.input_handler()


def read_file_in_list(some_string: str):
    if os.path.exists(some_string):
        with open(some_string, 'r', encoding='UTF-8') as data:
            if os.path.exists(some_string):
                class_list = data.readlines()
                return class_list
    else:
        print('Такого класса нет')
        controller.input_handler()


def transformation_in_dict(some_list: list):
    global main_class_list
    my_dict = {}
    for i in range(len(some_list)):
        some_list[i] = some_list[i].strip()
        my_dict[some_list[i].split('|')[0]] = some_list[i].split('|')[1]
        main_class_list.append(my_dict)
        my_dict = {}


def subjects(subj_string) -> dict:
    global help_dict
    global main_class_list
    global subject
    for i in main_class_list:
        for subject in i:
            if subj_string in subject:
                help_dict = i
                print(f'Вы выбрали предмет "{subject}"')
                return help_dict
    print('Такого предмета нет')
    return False


def show_all_pupils(some_dict: dict):
    global jornal
    for i in some_dict.values():
        for j in i.split(';'):
            if j != '':
                jornal[j.split(':')[0]] = list(map(int, j.split(':')[1].split(',')))             
        return jornal


def get_pupil(mypupil: str):
    global jornal
    global pupil
    for i in jornal:
        if mypupil in i:
            pupil = i
            print(f'У доски: "{i}"')
            return i
    print('Такого ученика нет')
    return False


def add_mark(mark: int):
    global jornal
    global pupil
    jornal[pupil].append(mark)


def exit_program():
    global jornal
    string = ''
    new_info = []
    for k, v in jornal.items():
        string += k + ':' +str(v).replace('[','').replace(']', '').replace(' ','') + ';'
    with open(view.cl, 'r', encoding='UTF-8') as data:
        file = data.readlines()
        for i in file:
            if subject in i:
                new_info.append(f'{subject}|{string}\n')
            else: new_info.append(i)
    with open(view.cl, 'w', encoding='UTF-8') as data:
        data.writelines(new_info)