from Config import *

def Parse(Input):
    Input = Input.lower().split()

    i = 0
    Start = "No Value"
    while i < len(Input): #See where the first function word is in the list "In"
        if Input[i] in Commands:
            Start = i
            break
        else:
            i = i + 1

    try:
        if Start == "No Value":
            print("What do you want to do?")
            pass
        elif Input[Start] not in ["go"]:
            if Input[(Start + 1)] in Not:
                if Input[(Start + 2)] in Not:
                    Offset = 3
                else:
                    Offset = 2
            else:
                Offset = 1
            Command_Table[Input[Start]](Object_Table[Input[(Start + Offset)]])
        elif Input[Start] in ["go"]:
            if Input[(Start + 1)] in Not:
                if Input[(Start + 2)] in Not:
                    Offset = 3
                else:
                    Offset = 2
            else:
                Offset = 1
            Command_Table[Input[Start]](Input[(Start + Offset)])
        pass
    except Exception as e:
        e = e.__class__.__name__
        if e == "IndexError":
            print("What do you want to do?")
        elif e == "KeyError":
            print("That doesn't exist. You might have typed it wrong.")
        pass

def FindRoom():
    return 0

def Look(Object):
    try:
        if Object in FindRoom().Items:
            print(Object.Look)
            return 0
        else:
            print(f"{Object.Name} isn't here!")
            return 0
        pass
    except:
        pass
    return 1

def Use(Object):
    try:
        if Object in FindRoom().Items:
            print(Object.Use)
            return 0
        else:
            print(f"{Object.Name} isn't here!")
            return 0
        pass
    except:
        pass
    return 1

def Take(Object):
    try:
        if Object in FindRoom().Items:
            if type(Object.Take).__name__ == "str":
                print(Object.Take)
                Player.Items.append(Object)
                FindRoom().Items.pop(FindRooms.Items.index(Object))
                return 0
            else:
                print(f"{Object.Name} doesn't move!")
                return 0
            pass
        else:
            print(f"{Object.Name} isn't here!")
            return 0
        pass
    except:
        pass
    return 1

def Leave(Object):
    try:
        if Object in FindRoom().Items:
            if type(Object.Take).__name__ == "str":
                print(Object.Leave)
                FindRoom().Items.append(Object)
                Player.Items.Pop(Player.Items.index(Object))
                return 0
            else:
                print(f"{Object.Name} doesn't move... wait a second...")
                return 0
        else:
            print(f"{Object.Name} isn't here!")
            return 0
    except:
        pass
    return 1

def WhereIs(Object):
    try:
        if type(Object).__name__ == "Player":
            print(f"{Object.Pos[0]}, {Object.Pos[1]}")
            return Object.Pos
        else:
            print(f"{RoomList.Items.index(Object).Pos[0]}, {RoomList.Items.index(Object).Pos[1]}")
            return RoomList.Items.index(Object).Pos
        pass
    except:
        pass
    return 1

def Go(Direction):
    OldPos = Player.Pos
    try:
        Direction_Table = {"west": -1, "east": 1, "south": -1, "north": 1}
        if Direction in ["west", "east"]:
            Player.Pos[0] = Player.Pos[0] + Direction_Table[Direction]
            if type(FindRoom()).__class__.__name__ == "Room":
                print(FindRoom().Go)
                return 0
            else:
                pass
        elif Direction in ["south", "north"]:
            Player.Pos[1] = Player.Pos[1] + Direction_Table[Direction]
            if type(FindRoom()).__class__.__name__ == "Room":
                print(FindRoom().Go)
                return 0
            else:
                pass
        print("You can't go there!")
        Player.Pos = OldPos
        print(FindRoom().Go)
        return 0
    except:
        pass
    return 1

Commands = ["go", "look", "use", "take", "leave", "where"]
Not = ["at", "to", "am", "that", "the"]
Command_Table = {"go": Go, "look": Look, "use": Use, "take": Take, "leave": Leave, "where": WhereIs}

while True:
    Parse(input(In_Prompt))
