import os
import random

os.system('cls') # para la consola

game_running = true


def guess():

returning = input("Elegi un numero entre el 1 y el 10:")
    if not returning.isdigit();
        print("Invalid Input")
        return guess()
        
    elif int(returning) < 1 or int(returning) > 10;  # del cuato al cuanto
        print("Invalid Input")
        return guess()
    
    else:
        return int(returning);



num_to_guess = random.randint(1,10)

# print(num_to_guess) si queres saber la respuesta :D
while game_running:
    user_guess = guess()
    
    if user_guess == num_to_guess:
        print(f"SI es esa!: {num_to_guess}")
        game_running = False

    else:
        print("Proba de nuevo")


   
            _  _
#          (.)(.)
#        /  ()  \
#       _ \ '--' / _
#       { '-`""""`-' }
#        `"/      \"`
#          \      /
#         _/  /\  \_
#        {   /  \   }
#         `"`    `"`
#            Thomyyy
 




