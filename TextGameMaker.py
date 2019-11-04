#TODO:
    #use the rooms and players object lists
    #make a put down function
    #write documentation
    #clean up code
    #???
    #profit
    
from Config import *

class Object:
    def __init__(self, Usable, Takeable, Look_Text, Name, Pos, Use_The_Following, Use_Text, Take_Text):
        self.Usable = Usable #Bool
        self.Takeable = Takeable #Bool
        self.Pos = Pos #List
        self.Look = Look_Text #String
        self.Name = Name #String
        if Use_The_Following:
            self.Use = Use_Text #String
            self.Take = Take_Text #String

class Player:
    def __init__(self):
        self.Pos = [2, 2] #List
        self.Objects = [] #List
Player = Player() #Define "Player"

class Room:
   def __init__(self, Pos, Look_Text, Go_Text):
        self.Pos = Pos #List
        self.Items = [] #List
        self.Look = Look_Text #String
        self.Go = Go_Text #String

def Parse(In):
    In = In.lower() #Lowercase the input
    In = In.split() #Split the input up
    r = -1 #Set "r" to a placeholder value
    
    i = 0
    while i < len(In): #See where the first function word is in the list "In"
        if In[i] in ["look", "use", "take", "go"]:
            Start = i
            break
        else:
            i = i + 1

    #Look
    try:
        if In[Start] == "look":
            if (len(In) - Start) == 1: #If there is nothing after "look" in the list then look at the room
                r = Look(FindRooms()) #Look at the room
            elif In[(Start + 1)] == "at":
                r = Look(Table[In[(Start + 2)]]) #Set "r" to Look (returns 1 or 0)
            else:
                r = Look(Table[In[(Start + 1)]]) #Set "r" to Look (returns 1 or 0)
                
        if r == 1: #If "r" is 1 then raise an error
            raise IndexError
        
    except (IndexError, KeyError):
        print("That is not here.")
    r = -1 #Reset "r"

    #Use
    try:
        if In[Start] == "use":
            r = Use(Table[In[(Start + 1)]]) #Set "r" to Use (returns 1 or 0)
            
        if r == 1: #If "r" is 1 then raise an error
            raise IndexError
        
    except (IndexError, KeyError):
        print("That is not here.")
    r = -1 #Reset "r"
    
    #Take
    try:
        if In[Start] == "take":
            r = Take(Table[In[(Start + 1)]]) #Set "r" to Take (returns 1 or 0)
            
        if r == 1: #If "r" is 1 then raise an error
            raise IndexError
        
    except (IndexError, KeyError):
        print("That is not here.")
    r = -1 #Reset "r"
    
    #Go
    try:
        if In[Start] == "go":
            r = Go(In[(Start + 1)]) #Set "r" to Go (returns 0, 1, or 2)
            
        if r == 1: #If "r" is 1 then raise an error
            raise IndexError
        elif r == 2: #If "r" is 2 then print the message telling the player that that is the end of the map
            print("You cant go there.")
        elif r == 0: #If "r" is 0 then print the entry text of a room
            print(FindRooms().Go)
            
    except (IndexError, KeyError):
        print("What direction do you want to go?")
    r = -1 #Reset "r"
    
def FindRooms():
    RoomList = [R1, R2, R3, R4, R5, R6, R7, R8, R9]
    i = 0
    while True: #Repeats until you have found a room with the players position
        if RoomList[i].Pos == Player.Pos:
            return RoomList[i] #Send the room back
        else:
            i = i + 1
            pass
    return 1 #Error
        
def Look(Object):
    if Object.Pos == Player.Pos: #If you are in the same room as the object
        try:
            print(Object.Look) #Print the look text
            return 0
        except:
            pass
    return 1 #Error
      
def Use(Object):
    if Object.Pos == Player.Pos: #If you are in the same room as the object
        try:
            if Object.Usable:
                print(Object.Use) #Print the Use text
                return 0
            else:
                print(Object.Name, "doesn't seem to do anything!") #Print that the object cant be used
                return 0
        except:
            pass
    return 1 #Error

def Take(Object):
    if Object.Pos == Player.Pos: #If you are in the same room as the object
        try:
            if Object.Takeable:
                print(Object.Take) #Print the take text

                #add the object to the list and take it from the room
                
                return 0
            else:
                print(Object.Name, "doesn't seem to move!") #Print that the object cant be picked up
                return 0
        except:
            pass
    return 1 #Error

def Go(Way):
    Px, Py = Player.Pos[0], Player.Pos[1] #set playerX and playerY vars
    try:
        if Way.lower() == "west" and Px > 1:
            Player.Pos[0] = (int(Player.Pos[0]) - 1)
        elif Way.lower() == "east" and Px < 3:
            Player.Pos[0] = (int(Player.Pos[0]) + 1)
        elif Way.lower() == "north" and Py > 1:
            Player.Pos[1] = (int(Player.Pos[1]) - 1)
        elif Way.lower() == "south" and Py < 3:
            Player.Pos[1] = (int(Player.Pos[1]) + 1)
        else:
            return 1 #Error
        
        if Player.Pos == [Px, Py]:
            return 2 #This is when it does not work
        else:
            return 0
    except:
        pass
    return 1 #Error
