"""Full Doku on: https://github.com/NapoII/Rust_Wheel_of_Fortune"
-----------------------------------------------
!!! ADD MUST HAVE INFO !!
------------------------------------------------
"""

#### import

import os
import sys
import pyperclip
import pyautogui
import random
from util.__funktion__ import *


#### pre Var

file_path = os.path.normpath(os.path.dirname(sys.argv[0]))
config_dir = file_path + os.path.sep + "cfg"+ os.path.sep +"config.ini"


invbar_1 = read_config(config_dir, "pos", "invbar_1", "tuple")
scrap_num_pos = read_config(config_dir, "pos", "scrap_num_pos", "tuple")
scrap_split_pos = read_config(config_dir, "pos", "scrap_split_pos", "tuple")
invbar_1_region = read_config(config_dir, "pos", "invbar_1_region", "tuple")
scrap_max = read_config(config_dir, "pos", "scrap_max", "tuple")

bet_1 = read_config(config_dir, "pos", "bet_1", "tuple")
bet_3 = read_config(config_dir, "pos", "bet_3", "tuple")
bet_5 = read_config(config_dir, "pos", "bet_5", "tuple")
bet_10 = read_config(config_dir, "pos", "bet_10", "tuple")
bet_20 = read_config(config_dir, "pos", "bet_20", "tuple")

regions = {
    "bet_1": Region(bet_1[0], bet_1[1],bet_1[2], bet_1[3]),
    "bet_3": Region(bet_3[0], bet_3[1], bet_3[2], bet_3[3]),
    "bet_5": Region(bet_5[0], bet_5[1], bet_5[2], bet_5[3]),
    "bet_10": Region(bet_10[0], bet_10[1], bet_10[2], bet_10[3]),
    "bet_20": Region(bet_20[0], bet_20[1], bet_20[2], bet_20[3]),
    }

#### Main
log(f'Programme has been started!','green')

while True:
    while True:
        
        print("STart Region cheack")
        region_name = detect_click_in_regions(regions)

        if region_name == "bet_1" or region_name == "bet_3" or region_name == "bet_5" or region_name == "bet_10" or region_name == "bet_20":
            rust = if_Rust_aktiv()
            if rust == True:
                log (f"Region click on {region_name}")
                break 
            else:
                pass
        else:
            pass

    
    invbar_1_region_x = invbar_1_region[0]
    invbar_1_region_y = invbar_1_region[1]
    invbar_1_region_h = invbar_1_region[2]
    invbar_1_region_w = invbar_1_region[3] 

    clipboard_content_sum = 0
    scrap_in_regio_Slots = 0
    x = -1
    while True:
        x = x + 1
        if x == 6:
            break
        invbar_region_x = invbar_1_region_x + (95 * (x))
        invbar_region = (invbar_region_x, invbar_1_region_y, invbar_1_region_h, invbar_1_region_w)
        print(invbar_region)

        scrap_in_regio = IF_Img(r"Rust_Wheel_of_Fortune\img\scrap.png", invbar_region, 0.75, "Cheack for Scrap in Region")
        if scrap_in_regio == True:
            scrap_in_regio_Slots = scrap_in_regio_Slots + 1

    if scrap_in_regio_Slots == 0:
        break
    
    
    x = -1
    while True:
        x = x + 1
        if x == scrap_in_regio_Slots:
            break


        ran = (random.uniform(0.1, 0.2))
        invbar_x = invbar_1[0] + (x*95)
        invbar_y = invbar_1[1]
        invbar = (invbar_x,invbar_y)

        log(f"moveTo -> {invbar}")
        pyautogui.moveTo(invbar[0],invbar[1], ran)
        log(f"Click -> {invbar}")
        pyautogui.click()

        log(f"moveTo -> {scrap_max}")
        pyautogui.moveTo(scrap_max[0],scrap_max[1], ran)
        log(f"Click -> {scrap_max}")
        pyautogui.click()

        log(f"moveTo -> {scrap_num_pos}")
        pyautogui.moveTo(scrap_num_pos[0],scrap_num_pos[1], ran)
        log(f"right Click -> {scrap_num_pos}")
        pyautogui.click(button='right')
        pyautogui.hotkey('ctrl', 'c')

        clipboard_content = int(pyperclip.paste())
        clipboard_content_sum = clipboard_content_sum + clipboard_content

        log(f"clipboard_content= {clipboard_content}")

    if region_name == "bet_1":
        gam_val = (clipboard_content_sum / 100) * 1
        drag_to_bet = bet_1[0]+15,bet_1[1]+15

    if region_name == "bet_3":
        gam_val = (clipboard_content_sum / 100) * 1
        drag_to_bet = bet_3[0]+15,bet_3[1]+15

    if region_name == "bet_5":
        gam_val = (clipboard_content_sum / 100) * 5
        drag_to_bet = bet_5[0]+15,bet_5[1]+15

    if region_name == "bet_10":
        gam_val = (clipboard_content_sum / 100) * 2.5
        drag_to_bet = bet_10[0]+15,bet_10[1]+15

    if region_name == "bet_20":
        gam_val = (clipboard_content_sum / 100) * 1
        drag_to_bet = bet_20[0]+15,bet_20[1]+15

    if gam_val < 1 :
        gam_val = 1

    print(gam_val)
    gam_val = (int(gam_val))

    pyperclip.copy(f"{gam_val}")

    if scrap_in_regio_Slots > 1 :

        log(f"moveTo -> {invbar_1}")
        pyautogui.moveTo(invbar_1[0],invbar_1[1], ran)
        log(f"Click -> {invbar_1}")
        pyautogui.click()

        log(f"moveTo -> {scrap_num_pos}")
        pyautogui.moveTo(scrap_num_pos[0],scrap_num_pos[1], ran)
        log(f"right Click -> {scrap_num_pos}")
        pyautogui.click(button='right')

    pyautogui.hotkey('ctrl', 'v')


    log(f"moveTo -> {scrap_split_pos}")
    pyautogui.moveTo(scrap_split_pos[0],scrap_split_pos[1], ran)

    pyautogui.dragTo(drag_to_bet[0], drag_to_bet[1], ran, button='left')