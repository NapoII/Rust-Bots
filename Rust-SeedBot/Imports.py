py_name = "Rust-SeedBot"
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

import os
import os, sys
import time
import pyautogui
from configparser import ConfigParser
import urllib
import numpy as np
import cv2
from win32gui import GetWindowText, GetForegroundWindow

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


def Screanshot(window_rect, Img_name, file_path_Bilder):
    #0, 0, 1920, 1080 fullscrean

    Page_img_dir = file_path_Bilder + Img_name + ".png"
 
    myScreenshot = pyautogui.screenshot(region=(window_rect))   # Screanshot
    myScreenshot.save(r""+ Page_img_dir)
    return Page_img_dir

def IF_Img(Img_dir, region, Genauigkeit, Text):
    #if_Rust_aktiv()
    Screanshot(region, "TEST", file_path_Bilder)
    myScreenshot = pyautogui.screenshot(region=(region))   # Screanshot
    open_cv_image = np.array(myScreenshot) 
    # Convert RGB to BGR 
    myScreenshot = open_cv_image[:, :, ::-1].copy()
    button = cv2.imread(Img_dir, cv2.IMREAD_UNCHANGED)

    result = cv2.matchTemplate(myScreenshot, button, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val > Genauigkeit:       # Genauigkeits abfrage
        print (f"{Text}: max_val={max_val} --> (True)")
        return True
    else :
        print (f"{Text}: max_val={max_val} --> (False)")
        return False

def Folder_gen_raw(Folder_Name, Folder_dir ):
    #    Erstellt einen neuen Ordner, falls er noch nicht vorhanden ist.
    #
    #       Args:
    #           folder_name (str): Der Name des zu erstellenden Ordners.
    #           folder_dir (str): Das Verzeichnis, in dem der Ordner erstellt werden soll.
    #
    #       Returns:
    #           str: Der vollständige Pfad des erstellten Ordners."""


   print("Ordner Struktur wird überprüft und ggf. angelegt...\n")
   folder = Folder_Name
    #C:\Users\Napo_II/Documents//Energy_Log
   full_path = f"{Folder_dir}/{Folder_Name}/"
   if os.path.exists(full_path):                       # Prüft datei pfad nach exsistänz Ture/False
      print("Ordner Struktur existiert bereits")
      print("  ->   " + str(full_path))
   else:                                               # Erstellt Ordner falls nicht vorhadnen
      os.makedirs(full_path)
      log(f"Der Ordner [{folder}] wurde erstellt im Verzeichnis:\n  ->   {full_path}" )
      print("\n")
   return(full_path)


def create_Projekt_list(dir):
    # Leere Liste, in die die Ordnernamen eingetragen werden
    folder_list = []

    # Durchlaufe alle Elemente im Verzeichnis
    for entry in os.scandir(dir):
    # Wenn das Element ein Ordner ist
        if entry.is_dir():
        # Trage den Ordnernamen in die Liste ein
            folder_list.append(entry.name)
    # Ausgabe der Liste mit den Ordnernamen
    return(folder_list)

def list_all_txt_files(dir):

    # Leere Liste, in die die Dateinamen eingetragen werden
    csv_file_list = []

    # Durchlaufe alle Elemente im Ordner
    for entry in os.scandir(dir):
    # Wenn das Element eine Datei ist und die Endung ".csv" hat
        if entry.is_file() and entry.name.endswith('.txt'):
            # Trage den Dateinamen in die Liste ein
            csv_file_list.append(entry.name)

    # Ausgabe der Liste mit den Dateinamen
    return(csv_file_list)

def Erstelle_TXT_Datei( Text_File_name, save_path, Inhalt ):

    """Erstellt eine neue Textdatei, falls sie noch nicht vorhanden ist, und füllt sie mit dem angegebenen Inhalt.

    Args:
        Text_File_name (str): Der Name der Textdatei.
        save_path (str): Der Pfad, in dem die Textdatei gespeichert werden soll.
        Inhalt (str): Der Inhalt, der in die Textdatei geschrieben werden soll.

    Returns:
        str: Der vollständige Pfad der erstellten Textdatei.

    """

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

def path_to_Fiel_name(dir):
    # Extrahiere den Dateinamen mit der os.path-Funktion basename
    filename = os.path.basename(dir)

    # Extrahiere den Dateinamen ohne die Endung mit der os.path-Funktion splitext
    name_without_extension = str(os.path.splitext(filename)[0])

    return(name_without_extension)

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

def remove_empty_strings(lst):
    return [x for x in lst if x != '']

def write_lines_to_file(lst, filepath):
    with open(filepath, 'w') as f:
        f.write('genes\n')
        for item in lst:
            f.write(item + '\n')