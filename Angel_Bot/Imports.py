py_name = "Angel_Bot"
v = "0.0.1"
f0I = """
              .#:                                 
             .#MM:                                
            .#MMMM:                ,+%%+          
            %MMMMMM:            .+@MMMMM.         
           +MMMMMMMM:          ,@MMMMMM:          
          ,MMMMMMMMMM:        ,MMMMMMM:           
          %MMMMMMMMMMM:      .@MMMMMM:            
         :@MMMMMMMMMMM@      #MMMMMM:             
        %MMMMMMMMMMMM@.     ,MMMMMM:              
       %MMMMMMMMMMMM@.      #MMMMM#               
      :MMMMMMMMMMMM@.      .MMMMMMM.          ,+  
      #MMMMMMMMMMM#.       ,MMMMMMM:         :MM. 
     :MMMMMMMMMM#:         ,MMMMMMM%        :MMM. 
    .MMMMMMMMMM@.          ,MMMMMMM@       :MMMM. 
    #MMMMMMMMMMM@.         ,MMMMMMMM:.    :MMMM@  
   ,MMMMMMMMMMMMM@.        .MMMMMMMMMM@%::MMMMM%  
   %MMMMMMMMMMMMMM@.        #MMMMMMMMMMMMMMMMMM,  
  .MMMMMM@+,MMMMMMM@.      :MMMMMMMMMMMMMMMMMM#   
  ,MMMMM%.  ,MMMMMMM@.    +MMMMMMMMMMMMMMMMMM@.   
  +MMMM+     ,MMMMMMM@.  +MMMMMMMMMMMMMMMMMMM,    
  %MMM%       ,MMMMMMM@.+MMMMMMMMMMMMMMMMMM@,     
  %MMM.        ,MMMMMMMMMMMMMMMMMMMMMMMMMM%.      
  %MM+          ,MMMMMMMMMMMMMMMM+:%###%:.        
  +MM,           ,MMMMMMMMMMMMMM+                 
  ,MM             ,MMMMMMMMMMMM+                  
   @#             .#MMMMMMMMMM#                   
   ..            .#MMMMMMMMMMMM+                  
                .#MMMMMMMMMMMMMM+                 
               .#MMMMMMMMMMMMMMMM+                
              .#MMMMMMMMMMMMMMMMMM+               
             .@MMMMMMMMMMMMMMMMMMMM+              
            .@MMMMMMMMMMMMMMMMMMMMMM+             
           .@MMMMMMMMMM@%MMMMMMMMMMMM+            
          ,@MMMMMMMMMM@. %MMMMMMMMMMMM+           
         ,@MMMMMMMMMM@.   %MMMMMMMMMMMM+          
        ,@MMMMMMMMMM@,     %MMMMMMMMMMMM+         
       ,MMMMMMMMMMM@,       %MMMMMMMMMMMM+        
      ,MMMMMMMMMMMM,         %MMMMMMMMMMMM+       
     :MMMMMMMMMMMM,           %MMMMMMMMMMMM+      
    :MMMMMMMMMMMM:             %MMMMMMMMMMMM+     
   :MMMMMMMMMMMM:               %MMMMMMMMMMMM+    
  ,MMMMMMMMMMMM:                 %MMMMMMMMMMMM+   
  @MM#+@MMMMMM+                   %MMMMMMMMMMMM:  
 ,MM%  .MMMMM+                     %MMMMMMMMMMMM. 
 :MM+   @MMM+                       %MMMMMMMMMMM: 
 :MM#. ,MMM%                         %MMMMMMMMMM: 
 .MMM@#MMM%                           %MMMMMMMMM, 
  +MMMMMM%                             %MMMMMMM@. 
   :@MM@:                               %MMMMMM,  
     ,.                                  :#M@%,
   


- Imports
- created by Napo_II
- """ + v + """
- python 3.10.7
- https://github.com/NapoII/

"""
####################################################################################################
#import

from ast import While
import os
import os, sys
import time
import pyautogui
from configparser import ConfigParser
import urllib
import numpy as np
import cv2
from win32gui import GetWindowText, GetForegroundWindow
import requests
import pyimgur
import json
####################################################################################################
#def

