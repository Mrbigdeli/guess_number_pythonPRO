import random
#################################################
#################################################
lst_positive = ["y", "Y", "YY", "yY","Yy", "yy", "yes", "yeah", "yeh", "yeahe",
                "Yes", "YES", "Yeah", "Yeah", "YEH", "Yeh", "آره", "YEAH"]
lst_negetive = ["n", "N", "nn", "NN", "Nn", "nN", "No", "NO", "nO", "no"
                "n0", "nop", "nope"]
lst_UP = ["up", "uP", "Up", "UP", "uup", "uupp", "uppp"]
lst_Down = ["down", "Down", "DOWN", "DoWN", "dowwn"]
lst_READY = ["r", "ready", "R", "Ready", "redy", "Redy"]
print("==============Guess Number v:1.0.0==============")
End_Number = 2000
print(f"please pick a number between 0 and {End_Number} for yourself, and then type (ready) for me")
qus_start_game = str( input( "Are you ready to start?" ) )
if (qus_start_game in lst_READY) or (qus_start_game in lst_positive) :
    main_GAME_loop_OP = True
else:
    main_GAME_loop_OP = False
while main_GAME_loop_OP == True:
    main_GAME_loop_OP = False
  
