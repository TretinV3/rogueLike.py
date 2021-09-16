from colorama import init
init()
from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()


mapLevel = None

def main():
    print('\033[2J')
    mapLevel = loadLevel("level1")
    #print(mapLevel)
    printLevel(mapLevel)

def loadLevel(name):
    textFile = open("./"+name+".map", "r").read()
    sizeI = len(textFile.split("\n"))
    arr = []
    for i in range(sizeI):
        sizeJ = len(textFile.split("\n")[i])

        coln = []
        for j in range(sizeJ):
            coln.append(textFile.split("\n")[i][j])
        arr.append(coln)
    return arr

def printLevel(level):
    for i in range(len(level)):
        string = ""
        for j in range(len(level[i])):
            string += ' ' + getColoredCaracter(level[i][j]) + ' '
        print(string)
    

def getColoredCaracter(char):
    if char == "#":
        return '#'
    if char == "@":
        return '@'
    return ' '



if __name__ == '__main__':
    main()
