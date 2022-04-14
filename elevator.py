import random, names
from components import Building, Elevator, Passenger

#creating instances of objects
building = Building()
elevator = Elevator()
floor_passengers=[]
elevator_direction = 0

#generating passenger objects for floor
for floor in range(building.max_height):
    for person_amount in range(random.randint(1, 5)):
        floor_passengers.append(Passenger(
            floor, names.get_first_name(), random.randint(1, building.max_height-1)
        ))
    floor_passengers.insert(0, floor)
    building.residents.append(floor_passengers)
    floor_passengers=[]

#below function is used just to show at terminal the elevator state and building
def console_log(elevator, residents):
    result = ''
    for passenger in reversed(residents):
        if elevator.position == passenger[0]:
            result += f'\n  _________________________________:  ELEVATOR AT FLOOR NO: {elevator.position}  :_________________________________\n\n'
            result += f'\t {elevator.elevator[:3]} \n'
            result += f'\t {elevator.elevator[3:]} \n' if len(elevator.elevator) > 3 else f''
            result += f'  ________________________________________________________________________________________________\n\n'
            result += f' {passenger[:5]} \n' if len(passenger) > 0 else f''
            result += f' {passenger[5:]} \n' if len(passenger) > 5 else f''
        else:
            result += f'\n\n============================================| floor {passenger[0]} |=============================================\n\n'
            result += f' {passenger[:5]} \n' if len(passenger) > 0 else f''
            result += f' {passenger[5:]} \n' if len(passenger) > 5 else f''

    return print(result)


"""
 * Decided to show 20 steps, each movement of elevator one step
 * First we are deciding in which direction to move elevator
   according waiting passangers when elevator is empty 
   then moving 
"""

for steps in range(20):
    if len(elevator.elevator) == 0:
        for groups in building.residents:
            for passenger in groups[1:]:
                if passenger.destination > elevator.position and passenger.origin == elevator.position:
                    elevator_direction += 1
                if passenger.destination < elevator.position and passenger.origin == elevator.position:
                    elevator_direction -= 1

    if elevator_direction >=0 and building.max_height > elevator.position:
        elevator.move_up(building.max_height, building.residents)
        console_log(elevator, building.residents)
    else:
        elevator.move_down(building.min_height, building.residents)
        console_log(elevator, building.residents)

