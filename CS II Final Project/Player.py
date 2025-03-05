class Player:
    def __init__(self, room =1,prev=0, ):
        self.room = room
        self.prev = prev
        self.keyOne = False
        self.keyTwo = False
        self.keyThree = False
    def movement(self, roomLi, roomDesc):
        try: #if you have a value congrats you move on
            self.choice = int(input('which direction would you like to go? N=0, W=1, E=2, S=3.\n'))
            self.prev = self.room
            self.room = roomLi[self.room][self.choice]
        except ValueError:
            print('Your mind starts to wander... floating cats, cheeses of all varieties... No! Focus you must escape!')
        except: # when you try to do something that doesn't work
            print("You look to the celling and jump, but you don't make it. You're still in the same room.")
        if self.room == 0: # you hit a wall and turn around
            print(roomDesc[0])
            self.room = self.prev
        if self.room == 1 and self.prev == 10:
            print("You crawl through the tunnel... It twists and turns, back and forth for what feels like hours but then you hit a what feels to be a wall but it crumbles as you push through to reveal... your cell?")
    def inspect(self,roomDesc, roomcheck):
        
        if roomcheck[self.room] == 0:# this is so when you enter a new room you hear its description
            if self.room != 5 and self.room != 12 and self.room != 13: #makes sure you don't try to go somewhere you can't
                print(roomDesc[self.room])
            elif (self.room == 5 and self.keyOne == True) or (self.room == 12 and self.keyTwo == True) or (self.room == 13 and self.keyThree == True):# checks if you are in a locked room with it's key
                print(roomDesc[self.room])
            else: #no key and going to a locked room, generate specific responses
                if self.room == 5:
                    print('You try to open the door but it won’t budge. There has to be a key somewhere.')
                elif self.room == 12:
                    print("You walk towards the terminal and try to start it up but there is no power, there has to be an extra gear somewhere.")
                self.room = self.prev # it's locked you can't stay inside it yet
        
        if roomcheck[self.room] == 1:
            self.choice = input('inspect the room? y/n \n')
            if self.choice == 'y' or self.choice == 'Y':
                print(roomDesc[self.room])
        if self.room != 0:# never change the wall room
            roomcheck[self.room] = 1