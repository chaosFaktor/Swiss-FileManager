import glob
import os, sys
import termios
import tty


orig_settings = termios.tcgetattr(sys.stdin)





KeyXa = "6"
KeyXs = "4"
KeyYa = "2"
KeyYs = "8"
KeyBack = "7"
KeySelect = "5"
#keyHandleAsDir = "d"
#keyHandleasFile = "f"
#keyExecuteTerminal = "x"
KeyQuit = "q"
KeyArchiveManager = "a"

in1=""

path = []

arr = [
"------------------",
"Bitte Pfad angeben:",
""
]
for i in arr:
    print(i)

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
in1 = str(input("»"))
path.append(str(in1))

if len(path) == 0:
    path.append("./")


loop1 = True
selx = 0
sely = 0

while loop1:
    dirs = []
    files = []

    pathstr = ""
    for i in path:
        pathstr = pathstr + i


    dirandfile = os.listdir(pathstr)

    for i in dirandfile:
        if os.path.isdir(pathstr + "/" + i):

            dirs.append(i)
        else:

            files.append(i)




#    for i in dirandfile:
#        if "." in str(i):
#            print("")
#        else:
#            dirs.append(i)
#            dirandfile.remove(i)
#    for i in dirandfile:
#        if "." in i:
#            files.append(i)


    if sely == -1:
        dotdot = "O|.."
    else:
        dotdot = " |.."
    arr = [
    "Path:",
    str(pathstr),
    "-"*80,
    "\n",
    dotdot
    ]
    os.system("clear")
    print("sely " + str(sely))
    for i in arr:
        print(i)


    dirs_am = 0

    for i in dirs:
        if selx == 0 and sely == dirs_am:
            print("O|" + str(i))
        else:
            print(" |" + str(i))
        dirs_am = dirs_am + 1

    print("/"*80)

    files_am = 0
    for i in files:
        if selx == 1 and sely == files_am:
            print("O|" + str(i))

        else:
            print(" |" + str(i))


        files_am = files_am + 1

    print(in1)
    tty.setcbreak(sys.stdout)
    in1 = sys.stdin.read(1)[0]

    os.system("clear")

    if in1 == KeyXs and selx!=0:
        selx = 0
        sely = 0
    if in1 == KeyXa and selx!=1:
        selx = 1
        sely = 0
    if in1 == KeyYs:
        sely = sely - 1
    if in1 == KeyYa:
        sely = sely + 1
    if in1 == KeyQuit:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
        loop1=False
        os.system("clear")
        quit()
    if in1 == KeySelect:
        if selx == 0:
            if path[-1] == "/":
                path.append(str(dirs[sely]))
            else:
                path.append("/" + str(dirs[sely]))
        if selx == 1:
            print("\n")
            print("Bitte Befehl eingeben um mit " + str(files[sely]) + " zu interagieren ('handleasdir' um die Datei als Ordner zu verwenden)")
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
            in2 = input("» ")



            if in2 == "handleasdir":

                if path[-1] == "/":
                    path.append(str(files[sely]))
                else:
                    path.append("/" + str(files[sely]))
            else:
                os.system(in2 + " " + str(pathstr) + str(files[sely]))
    if in1 == KeyBack:
        del path[-1]
    if in1 == KeyArchiveManager:
        loop2 = True
        while loop2:
            os.system("clear")





    if len(files) == 0:
        selx = 0
    if len(dirs) == 0:
        selx = 1

    if selx <= -1:
        selx = 0
    if selx > 1:
        selx = 1
    if sely < -1:
        sely = -1
    if selx == 1 and sely >= len(files):
        sely = len(files) - 1
    if selx == 0 and sely >= len(dirs):
        sely = len(dirs) - 1

    dirandfile = []
    if len(path) == 0:
        path.append("./")


termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
