from task_15 import main_handler


def main():
    while(True):
        operation = int(input('''\n
What do you want to do with the Product-table?
    1. View content
    2. Add a row
    3. Update field by index
    4. Delete row by index
    0 - exit
: '''))
        if operation == 0:
            break
        else:
            main_handler[operation]()
