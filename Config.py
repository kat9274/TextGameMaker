class Object:
    def __init__(self, Name, Look, Use, Take, Leave, On_Use, Args, On):
        global ObjectsName, Object_Table
        self.Name = Name  # String
        self.Look = Look  # String
        self.Use = Use  # List
        self.Take = Take  # String
        self.Leave = Leave  # String

        self.On_Use = On_Use  # Function
        self.Args = Args  # Tuple
        self.On = On  # Bool

        ObjectsName.append(Name.lower())
        Object_Table[str(Name).lower()] = self

class Player:
    def __init__(self):
        global ObjectsName
        self.Pos = [0, 0]  # List
        self.Items = []  # List

        ObjectsName.append("i")

class Room:
    def __init__(self, Pos, Look):
        global RoomList
        self.Pos = Pos  # List
        self.Items = [self]  # List
        self.Look = Look  # String
        RoomList.append(self)

# Needed:
ObjectsName = []
RoomList = []  # Define "RoomList"
In_Prompt = ">>> "
Player = Player()  # Define "Player"
Object_Table = {"i": Player}

# Rooms:
Room00 = Room([0, 0], "A pretty plain room. There is a fan here. The wall to the north seems strange.")

# Funcs:
def Fan_Blows_Room00():
    Fan.Use[0] = "The fan turns on"
    Room01 = Room([0, 1], "")
    Room00.Look = "A pretty plain room. There is a fan here. The wall to the north has a door."
    RoomList.append(Room10)

# Objects:
Fan = Object("Fan", "It's a old fan.", ["The fan turns on. The wind from the fan blows a door to the north open.", "The fan turns off."], False, False, Fan_Blows_Room00, (False, False), False)
Room00.Items.append(Fan)
