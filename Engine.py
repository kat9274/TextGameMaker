class Object:
    def __init__(self, Room, Name, *args, **kwargs):
        ############## = ##########(###########, [Look, [GetO, GetI], Take, Leave])
        self.Text_List = kwargs.get("Text_List", [None, [None, None], None, None])
        self.Func_List = kwargs.get("Func_List", [None, [None, None], None, None])
        self.Args_List = kwargs.get("Args_List", [None, [None, None], None, None])

        Room.Item_Table[Name.lower()] = self
        All_Names.append(Name.lower())

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

def Parse(Room, Command_Table, *args, **kwargs):

    #Command_Table needs to be customizable to add new ones #Just do that in the input to the parse func (def Parse(HERE))

    Input = input(kwargs.get("Input_Prompt", ">>> ")).lower().split() #Get input and split it up

    Start = None
    i = 0
    while i < len(Input): #Find Command and where it is in the list
        if Input[i] in Command_Table:
            Start = i
            break
        i = i + 1

    if Start.__class__.__name__ == "NoneType": #If there is no command
        print(kwargs.get("No_Command", "What do you want to do?")) #Print No_Command

    elif Input[Start] in ["stop", "end", "exit", "done"]: #If the command is an exit command
        print(kwargs.get("Exit_Text", "")) #Print Exit_Text
        exit() #Exit

    Offset = 0
    while Input[(Start + Offset)] not in All_Names.extend(["north", "south", "east", "west"]): #Find Offset to Start that leads to object or direction
        Offset = Offset + 1

    if Room.Object_Table.get(Input[(Start + Offset)], None).__class__.__name__ != "NoneType": #If the object exists
        Command_Table[Input[Start]](Room.Object_Table.get(Input[(Start + Offset)], None)) #Run the command with the object

    elif Input[(Start + Offset)] in ["north", "south", "east", "west"]: #If its a direction
        Command_Table[Input[Start]](Input[(Start + Offset)]) #Run the command with the direction

    else: #If it's not either of those
        print(kwargs.get("No_Args", "What do you want to do?")) #Print No_Args

a = Room([0, 0], "", Item_Table={"Cat": 1, "Dog": 2, "fan": 3, "a nother cat": 8574, "mom telling me to trim my nails": 4, "light": 5, "Something": 6})

def Dynamic(Room):
    List = list(Room.Item_Table.keys())
    Temp = []
    i = 0
    while i <= (len(List) - 2):
        if i == 0:
            Temp.append(f"There is a {List[i]}")
        else:
            Temp.append(f", a {List[i]}")
        i = i + 1
    Temp.append(f", and a {List[i]} here.")
    return ''.join(Temp)

All_Names = []
