class Player:
    Pos = [0, 0]
    Objects = []

class Object:
    def __init__(self, ItemList, *args, **kwargs):
        self.ItemList = ItemList

        self.Look = kwargs.get("Look", None)

        self.Custom_Func_List = kwargs.get("Custom_Func_List", [None, None, None, None])
        self.Custom_Args_List = kwargs.get("Custom_Args_List", [None, None, None, None])

        Object_List.append(self)


class Room:
    def __init__(self, Pos, Look):
        self.Pos = Pos
        self.Look = Look
        self.Objects = []
        self.Object_Table = {}

def FindRoom(Pos):
    i = 0
    while i < len(RoomList):
        if RoomList[i].Pos == Pos:
            return RoomList[i]
        else:
            i = i + 1

def Parse():
    Input = str(input("Input_Prompt")).lower().split()

    Start = None
    i = 0
    while i < len(Input):
        if Input[i] in Commands:
            Start = i
            break
        else:
            i = i + 1

    try:
        if str(type(Start).__class__.__name__).lower() == "nonetype":
            print("NO_COMMAND")

        elif Input[Start] in Exit_Commands:
            exit()

        Offset = 0
        while Input[(Start + i)] not in Object_List.extend(Direction_List): #Find the object or direction
            Offset = Offset + 1
            pass

        if Input[(Start + Offset)] not in Direction_List: #If the command isn't go:
            if Input[(Start + Offset)] in FindRoom(Player.Pos): #If the object is in the same room as the player:
                Command(FindRoom(Player.Pos).Object_Table[Input[(Start + Offset)]], Input[Start].lower())
            else:
                print("NOT_HERE")

        else:
            Command_Table[Input[Start]](Direction_Table[Input[(Start + Offset)]])

    except Exception as e:
        raise

def Command(Object, Command):
    Table = {"look": 0, "use": 1, "take": 2, "leave": 3}
    List = [Object.Look, Object.Use, Object.Take, Object.Leave]
    print(List[Table[Command]])
    if Command == "take":
        print(Object.Take)
        Player.Objects.append(Object)
        FindRoom(Player.Pos).Objects.pop(FindRoom(Player.Pos).Objects.index(Object))
    elif Command == "leave":
        Player.Objects.pop(Player.Objects.index(Object))
        FindRoom(Player.Pos).Objects.append(Object)
    if Object.Custom_Func_List[Table[Command]].__class__.__name__.lower() != "nonetype":
        if Object.Custom_Args_List[Table[Command]].__class__.__name__.lower() != "nonetype":
            Object.Custom_Func_List[Table[Command]](Object.Custom_Args_List[Table[Command]])
        else:
            Object.Custom_Func_List[Table[Command]]()

def Where(Object):
    if type(Object).__name__ == "Player": #If the object is the player print their position
        print(f"{Object.Pos[0]}, {Object.Pos[1]}")
        return Object.Pos
    else: #If its not then get the object pos
        print(f"{RoomList.Objects.index(Object).Pos[0]}, {RoomList.Objects.index(Object).Pos[1]}")
        return RoomList.Objects.index(Object).Pos

def Go(Direction):
    Direction_Table = {"west": [0, -1], "east": [0, 1], "south": [1, -1], "north": [1, 1]}
    Player.Pos[Direction_Table[Direction][0]] = Player.Pos[Direction_Table[Direction][0]] + Direction_Table[Direction][1]
    if str(type(FindRoom(Player.Pos)).__name__) == "Room":
        print(FindRoom(Player.Pos).Look)
    else:
        print("You cant go there!")
        Player.Pos[Direction_Table[Direction][0]] = Player.Pos[Direction_Table[Direction][0]] - Direction_Table[Direction][1]

Commands = ["go", "look", "use", "take", "leave", "where"]
Exit_Commands = ["stop", "end", "exit", "done"]

Object_List = []
Direction_List = ["north", "south", "east", "west"]

Commands = Commands.extend(Exit_Commands)
