################################################################################################################################
#Test_1
#from Imports import*
#config_dir = file_path +"/config.ini

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



max_x = 6
max_y = 5
A0_pos = (1300,500)
list = Item_box_pos(A0_pos,max_x, max_y)

print(list)