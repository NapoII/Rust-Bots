################################################################################################################################
#Test_2
from Imports import*
#config_dir = file_path +"/config.ini

Low_Fish_Region = parse_int_tuple(read_config(config_dir, "CV_Region", "Low_Fish_Region"))
Low_Fish_png = file_path_Bilder+"Low_Fish.png"
Bait_for_Fish_png = file_path_Bilder+"Bait_for_Fish.png"
Bait_for_Fish_Region = parse_int_tuple(read_config(config_dir, "CV_Region", "Bait_for_Fish_Region"))
Gut_Fish_Region = parse_int_tuple(read_config(config_dir, "CV_Region", "Gut_Fish_Region"))
Start_pos = (700, 617)
pos_jump = 100
Gut_pos = parse_int_tuple(read_config(config_dir, "CV_Region", "Gut_pos"))
Zeit_pause(3)

def Find_the_bait(Start_pos, ):
    log ("Find_the_bait")
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
                    Bait_for_Fish = IF_Img(Bait_for_Fish_png, Bait_for_Fish_Region, 0.75, "Bait_for_Fish")
                    if Bait_for_Fish == True:
                        return pos
                    if Bait_for_Fish == False:
                        break
            if x == 5:
                x = -1
                break