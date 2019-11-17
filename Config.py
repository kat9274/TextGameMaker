class Object:
    def __init__(self, Name, Look, Take, Leave, Use, On, *args, **kwargs):
        global ObjectsName, Object_Table
        self.Name = Name  #String
        self.Look = Look  #String
        self.Take = Take  #String
        self.Leave = Leave  #String
        self.Use = Use  #List
        self.On = On #Bool

        self.On_Look = kwargs.get('On_Look', None)
        self.On_Take = kwargs.get('On_Take', None)
        self.On_Leave = kwargs.get('On_Leave', None)
        self.On_Use = kwargs.get('On_Use', None)

        self.Args_Look = kwargs.get('Args_Look', None)
        self.Args_Take = kwargs.get('Args_Take', None)
        self.Args_Leave = kwargs.get('Args_Leave', None)
        self.Args_Use = kwargs.get('Args_Use', None)

        self.Type = kwargs.get('Type', None)
        self.Text = kwargs.get('Text', None)

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
Object_Table = {"i": Player} #ADD pos to the end on the thing i hope i remember
CustomCommand_List = []

#Rooms:
Room00 = Room([0, 0], "It is a dark room. There is a fan, a table, a flower pot. The wall to the north seems strange, and there is a door to the east.")
Room10 = Room([1, 0], "This room has a shining light blub hanging from a rope. There is also a table with a note on it. There is a door to the west.") #MAKE READ FUNC

#Funcs:
def Fan_Blows_Door00():
    Fan.Use[0] = "You flip the on switch but nothing happens, the fan broke."
    Room01 = Room([0, 1], "This is a very bright room, it has a table and there is a key on the table. There is a door to the south.")
    Room00.Look = "It is a dark room. There is a fan, a table, a flower pot. There is a door to the north and to the east."

def Pot_Take00():
    Note00 = Object("Note", "It's an old, dirty note.", "You put the note in your pocket.", "You put the note down.", False, False, Text="Use the fan!", Type="note")
    Room00.Items.append(Note00)

def EndGame():
    print("You win!")
    exit()

#Objects (Name, Look, Take, Leave, Use, On, *args, **kwargs) (Optional: On_(Look, Take, Leave, Use), Args_(Look, Take, Leave, Use), Type, Text):
Table00 = Object("Table", "It's a table that is about 4 feet tall. It has a Flower Pot on it. I wonder where the flower went?", False, False, False, False, Type="table")
Fan00 = Object("Fan", "Its a big fan. It looks very powerful. There is a button that is labled On/Off on the side.", False, False, ["The fan turns on. Its very strong. The wall to the north falls down. The fan breaks.", "You flip the off switch, nothing happens."], False, On_Use=Fan_Blows_Door00, Type="fan")
Flower_Pot00 = Object("Pot", "It's a flower pot.", "You take the flower pot. There is a note under it.", "You put down the flower pot.", ["You can't use a flower pot.", "You can't use a flower pot."], False, Type="flowerpot", On_Take=Pot_Take00)
Room00.Items.extend([Table00, Fan00, Flower_Pot00])

Light_Bulb10 = Object("Light Bulb", "Its a light bulb, it's on.", False, False, ["The light turns on.", "The light turns off."], True, Type="light")
Table10 = Object("Table", "It's another table, just like the one in the room to the west.", False, False, False, False, Type="table")
Note10 = Object("Note", "It's a note.", "You put the note in your pocket.", "You put the note down.", False, False, Text="Get the key and use it!", Type="note")

Table01 = Object("Table", "It's a table.", False, False, False, False, Type="table")
Key01 = Object("Key", "A golden key.", "You take the key.", "You put the key down.", ["You use the key. The door opens.", ''], False, On_Use=EndGame)

#Custom Commands:
def Read(Object):
    if Object.Type.lower() == "note":
        print(f"You read the note. It says:\n {Object.Text}")
CustomCommand_List.append(["read", Read])
