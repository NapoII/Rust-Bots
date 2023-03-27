################################################################################################################################
#Test_2
from Imports import*
#config_dir = file_path +"/config.ini

gen_pos__list_x = (797,824,851,879,905,933)
gen_pos_y = 300
gen_pos_w = 18
gen_pos_h = 18

G_Gen_img = file_path_Bilder + "G.png"
H_Gen_img = file_path_Bilder + "H.png"
W_Gen_img = file_path_Bilder + "W.png"
X_Gen_img = file_path_Bilder + "X.png"
Y_Gen_img = file_path_Bilder + "Y.png"

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

    Gen_genetik_full = Gen_genetik_full + Gen_genetik

print(Gen_genetik_full)
