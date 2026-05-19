# Псевдокод:
# - посмотреть список задач
# - добавить задачу
# - удалить задачу
import json

with open('my.json', 'r', encoding='utf-8') as file:
    tasks = json.load(file)

menu = """
    1. Посмотреть список задач.
    2. Добавить задачу.
    3. Удалить задачу.
    4. Выход.
"""


def save_tasks():
    with open('my.json', 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=3, ensure_ascii=False)


def show_tasks():
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


def add_task():
    added_task = input('Введи свою задачу. ')
    tasks.append(added_task)
    save_tasks()


def delete_task():
    show_tasks()
    del_input = int(input('Какую задачу ты хочешь удалить? '))
    del_input = del_input - 1
    tasks.pop(del_input)
    save_tasks()


def show_menu():
    while True:
        print(menu)
        try:
            user_input = int(input('Введи пункт меню. '))
            if user_input == 1:
                if len(tasks) == 0:
                    print('Список задач пуст...')
                else:
                    show_tasks()
            elif user_input == 2:
                add_task()
                print('Задача добавлена. Можешь найти ее в списке задач')
            elif user_input == 3:
                delete_task()
            elif user_input == 4:
                save_tasks()
                return
            else:
                print('Такого пункта в меню нет')
        except ValueError:
            print('Введите число, а не текст')


show_menu()
