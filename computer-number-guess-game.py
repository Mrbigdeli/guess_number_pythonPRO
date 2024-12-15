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
  #######################################################################################################################################

#مراحل کامل کردن بازی با وارد کردن ورودی  حدس زدن اعداد محدویت حدس زدن

import random

# لیست‌های پاسخ‌های مثبت و منفی
lst_positive = ["y", "Y", "yes", "Yeah", "YEAH"]
lst_negative = ["n", "N", "no", "NO"]

def start_game():
    print("============== Guess Number v:1.0.0 ==============")
    End_Number = 2000
    print(f"Please pick a number between 0 and {End_Number} for yourself, and then type 'ready' for me.")

    qus_start_game = input("Are you ready to start? ")
    return qus_start_game in lst_positive

def play_game(End_Number, max_attempts=10):
    secret_number = random.randint(0, End_Number)
    attempts = 0
    guessed = False
    
    print("I have picked a number between 0 and", End_Number)
    print(f"You have {max_attempts} attempts to guess the number.")

    while not guessed and attempts < max_attempts:
        try:
            user_guess = int(input("Please enter your guess: "))
            attempts += 1
            
            if user_guess < secret_number:
                print("Too low, try again!")
            elif user_guess > secret_number:
                print("Too high, try again!")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                guessed = True  # عدد درست حدس زده شد
            
            if attempts >= max_attempts:
                print(f"You've used all your attempts! The number was {secret_number}.")
                break  # پایان بازی در صورت اتمام تلاش‌ها
                
        except ValueError:
            print("Please enter a valid integer.")

def play_again():
    play_again_response = input("Do you want to play again? (y/n): ")
    return play_again_response in lst_positive

def main():
    if start_game():
        while True:
            play_game(2000)
            if not play_again():
                print("Thank you for playing!")
                break
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()

