class Object:
    def __init__(self, Name, Look, Use, Take, Leave):
        #got rid of pos in favor of items lists
        self.Name = Name #String
        self.Look = Look #String
        self.Use = Use #List
        self.Take = Take #String
        self.Leave = Leave #String

        self.On_Use = False #Function
        self.Args = (False, ) #Tuple
        self.On = False #Bool

class Player:
    def __init__(self):
        self.Pos = [0, 0] #List
        self.Items = [] #List
Player = Player() #Define "Player"

class Room:
   def __init__(self, Pos, Look, Go):
        self.Pos = Pos #List
        self.Items = [self] #List
        self.Look = Look #String
        self.Go = Go #String

Object_Table = {'i': Player, "me": Player, "fan": Object}
RoomList = [Room]
In_Prompt = ">>> "
