#"Simple Elevetor Algorithm"

## Objective:
Create an Elevator workflow simulation, which can move up and down according to passengers destionation, and can hold maximum 5 people

## Problem Description:
* Create and application without UI (console), or with a minimal UI. Use OOP and adhere to the principles of SOLID, DRY and ETC.
* The building consists of the nth number of floors, where n is a random number generated at the start of the program in the range 5 <= n <= 20.
* There are k number of passengers on each floor, where k is a random number generated at the start of the program in the range 0 <= k <= 10.
* Each passenger wants to arrive at a certain floor different from the one on which he is.
* The elevator has a capacity limit of 5 people maximum.
* First time the elevator is loaded with people from the first floor, and travels from the first (current) to the largest of those that passengers need. On the way,  
  elevator stops at those floors where passengers need to drop them off and pick up people who need to go in the same direction in which the elevator is moving.

## My Approach
  1) Created classes objects for each part like, Elevator, Buidling, Passenger, so they were independed as possible
  2) Each passenger object has origin floor number, name, and destination floor number  in next format, ``` [0, passenger_name, 0->4 ] ```

## Usage
  1) git clone https://github.com/ashyrbaew/elevator_algo.git
  2) pip install -r requirements.txt
  3) Open python environment and import * elevator.py it will directly show next 20 steps ``` from elevator import * ```
