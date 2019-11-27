from Engine import *

def Win():
    print("You win!")
    exit()

def Fan1On():
    print("The fan blows down the wall to the north!")
    Room01 = Room([0, 1], "A dim room. It is lit by the room to the south.")
    Key00 = Object(Room01, "Key", Text_List=["It's a key. Maybe you shoud use it.", ["You win!", None], "You take the key.", "You put the key down."], Func_List=[None, [Win, None], None, None])

Room00 = Room([0, 0], "It is a pretty bright room.")

Fan1 = Object(Room00, "Fan", Text_List=["It's a fan.", ["You turn the fan on.", "You turn the fan off."], None, None], Func_List=[None, [Win, None], None, None])

while True:
    Parse(Input_Prompt=">>> ", Exit_Text="Bye.", No_Command="What?", No_Text="You can't do that!")
#NO CUSTOM COMMANDS FIX LATER
