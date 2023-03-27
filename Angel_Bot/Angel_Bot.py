
py_name = "Angel_Bot" 
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
import keyboard

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
Bot_aktiv = str_to_bool(read_config(config_dir, "Telegram", "Bot_aktiv"))
CLINT_ID_imgur = read_config(config_dir, "Imgur", "CLINT_ID_imgur")
Telegram_token = read_config(config_dir, "Telegram", "Telegram_token")
chat_Id = read_config(config_dir, "Telegram", "chat_Id")
fullscrean = parse_int_tuple(read_config(config_dir, "Imgur", "fullscrean"))
Broken_Region = parse_int_tuple(read_config(config_dir, "CV_Region", "Broken_Region"))
Broken_png = Low_Fish_png = file_path_Bilder +"Broken.png"
Inventar_Region = parse_int_tuple(read_config(config_dir, "CV_Region", "Inventar_Region"))
Bait_Region = parse_int_tuple(read_config(config_dir, "CV_Region", "Bait_Region"))
New_Fish_Region = parse_int_tuple(read_config(config_dir, "CV_Region", "New_Fish_Region"))
Low_Fish_Region = parse_int_tuple(read_config(config_dir, "CV_Region", "Low_Fish_Region"))
Start_pos = parse_int_tuple(read_config(config_dir, "CV_Region", "Start_pos"))
Gut_Fish_Region = parse_int_tuple(read_config(config_dir, "CV_Region", "Gut_Fish_Region"))
Bait_for_Fish_Region = parse_int_tuple(read_config(config_dir, "CV_Region", "Bait_for_Fish_Region"))
pos_jump =  int((read_config(config_dir, "CV_Region", "pos_jump")))
Gut_pos = parse_int_tuple((read_config(config_dir, "CV_Region", "Gut_pos")))
Slot1 = parse_int_tuple((read_config(config_dir, "CV_Region", "Slot1")))
New_fish_png = file_path_Bilder+"New_fish.png"
Bait_png = file_path_Bilder +"Bait.png"
Inventar_png = file_path_Bilder +"Inventar.png"
Low_Fish_png = file_path_Bilder +"Low_Fish.png"
Bait_for_Fish_png = file_path_Bilder +"Bait_for_Fish.png"
Gut_png = file_path_Bilder +"Gut.png"

Slot = Slot1
Slot_key = 1
################################################################################################################################
# Main ProgrammSD

