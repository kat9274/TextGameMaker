class Object:
    def __init__(self, Room, Name, *args, **kwargs):
        ############## = ##########(###########, [Look, [GetO, GetI], Take, Leave])
        self.Text_List = kwargs.get("Text_List", [None, [None, None], None, None])
        self.Func_List = kwargs.get("Func_List", [None, [None, None], None, None])
        self.Args_List = kwargs.get("Args_List", [None, [None, None], None, None])

        Room.Item_Table[Name] = self

class Room:
    def __init__(self, Pos, Look, *args, **kwargs):
        self.Pos = Pos
        self.Look = Look
        self.Item_Table = kwargs.get("Item_Table", {})

class Player:
    def __init__(self, *args, **kwargs):
        self.Pos = kwargs.get("Pos", [0, 0])
        self.Item_Table = kwargs.get("Item_Table", {})

#Commands i need to make possible:
#Look east
#Look (AT ROOM)

def Parse(Room, Command_Table, All_Objects, *args, **kwargs):

    #Command_Table needs to be customizable to add new ones
    #All_Objects Rename to something that implies names of objects

    Input = input(kwargs.get("Input_Prompt", ">>> ")).lower().split()

    Start = None
    i = 0
    while i < len(Input):
        if Input[i] in Command_Table:
            Start = i
            break
        i = i + 1

    if Start.__class__.__name__ == "NoneType":
        print(kwargs.get("No_Command", "What do you want to do?"))

    elif Input[Start] in ["stop", "end", "exit", "done"]:
        print(kwargs.get("Exit_Text", ""))
        exit()

    Offset = 0
    while Input[(Start + Offset)] not in All_Objects.extend(["north", "south", "east", "west"]):
        Offset = Offset + 1

    if Room.Object_Table.get(Input[(Start + Offset)], None).__class__.__name__ != "NoneType":
        Command_Table[Input[Start]](Room.Object_Table.get(Input[(Start + Offset)], None))
    elif Input[(Start + Offset)] in ["north", "south", "east", "west"]:
        Command_Table[Input[Start]](Input[(Start + Offset)])
    else:
        print(kwargs.get("No_Args", "What do you want to do?"))
