from Player import *
from functools import reduce
import random
# room list: each room is formatted [N,W,E,S]
roomLi = [[0,0,0,0],[2,0,0,0],[0,3,4,1],[8,5,2,0],[6,2,0,0],[0,0,3,0],[13,0,7,4],[0,6,0,0],[9,0,0,3],[0,10,11,8],[0,1,9,0],[12,9,0,0],[0,0,0,11],[0,0,0,6]]
#to log if you entered the room before
roomcheck = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# each rooms desription
roomDesc= ['There is a wall there.', 'Your cell… there is etches scrawled along the walls of dreams to escape. The guard left your door wide open.', 'The prison hallways go on forever in both the west and the east.', 'The halls grow shorter, to the west there is a cell. You cant make out the figure inside the cell but you could see a glimmer of… something.', 'The halls continue to wind, you see giant bone sculptures one vaguely resembles a goblin?', 'You walk through the now unlocked door, to a cell tattered and strewn cloths cover the room. In the corner of the room, there is a goblin giggling to himself. ', 'The hallway stretches onward. To the north there is a door with a glimpse of the outside, and the east lies another door with the label “storage closet”.', 'You walk into the storage closet and see crates and crates of random junk someone must have taken alike to. But then you see a small key, hidden between to crates.', 'The hallway continues on to the north. There are murals of what looks like beasts on the wall…', 'The hallway stops and forks to the west and east. There is a line of rats walking single file towards the east, seemingly towards something.', 'You walk into what looks to be barracks, with sleeping guards in each bed. To the west you see a tunnel, you wonder where it could lead.', 'You follow where the rats lead into a room with gears lining the walls to the north there seems to be a missing gear along with a terminal. Maybe the gears power the terminal.', 'You slot the gear into the chain and it starts turning with the chain and suddenly the terminal powers on.', 'The door is open you walk through to the full moon, the rolling hills look so much more magnificent then ever yet ominous. Run before the guards wake up!']
logit = ['You hit a wall.', 'You were in your cell.', 'You wander the halls outside your cell.', 'You found another cell.', 'You saw a bone sculpture in a hall.', 'You walked into the giggling goblins cell.', "You've seen the outside and a storage closet.", 'You visited a storage closet.', 'You saw murals of beasts.', 'You saw rats walking in a lin in the hallway.', 'You entered the barracks there was a tunnel.', 'You followed the rats to a room with a terminal.', 'You messed with the terminal.', 'You finally escaped.']
run = True
play = Player()
with open('log.txt', mode='w') as log: #replaces what is in log with the first otem so you don't 
    log.write(logit[1])
def terminalCheck(li): #adds up all the rooms you've seen so far 
    results = reduce(lambda x, y: x+y, li)
    print("You have seen ", results, "/12 rooms so far!!") #Technically room 13 isn't a room so it's not counted
    if results>=12: #shouldn't exceed 12 but if something goes wrong then it still works
        print("You just got to escape now!")
def giggles():
    seq = [random.randrange(1,10) for i in range(0,5)]
    while True:
        print('Consider the following sequence\n', seq,"\nWhat is the next number?")
        try:
            int(input(''))
            print('HAHAHA it was random but here take this for the good laugh!\nYou got a small shiny gear!')
            play.keyTwo = True
            break
        except ValueError:
            print("PFFT You don't know what a number is?")
print(roomDesc[1])
roomcheck[1]=1
while run == True:
    play.movement(roomLi, roomDesc)# asks you to move so you can continue on
    play.inspect(roomDesc, roomcheck)# always makes sure you know where you are going
    with open('log.txt', mode='a') as log:
        log.write(logit[play.room])
    if play.room == 7:
        print("You reach for the key and take it, \nit looks like a simple iron key. You think it goes to a cell. \nitem obtanied: key 1")
        play.keyOne = True
    if play.room == 5 and play.keyTwo == False:
        giggles()
    if play.room == 12 and play.keyTwo == True:
        frontof = True
        print("There is two buttons glowing on the terminal, one green and one red. Should yoy push them?")
        while frontof ==True:
            choices = input("Green=0, red=1 :")
            if choices == "0":
                terminalCheck(roomcheck) # runs terminal checker
            elif choices == "1":
                play.keyThree = True
                print("boom...Boom...BOOM...\nYou heard something moving somewhere. you should check")
            else:
                print("You decide to press nothing. You feel like maybe you should at least press a button.")
            going = input("Would you like to leave the terminal? y/n:")
            if going == 'y' or going == 'Y':
                frontof = False
        play.room = play.prev
    if play.room == 13 and play.keyThree == True:
        run = False
print("you completed the game! congratulations")
logs = input('would you like to see the log of your actions? y/n')
if logs == 'y' or logs == 'Y':
    with open('log.txt', mode='r') as log:
        logent = ' '.join(log.readlines())
        print(logent.replace('.','.\n'))