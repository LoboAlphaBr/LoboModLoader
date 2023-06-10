import os
import configparser
import shutil
from datetime import datetime

VERSION = '0.0.1'
########################################### STUFF I GUESS ################################


def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')
clearTerminal()


class colors:
    PINK = '\033[95m' 
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    NORMAL = '\033[0m'
    BOLD = '\033[1m'
    SUBL = '\033[4m'



def start():
    print('\n')
    print(f'{colors.BLUE}Options:'
            '\n'f'{colors.YELLOW}exit{colors.NORMAL}: 'f'{colors.GREEN}Exits'
            '\n'f'{colors.YELLOW}new'f'{colors.NORMAL} >name<:'f'{colors.GREEN} Creates Modpack'
            '\n'f'{colors.YELLOW}list{colors.NORMAL}: 'f'{colors.GREEN}Lists Your Current Modpacks'
            '\n'f'{colors.YELLOW}remove {colors.NORMAL}>name<: 'f'{colors.GREEN}Moves Modpack To Trashcan'
            '\n'f'{colors.YELLOW}emptycan{colors.NORMAL}: 'f'{colors.GREEN}Clears Trashcan (will erase every deleted modpack)'
            '\n'f'{colors.YELLOW}recovery {colors.NORMAL}>name<: 'f'{colors.GREEN}Tries To Recovery Given Modpack'
            '\n'f'{colors.YELLOW}save{colors.NORMAL} >name<: 'f'{colors.GREEN} Save Current Loaded Modpack Into Given Name'
            '\n'f'{colors.YELLOW}load {colors.NORMAL}>name<: 'f'{colors.GREEN}Loads The Choosen Modpack'
            '\n'f'{colors.YELLOW}rename {colors.NORMAL}>name< >newname<: 'f'{colors.GREEN} Rename Modpack'

            
            #'\n'f'{colors.YELLOW} 'f'{colors.GREEN}'
            #'\n'f'{colors.YELLOW} 'f'{colors.GREEN}'
            #'\n'f'{colors.YELLOW} 'f'{colors.GREEN}'
            #'\n'f'{colors.YELLOW} 'f'{colors.GREEN}'
            #'\n'f'{colors.YELLOW} 'f'{colors.GREEN}'
            f'{colors.NORMAL}')








################################################# BODY OF THE SCRIPT ##################################

config = configparser.ConfigParser()
config.read('config.cfg')
TLTESTFOLDER = config['TLDIRECTORY']['TLDIRECTORY']


TLFolder =              f'{TLTESTFOLDER}'

ModsDir               = TLFolder+r'\game\mods\\'
LoboModLoaderPATH     = TLFolder+r'\game\LoboModLoader'
Trashcan              = LoboModLoaderPATH+r'\Trashcan\\'
MODPACKFOLDER         = TLFolder+r'\game\LoboModLoader\Modpacks\\'


#initialize
if not os.path.exists(LoboModLoaderPATH):
    os.makedirs(LoboModLoaderPATH)

if not os.path.exists(MODPACKFOLDER):
    os.makedirs(MODPACKFOLDER)

if not os.path.exists(Trashcan):
    os.makedirs(Trashcan)

def getCurrentDate():
    x = datetime.now()
    x = x.strftime("%d-%m-%Y-%H-%M-%S")
    return x

def makeFoldersInModpack(name, mods):  #, scrips, resourcepacks, config, resources
    os.makedirs(MODPACKFOLDER+str(name+"/"+str(mods)))
    #os.makedirs(MODPACKFOLDER+str(name+"/"+str(scrips)))
    #os.makedirs(MODPACKFOLDER+str(name+"/"+str(resourcepacks)))
    #os.makedirs(MODPACKFOLDER+str(name+"/"+str(config)))
    #os.makedirs(MODPACKFOLDER+str(name+"/"+str(resources)))

def createModpack(name):
    try:
        os.makedirs(MODPACKFOLDER+str(name))
        makeFoldersInModpack(name, 'mods')
        print(f'{colors.GREEN}Modpack Created: {colors.NORMAL}{colors.BOLD}{name}{colors.NORMAL}')
    except:
        print(f'{colors.RED}ERROR: Could not create modpack')
        pass

