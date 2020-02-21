def HoleL_Key():
    KeyL = Object(RoomL, "Key", Text_List=["It's a golden key. Maybe you can use it to unlock that door you saw earlier.", ["You use the key.", "You use the key."], "You take the key.", None], Func_List=[None, [KeyL_Use, KeyL_Use], None, None])

def KeyL_Use():
    if Player.Pos == [0, 0, 0]:
        Player.Item_Table.pop("key")
        RoomR.Look = "It is a garden with a fountain in it."
    else:
        print("There's nothing to use it on here!")

def TrashL_Can():
    if "trashcan" in list(FindRoom().Item_Table.keys()) and "trash" in list(FindRoom().Item_Table.keys()) or list(Player.Item_Table.keys()):
        Player.Item_Table.pop("trash")
        print("You throw the trash away in the trash can.")
    else:
        print("You throw the trash on the ground")

#Short term:
#Only ever use roomlist no rooms specific names
#Fix Parse
#Make functions to add fucntions to objects or rooms
#make functions to add args included in the one to add functions
#do some other stuff


#Long term:
#Make saves
#Write documentation
#Make characters you can talk to and shops you can buy from
#SpellCheck
RoomC = Room([0, 0, 0], "It is a pretty bright room.")
RoomCU = Room([0, 0, 1], "It is the roof of the house you were just in. There is no other way but down. To the west there is a garden with a fountain, to the east there is a fenced field, and to the north and south there is a forest that surrounds everything in sight.")
RoomL = Room([-1, 0, 0], "It is a fenced in field.")
RoomR = Room([1, 0, 0], "locked.")

FanC = Object(RoomC, "Fan", Text_List=["It's a pretty big fan.", ["You turn the fan on.", "You turn the fan off."], None, None])
TableC = Object(RoomC, "Table", Text_List=["It's a big table that is made from brown wood.", [None, None], None, None])
CupC = Object(RoomC, "Cup", Text_List=["It's a blue cup with some water in it.", ["You drink the water.", "You drink the water."], "You take the cup.", "You put the cup down."])

HoleL = Object(RoomL, "Hole", Text_List=["It's a hole in the ground with a key in it.", [None, None], None, None], Func_List=[HoleL_Key, [None, None], None, None])
PlantL = Object(RoomL, "Plant", Text_List=["It's a green plant with probably like 73 leaves.", [None, None], "You take the plant.", "You leave the plant."])
TrashL = Object(RoomL, "Trash", Text_List=["It's trash.\n", [None, None], "You pick up the trash.\n", None], Func_List=[None, [None, None], None, TrashL_Can], No_Text='', End='')

TrashCanCU = Object(RoomCU, "TrashCan", Text_List=["It's a trash can with nothing in it.", [None, None], None, None], Func_List=[None, [TrashL_Can, TrashL_Can], None, None])

FountainR = Object(RoomR, "Fountain", Text_List=["It's a fountain with a lever on the side.", [None, None], None, None])
LeverR = Object(RoomR, "Lever", Text_List=["It's a lever attached to the fountain.", [None, None], None, None]) #Func_List=[None, [LeverR_Func_On, LeverR_Func_Off], None, None])

print(f"This is a very short example game.\n{FindRoom().DynamicText()}")
Start()
