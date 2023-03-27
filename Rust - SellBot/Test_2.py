################################################################################################################################
from Imports import *

file_path = os.path.dirname(sys.argv[0])
file_path_Bilder = file_path + "/Bilder/"
file_path_Work_Folder = file_path + "/Work_Folder/"

Bot_Path = os.path.dirname(sys.argv[0])
config_dir = file_path +"/config.ini"


Bot_aktiv = read_config(config_dir, "Telegram", "Bot_aktiv")
print((Bot_aktiv))
print(type(Bot_aktiv))

print("\n TEst:")
if Bot_aktiv == "True":
    Bot_aktiv = True
else:
    Bot_aktiv = False

"""

Bot_aktiv = bool(Bot_aktiv)
print(type(Bot_aktiv))"""

if Bot_aktiv == True:
    print("IS TRUE")
if Bot_aktiv == False:
    print(" IS False")
if  Bot_aktiv != True and Bot_aktiv != False:  
    print(Bot_aktiv)
    print(type(Bot_aktiv))
    print("wrong")