def Folder_gen(Folder_Name, Folder_dir ):
   print("Ordner Struktur wird überprüft und ggf. angelegt...\n")
   folder = Folder_Name
   dir = "~/"+str(Folder_dir)+"/"+str(folder)           # gibt gewünschten Datei-Pfad an
   full_path = os.path.expanduser(dir)                 # ergänzt datei pfad mit PC User name
   if os.path.exists(full_path):                       # Prüft datei pfad nach exsistänz Ture/False
      print("Ordner Struktur existiert bereits")
      print("  ->   " + str(full_path))
   else:                                               # Erstellt Ordner falls nicht vorhadnen
      os.makedirs(full_path)
      print("Der Ordner ["+folder+"] wurde erstellt im Verzeichnis:" )
      print("  ->   " + str(full_path))
   print("\n")
   return(full_path)

def Datei_name_mit_Zeit(FileName):
    Date = Date_Time=(time.strftime("%d_%m-%Y-%H.%M"))        # Generiert date formater
    FullName = (FileName+"-"+(Date))                           # Generiert Datei name
    return FullName

def Erstelle_TextDatei( Text_File_name, save_path, Inhalt ):
    complete_Path_Text = os.path.join(save_path+"\\"+Text_File_name+".txt")     # Path + text datei name
    if os.path.exists(complete_Path_Text):
        return complete_Path_Text
    else:
        print("\nTextdatei ["+str(Text_File_name)+".txt] wird erstellt...")
        file1 = open(complete_Path_Text, "w")                                         # Datei erstellen
        #toFile = input("Write what you want into the field")                   # Datei input def.
        file1.write(Inhalt)                                                    # Datei wird gefüllt mit input
        file1.close()
        return complete_Path_Text

def Fill_Datei(dir, toFill, Attribut):
    file1 = open(dir, Attribut,encoding="utf-8")                                 # Datei wird geöffnet
    #print("Datei ["+str(dir) + "] wird beschrieben und gespeichtert...\n")
    file1.write(toFill)                                             # Datei wird gefüllt mit input
    file1.close()

def TimeStemp():
    TimeStemp = Date_Time=(time.strftime("%d_%m-%Y_%H:%M:%S"))
    return TimeStemp

def log(Log_input):
    Fill_Datei(Log_File, TimeStemp()+" --> " + Log_input+"\n", "a")
    print (TimeStemp()+" --> " + Log_input+"\n")

def Zeit_pause(seconds):
    print(f"Pause für {seconds}")
    start_time = time.time()
    while True:                             # Zeit schelife startet
        current_time = time.time()
        elapsed_time = current_time - start_time        # berechung rest Zeit
        if elapsed_time > seconds:
            break

def read_config(config_dir, section, option):
    config = ConfigParser()
    config.read(config_dir)
    load_config = (config[section][option])

    print("Config geladen: [ "+(option) +" = "+ (load_config)+" ]")

    return load_config

def write_config(config_dir, section, Key, option):

    config = ConfigParser()
    # update existing value
    config.read(config_dir)
    try:
        config.add_section(section)
    except:
        pass
    config.set(section, Key,option) #Updating existing entry 
    with open(config_dir, 'w') as configfile:
        config.write(configfile)
    print ("\nEinstellungs änderung -> "+str(config_dir)+"\n"+"["+str(section)+"]\n"+str(Key)+" = " + str(option)+"\n")

def Download_from_link(link, dir):
    link = "https://i.imgur.com/Mk1KPNa.png"
    dir = "E://Pr0grame//My_ Pyhton//work_in_progress//Discord-Ticket-Bot//Bilder//Test.png"
    urllib.request.urlretrieve(link, dir)
    log ("Img download [" +link + "] und gespeichert in [ "+dir+ " ]")
    return dir

def parse_int_tuple(input):
    return tuple(int(k.strip()) for k in input[1:-1].split(','))

def parse_tuple(input):
    return tuple(k.strip() for k in input[1:-1].split(','))

def str_to_bool(input):
    if input == "True":
        input = True
    else:
        input = False
    return input

################################################################################################################################
#PreSet Programm

file_path = os.path.dirname(sys.argv[0])
file_path_Bilder = file_path + "/Bilder/"
file_path_Work_Folder = file_path + "/Work_Folder/"
config_dir = file_path +"/config.ini"


Doku_Folder = Folder_gen (py_name, "Documents/")
Log_Folder = Folder_gen ("Log", ("Documents/"+str(py_name)))
Log_File_name = Datei_name_mit_Zeit ("LogFile-"+str(py_name))
Log_File = Erstelle_TextDatei (Log_File_name, Log_Folder, f0I + "Log-File:\n---------------------------------------------------------------------------------------\n")

Bot_Path = os.path.dirname(sys.argv[0])
log ( "Bot_Path: ["+str(Bot_Path) + "]\n")


################################################################################################################################
log ("Imports geladen : [" +str(file_path) + "/Imports.py]")
################################################################################################################################
#def spez.

