from project.room import Room


class Hotel:

    def __init__(self, name: str, ):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        for room in self.rooms:
            if room.number == room_number and not room.is_taken:
                room.take_room(people)
                self.guests += people

    def free_room(self, room_number: int):
        for room in self.rooms:
            if room.number == room_number and room.is_taken:
                self.guests -= room.guests
                room.free_room()

    def status(self):
        free_rooms = [str(x.number) for x in self.rooms if not x.is_taken]
        taken_rooms = [str(x.number) for x in self.rooms if x.is_taken]

        result = [
            f'Hotel {self.name} has {self.guests} total guests',
            f'Free rooms: {", ".join(free_rooms)}',
            f'Taken rooms: {", ".join(taken_rooms)}'
        ]

        return '\n'.join(result)


