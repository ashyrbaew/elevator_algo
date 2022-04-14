import random, names


class Building:
    def __init__(self):
        self.max_height = random.randint(5, 20)
        self.min_height = 0
        self.floor_volume = 10
        self.residents=[]

    def residents_in_floor(self, passangers):
        residents_in_floors = []
        for floor in range(self.max_height):
            for person in passangers:
                if person.origin == floor:
                    residents_in_floors.append(person)
            self.residents.append(residents_in_floors)

        return self.residents


class Passenger:
    def __init__(self, origin: int, name: str, destination: int):
        self.origin = origin
        self.name = name
        self.destination = destination

    def __repr__(self):
        return f'{self.name} {self.origin}->{self.destination}'


class Elevator:
    def __init__(self):
        self.volume = 5
        self.position = 0
        self.elevator=[]

    def move_up(self, max_height, residents):
        if self.position < max_height:
            for group in residents:
                temp_group = group[:]
                for person in temp_group[1:]:
                    if person.origin == self.position and\
                            person.destination > self.position and\
                            len(self.elevator) < self.volume:
                        self.elevator.append(person)
                        group.remove(person)

            self.position +=1
            for person in self.elevator[:]:
                person.origin = self.position
                if person.origin == person.destination:
                    for group in residents[:]:
                        if group[0] == person.origin:
                            group.append(person)
                            self.elevator.remove(person)
        else:
            return "Its a last floor, please, move down"
        return residents, self.elevator

    def move_down(self, min_height, residents):
        if self.position > min_height:
            for group in residents:
                temp_group = group[:]
                for person in temp_group[1:]:
                    if person.origin == self.position and\
                            person.destination < self.position and\
                            len(self.elevator) < self.volume:
                        self.elevator.append(person)
                        group.remove(person)

            self.position -= 1
            for person in self.elevator[:]:
                person.origin = self.position
                if person.origin == person.destination:
                    for group in residents[:]:
                        if group[0] == person.origin:
                            group.append(person)
                            self.elevator.remove(person)
        else:
            return "Its a first floor, please, move UP"

        return residents, self.elevator

