class Object:
    def __init__(self, Usable, Takeable, Look_Text, Name, Pos, Use_The_Following, Use_Text, Take_Text):
        self.Usable = Usable #Bool
        self.Takeable = Takeable #Bool
        self.Pos = Pos #List
        self.Look = Look_Text #String
        self.Name = Name #String
        if Use_The_Following:
            self.Use = Use_Text #String
            self.Take = Take_Text #String

class Player:
    def __init__(self):
        self.Pos = [2, 2] #List
Player = Player() #Define "Player"

class Room:
   def __init__(self, Pos, Look_Text, Go_Text):
        self.Pos = Pos #List
        self.Look = Look_Text #String
        self.Go = Go_Text #String
        

