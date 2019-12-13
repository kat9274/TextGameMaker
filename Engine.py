import random, time, os, sys, ast

class Object:
    def __init__(self, Room, Name, **kwargs):
        self.Name = Name.lower()
        
        ############## = ##########(###########, [Look, [On, Off]###, Take, Leave])
        self.Text_List = kwargs.get("Text_List", [None, [None, None], None, None])
        self.Func_List = kwargs.get("Func_List", [None, [None, None], None, None])
        self.Args_List = kwargs.get("Args_List", [None, [None, None], None, None])

        self.On = kwargs.get("On", False)
        self.No_Text = kwargs.get("No_Text", "You can't do that!")
        self.End = kwargs.get("End", "\n")

        Room.Item_Table[Name.lower()] = self

class Room:
    def __init__(self, Pos, Look, **kwargs):
        self.Pos = Pos
        self.Look = Look
        self.Item_Table = {}
        self.No_Room = kwargs.get("No_Room", "You can't go there!")
        self.Go_Command = kwargs.get("Go_Command", None)

        RoomList.append(self)

    def DynamicText(self):
        ItemTextList = []
        Pre = " There is a "
        Ap = ", "
        for i in range(len(list(self.Item_Table.keys()))):
            if len(list(self.Item_Table.keys())) != 1:
                ItemTextList.append(f"{Pre}{list(self.Item_Table.keys())[i]}{Ap}")
                Pre = "and a " if i == (len(list(self.Item_Table.keys())) - 2) else "a "
                Ap = "." if i == (len(list(self.Item_Table.keys())) - 2) else ", "
            else:
                ItemTextList = [f" There is nothing but a {list(self.Item_Table.keys())[i]}."]

        RoomTextList = []
        Rooms = []
        List = [1, -2]
        Pre = " There is a "
        Ap = ", "
        for i in range(3):
            TempPos = list(Player.Pos)
            for i2 in range(2):
                TempPos[i] = TempPos[i] + List[i2]
                if type(FindRoom(Pos=TempPos)).__name__ == "Room":
                    Rooms.append(FindRoom(Pos=TempPos))
        Direction = 1
        for i in range(len(Rooms)):
            for i2 in range(3):
                if Rooms[i].Pos[i2] > Player.Pos[i2]:
                    Direction = ["east", "north", "up"][i2]
                elif Rooms[i].Pos[i2] < Player.Pos[i2]:
                    Direction = ["west", "south", "down"][i2]

            Locked = "" if Rooms[i].Look != "locked." else "locked "
            if len(Rooms) != 1:
                RoomTextList.append(f"{Pre}{Locked}way{' to the ' if Direction not in ['up', 'down'] else ' '}{Direction}{Ap}")
                Pre = "and a " if i == (len(Rooms) - 2) else "a "
                Ap = "." if i == (len(Rooms) - 2) else ", "
            else:
                RoomTextList = [f" There is no other way but a {Locked}way{' to the ' if Direction not in ['up', 'down'] else ' '}{Direction}."]

        PlayerItemList = []
        Pre = " You have: "
        Ap = ", "
        if len(list(Player.Item_Table.keys())) != 1:
            for i in range(len(list(Player.Item_Table.keys()))):
                PlayerItemList.append(f"{Pre}a {list(Player.Item_Table.keys())[i]}{Ap}")
                ItemTextList.append(f"{Pre}{list(Player.Item_Table.keys())[i]}{Ap}")
                Pre = "and a " if i == (len(list(Player.Item_Table.keys())) - 2) else "a "
                Ap = "." if i == (len(list(Player.Item_Table.keys())) - 2) else ", "
        elif len(list(Player.Item_Table.keys())) == 1:
            PlayerItemList = [f" You have: a {list(Player.Item_Table.keys())[0]}."]
        elif len(list(Player.Item_Table.keys())) < 1:
            pass

        return self.Look + ''.join(ItemTextList) + ''.join(RoomTextList) + ''.join(PlayerItemList)

class Player:
    def __init__(self, **kwargs):
        self.Pos = kwargs.get("Pos", [0, 0, 0])
        self.Item_Table = kwargs.get("Item_Table", {})
Player = Player()

