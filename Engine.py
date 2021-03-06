#NO CUSTOM FUNCTIONS
#NO CUSTOM FUNCTIONS
#NO CUSTOM FUNCTIONS
#NO CUSTOM FUNCITONS
#NO CUSTOM FUCNTIONS
#NO CUSTOM FUCNTIONS
#NO CUSTOM FUNCITONS
class Object:
    def __init__(self, Name, Room, **kwargs):
        self.Name = Name.lower()
        self.On = kwargs.get("On", False)
        #                               Look  Use On/Off
        self.Text = kwargs.get("Text", [None, [None, None]])

        room.Items[self.Name] = self

class Room:
    def __init__(self, pos, look, **kwargs):
        self.Pos = Pos
        self.Look = Look
        self.Items = kwargs.get("Items", {})

        Rooms[str(Pos)] = self

    def Text(self):
        Objects = list(self.Items.values()) #.values is a list of the values.
        Text = [" There is" if len(Objects) != 1 else " There is nothing but"]
        for i in range(len(Objects)):
            Text.append(f"{' and ' if len(Objects) != 1 else ' '}a {Objects[i].Name}{'.' if i == (len(Objects) - 1) else ','}")

        #Directions =
        #DO THIS
        #Text.append(" There is")
        #for i in range(len(Directions)):
        #    Text.append(f"{' and ' if len(Directions) != 1 else ' '}a {Directions[i]}{'.' if i == (len(Directions) - 1) else ','}")

class Player:
    Pos = [0, 0, 0]
    Item_Table = {}

class Room:
    def __init__(self, Pos, Look, **kwargs):
        self.Pos = Pos
        self.Look = Look
        self.Item_Table = kwargs.get("Item_Table", {})
        self.Go_Command = kwargs.get("Go_Command", None)

        RoomList.append(self)

    def DynamicText(self):
        ItemTextList = []
        Pre = " There is "
        for i in range(len(list(self.Item_Table.keys()))):
            ItemTextList.append(f"{Pre}{'a ' if len(list(self.Item_Table.keys())) != 1 else 'nothing but a '}{list(self.Item_Table.keys())[i]}{'.' if i == (len(list(self.Item_Table.keys())) - 1) else ', '}")
            Pre = "and " if i == (len(list(self.Item_Table.keys())) - 2) else ""

        RoomTextList = []
        Rooms = []
        Direction = 1
        Pre = " There is a " if len(Rooms) != 1 else " There is no other way but a "
        for i in range(3):
            TempPos = list(Player.Pos)
            for i2 in range(2):
                TempPos[i] = TempPos[i] + [1, -1][i2]
                if type(FindRoom(Pos=TempPos)).__name__ == "Room":
                    Rooms.append(FindRoom(Pos=TempPos))
        for i in range(len(Rooms)):
            for i2 in range(3):
                if Rooms[i].Pos[i2] > Player.Pos[i2]:
                    Direction = ["east", "north", "up"][i2]
                elif Rooms[i].Pos[i2] < Player.Pos[i2]:
                    Direction = ["west", "south", "down"][i2]

            RoomTextList.append(f"{Pre}{'' if Rooms[i].Look != 'locked.' else 'locked '}way{' to the ' if Direction not in ['up', 'down'] else ' '}{Direction}{'.' if i == (len(Rooms) - 1) else ', '}")
            Pre = "and a " if i == (len(Rooms) - 2) else "a "

        PlayerItemList = []
        Pre = " You have: "
        for i in range(len(list(Player.Item_Table.keys()))):
            PlayerItemList.append(f"{Pre}a {list(Player.Item_Table.keys())[i]}{'.' if i == (len(list(Player.Item_Table.keys())) - 1) else ', '}")
            #IDK IF NEED #ItemTextList.append(f"{Pre}{list(Player.Item_Table.keys())[i]}{"." if i == (len(list(Player.Item_Table.keys())) - 1) else ", "}")
            Pre = "and a " if i == (len(list(Player.Item_Table.keys())) - 2) else "a "

        return self.Look + ''.join(ItemTextList) + ''.join(RoomTextList) + ''.join(PlayerItemList)

    def SaveItems(self):
        Items = []
        for i in range(len(list(self.Item_Table.keys()))):
            Object = self.Item_Table[list(self.Item_Table.keys())[i]]
            Items.append(f"{Object.Name}-{Object.Text_List}-{Object.Func_List}-{Object.Args_List}-{Object.On}")
        return Items

class Player:
    def __init__(self, **kwargs):
        self.Pos = kwargs.get("Pos", [0, 0, 0])
        self.Item_Table = kwargs.get("Item_Table", {})
Player = Player()

