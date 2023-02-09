import model
import view


def input_handler():
    model.transformation_in_dict(model.read_file_in_list(view.main_menu()))
    model.subjects(view.enter_subject())
    while len(model.help_dict) == 0:
        model.subjects(view.enter_subject())
    view.show_pupils(model.show_all_pupils(model.help_dict))
    while view.choise_program() == '1':
        while model.get_pupil(view.get_pupil()) == False:
            model.get_pupil(view.get_pupil())
        model.add_mark(view.which_mark())
        view.show_pupils(model.jornal)

    model.exit_program()
