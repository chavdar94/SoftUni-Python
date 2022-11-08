from task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'
        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):
        try:
            task = next(filter(lambda x: x.username == task_name, self.tasks))
        except StopIteration:
            return f'Could not find task with the name {task_name}'

        task.completed = True
        return f'Completed task {task_name}'

    def clean_section(self):
        count = 0
        for pos, tasks in enumerate(self.tasks):
            if tasks.completed:
                count += 1
                self.tasks.remove(tasks)
        return f"Cleared {count} tasks."

    def view_section(self):
        result = [f'Section {self.name}:']
        for tsk in self.tasks:
            result.append(f'{tsk.details()}')
        return '\n'.join(result)


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
