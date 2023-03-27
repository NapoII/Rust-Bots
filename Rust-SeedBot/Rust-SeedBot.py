py_name = "Rust-SeedBot" 
v = "0.0.1"
####################################################################################################
# #   Intro

f0 =  """ 


- """ + py_name + """
- created by Napo_II
- """ + v + """
- python 3.10.7
- https://github.com/NapoII/

"""
print(" \nProgramm wird gestartet ...")

####################################################################################################
#import

import os
import os, sys
import time
import pyautogui
from Imports import*
import webbrowser

################################################################################################################################
#PreSet Programm

file_path = os.path.dirname(sys.argv[0])
file_path_Bilder = file_path + "/Bilder/"
file_path_Work_Folder = file_path + "/Work_Folder/"


Doku_Folder = Folder_gen (py_name, "Documents/")
Log_Folder = Folder_gen ("Log", ("Documents/"+str(py_name)))
Log_File_name = Datei_name_mit_Zeit ("LogFile-"+str(py_name))
Log_File = Erstelle_TextDatei (Log_File_name, Log_Folder, f0 + "Log-File:\n---------------------------------------------------------------------------------------\n")

Bot_Path = os.path.dirname(sys.argv[0])
config_dir = file_path +"/config.ini"

log ( "Bot_Path: ["+str(Bot_Path) + "]\n")

################################################################################################################################
# Load Config

#x = read_config(config_dir, section, option)

gen_pos__list_x = (797,824,851,879,905,933)
gen_pos_y = 300
gen_pos_w = 18
gen_pos_h = 18

G_Gen_img = file_path_Bilder + "G.png"
H_Gen_img = file_path_Bilder + "H.png"
W_Gen_img = file_path_Bilder + "W.png"
X_Gen_img = file_path_Bilder + "X.png"
Y_Gen_img = file_path_Bilder + "Y.png"

Full_GenList = []



################################################################################################################################
#Programm Folder erstellen wenn nötig
Mess_Projekte_dir = Folder_gen_raw("Seed-GenListen", Doku_Folder )
Mess_Projekte_list = create_Projekt_list(Mess_Projekte_dir)

#Projekte anlegen oder öffnen
Mess_Projekte_list.append("Neu")
Projekt_name = pyautogui.confirm(text='Wähle ein Mess Projekt aus oder erstlle ein neues!', title='Seed-Bot', buttons= Mess_Projekte_list)
if Projekt_name == "Neu":
    Projekt_name = pyautogui.prompt(text='Wie soll das neue Seed-Bot Projekt heißen?', title='Seed-Bot - Neu' , default='')
    Projekt_dir = Folder_gen_raw(Projekt_name, Mess_Projekte_dir)

else:
    Projekt_dir = f"{Mess_Projekte_dir}/{Projekt_name}/"

# Erstlle oder öffne csv Datei
csv_file_list = list_all_txt_files(Projekt_dir)


if len(csv_file_list) == 0 :

    Seed_art = pyautogui.confirm(text='Wähle ein Die Seed Art aus!', title='Seed-Bot', buttons= ["Hemp","Blue Berry", "Green Berry", "Red Berry", "White Berry", "Yellow Berry", "Andere"])
    if Seed_art == "Andere":
        Seed_art = pyautogui.prompt(text='Welche Seed Art?', title='Seed-Bot - Neu' , default='Kuerbis')

    Projekt_name_plus_timestemp = Datei_name_mit_Zeit(Seed_art)
    Projekt_csv_file = Erstelle_TXT_Datei( Projekt_name_plus_timestemp, Projekt_dir, f"genes" )
    File_name = Projekt_csv_file
else:
    csv_file_list.append("Neu")
    Projekt_csv_file = pyautogui.confirm(text='Wähle ein Seed aus oder erstlle ein neues!', title='Seed-Bot - File', buttons = csv_file_list)
    if Projekt_csv_file == "Neu":
        Seed_art = pyautogui.confirm(text='Wähle ein Die Seed Art aus!', title='Seed-Bot', buttons= ["Hemp","Blue Berry", "Green Berry", "Red Berry", "White Berry", "Yellow Berry", "Andere"])
        if Seed_art == "Andere":
            Seed_art = pyautogui.prompt(text='Welche Seed Art?', title='Seed-Bot - Neu' , default='Kuerbis')

        Projekt_name_plus_timestemp = Datei_name_mit_Zeit(Seed_art)
        Projekt_csv_file = Erstelle_TXT_Datei( Projekt_name_plus_timestemp, Projekt_dir, f"genes" )
        File_name = path_to_Fiel_name(Projekt_csv_file)
    else:
        Projekt_csv_file =f"{Projekt_dir}/{Projekt_csv_file}"
        File_name = path_to_Fiel_name(Projekt_csv_file)


# Main Programm


def Item_box_pos(A0_pos,max_x, max_y):

    pos_list = []
    A0_pos_x = A0_pos[0]
    A0_pos_y = A0_pos[1]

    y = -1
    while True:
        y = y + 1
        if y == max_y:
            break

        A0_pos_y_2 = A0_pos_y + 100*y


        x = -1
        while True:
            x = x + 1
            if x == max_x:
                
                break
            Pos_slot_x_2 = A0_pos_x + 100*x
            new_pos = (Pos_slot_x_2, A0_pos_y_2)
            pos_list.append(new_pos)
    return(pos_list)


Large_box_A0_pos = (1300,200)
Frisge_A0_pos = (1300,500)

Large_box_max_y = 8
Frisge_max_y = 5

max_x = 6

list = Item_box_pos(Large_box_A0_pos, max_x, Large_box_max_y)

list_len = len(list)
x = -1

if_Rust_aktiv()
while True:
    x = x + 1
    if x == list_len:
        break
    Pos_ = list[x]
    Pos_x = Pos_[0] 
    Pos_y = Pos_[1]

    print(Pos_x, Pos_y)
    if_Rust_aktiv()
    pyautogui.moveTo(Pos_x, Pos_y)
    pyautogui.click()
    #Zeit_pause(0.1)

    Gen_genetik_full = ""

    X = -1

    while True:
        X = X + 1
        if X == 6:
            break

        gen = (gen_pos__list_x[X],gen_pos_y,gen_pos_w,gen_pos_h)

        while True:
            Gen_bool = IF_Img(G_Gen_img, gen, 0.75, "G Gen")
            if Gen_bool == True:
                Gen_genetik = "G"
                break

            Gen_bool = IF_Img(H_Gen_img, gen, 0.75, "H Gen")
            if Gen_bool == True:
                Gen_genetik = "H"
                break

            Gen_bool = IF_Img(W_Gen_img, gen, 0.75, "W Gen")
            if Gen_bool == True:
                Gen_genetik = "W"
                break

            Gen_bool = IF_Img(X_Gen_img, gen, 0.75, "X Gen")
            if Gen_bool == True:
                Gen_genetik = "X"
                break

            Gen_bool = IF_Img(Y_Gen_img, gen, 0.75, "Y Gen")
            if Gen_bool == True:
                Gen_genetik = "Y"
                break

            Gen_genetik = False
            break
        
        if Gen_genetik == False:
            break
        Gen_genetik_full = Gen_genetik_full + Gen_genetik

    print(Gen_genetik_full)
    Full_GenList.append(Gen_genetik_full)

Full_GenList = remove_empty_strings(Full_GenList)
print(Full_GenList)
write_lines_to_file(Full_GenList, Projekt_csv_file)

webbrowser.open(Projekt_dir)
webbrowser.open(r"https://wgn.si/genetics/")
    





