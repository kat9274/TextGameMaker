import random

class Object:
    def __init__(self, Room, Name, *args, **kwargs):
        ############## = ##########(###########, [Look, [On, Off]###, Take, Leave])
        self.Text_List = kwargs.get("Text_List", [None, [None, None], None, None])
        self.Func_List = kwargs.get("Func_List", [None, [None, None], None, None])
        self.Args_List = kwargs.get("Args_List", [None, [None, None], None, None])

        self.On = kwargs.get("On", False)

        Room.Item_Table[Name.lower()] = self

class Room:
    def __init__(self, Pos, Look, *args, **kwargs):
        self.Pos = Pos
        self.Look = Look
        self.Item_Table = kwargs.get("Item_Table", {})

        RoomList.append(self)

class Player:
    def __init__(self, *args, **kwargs):
        self.Pos = kwargs.get("Pos", [0, 0])
        self.Item_Table = kwargs.get("Item_Table", {})
Player = Player()

def Parse(*args, **kwargs):
    In = input(kwargs.get("Input_Prompt", ">>> ")).lower().split()
    Room = FindRoom()

    i = 0
    while i in range(len(In)):
        if In[i] in list(Room.Item_Table.keys()) + ["north", "south", "east", "west"]:
            Offset = i
        elif In[i] in list(Command_Table.keys()):
            Start = i
        i = i + 1

    try:
        if In[Start] in ["look", "use", "take", "leave"]:
            try:
                Command_Table[In[Start]](Room.Item_Table[In[(Start + Offset)]], In[Start], No_Text=kwargs.get("No_Text", ""))
            except UnboundLocalError:
                if In[Start] == "look":
                    Command_Table[In[Start]](Room, "room")
                else:
                    pass
        elif In[Start] == "exit":
            print(kwargs.get("Exit_Text", ""))
            exit()
        else:
            Command_Table[In[Start]](In[(Start + Offset)] if In[(Start + Offset)] in ["north", "south", "east", "west"] else Room.Item_Table[(Start + Offset)])
    except Exception as e:
        if e.__class__.__name__ == "UnboundLocalError":
            print(kwargs.get("No_Command", "What do you want to do?"))
            pass

def Commands(Object, Command, *args, **kwargs):
    Num = {"look": 0, "use": 1, "take": 2, "leave": 3, "room": 4}[Command]
    if Num == 2:
        Player.Item_Table[Object.Name] = Object
        Room.Item_Table.pop(Object.Name)
    elif Num == 3:
        Room.Item_Table[Object.Name] = Object
        Player.Item_Table.pop(Object.Name)
    if Num == 4:
        DynamicText(FindRoom())
        print(Object.Dynamic)
    else:
        if Num == 1:
            print(Object.Text_List[Num][int(Object.On)] if Object.Text_List[Num][int(Object.On)] != None else kwargs.get("No_Text"))
            if Object.Func_List[Num][int(Object.On)] != None and Object.Args_List[Num][int(Object.On)] != None:
                Object.Func_List[Num][int(Object.On)]()
            elif Object.Func_List[Num][int(Object.On)] != None:
                Object.Func_List[Num][int(Object.On)](Object.Args_List[Num][int(Object.On)])
            Object.On = not Object.On
        else:
            print(Object.Text_List[Num] if Object.Text_List[Num] != None else kwargs.get("No_Text"))
            if Object.Func_List[Num] != None and Object.Args_List[Num] != None:
                Object.Func_List[Num]()
            elif Object.Func_List[Num] != None:
                Object.Func_List[Num](Object.Args_List[Num])

def Go(Direction, *args, **kwargs):
    Direction_Table = {"west": [0, -1], "east": [0, 1], "south": [1, -1], "north": [1, 1]}
    Player.Pos[Direction_Table[Direction][0]] = Player.Pos[Direction_Table[Direction][0]] + Direction_Table[Direction][1]
    if str(type(FindRoom()).__name__) == "Room":
        print(FindRoom().Look)
    else:
        print(kwargs.get("No_Room", "You can't go there."))
        Player.Pos[Direction_Table[Direction][0]] = Player.Pos[Direction_Table[Direction][0]] - Direction_Table[Direction][1]

def FindRoom():
    for i in range(len(RoomList)):
        if RoomList[i].Pos == Player.Pos:
            return RoomList[i]

def DynamicText(Room):
    Num = 0
    i = 0
    DynamicTextList = []
    Pre = [" There is ", "", "and "]
    Ap = ", "
    Item_List = list(Room.Item_Table.keys())
    while i < len(Item_List):
        DynamicTextList.append(f"{Pre[Num]}a {Item_List[i]}{Ap}")
        if len(Item_List) > 3:
            if Item_List[-2] != Item_List[i]:
                Num = 1
            else:
                Ap = "."
                Num = 2
        i = i + 1
    Room.Dynamic = Room.Look + ''.join(DynamicTextList)

Command_Table = {"go": Go, "look": Commands, "use": Commands, "take": Commands, "leave": Commands, "exit": 0}
RoomList = []

print("TextGameMaker by Kat9274")
