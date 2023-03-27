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

from calendar import SATURDAY
import os
import os, sys
import time
from numpy import true_divide
import pyautogui
from Imports import*

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
Inventar_Region = parse_int_tuple(read_config(config_dir, "CV_Region", "Inventar_Region"))
Bait_Region = parse_int_tuple(read_config(config_dir, "CV_Region", "Bait_Region"))
New_Fish_Region = parse_int_tuple(read_config(config_dir, "CV_Region", "New_Fish_Region"))
Low_Fish_Region = parse_int_tuple(read_config(config_dir, "CV_Region", "Low_Fish_Region"))
Start_pos = parse_int_tuple(read_config(config_dir, "CV_Region", "Start_pos"))
Gut_Fish_Region = parse_int_tuple(read_config(config_dir, "CV_Region", "Gut_Fish_Region"))
Bait_for_Fish_Region = parse_int_tuple(read_config(config_dir, "CV_Region", "Bait_for_Fish_Region"))
pos_jump =  int((read_config(config_dir, "CV_Region", "pos_jump")))
Gut_pos = parse_int_tuple((read_config(config_dir, "CV_Region", "Gut_pos")))
New_fish_png = file_path_Bilder+"New_fish.png"
Bait_png = file_path_Bilder +"Bait.png"
Inventar_png = file_path_Bilder +"Inventar.png"
Low_Fish_png = file_path_Bilder +"Low_Fish.png"
Bait_for_Fish_png = file_path_Bilder +"Bait_for_Fish.png"
Gut_png = file_path_Bilder +"Gut.png"

Broken_Region = parse_int_tuple(read_config(config_dir, "CV_Region", "Broken_Region"))
Broken_png = Low_Fish_png = file_path_Bilder +"Broken.png"
################################################################################################################################
# Main ProgrammSD



print(New_Fish_Region)
Zeit_pause(2)
Screanshot(New_Fish_Region, "TEST", file_path_Bilder)
Bait = IF_Img(Broken_png, Broken_Region, 0.68   , "Bait") 