hotkey = pyautogui.prompt(text='HOTKEY für abfrage Zeitraum bestimmen.', title=' X und Y Coredinate der Maus bestimmen' , default='p')
print ("Ready for [{hotkey}]")
while True:
    
    
    if keyboard.is_pressed(hotkey):

        #SDScreanshot_dir = Screanshot(fullscrean, f"{py_name}-Screen_Start", file_path_Bilder)
        #TeleBot_Say( f"{f0}\n------------------------\n {py_name} wurde gestartet.", chat_Id, Telegram_token)
        #TeleBot_img("Rust - Screen", Screanshot_dir, CLINT_ID_imgur, chat_Id, Telegram_token )

        print("go")
        Stop = False
        while True:
            TeleBot_scr_run(Telegram_token, fullscrean, CLINT_ID_imgur, chat_Id)
            if Stop == True:
                break
            if_Rust_aktiv()
            Zeit_pause(0.5)
            Inventar = open_inv(Inventar_png, Inventar_Region, 0.75,)
            Broken = IF_Img(Broken_png, Broken_Region, 0.68   , "Broken")
            if Broken == True:
                Slot_key = Slot_key + 1
                Broken_Region = ((Broken_Region[0]+pos_jump),Broken_Region[1],Broken_Region[2],Broken_Region[3])
                Slot = ((Slot[0]+pos_jump), Slot[1])
                pyautogui.moveTo(Slot[0], Slot[1], 0.5) 
                pyautogui.click()
                pyautogui.press(str(Slot_key))

                Zeit_pause(0.5)
            else:
                pyautogui.moveTo(Slot[0], Slot[1], 0.5) 
                pyautogui.click()
                Zeit_pause(0.5)
            Bait = IF_Img(Bait_png, Bait_Region, 0.75, "Bait") 
            if Bait == True:
                Inventar = close_inv(Inventar_png, Inventar_Region, 0.75,)
            if Bait == False:
                
                Bait_x = 0
                while True:
                    Bait_x = Bait_x + 1
                    
                    if Bait_x == 3:
                        Stop = True
                        print("Stop")
                        break
                    Inventar = open_inv(Inventar_png, Inventar_Region, 0.75, )
                    Fish_Bait = Find_the_bait(Start_pos, pos_jump, Bait_for_Fish_png, Bait_for_Fish_Region, )
                    
                    if Fish_Bait[0] == False:
                        Gut_all_LowFish(Start_pos, pos_jump, Low_Fish_png, Low_Fish_Region, Gut_png, Gut_Fish_Region, Gut_pos,)
                    if Fish_Bait[0] == True:
                        
                        break
                Real_Route_cheack = 0
                while True:
                    if Stop == True:
                        break
                    Inventar = open_inv(Inventar_png, Inventar_Region, 0.75, )
                    pos = Fish_Bait[1]
                    pyautogui.moveTo(pos[0], pos[1], 0.5) 
                    pyautogui.dragTo(Slot[0], Slot[1], 0.5, button='left')
                    Zeit_pause(0.5)
                    pyautogui.moveTo(Slot[0], Slot[1], 0.5) 
                    pyautogui.click()
                    Zeit_pause(0.5)
                    Bait = IF_Img(Bait_png, Bait_Region, 0.75, "Bait")
                    Real_Route_cheack = Real_Route_cheack + 1
                    if Real_Route_cheack == 3:
                        Stop = True
                        break
                    Inventar = close_inv(Inventar_png, Inventar_Region, 0.75,)
                    if Bait == True and Inventar == False:
                        break
            Zeit_pause(4.5)
            Broken = IF_Img(Broken_png, Broken_Region, 0.68   , "Broken")
            if Broken == True:
                Slot_key = Slot_key + 1
                Broken_Region = ((Broken_Region[0]+pos_jump),Broken_Region[1],Broken_Region[2],Broken_Region[3])
                Slot = ((Slot[0]+pos_jump), Slot[1])
                pyautogui.moveTo(Slot[0], Slot[1], 0.5)
                pyautogui.click()
                Zeit_pause(0.5)

            Angel_auswerfen()
            Zeit_pause(3.82)
            x_Drill_Cheak = 0
            while True:
                x_Drill_Cheak = x_Drill_Cheak + 1
                log(f"x_Drill_Cheak = {x_Drill_Cheak}/15")
                if x_Drill_Cheak == 15:
                    Screanshot_dir = Screanshot(fullscrean, f"{py_name}-Drill_Fail", file_path_Bilder)
                    TeleBot_Say( f"{f0}\n------------------------\n {py_name} Drill Fail. {x_Drill_Cheak}/15", chat_Id, Telegram_token)
                    TeleBot_img("Rust - Screen", Screanshot_dir, CLINT_ID_imgur, chat_Id, Telegram_token )
                    print ("Ready for [{hotkey}]")
                    break
                if Stop == True:
                    Screanshot_dir = Screanshot(fullscrean, f"{py_name}-Stop", file_path_Bilder)
                    TeleBot_Say( f"{f0}\n------------------------\n {py_name} StopSA.", chat_Id, Telegram_token)
                    TeleBot_img("Rust - Screen", Screanshot_dir, CLINT_ID_imgur, chat_Id, Telegram_token )
                    print ("Ready for [{hotkey}]")
                    break  
                Dril = Fisch_Dril(New_fish_png, New_Fish_Region, 0.75, Telegram_token, fullscrean, CLINT_ID_imgur, chat_Id)
                if Dril == False:
                    break
