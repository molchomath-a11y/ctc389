# Moshe Molcho CTC389
# Interactive Story Lab
# Choose your own adventure (I hate reading these and I thought the Black Mirror Episode... Really sucked)
# I wanted to make this scary, related to math and halloween?
# Escape the Possessed Math Classroom

# This variable controls whether the game repeats.  I am assuming people want to continue playing untill they survive and their many ways to die, so I will be writing this program over 3 sittings.


# Feel frustrated about typing so much decided retroactively to start making a function.
# Please don't penalize me for \n... I was programming in QBASIC in 2000, not everything is chatGPT for ***sake. 
# Printing formating is just difficult if you want to render on a command prompt... Please a lot of effort is going into this.

def make_choice(question, option1, option2, option3):

    print()
    print(question)
    print()
    print("1.",option1)
    print("2.",option2)
    print("3.", option3)
    print()

    choice = int(input("Enter your choice: "))

    return choice

# I am about to make a function for game over...  It's going to print a multi-line response... please let me use \n I am not cheating.  This is just the way that I would do it without fancy formatting please.

def game_over(message):
    print()
    print(message)
    print()
    print("GAME OVER.")

    return False


# Initializing some variables.

play_again = "yes"

# Keep playing while the player answers yes.

while play_again == "yes":

    print()
    print("==========================================")
    print("   ESCAPE THE POSSESSED MATH CLASSROOM    ")
    print("==========================================")
    print()

    name = input("What is your name? ")

    print("Hello", name,".")
    print()
    print("You stayed after school to finish your math homework.")
    print("Suddenly, the classroom door slams shut.")
    print()
    print("The lights begin flashing.")
    print("The numbers written on the whiteboard start moving.")
    print()
    print("Then you hear laughter from the back of the classroom...")
    print()
    print("An evil clown has possessed your math classroom!")
    print("You must solve the classroom's puzzles and escape.")
    print("Good luck... Hope you don't die....")
    print()

    # Keeps track of whether a player can continue.
    escaped = True

    #___________________________
    #        DECISION #1
    #___________________________

    print("DECISION #1")
    print()
    print("The clown appears on the classroom porjector.")
    print()
    print(' "Welcome to my class!" the clown says.')
    print()
    print("The classroom door is locked.")
    print("You noticed thtee possible places to search.")
    print("1. Search the teacher's desk.")
    print("2. Open the supply closet.")
    print("3. Look inside the trash can.")
    print()

    choice = int(input("Where will you search? Choose 1, 2, or 3."))

    if choice == 1:
        print()
        print("You searched the teacher's desk.  Good for you... :)")
        print("Inside the top drawer you found a small bronze key.")
        print("A not attached to it says:")
        print()
        print(' "ONE PUZZLE DOWN.... FOUR TO GO!!!!" ')

    elif choice == 2:

        print()
        print(" You opened the supply closet.")
        print(" A giant clown balloon jumps out!")
        print(" It pulls you inside the closet... The door locks behind you.")
        print(name," is trapped in the supply closet... forever.")
        print("GAME OVER.")
        escaped = False

    elif choice == 3:
        print()
        print("You look inside the trash can.")
        print("The clown's face suddenly appears inside it.")
        print()
        print("It magically sucks you into an infinite dark void inside the trash.")
        print("Oscar the grouch isn't in there. WRONG CHOICE!!!!")
        print("The classroom lights turn off and the exit disappears.")
        print("GAME OVER.")
        escaped = False

    else:
        print("That was not one of the choices.")
        print("Do you know how to read instructions?")
        print("GAME OVER.")
        escaped = False

#________________________
#      DECISION #2       
#________________________


    if escaped == True:
        print("The silver key opens a locked box.")
        print("Inside is a calculator.")
        print()
        print('The clown says, "SOLVE THIS OR STAY FOREVER!" ')

        choice = make_choice(
                "Decision 2: What is 8 + 4 * 2 ?" ,
                "24",
                "16",
                "20"
        )

        if choice == 2:

            print("Correct!")
            print("Multiplication happens before addition.")
            print()
            print("A hidden drawer opens.")
            print("Inside is a red classroom pass.")

        elif choice == 1:

            escaped = game_over(
                    "The clown laughs. \n"
                    ' "YOU FORGOT THE ORDER OF OPERATIONS!" '
            )

        elif choice == 3:

            escaped = game_over(
                    'The clown says, "SO CLOSE... BUT WRONG!! " '
            )

        else:

            escaped = game_over(
                    "That was not one of the choices."
            )