def Parse(**kwargs):
    In = input(kwargs.get("Input_Prompt", ">>> ")).lower().split() #Get input
    Room = FindRoom() #Set room

    for i in range(len(In)):
        if In[i] in list(Room.Item_Table.keys()) + list(Player.Item_Table.keys()) + ["north", "south", "east", "west", "up", "down"]: #Find the object/direction
            Offset = i
        elif In[i] in list(Command_Table.keys()): #Find the command
            Start = i

    try:
        if In[Start] in ["go", "exit"]: #If the command is go or exit
            Command_Table[In[Start]](In[(Start + Offset)] if In[Start] == "go" else kwargs.get("Exit_Text", "Bye.")) #Run the command
        elif In[Start] in list(Command_Table.keys()): #If the command is not go or Exit
            Command_Table[In[Start]](Room.Item_Table[In[(Start + Offset)]] if In[(Start + Offset)] in list(Room.Item_Table.keys()) else Player.Item_Table[In[(Start + Offset)]], In[Start]) #Run the command
    except UnboundLocalError:
        try:
            if In[Start] in ["look", "help"]:
                Command_Table[In[Start]](Room, "room") #If the command is look or help with no argument then run it with a room argument
            else:
                raise IndexError #If the command just doesn't make sense print "What?"
        except (UnboundLocalError, IndexError):
            print(kwargs.get("No_Command", "What?"))

def Commands(Object, Command, **kwargs):
    Room = FindRoom()
    Num = {"look": 0, "use": 1, "take": 2, "leave": 3, "room": 4}[Command] #Find a number to identify what command and do the appropriate responce
    if Num == 2 and Object.Text_List[Num] != None:
        Player.Item_Table[Object.Name] = Room.Item_Table.pop(Object.Name) #Pop returns the item it pops so adds it from room to player
    elif Num == 3 and Object.Text_List[Num] != None:
        Room.Item_Table[Object.Name] = Player.Item_Table.pop(Object.Name) #Pop returns the item it pops so adds it from player to room
    elif Num == 4: #If you ran the look command with no args then print dynamic text
        print(FindRoom().DynamicText())
        return 0
    if Num == 1:
        print(Object.Text_List[Num][int(Object.On)] if Object.Text_List[Num][int(Object.On)] != None else Object.No_Text, end=Object.End)
        if Object.Func_List[Num][int(Object.On)] != None and Object.Args_List[Num][int(Object.On)] != None:
            Object.Func_List[Num][int(Object.On)](Object.Args_List[Num][int(Object.On)])
        elif Object.Func_List[Num][int(Object.On)] != None:
            Object.Func_List[Num][int(Object.On)]()
        Object.On = not Object.On
    else:
        print(Object.Text_List[Num] if Object.Text_List[Num] != None else Object.No_Text, end=Object.End)
        if Object.Func_List[Num] != None and Object.Args_List[Num] != None:
            Object.Func_List[Num](Object.Args_List[Num])
        elif Object.Func_List[Num] != None:
            Object.Func_List[Num]()

def Go(Direction, **kwargs):
    try:
        Direction_List = {"west": [0, -1], "east": [0, 1], "south": [1, -1], "north": [1, 1], "up": [2, 1], "down": [2, -1]}[Direction] #Get list for directions
        Player.Pos[Direction_List[0]] = Player.Pos[Direction_List[0]] + Direction_List[1] #Go in that direction
        Room = FindRoom() #Set room
        if Room.Look != "locked.": #If the room is not locked
            print(Room.DynamicText()) #Print the text
            if Room.Go_Command != None: #If there is a go command
                Room.Go_Command() #Run it
        else: #If it is locked
            print("locked.") #Print locked.
            Player.Pos[Direction_List[0]] = Player.Pos[Direction_List[0]] - Direction_List[1] #Go back to the way you came from
    except (KeyError, AttributeError):
        print("You can't go there.") #If there is not a room print this

def FindRoom(**kwargs):
    for i in range(len(RoomList)): #Go through all the rooms
        if RoomList[i].Pos == kwargs.get("Pos", Player.Pos): #If the rooms pos is the same as the inputed pos then return the room
            return RoomList[i]

def Help(*args):
    print(f'Commands:\n  Go: type "go [direction]" to go in that direction. The directions are: north, south, east, west, up, and down.\n  Look: Type "look [object]" to see a short discription of that object. You can also just type "look" to see a discription of the room, a list of items, and all the rooms you can go to.\n  Use: Type "use [object]" to use an object. The thing it does will vary by object.\n  Take: Type "take [object]" to add the item to your inventory.\n  Leave: Type "leave [object]" to put the item down and remove it from your inventory.\n  Exit: Type: "exit" and the game will exit and save your progress.\n  Help: Type "help" to get to this again.\n  Custom Commands: Some games might have various custom commands that cannot be listed here.')

Command_Table = {"go": Go, "look": Commands, "use": Commands, "take": Commands, "leave": Commands, "exit": exit, "help": Help}
RoomList = []
