import random
#################################################
def findNumber_inRow(d:dict, whichWay:str, end_Part:int):
    loop_OP = True
    a_func = end_Part / 4
    a_func = int(a_func)
    if whichWay == "none" :
        chance = random.randint(1, 4)
        if chance == 1 :
            x1 = 0
            y1 = x1 + a_func
        elif chance == 2 :
            x1 = a_func
            y1 = x1 + a_func
        elif chance == 3 :
            x1 = a_func * 2
            y1 = a_func * 3
        elif chance == 4 :
            x1 = a_func * 3
            y1 = a_func * 4
        d["up"] = y1
        d["down"] = x1
    elif whichWay in lst_UP :
        x1 = 0
        while loop_OP == True :
            Down_part = d["down"]
            UP_part = d["up"]
            if (x1 != Down_part) and (x1 >= UP_part) :
                d["down"] = x1 
                y1 = x1 + a_func
                d["up"] = y1
                loop_OP = False
            else :
                if (x1 + a_func != end_Part) :
                    x1 = x1 + a_func
                elif (x1 + a_func == end_Part) :
                    print("it isn't possible")
                    d["up"] = 0
                    d["down"] = 0
                    loop_OP = False
    elif whichWay in lst_Down :
        y1 = end_Part
        while loop_OP == True :
            Down_part = d["down"]
            UP_part = d["up"]
            if (y1 != UP_part) and (y1 <= Down_part) :
                x1 = y1 - a_func
                if ( x1 >= 0 ) and ( y1 > 0 ) and ( y1 - x1 == a_func ) :
                    d["up"] = y1
                    d["down"] = x1
                    loop_OP = False
                else :
                    continue
            else :
                y1 = y1 - end_Part
    return d

def Minus_Counter(d:dict) :
    u = d["up"]
    d = d["down"]
    tafazol = int( u - d )
    result = tafazol / 2
    return result

def findNumber_inColumn (d:dict):
    distance = Minus_Counter(d)
    end_range = d["up"]
    start_range = d["down"]
    lst_func_three = ["0", "1"]
    inColumn_Loop_OP = True 
    while inColumn_Loop_OP == True :
        chance = random.randint(0, 1)
        len_lst = len(lst_func_three)
        if len_lst == 1 :
            ch = lst_func_three[0]
            chance = int(ch)
        elif len_lst == 2 :
            ch = lst_func_three[chance]
            lst_func_three_new = lst_func_three.pop(chance)
            chance = int(ch)
            lst_func_three = lst_func_three_new
        if chance == 0 :
            x_down = d["down"]
            x_up = x_down + distance
            if x_up <= end_range :
                d["up"] = x_up
                d["down"] = x_down
                inColumn_Loop_OP = False
        elif chance == 1 :
            x_up =d["up"]
            x_down = x_up - distance
            if x_down >= start_range :
                d["up"] = x_up
                d["down"] = x_down
                inColumn_Loop_OP = False
        else :
            print("it isn't possible")
            d["up"] = 0
            d["down"] = 0
            inColumn_Loop_OP = False
    return d

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