#______________________
#       DECISION 3
#______________________

        if escaped == True:

            print()
            print("You use the red classroom pass.")
            print()
            print("Inside are three lockers.")
            print()
            print(' the clown writes: "CHOOSE THE PRIME NUMBER!!! " ')
            
            choice = make_choice(
                "Decision 3: Which locker should you open?",
                "Locker 12",
                "Locker 15",
                "Locker 17"
            )

            if choice == 3:

                print()
                print("CORRECT!")
                print("17 is a prime number.")
                print()
                print("Locker 17 opens.")
                print("Inside you find a flashlight.")

            elif choice ==1:

                escaped = game_over(
                        "A clown horn blasts!\n"
                        '"12 ISNOT A PRIME NUMBER!"'
                )
            elif choice == 2:
 
                escaped = game_over(
                        'The lcown laughs. \n'
                        ' "15 CAN BE DIVIDED BY 3 AND 5!"'
                )

            else:

                escaped = game_over(
                    "That was not one of the choices."
                )


#________________________________________
#              DECISION 4
#________________________________________

         if escaped == True:

             print()
             print("You turn on the flashlight.")
             print()
             print("A secret message appears on the whiteboard.")
             print()
             print("The clown whispers:")
             print('"FIND THE SHAPE WITH FOUR EQUAL SIDES..."')

             choice = make_choice(
                     "DECISION 4: Which shape should you choose?",
                     "Rectangle",
                     "Triangle",
                     "Square"

            )

             if choice == 3:

                 print()
                 print("CORRECT!!")
                 print()
                 print("You touch the square.")
                 print("A section of the whiteboard slides open.")
                 print()
                 print("Behind it is a keypad.")

            elif choice == 2:
                escaped = game_over(
                        'The clown laughs: \n'
                        '"A TRIANGLE ONLY HAS THREE SIDES!"'
                )



            elif choice == 1:

                escaped = game_over(
                        'The clown says: \n'
                        ' "A RECTANGLE DOES NOT ALWAYS HAVE FOUR EQUAL SIDES!!"'
                )

            else:

                escaped = game_over(
                        "The was not one of the choices."
                )

#___________________________________
#           DECISION 5
#___________________________________

    if escaped == True:

        print()
        print("You have reached the final keypad.")
        print()
        print("The classroom door begins shaking.")
        print()
        print("The evil clown appears on the projector.")
        print()
        print('"ONE FINAL PROBLEM!"')

        choice = make_choice(
                "DECISION 5: if 3x = 18, what is x?",
                "3",
                "6",
                "9"
            )
        
        if choice == 2:

            print()
            print("CORRECT!")
            print()
            print("You enter 6 into the keypad.")
            print()
            print("BEEP!")
            print("BEEP!")
            print("CLICK")
            print()
            print("The evil clown appears one final time.")
            print()
            print("The lights return to normal.")
            print("The numbers stop moving.")
            print("The clown disappears.")
            print()
            print(name," runs out of the classroom!")
            print()
            print("============================================")
            print("            CONGRATULATIONS!")
            print("     YOU ESCAPED THE MATH CLASS AND WIN!")
            print("============================================")
            
        elif choice == 1:

            escaped = game_over(
                    'the clown says: \n'
                    '"3 TIMES 3 IS ONLY 9!"'
                )

        elif choice == 3:

            escaped = game_over(
                    'The clown laughs. \n'
                    '"3 TIMES 9 IS 27!"'
            )


        else:
            
            escaped = game_over(
                    "That was not one of the choices."
                )




    play_again = input('Would you like to play again? "yes" or "no": ')


print("Thanks for playing Escape the Possessed Math Classroom!")









# Question #1.


          
