from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def __find_horse(self, horse_type):
        found_horse = [h for h in self.horses if type(h).__name__ == horse_type]
        try:
            found_horse = found_horse[-1]
        except IndexError:
            found_horse = None
        # found_horse = next(filter(lambda x: (type(x).__name__ == horse_type and not x.is_taken),
        #                           reversed(self.horses)), None)
        if not found_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        return found_horse

    def __find_jockey(self, jockey_name):
        found_jockey = [j for j in self.jockeys if j.name == jockey_name]
        try:
            found_jockey = found_jockey[0]
        except IndexError:
            found_jockey = None
        # found_jockey = next(filter(lambda x: x.name == jockey_name, self.jockeys), None)
        if not found_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        return found_jockey

    def __find_horse_race(self, race_type):
        found_race = [r for r in self.horse_races if r.race_type == race_type]
        try:
            found_race = found_race[0]
        except IndexError:
            found_race = None
        # found_race = next(filter(lambda x: x.race_type == race_type, self.horse_races), None)
        if not found_race:
            raise Exception(f"Race {race_type} could not be found!")
        return found_race

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in ('Appaloosa', 'Thoroughbred'):
            return
        if horse_name in [horse.name for horse in self.horses]:
            raise Exception(f'Horse {horse_name} has been already added!')

        if horse_type == 'Appaloosa':
            self.horses.append(Appaloosa(horse_name, horse_speed))
        elif horse_type == 'Thoroughbred':
            self.horses.append(Thoroughbred(horse_name, horse_speed))

        return f'{horse_type} horse {horse_name} is added.'

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [jockey.name for jockey in self.jockeys]:
            raise Exception(f'Jockey {jockey_name} has been already added!')
        self.jockeys.append(Jockey(jockey_name, age))
        return f'Jockey {jockey_name} is added.'

    def create_horse_race(self, race_type: str):
        if race_type in [horse_race.race_type for horse_race in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")
        self.horse_races.append(HorseRace(race_type))
        return f'Race {race_type} is created.'

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):

        jockey = self.__find_jockey(jockey_name)
        horse = self.__find_horse(horse_type)

        if jockey.horse:
            return f'Jockey {jockey_name} already has a horse.'

        jockey.horse = horse
        horse.is_taken = True
        return f'Jockey {jockey_name} will ride the horse {horse.name}.'

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):

        jockey = self.__find_jockey(jockey_name)
        race = self.__find_horse_race(race_type)

        if not jockey.horse:
            raise Exception(f'Jockey {jockey_name} cannot race without a horse!')

        if jockey in race.jockeys:
            return f'Jockey {jockey_name} has been already added to the {race_type} race.'

        race.jockeys.append(jockey)
        return f'Jockey {jockey_name} added to the {race_type} race.'

    def start_horse_race(self, race_type: str):

        race = self.__find_horse_race(race_type)

        if len(race.jockeys) < 2:
            raise Exception(f'Horse race {race_type} needs at least two participants!')

        winner = {'name': '', 'speed': 0, 'horse_name': ''}
        for jockey in race.jockeys:
            if jockey.horse.speed >= winner['speed']:
                winner['name'] = jockey.name
                winner['speed'] = jockey.horse.speed
                winner['horse_name'] = jockey.horse.name

        return f'The winner of the {race_type} race, with a speed of {winner["speed"]}km/h is ' \
               f'{winner["name"]}! Winner\'s horse: {winner["horse_name"]}.'