def IF_Img(Img_dir, region, Genauigkeit, Text):
    if_Rust_aktiv()
    Screanshot(region, "TEST", file_path_Bilder)
    myScreenshot = pyautogui.screenshot(region=(region))   # Screanshot
    open_cv_image = np.array(myScreenshot) 
    # Convert RGB to BGR 
    myScreenshot = open_cv_image[:, :, ::-1].copy()
    button = cv2.imread(Img_dir, cv2.IMREAD_UNCHANGED)

    result = cv2.matchTemplate(myScreenshot, button, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val > Genauigkeit:       # Genauigkeits abfrage
        log (f"{Text}: max_val={max_val} --> (True)")
        return True
    else :
        log (f"{Text}: max_val={max_val} --> (False)")
        return False

def Gut_all_LowFish(Start_pos, pos_jump, Low_Fish_png, Low_Fish_Region, Gut_png, Gut_Fish_Region, Gut_pos):
    if_Rust_aktiv()
    log ("Gut all Low Fish")
    x = -1
    y = -1
    while True:
        y = y + 1
        if y == 4:
            break
        while True:
            x = x + 1
            pos = ((Start_pos[0]+(pos_jump*x)),(Start_pos[1]+(pos_jump*y)))
            pyautogui.moveTo(pos[0], pos[1], 0.3)
            pyautogui.click()
            Low_Fish = IF_Img(Low_Fish_png, Low_Fish_Region, 0.75, "Low Fish")
            if Low_Fish == True:
                while True:
                    Gut_Fish = IF_Img(Gut_png, Gut_Fish_Region, 0.75, "Gut_Fish")
                    if Gut_Fish == True:
                        pyautogui.moveTo(Gut_pos)
                        pyautogui.click()
                    if Gut_Fish == False:
                        break
            if x == 5:
                x = -1
                break


def Find_the_bait(Start_pos, pos_jump, Bait_for_Fish_png, Bait_for_Fish_Region,):
    if_Rust_aktiv()
    log ("Find_the_bait")
    x = -1
    y = -1
    while True:
        y = y + 1
        if y == 4:
            return False, pos
        while True:
            x = x + 1
            pos = ((Start_pos[0]+(pos_jump*x)),(Start_pos[1]+(pos_jump*y)))
            pyautogui.moveTo(pos[0], pos[1], 0.3)
            pyautogui.click()
            while True:
                Bait_for_Fish = IF_Img(Bait_for_Fish_png, Bait_for_Fish_Region, 0.75, "Bait_for_Fish")
                if Bait_for_Fish == True:
                    return True, pos
                if Bait_for_Fish == False:
                    break
            if x == 5:
                x = -1
                break


def Angel_auswerfen():
    if_Rust_aktiv()
    log("Angel auswerfen.")
    pyautogui.mouseDown(button='right')  # press the right button down
    Zeit_pause(1.3)
    # move the mouse to 100, 200, then release the right button up.
    print("1111111111")
    pyautogui.click()
    pyautogui.mouseUp(button='right')

def Fisch_Dril(Img_dir, region, Genauigkeit, Telegram_token, fullscrean, CLINT_ID_imgur, chat_Id):
    log("Fish drill.")
    
    key_down_time = 1.3
    Key_up_Time = 2.1
    if_Rust_aktiv()
    TeleBot_scr_run(Telegram_token, fullscrean, CLINT_ID_imgur, chat_Id)

    Dril = True
    New_Fish = IF_Img(Img_dir, region, Genauigkeit, "New Fish",)
    if New_Fish == True:
        Dril = False
        return Dril
    Zeit_pause(Key_up_Time)
    pyautogui.keyDown('S')  # hold down the shift key
    pyautogui.keyDown('A')  # hold down the shift key
    New_Fish = IF_Img(Img_dir, region, Genauigkeit, "New Fish")
    if New_Fish == True:
        Dril = False
        return Dril
    Zeit_pause(key_down_time)
    pyautogui.keyUp('S')    # release the shift key
    pyautogui.keyUp('A')    # release the shift key
    New_Fish = IF_Img(Img_dir, region, Genauigkeit, "New Fish")
    if New_Fish == True:
        Dril = False
        return Dril
    Zeit_pause(Key_up_Time)
    pyautogui.keyDown('S')  # hold down the shift key
    pyautogui.keyDown('D')  # hold down the shift key
    New_Fish = IF_Img(Img_dir, region, Genauigkeit, "New Fish")
    if New_Fish == True:
        Dril = False
        return Dril
    Zeit_pause(key_down_time)
    pyautogui.keyUp('S')    # release the shift key
    pyautogui.keyUp('D')    # release the shift key
    return Dril

def parse_int_tuple(input):
    return tuple(int(k.strip()) for k in input[1:-1].split(','))

def Screanshot(window_rect, Img_name, file_path_Bilder):
    #0, 0, 1920, 1080 fullscrean

    Page_img_dir = file_path_Bilder + Img_name + ".png"
 
    myScreenshot = pyautogui.screenshot(region=(window_rect))   # Screanshot
    myScreenshot.save(r""+ Page_img_dir)
    return Page_img_dir

def open_inv(Img_dir_inv, region_inv, Genauigkeit_inv):
    if_Rust_aktiv()
    Zeit_pause(0.5)
    while True:
        Inventar = IF_Img(Img_dir_inv, region_inv, Genauigkeit_inv, "Inventar")
        if Inventar == False:
            log("Open Inventar.")
            pyautogui.press('Tab')
            Zeit_pause(0.5)
        if Inventar == True:
            return True

def close_inv(Img_dir_inv, region_inv, Genauigkeit_inv):
    if_Rust_aktiv()
    Zeit_pause(0.5)
    while True:
        Inventar = IF_Img(Img_dir_inv, region_inv, Genauigkeit_inv, "Inventar")
        if Inventar == True:
            log("Close Inventar.")
            pyautogui.press('Tab')
            Zeit_pause(0.5)
        if Inventar == False:
            return False

def if_Rust_aktiv():
    while True:
        aktiv_window = (GetWindowText(GetForegroundWindow()))
    
        if aktiv_window == "Rust":
            return True
        
        else :
            log ("Rust ist zurzeit nicht das aktive Fenster.\n\nAktiv: " + str(aktiv_window))
            print ("TAB in RUST!")
            pyautogui.alert("Rust ist zurzeit nicht das aktive Fenster. Bitte öffne Rust!")
            Zeit_pause(3)

###
#Telegramm Bot

def TeleBot_Say(Text, chat_Id, token):
    params = {"chat_id":chat_Id, "text":Text}
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    message = requests.post(url, params=params)
def TeleBot_img(Name, PATH, CLINT_ID, chat_Id, token ):

    ## Imgur Upload
    #CLINT_ID = "fb9b5757ec16f06"
    im = pyimgur.Imgur(CLINT_ID)
    uploaded_image = im.upload_image (PATH, title=Name)
    print("Imgur upload:\n" + "-----------------------------------------\n" + "Image Name: " + uploaded_image.title + "\n" + "Image Type: " + uploaded_image.type + "\n" + "Image größe: " +str((uploaded_image.size)/1000) +" KB" + "\n" + "-----------------------------------------\n" + uploaded_image.link + "\n")
    Url = uploaded_image.link

    ## Telegram imge send:
    # token = "5357034455:AAE785813q8L1np9oBoq0S6Vmyr9MB2F_oU"
    #chat_Id = "5322450822"
    params = {"chat_id":chat_Id, "photo":Url}
    url = f"https://api.telegram.org/bot{token}/sendphoto"
    message = requests.post(url, params=params)
    print ( "Bild: " )

def Last_Chat(token):
    answer = requests.get(f"https://api.telegram.org/bot{token}/getUpdates")
    content = answer.content
    data = json.loads(content)
    #print(data)
    num_updates = len(data["result"])
    last_update = num_updates - 1
    try: 
        text = data["result"][last_update]["message"]["text"]
    except:
        text = ""
    chat_id = data["result"][last_update]["message"]["chat"]["id"]
    Chat_Date_ID = data["result"][last_update]["message"]["date"]
    first_name = data["result"][last_update]["message"]["from"]["first_name"]
    last_name = data["result"][last_update]["message"]["from"]["last_name"]
    full_name = str(first_name) + " " + str(last_name)
    print((full_name) + " say: " +text)
    return text, chat_id ,Chat_Date_ID

def TeleBot_scr_run(Telegram_token, fullscrean, CLINT_ID_imgur, chat_Id):
    Last_chat_Data = Last_Chat(Telegram_token)
    chat_date_id = Last_chat_Data[2]

    if Last_chat_Data[0] == "/scr":

        log ("Screanshot wurde an den Telebot gesendet.")
        Screanshot_dir = Screanshot(fullscrean, "Rust - Screen", file_path_Bilder)
        TeleBot_img("Rust - Screen", Screanshot_dir, CLINT_ID_imgur, chat_Id, Telegram_token )


