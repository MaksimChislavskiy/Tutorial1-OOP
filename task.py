# Менеджер задач
#
# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self, task_description, due_date, status=False):
        self.task_description = task_description
        self.due_date = due_date
        self.status = status

    def __repr__(self):
        return f'{self.task_description}, {self.due_date}'

tasks = []

def add_task(task_description, due_date):
    tasks.append(Task(task_description, due_date))
    print(f'Добавлена задача: {task_description}, Срок: {due_date}')

def task_completion(task_description):
    for task in tasks:
        if task.task_description == task_description:
            task.status = True
    print(f'Задача {task_description} выполнена.')

def info():
    current = []
    all_competed = True
    for task in tasks:
        if not task.status:
            current.append(task)
            all_competed = False

    if all_competed:
        print('Все задачи выполнены')
    else:
        print(f'Не выполненные задачи: {current}')


# Пример использования
if __name__ == "__main__":
    add_task('Позвонить маме', '22.05.2025')
    add_task('Купить хлеб', '20.05.2025')

    info()

    task_completion('Купить хлеб')

    info()