def Parse(**kwargs):
    In = input(kwargs.get("Input_Prompt", ">>> ")).lower().split() #Get input
    Room = FindRoom() #Set room

    for i in range(len(In)):
        if In[i] in list(Command_Table.keys()): #Find the command
            Start = i
        elif In[i] in list(Room.Item_Table.keys()) + list(Player.Item_Table.keys()) + ["north", "south", "east", "west", "up", "down"]: #Find the object/direction
            Offset = i

    Object = Room.Item_Table[In[Offset]]

    if In[Start] in ["go", "exit"]: #If the command is go or exit
        Command_Table[In[Start]](In[(Start + Offset)] if In[Start] == "go" else kwargs.get("Exit_Text", "Bye.")) #Run the command
    elif In[Start] in list(Command_Table.keys()): #If the command is not go or Exit
        Command_Table[In[Start]](Object, In[Start]) #Run the command

def Commands(Object, Command, **kwargs):
    Room = FindRoom()
    Num = {"look": 0, "use": 1, "take": 2, "leave": 3, "room": 4}[Command] #Find a number to identify what command and do the appropriate responce
    if Num in [2, 3]:
        [None, None, Player, Room][Num].Item_Table[Object.Name] = [None, None, Room, Player][Num].Item_Table.pop(Object.Name) #Pop returns the item it pops so adds it from room to player
    elif Num == 4:
        print(Room.DynamicText())
        return 0

    Func = Object.Func_List[Num][int(Object.On)] if Num == 1 else Object.Func_List[Num]
    Args = Object.Args_List[Num][int(Object.On)] if Num == 1 else Object.Args_List[Num]
    Text = Object.Text_List[Num][int(Object.On)] if Num == 1 else Object.Text_List[Num]
    print(Text if Text != None else Object.No_Text, end=Object.End)
    if Func != None:
        Func(Args)
        Object.On = not Object.On if Num == 1 else Object.On

def Go(Direction, **kwargs):
    try:
        Room = FindRoom() #Set room
        Direction_List = {"west": [0, -1], "east": [0, 1], "south": [1, -1], "north": [1, 1], "up": [2, 1], "down": [2, -1]}[Direction] #Get list for directions
        Player.Pos[Direction_List[0]] = Player.Pos[Direction_List[0]] + Direction_List[1] #Go in that direction
        print(Room.DynamicText() if Room.Look != "locked." else Room.Look)
        if Room.Look == "locked.": #If the room is locked
            Player.Pos[Direction_List[0]] = Player.Pos[Direction_List[0]] - Direction_List[1] #Go back to the way you came from
        else: #If it is not locked
            if Room.Go_Command != None: #If there is a go command
                Room.Go_Command() #Run it
    except (KeyError, AttributeError):
        print("You can't go there.") #If there is not a room print this
        Player.Pos[Direction_List[0]] = Player.Pos[Direction_List[0]] - Direction_List[1]

def FindRoom(**kwargs):
    for i in range(len(RoomList)): #Go through all the rooms
        if RoomList[i].Pos == kwargs.get("Pos", Player.Pos): #If the rooms pos is the same as the inputed pos then return the room
            return RoomList[i]

def Exit(Text, **kwargs):
    file = open("Save.dat", "a+")
    for i in range(len(RoomList)):
        file.write(f"{RoomList[i].Pos}:{RoomList[i].Look}:{RoomList[i].Go_Command}:{RoomList[i].SaveItems()}\n")

    exit(Text)

def Start(**kwargs):
    file = open("Save.dat", "r+")
    for i in file:
        Room = FindRoom(eval(file[i].split(":")[0]))
        Room.Look = file[i].split(":")[1]
        # Set go command here. needs a little bit of work because you cant just use eval() to get a function.
        for i2 in range(len(list(Room.Item_Table.keys()))):
            ObjectList = eval(line[i].split(":")[3])
            Object = Room.Item_Table[ObjectList[i2].split("-")[0]]
            Object.Text_List = eval(ObjectList[i2].split("-")[1])
            Object.Func_List = eval(ObjectList[i2].split("-")[2])
            Object.Args_List = eval(ObjectList[i2].split("-")[3])
            Object.On = eval(ObjectList[i2].split("-")[4])

    while True:
        Parse(Input_Prompt=kwargs.get("Input_Prompt", ">>> "), Exit_Text=kwargs.get("Exit_Text", "Bye."), No_Parse=kwargs.get("No_Parse", "What?"))

def Help(*args):
    print(f'Commands:\n  Go: type "go [direction]" to go in that direction. The directions are: north, south, east, west, up, and down.\n  Look: Type "look [object]" to see a short discription of that object. You can also just type "look" to see a discription of the room, a list of items, and all the rooms you can go to.\n  Use: Type "use [object]" to use an object. The thing it does will vary by object.\n  Take: Type "take [object]" to add the item to your inventory.\n  Leave: Type "leave [object]" to put the item down and remove it from your inventory.\n  Exit: Type: "exit" and the game will exit.\n  Help: Type "help" to get to this again.\n  Custom Commands: Some games might have various custom commands that cannot be listed here.')

Command_Table = {"go": Go, "look": Commands, "use": Commands, "take": Commands, "leave": Commands, "exit": Exit, "help": Help}
RoomList = []
