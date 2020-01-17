import os, sys, getopt

try:
    args, none = getopt.getopt(sys.argv[1:], 'o:i:', ['output=', 'i='])
    for i in range(len(args)):
        if str(args[i][0]) == "-o":
            FileName = args[0][1]
        elif str(args[i][0]) == "-i":
            InputName = args[1][1]
except Exception as e:
    raise
    FileName = input("Input game name.\n>>> ")
    InputName = input('Input config file name.\n>>> ')
    pass

try:
    MakeFile = open(f"{FileName}.py", "x")
except Exception as e:
    if "y" in list(str(input("Overwrite?\n>>> "))):
        os.remove(f"{FileName}.py")
    else:
        exit()

NewFile = open(f"{FileName}.py", "a+")
ReadEngine = open(f"Engine.py", "r+")
ReadConfig = open(f"{InputName}.py", "r+")
NewFile.write(ReadEngine.read())
NewFile.write(ReadConfig.read())
NewFile.write('while True:\n    Parse(Input_Prompt=">>> ", Exit_Text="Bye.", No_Parse="What?")')
print("Done.\n")
