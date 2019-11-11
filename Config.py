class Object:
    def __init__(self, Name, Look, Use, Take, Leave, On_Use, Args, On):
        #got rid of pos in favor of items lists
        self.Name = Name #String
        self.Look = Look #String
        self.Use = Use #List
        self.Take = Take #String
        self.Leave = Leave #String

        self.On_Use = On_Use #Function
        self.Args = Args #Tuple
        self.On = On #Bool

class Player:
    def __init__(self):
        self.Pos = [0, 0] #List
        self.Items = [] #List
Player = Player() #Define "Player"

class Room:
   def __init__(self, Pos, Look):
        self.Pos = Pos #List
        self.Items = [self] #List
        self.Look = Look #String

#Rooms:
Room00 = Room([0, 0], "A pretty plain room. There is a fan here. The wall to the east seems strange.")

#Funcs:
def Fan_Blows_Room00():
    Fan.Use[0] = "The fan turns on"
    Room10 = Room([1, 0], "")
    Room00.Look = "A pretty plain room. There is a fan here. The wall to the east has a door."
    RoomList.append(Room10)

#Objects:
Fan = Object("Fan", "It's a old fan.", ["The fan turns on. The wind from the fan blows a door to the west open.", "The fan turns off."], False, False, Fan_Blows_Room00, (False, ), False)
Room00.Items.append(Fan)

Object_Table = {'i': Player, "me": Player, "fan": Fan}
RoomList = [Room00]
In_Prompt = ">>> "
