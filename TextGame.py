from Config import * #Import the config

# TODO:
# MAKE IT TO WHERE YOU CAN USE MULTIPLE OBJECTS WITH SAME NAME

def Parse(Input):
    Input = Input.lower().split() #Get the input and split it up

    i = 0
    while i < len(Input):
        if Input[i] in Commands: #If the str in Input[i] is a command then set that to start
            Start = i
            break
        else:
            i = i + 1

    try:
        if Start.__class__.__name__ == "nonetype": #If there is no command then print
            print("What do you want to do?")
            pass

        elif Input[Start] in ["stop", "end", "exit", "done", "leave"]: #If the command is an exit command leave
            exit()

        elif Input[Start] not in ["go"]: #If the command is not go
            try:
                i = 0
                while Input[(Start + i)] not in ObjectsName: #Find the object
                    i = i + 1
                    pass
                Offset = i
                Command_Table[Input[Start]](Object_Table[Input[(Start + Offset)]]) #Run the command
            except IndexError: #If there is no object use the room as the object
                Command_Table[Input[Start]](FindRoom(Player.Pos))

        elif Input[Start] in ["go"]: #If the command is go
            i = 0
            while Input[(Start + i)] not in ["north", "south", "east", "west"]: #Find the direction
                i = i + 1
                pass
            Offset = i
            Command_Table[Input[Start]](Input[(Start + Offset)]) #Run the command
        pass
    except Exception as e:
        e = e.__class__.__name__
        if e == "IndexError": #If there is nothing to do print
            print("What do you want to do?")
        elif e == "KeyError": #If the object doesn't exist
            print("That doesn't exist. You might have typed it wrong.")

def FindRoom(Pos):
    i = 0
    while i < len(RoomList):
        if RoomList[i].Pos == Pos:
            return RoomList[i]
        else:
            i = i + 1
            pass

def Look(Object):
    if Object in FindRoom(Player.Pos).Items:
        print(Object.Look)
        if Object.On_Look.__class__.__name__ != "nonetype":
            if Object.Args_Look.__class__.__name__ != "nonetype":
                Object.On_Look(Object.Args_Look)
            else:
                Object.On_Look()
    else:
        print(f"{Object.Name} isn't here!")

def Use(Object):
    if Object in FindRoom(Player.Pos).Items:
        print(Object.Use[int(Object.On)])
        Object.On = not Object.On
        if Object.On_Use.__class__.__name__ != "nonetype":
            if Object.Args_Use.__class__.__name__ != "nonetype":
                Object.On_Use(Object.Args_Use)
            else:
                Object.On_Use()
    else:
        print(f"{Object.Name} isn't here!")

def Take(Object):
    if Object in FindRoom(Player.Pos).Items:
        if type(Object.Take).__name__ == "str":
            print(Object.Take)
            Player.Items.append(Object)
            FindRoom(Player.Pos).Items.pop(FindRooms.Items.index(Object))
            if Object.On_Take.__class__.__name__ != "nonetype":
                if Object.Args_Take.__class__.__name__ != "nonetype":
                    Object.On_Take(Object.Args_Take)
                else:
                    Object.On_Take()
        else:
            print(f"{Object.Name} doesn't move!")
    else:
        print(f"{Object.Name} isn't here!")

def Leave(Object):
    if Object in Player.Items:
        print(Object.Leave)
        FindRoom(Player.Pos).Items.append(Object)
        Player.Items.Pop(Player.Items.index(Object))
        if Object.On_Leave.__class__.__name__ != "nonetype":
            if Object.Args_Leave.__class__.__name__ != "nonetype":
                Object.On_Leave(Object.Args_Leave)
            else:
                Object.On_Leave()

def WhereIs(Object):
    try:
        if type(Object).__name__ == "Player": #If the object is the player print their position
            print(f"{Object.Pos[0]}, {Object.Pos[1]}")
            return Object.Pos
        else: #If its not then get the object pos
            print(f"{RoomList.Items.index(Object).Pos[0]}, {RoomList.Items.index(Object).Pos[1]}")
            return RoomList.Items.index(Object).Pos
    except:
        return 1

def Go(Direction):
    try:
        Direction_Table = {"west": [0, -1], "east": [0, 1], "south": [1, -1], "north": [1, 1]}
        Player.Pos[Direction_Table[Direction][0]] = Player.Pos[Direction_Table[Direction][0]] + Direction_Table[Direction][1]
        if str(type(FindRoom(Player.Pos)).__name__) == "Room":
            print(FindRoom(Player.Pos).Look)
        else:
            print("You cant go there!")
            Player.Pos[Direction_Table[Direction][0]] = Player.Pos[Direction_Table[Direction][0]] - Direction_Table[Direction][1]
        return 0
    except:
        return 1

Commands = ["go", "look", "use", "take", "leave", "where", "stop", "end", "exit", "done", "leave"]
Command_Table = {"go": Go, "look": Look, "use": Use, "take": Take, "leave": Leave, "where": WhereIs}

i = 0
while i < len(CustomCommand_List): #Add CustomCommand_List to Command_Table
    if len(CustomCommand_List) > 0:
        Command_Table[CustomCommand_List[i][0]] = CustomCommand_List[i][1]
        Commands.append(CustomCommand_List[i][0])
    i = i + 1

while True:
    Parse(input(In_Prompt))