def removeModpack(modpack):
    try:
        shutil.move(f'{MODPACKFOLDER}{modpack}', f'{Trashcan}')
        print(f'{colors.CYAN}Deleted: {colors.NORMAL}{colors.BOLD}{modpack}{colors.NORMAL}')
    except:
        print(f'{colors.RED}ERROR: Could not delete modpack: {modpack} (make sure it exists){colors.NORMAL}')

    pass

def clearTrashcan():
    shutil.rmtree(f'{Trashcan}')
    print(f'{colors.CYAN}Trashcan Cleared!{colors.NORMAL}')

def recoveryFromTrashcan(modpack):
    try:
        shutil.move(f'{Trashcan}{modpack}', f'{MODPACKFOLDER}')
    except:
        print(f'{colors.RED}ERROR: Could not recovery: {modpack}')

def saveModpack(name):
    os.makedirs(f'{MODPACKFOLDER}{name}\mods')
    x = f'{MODPACKFOLDER}{name}\mods'
    try:
        for i in os.listdir(ModsDir):
            shutil.move(f'{ModsDir}{i}',f'{x}')
    except:
        print(f'{colors.RED}ERROR: Could not save modpack!')
        pass

def loadModpack(name):
    yorn = input(f'{colors.CYAN}Do you with to save the current loaded modpack? y/n \n {colors.PINK}> {colors.NORMAL}')
    match yorn:
        case 'y':
            saveModpack(f'modpack-{getCurrentDate()}')
            for i in os.listdir(f'{MODPACKFOLDER}{name}\mods'):
                shutil.copy(f'{MODPACKFOLDER}{name}\mods\{i}', TLFolder+r'\game\mods')
        case 'n':
            for i in os.listdir(f'{MODPACKFOLDER}{name}\mods'):
                shutil.copy(f'{MODPACKFOLDER}{name}\mods\{i}', TLFolder+r'\game\mods')
        case _:
            print(f'{colors.RED}ERROR: answer with only \'y\' or \'n\'{colors.NORMAL}')

def renameModpack(name, newname):
    try:
        shutil.move(f'{MODPACKFOLDER}{name}',f'{MODPACKFOLDER}{newname}')
        
    except:
        print(f'{colors.RED}ERROR: Could not rename {name}!')
        pass

def getModpacks():
    x = os.listdir(LoboModLoaderPATH+'/Modpacks')
    return x

def printModpacks():
    x = getModpacks()
    print(f'{colors.GREEN}Current Modpacks: {colors.NORMAL}')
    for i in x:
        try:
            y = len(os.listdir(f'{MODPACKFOLDER}/{i}/mods/'))
            
        except:
            y = '0'
        print(f'{colors.BOLD}> {i}{colors.NORMAL} {y} mods')

########################################### START STUFF ##########################################
print(f'{colors.PINK}Welcome To Lobo ModLoader! {VERSION}{colors.NORMAL}')
print(f'\n{colors.GREEN}Serving On Folder: \'{TLFolder}\' {colors.NORMAL}')




############################################### MAIN LOOP ###########################################

while True:
    start()
    x = input(f'{colors.PINK} > {colors.NORMAL}')
    x = x.split(' ', 2)

    match x[0]:
        case 'exit':
            clearTerminal()
            break
        case 'new':
            clearTerminal()
            createModpack(x[1])
            pass
        case 'list':
            clearTerminal()
            printModpacks()
            pass
        case 'remove':
            clearTerminal()
            removeModpack(x[1])
            pass
        case 'emptycan':
            clearTerminal()
            clearTrashcan()
        case 'recovery':
            clearTerminal()
            recoveryFromTrashcan(x[1])
        case 'save':
            saveModpack(x[1])
        case 'load':
            loadModpack(x[1])
        case 'rename':
            renameModpack(x[1], x[2])
        
        
        case _:
            clearTerminal()
            print(f'{colors.RED}Input Incorrect, Try Again')
            print(x)
             