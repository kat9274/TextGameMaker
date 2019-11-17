from Config import *

def Parse(Input):
    Input = Input.lower().split()

    i = 0
    Start = "No Value"  # Set Start to "No Value" so that if there is no start word it will know
    while i < len(Input):  # See where the first function word is in the list "Input"
        if Input[i] in Commands:
            Start = i
            break
        else:
            i = i + 1

    try:
        if Start == "No Value":  # If there's no command
            print("What do you want to do?")
            pass

        elif Input[Start] in ["stop", "end", "exit", "done", "leave"]:
            exit()

        elif Input[Start] not in ["go"]:  # If the command is not "go"
            try:  # Needs the try so when IndexError is raised it will look at the room
                i = 0
                while Input[(Start + i)] not in ObjectsName:
                    i = i + 1
                    pass
                Offset = i
                Command_Table[Input[Start]](Object_Table[Input[(Start + Offset)]])  # Run the command
            except IndexError:
                Command_Table[Input[Start]](FindRoom(Player.Pos))
        elif Input[Start] in ["go"]:
            i = 0
            while Input[(Start + i)] not in ["north", "south", "east", "west"]:
                i = i + 1
                pass
            Offset = i
            Command_Table[Input[Start]](Input[(Start + Offset)])  # Run the command
        pass
    except Exception as e:  # Errors
        e = e.__class__.__name__
        if e == "IndexError":
            print("What do you want to do?")
        elif e == "KeyError":
            print("That doesn't exist. You might have typed it wrong.")

def FindRoom(Pos):
    i = 0
    while i < len(RoomList):
        if RoomList[i].Pos == Pos:  # Where room pos == "Pos"
            return RoomList[i]
        else:
            i = i + 1
            pass

def Look(Object):
    try:
        # Print the look text or say the object isnt here
        print(Object.Look if Object in FindRoom(Player.Pos).Items else f"{Object.Name} isn't here!")
        return 0
    except:
        return 1

def Use(Object):
    try:
        # If the object is in the rooms items list
        if Object in FindRoom(Player.Pos).Items:
            # Print the Use text most appropriate
            print(Object.Use[int(Object.On)])
            Object.On = not Object.On  # Toggle on
            if Object.On_Use != False:
                if Object.Args != (False, False):
                    Object.On_Use(Object.Args)
                else:
                    Object.On_Use()
        else:
            print(f"{Object.Name} isn't here!")
        return 0
    except:
        return 1

def Take(Object):
    try:
        if Object in FindRoom(Player.Pos).Items:
            if type(Object.Take).__name__ == "str":  # If the object is takeable
                print(Object.Take)
                Player.Items.append(Object)
                FindRoom(Player.Pos).Items.pop(FindRooms.Items.index(Object))
            else:
                print(f"{Object.Name} doesn't move!")
        else:
            print(f"{Object.Name} isn't here!")
        return 0
    except:
        return 1

def Leave(Object):
    try:
        if Object in Player.Items:
            print(Object.Leave)  # Just do the opposite of take
            FindRoom(Player.Pos).Items.append(Object)
            Player.Items.Pop(Player.Items.index(Object))
            return 0
    except:
        return 1

def WhereIs(Object):
    try:
        if type(Object).__name__ == "Player":  # If player
            print(f"{Object.Pos[0]}, {Object.Pos[1]}")  # Find player
            return Object.Pos
        else:
            print(f"{RoomList.Items.index(Object).Pos[0]}, {RoomList.Items.index(Object).Pos[1]}")
            return RoomList.Items.index(Object).Pos
    except:
        return 1

def Go(Direction):
    try:
        Direction_Table = {"west": [0, -1], "east": [0, 1], "south": [1, -1], "north": [1, 1]}  # Table
        Player.Pos[Direction_Table[Direction][0]] = Player.Pos[Direction_Table[Direction][0]] + Direction_Table[Direction][1]
        if str(type(FindRoom(Player.Pos)).__name__) == "Room":
            print(FindRoom(Player.Pos).Look)  # If the room exists print
        else:
            # If it doesnt exist print and reset the pos
            print("You cant go there!")
            Player.Pos[Direction_Table[Direction][0]] = Player.Pos[Direction_Table[Direction][0]] - Direction_Table[Direction][1]
        return 0
    except:
        return 1

Commands = ["go", "look", "use", "take", "leave", "where", "stop", "end", "exit", "done", "leave"]
Command_Table = {"go": Go, "look": Look, "use": Use, "take": Take, "leave": Leave, "where": WhereIs}

i = 0
while i < len(CustomCommand_List):
    if len(CustomCommand_List) > 0:
        Command_Table[CustomCommand_List[i][0]] = CustomCommand_List[i][1]
        Commands.append(CustomCommand_List[i][0])
    i = i + 1

while True:
    Parse(input(In_Prompt))
