from employee import Employee
from person import Person


class Teacher(Employee, Person):
    def teach(self):
        return 'teaching...'

