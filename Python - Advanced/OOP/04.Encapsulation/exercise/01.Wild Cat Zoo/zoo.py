class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price: int):
        if len(self.animals) == self.__animal_capacity:
            return f'Not enough space for animal'
        if price > self.__budget:
            return 'Not enough budget'
        self.animals.append(animal)
        self.__budget -= price
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return 'Not enough space for worker'
        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'

        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_to_pay = sum(x.salary for x in self.workers)

        if self.__budget - total_to_pay >= 0:
            self.__budget -= total_to_pay
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'

        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        total_to_tend = sum(x.money_for_care for x in self.animals)

        if self.__budget - total_to_tend >= 0:
            self.__budget -= total_to_tend
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = {'Lion': [], 'Tiger': [], 'Cheetah': []}

        for animal in self.animals:
            result[animal.__class__.__name__].append(str(animal))

        output_info = [f"You have {len(self.animals)} animals",
                       f"----- {len(result['Lion'])} Lions:", *result['Lion'],
                       f"----- {len(result['Tiger'])} Tigers:", *result['Tiger'],
                       f"----- {len(result['Cheetah'])} Cheetahs:", *result['Cheetah']]

        return '\n'.join(output_info)

    def workers_status(self):
        result = {'Keeper': [], 'Caretaker': [], 'Vet': []}

        for worker in self.workers:
            result[worker.__class__.__name__].append(str(worker))

        output_info = [f"You have {len(self.workers)} workers",
                       f"----- {len(result['Keeper'])} Keepers:", *result['Keeper'],
                       f"----- {len(result['Caretaker'])} Caretakers:", *result['Caretaker'],
                       f"----- {len(result['Vet'])} Vets:", *result['Vet']]

        return '\n'.join(output_info)
