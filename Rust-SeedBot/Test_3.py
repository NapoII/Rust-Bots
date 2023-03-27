################################################################################################################################
#Test_3
from Imports import*
#config_dir = file_path +"/config.ini

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

Inhalt = f"genes"

if len(csv_file_list) == 0 :

    Seed_art = pyautogui.confirm(text='Wähle ein Die Seed Art aus!', title='Seed-Bot', buttons= ["Hemp","Blue Berry", "Green Berry", "Red Berry", "White Berry", "Yellow Berry", "Andere"])
    if Seed_art == "Andere":
        Seed_art = pyautogui.prompt(text='Welche Seed Art?', title='Seed-Bot - Neu' , default='Kuerbis')

    Projekt_name_plus_timestemp = Datei_name_mit_Zeit(Seed_art)
    Projekt_csv_file = Erstelle_TXT_Datei( Projekt_name_plus_timestemp, Projekt_dir, Inhalt )
    File_name = Projekt_csv_file
else:
    csv_file_list.append("Neu")
    Projekt_csv_file = pyautogui.confirm(text='Wähle ein Seed aus oder erstlle ein neues!', title='Seed-Bot - File', buttons = csv_file_list)
    if Projekt_csv_file == "Neu":
        Seed_art = pyautogui.confirm(text='Wähle ein Die Seed Art aus!', title='Seed-Bot', buttons= ["Hemp","Blue Berry", "Green Berry", "Red Berry", "White Berry", "Yellow Berry", "Andere"])
        if Seed_art == "Andere":
            Seed_art = pyautogui.prompt(text='Welche Seed Art?', title='Seed-Bot - Neu' , default='Kuerbis')

        Projekt_name_plus_timestemp = Datei_name_mit_Zeit(Seed_art)
        Projekt_csv_file = Erstelle_TXT_Datei( Projekt_name_plus_timestemp, Projekt_dir, Inhalt )
        File_name = path_to_Fiel_name(Projekt_csv_file)
    else:
        Projekt_csv_file =f"{Projekt_dir}/{Projekt_csv_file}"
        File_name = path_to_Fiel_name(Projekt_csv_file)

