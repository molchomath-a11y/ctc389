#A student led RPG game

#contributors
#gpoppe


#imported libraries

import math
import time

#function definitions

def room1():
    #room1
    #Ted :)
    print("Walt Disney World Vacation")

def room2():
    #room2
    print("This door is locked.")


def room3():
    #room3
    #Arpita Shah
    again = "yes"

    def choice1(input1):
        print("")
        print("You discover a dusty old map showing escape route. What do you want to do with map?")
        print("")
        print("1. Follow the marked trail")
        print("2. Ignore the map and explore freely")
        print("3. Tear the map open (something is inside)")
        option1 = int(input("Choose one of the following options."))
        if option1==1:
            print( name, " , as you are following the marked trail, you found the old bunker.")
            option10=choice2(option1)
            return option10
        elif option1==2:
            print( name, " , since you ignored the map;")
            option11=choice4(option1)
            return option11
        elif option1==3:
            print(name, ", you tear the map open and find a metal key which you used to call tribal warrior.")
            option12 = choice2(option1)
            return option12
    
        
    
    def choice2(input2):
        print("")
        print("A tribal warrior appears and calls out to you.")
        print("")
        print("1. Ask the warrior for help")  
        print("2. Hide behind rocks")
        print("3. Offer the metal key you found")
        option3 = int(input("What do you choose? "))
        if option3==2:
            print(name,", as you were hiding behind the underground door.")
            option13= choice4(option3)
            return option13  
        if option3==1:
            print (name, ", a warrior appear in front of you and showed you the cave")
            option14= choice3(option3)
            return option14
        if option3==3:
            print(name, ", in exchange of the metal key you warrior showed you a way to the island.")
            option15= choice5(option3)
            return option15
    
    def choice3(input3):
        print("")
        print("You reach the base of the volcano. Smoke fills the air.")
        print("")
        print("1. Enter the lava tube tunnel")  
        print("2. Climb the outer ridge")
        print("3. Search for the old bunker")
        option4 = int(input("What do you choose? "))
        if option4==1:
            print(name, ", you have reached to the end of the tunnel.")
            option16= choice5(option4)
            return option16
        if option4==2:
            print(name, ", you have found a key on the way the island.")
            option17= choice2(option4)
            return option17
        if option4==3:
            print(name, ", you found the old map in the old bunker.")
            option18=choice1(option4)
            return option18
    
    def choice4(input4):
        print("")
        print("A loud alarm blares—the final evacuation is happening now!")
        print("")
        print("1. Board the rescue helicopter")  
        print("2. Sail away on a wooden raft")
        print("3. Ride a zipline across the canyon")
        option5 = int(input("What do you choose? "))
        if option5 == 1:
            print("The helicopter lifts off just as the volcano erupts." ,name , " , you have successfully escaped Volcano Island!")
        elif option5 == 2:
            print("The raft carries you away, but the waves grow violent.", name, ", you barely escape with your life!")
        elif option5 == 3:
            print("The zipline snaps halfway across the canyon.", name, ", you fall into the jungle and perish.")
        else:
            print(name, "your hesitation costs you precious time. The volcano erupts and you do not survive.")
        
        return option5
    
    def choice5(input5):
        print("")
        print("You walk deeper into the island and reach a dangerous crossroads.")
        print("The volcano shakes violently, and you must choose quickly.")
        print("")
        print("1. Cross the shaky wooden bridge")
        print("2. Crawl through a narrow lava tunnel")
        print("3. Climb the steep rocky cliff")
        print("4. Follow the hidden path behind the waterfall")
        option6 = int(input("What do you choose? "))
    
        while option6 < 1 or option6 > 4:
            option6 = int(input("Choose option from above. What do you choose? "))
    
        if option6 == 1:
            print(name, ", you carefully cross the shaky bridge and reach a safe zone.")
            return choice4(option6)
    
        elif option6 == 2:
            print(name, ", you crawl through the lava tunnel and barely escape the heat.")
            return choice4(option6)
    
        elif option6 == 3:
            print(name, ", you climb the cliff and see the evacuation area from above.")
            return choice4(option6)
    
        elif option6 == 4:
            print(name, ", you follow the hidden path and discover a secret rescue station!")
            return choice4(option6)
    
     #Main body
    name = str(input("Welcome traveler!  What is your name? "))
    while again =="yes" or again == "Yes" or again== "YES":
    
        
        print("Hello ", name , " you wake up on a mysterious island.  The ground shakes beneath you. A volcano at the center of the island is about to erupt.  You must escape")
        print(" ")
        print(" You see three possible paths in front of you. ")
        print ("************************************************************")
        print ("1. Climb the watch tower")
        print ("2. Go to the jungle")
        print ("3. Go to the beach")
        print ("************************************************************")
        option= int(input("what do you choose, before lava gets to you? "))
        
        if option==1:
            print( name, " , you just climbed the watch tower and reached the top.")
            option1=choice1(option)
          
        
        if option==2:
            print(name, " , you are in the jungle now. ")
            option2 = choice2(option)
        if option == 3:
            print (name, ", you are the beach where you can hear the sound of waves. Danger is still dangling.")
            option3 = choice3(option)
            
    
        while option <1 or option>3 :
            option = int(input("Choose option from above. What do you choose? "))  
    
        print (" ")
        again = input("Would you like to play again? (yes/no)")
    print("Thank you for playing! Have a mathemagical day!")
    

def room4():
    #room4
    #Alejandra Ibarra
    print("Pokemon Master!")

    newlist = ["Pick a starter pokemon:","1.Piplup","2.Chimchar","3.Turtwig"]
        
    option1 = ["Pick a starter pokemon:","1.Squirtle","2.Charmander","3.Bulbasaur"]

    option2 = ["How do you want to dress your Pokemon:","1.Goggles","2.Top Hat","3.Party Hat"]

    option3 = ["What do you want to do with your starter:","1.Free Play","2.Battle Ground","3.Show off your pokemon!"] 

    option4 = ["Do you wish to evolve your Pokemon?:","1.No.","2.Evolve Once","3.Fully Evolve"]

    option5 = ["Your Pokemon is being attacked, how do you wish to proceed?:","1.Join your Pokemon in battle.","2.Catch the Pokemon yourself.","3.Watch your Pokemon battle."]

    redo_game = ["Do you want to play again?", "1.Yes", "2.No"]
    again = 1
    while(again==1):
        print("Welcome Trainer, your Pokemon adventure begins now! Lets see if you have what it takes to become a Pokemon Master!")

#Level1
    
        choice = int(input("Do you want starters from generation 1 or 4? "))
        if choice == 1:

            for item in option1:
                print(item)

            starter_choice = int(input("Pick a number 1-3: "))

            if starter_choice == 1:
                print("A smart choice! Squirtle is ready to make a splash and take on whatever challenges come your way.")

            if starter_choice == 2:
                print("Your adventure is heating up. Charmander is ready to bring the energy and power through every challenge.")

            if starter_choice == 3:
                print("The best choice! Bulbasaur is ready to grow, learn, and tackle every challenge that comes your way.")
        else:

            for item in newlist:
                print(item)
        
            starter_choice = int(input("Pick a number 1-3: "))

            if starter_choice == 1:
                print("Leave the familiar behind and experience the Sinnoh region!")
                print("Piplup is excited to start your journey together!")

            if starter_choice == 2:
                print("Leave the familar behind and experience the Sinnoh region!")
                print("Chimchar is bursting with energy and ready to start your journey together!")

            if starter_choice == 3: 
                print("Leave the familiar behind and experience the Sinnoh region!")
                print("Turtwig is ready to step forward and follow you on your adventure!")

    
        print("Before begining your journey lets dress your Pokemon!")

#Minigame/Loop
        mini=True
        print("Lets play a minigame.")
        pokemans = ["1.Luigia", "2.Diglett", "3.Mudkip", "4.Drilbur", "5.Garchomp", "6.Applin"]
        while(mini):
            for poke in pokemans:
                print(poke)
            guess = int(input("Guess what my favorite Pokemon is: "))
            if guess == 6:
                mini = False 
        print("Congrats you guessed correctly, I love Applin and his green shiny!<3")

#Level2
        for item in option2:
            print(item)

        dress_choice = int(input("Pick a number 1-3: "))

        if dress_choice == 1:
            print("Adventure mode on! Your Pokemon is geared up and ready to explore, discover, and take on the next challenge!")

        if dress_choice == 2:
            print("Fancy choice, trainer! Your Pokemon is looking ready for a VIP battle.")

        if dress_choice == 3:
            print("Party time! Your Pokemon is ready to party AND play.")
#Level3
        for item in option3:
            print(item)
    
        journey = int(input("Pick a number 1-3: "))

        if journey == 1:
            print("No rules, no pressure... just explore, experiment and have fun! Take your Pokemon on an adventure and see what you discover!")

        if journey == 2:
            print("Its time to put your skill to the test. Choose your moves wisely, earn XP, and see if you have waht it take to battle!")

        if journey == 3:
            print("Your Pokemon is ready for the spotlight! Show off your style and let everyone see your AWESOME Pokemon. Remember: Strike a pose, trainer!")

        for item in option4:
            print(item)

        evolution = int(input("Pick a number 1-3: "))

        if evolution == 1:
            print("Staying just the way you are! Your Pokemon doesnt need to evolve to be awesome. Keep training, keep learning, and show everyone what you can do!")

        if evolution == 2:
            print("Evolution unlocked! Your Pokemon has leveled up and grown stronger. Look at you go, trainer.")

        if evolution == 3:
            print("You've powered up your Pokemon ALL the way. Your dedication has paid off, and your Pokemon has reached its final form. You are on step close to become a Pokemon Master.")

#Level5
    
        for item in option5:
            print(item)

        attack = int(input("Pick a number 1-3: "))

        if attack == 1:
            print("Teamwork makes the dream work, trainer! Your Pokemon is stonger wit you by its side. You really are a Pokemon Master.")

        if attack == 2:
            print("You fool! You should know working together is ALWAYS the right choice. You are not ready to be a Pokemon Master.")

        if attack == 3:
            print("You stand back and watch your Pokemon battle?? Uh-Oh. NEVER leave your Pokemon to battle alone! Your Pokemon needs you by their side.")


#End Game
    
        for item in redo_game:
            print(item)
    
        again = int(input("Please enter 1 or 2: "))

def room5():
    #room5
    #Carmen Aguilar-Reyes
    print("Legendary Adventurer")
 
    name = input ("Welcome adventurer!What is your name?: ")

    print ("Hello", name, "you have discovered a mysterious island filled with ancient secrets.")
    print ("Your goal is to find the legendary Crystal to help you escape the island.")

    print ("You arrived at a fork in the path")

    print("1. Enter the jungle")
    print("2. Climb the mountain trail")
    print("3. Follow the beach")
    choice1 = input("Which path do you choose? ")


    if choice1 == "1":
        print(name, "enters the jungle.")
    elif choice1 == "2":
        print(name, "climbs the mountain trail.")
    elif choice1 == "3":
        print(name, "follows the beach.")
    else:
        print("You got lost and the adventure ends.")
        return
# Decision 2

    print("You discover an abandoned camp with three useful items.")
    print("1. Compass")
    print("2. Flashlight")
    print("3. Rope")
    choice2 = input("Which item do you take? ")


    if choice2 == "1":
        print("You take the compass.")
    elif choice2 == "2":
        print("You take the flashlight.")
    elif choice2 == "3":
        print("You take the rope.")
    else:
        print("You waste too much time and the adventure ends.")
        return 

# Decision 3

    print("Later, you reach a rushing river.")
    print("1. Swim across")
    print("2. Build a raft")
    print("3. Search for a bridge")
    choice3 = input("What do you do? ")

    if choice3 == "1":
        print("You carefully swim across.")
    elif choice3 == "2":
        print("You build a sturdy raft.")
    elif choice3 == "3":
        print("You find an old bridge and cross safely.")
    else:
        print("You fall into the river and lose the adventure.")
        return

# Decision 4

    print("You discover the entrance to an ancient temple.")
    print("1. Enter through the main gate")
    print("2. Use a hidden side entrance")
    print("3. Climb through a rooftop opening")
    choice4 = input("How will you enter? ")

    if choice4 == "1":
        print("You walk through the massive gate.")
    elif choice4 == "2":
        print("You sneak through the side entrance.")
    elif choice4 == "3":
        print("You climb into the temple from above.")
    else:
        print("You trigger a trap and lose.")
        return

# Decision 5

    print("Inside the temple are three crystal pedestals.")
    print("1. Red Crystal")
    print("2. Blue Crystal")
    print("3. Green Crystal")
    choice5 = input("Which crystal will you take? ")

    if choice5 == "1":
        print("The temple begins to glow!")

    elif choice5 == "2":
        print("The temple begins to glow!")
    elif choice5 == "3":
        print("The temple begins to glow!")
    else:
        print("The temple collapses before you make a choice.")
        return
#Decision Treasure
    
    print ("While exploring the temple, you find a treasure chest!")
    print ("1. Open it")
    print ("2. Ignore it")
    print ("3. Inspect it carefully")

    treasurechoice = input("What do you do?")

    if treasurechoice == "1": 
        print ("You found the Golden Idol!")
    elif treasurechoice == "2": 
        print ("You leave the chest alone.")
    elif treasurechoice == "3": 
        print ("You discovered an Ancient map.")
    else: 
        print ("You walk away from the chest")
        return 

# Decision 6

    print("You must escape the island.")
    print("1. Sail away on a boat")
    print("2. Fly away in an ancient airship")
    print("3. Use a hidden portal")
    choice6 = input("How will you escape? ")

    if choice6 == "1":
        print("Congratulations", name,  "! You sail away with the Crystal of Destiny and win!")
    elif choice6 == "2":
        print("Congratulations", name, "! You fly away with the Crystal of Destiny and win!")
    elif choice6 == "3":
        print("Congratulations", name, "! You step through the portal with the Crystal of Destiny and win!")
    else:
        print("You hesitate too long and remain trapped on the island.")

# Main game loop

    play_again = input("Would you like to play again? ")

    if play_again == "yes": 
        room5()
    else: 
        print("Thanks for playing!")

    
def room6():
    #room6
    #Angela Vasquez
    print("Welcome to The Halloween Adventure Park!")

def room7():
    #room7
    #Joanne Dragich
    print("Your first Ducks game!")
    #Joanne Dragich CTC389 Lab 8 Your First Ducks Game
    def playagain():
        print("Would you like to play Your First Ducks Game?")
        print("Type 1 for No and 2 for Yes.")
        play = 0
        play = int(input(">"))
        return play

    play = playagain()

    if (play == 1):
        print("Thanks for playing and let's go, Ducks!")
    while (play == 2):
        print("You exit the freeway on your way to the arena. Where do you want to park?")
        print("Type 1 - Pull into the free Katella or Cerritos parking structures.")
        print("Type 2 - Pay to park in the lot of a nearby business and walk over.")
        print("Type 3 - Pay extra for the new River parking structure.")
        parking = int(input(">"))
        if (parking == 1):
            print("It may be free, but it's super crowded. You are trapped by the traffic at the end of the game and die of starvation.")
            play = 1
            playagain()
        elif (parking == 2):
            print("You go bankrupt paying the ridiculous parking fees. Seriously, you know the structures are free, right?")
            play = 1
            playagain()
        elif (parking == 3):
            play = 1
            print("Wow, that was easy and so close. This was totally worth the money. Let's head into the arena.")
            print("Where do you head first?")
            print("Type 1 - Take a picture with Wild Wing.")
            print("Type 2 - Get a free 1st game certificate at Guest Services.")
            print("Type 3 - Check out the food court options.")
            choice2 = int(input(">"))
            if (choice2 == 1):
                print("You took a picture, but hunger made you lightheaded. You fell, hit your head, and died.")
                play = 1
                playagain()
            elif (choice2 == 2):
                print("That certificate is just a dust-catcher. Now, the food lines are super long. You die of old age waiting in line.")
                play = 1
                playagain()
            elif (choice2 == 3):
                print("Oh, wow! There are some great options here. The lines are still short this early, so you have your pick. Where do you go?")
                print("Type 1 - Hat Trick Hawaiian")
                print("Type 2 - Feather & Flame BBQ")
                print("Type 3 - El Patito Taqueria")
                choice3 = int(input(">"))
                if (choice3 == 1):
                    print("It was overpriced, and you died of food poisoning.")
                    play = 1
                    playagain()
                elif (choice3 == 2):
                    print("The liquid smoke chokes you out before you make it 10 feet.")
                    play = 1
                    playagain()
                elif (choice3 == 3):
                    print("The masa quesadilla, Red Line Margarita, and bag of churros are epic. Great choice! The game started. It's time to head to your seat.")
                    print("Type 1 - Walk right in ignoring the guard telling you to stop.")
                    print("Type 2 - Stop and talk to some Florida fans.")
                    print("Type 3 - Wait until the refs stop play to walk to your seat.")
                    choice4 = int(input(">"))
                    if (choice4 == 1):
                        print("You get hit in the head with a puck. Yeah, that rule is there because fans have gotten hurt and died.")
                        play = 1
                        playagain()
                    elif (choice4 == 2):
                        print("The Florida fans are rats just like their team. They murder you and hide the body. Your family buries an empty casket.")
                        play = 1
                        playagain()
                    elif (choice4 == 3):
                        print("The refs blow the play dead, and you walk to your seat. You have a great view!")
                        print("You're having a great time. There are 10 minutes left in the game. What do you do?")
                        print("Type 1 - Leave early to beat the traffic.")
                        print("Type 2 - Leave to buy a beer.")
                        print("Type 3 - Stay in your seat until the end.")
                        choice5 = int(input(">"))
                        if (choice5 == 1):
                            print("As you approach your car, you hear a huge roar and the goal horn. You missed the biggest goal of the season? You died of embarassment.")
                            play = 1
                            playagain()
                        elif (choice5 == 2):
                            print("A beer in the last 10 minutes? They stopped selling them after the second intermission. You hear a huge cheer and the goal horn. You missed the biggest goal of the year, and you have no beer. You died of embarassment.")
                            play = 1
                            playagain()
                        elif (choice5 == 3):
                            print("You saw the biggest goal of the year! You swear afterwards that Leo Carlsson pointed right at you during his celly. You get a high five from Wild Wing on the way out. It was the best night ever!")
                            Ducklings = ["McQueen", "Solberg", "Klepov"]
                            NewGuys = ["Brossoit", "Greer", "Woo"]
                            Ducks = ["Carlsson", "Gauthier", "Mintyukov"]
                            print("You decide to hang out around the arena driveway to try to get selfies with players as they pull out in their cars. Who did you get selfies with?")
                            print("Type 1 for the Ducklings: the new class of rookies joining the big show.")
                            print("Type 2 for the New Guys: the recently traded players who signed on during the off season.")
                            print("Type 3 for the Favorites: the established players whose fans show up in their jerseys.")
                            choice6 = int(input(">"))
                            if (choice6 == 1):
                                print(Ducklings[0], " was a cool guy, but ", Ducklings[1], " and ", Ducklings[2], " just drove by.")
                                play = 1
                                playagain()
                            elif (choice6 == 2):
                                print(NewGuys[0], " , ", NewGuys[1], ", and ", NewGuys[2], " all carpooled together.")
                                play = 1
                                playagain()
                            elif (choice6 == 3):
                                print(Ducks[0], " autographs your hat.", Ducks[1], " signs your jersey.", Ducks[2], " autographs your bobblehead. They're really trying to make up for taking up so much cap space we can't sign more veterans to close the gaps this season. Well, at least you got some autographs.")
                            playagain()
def room8():
    #room8
    print("Welcome to the best game!")

def room9():
    #room9
    print("This door is locked.")

def room10():
    #room10
    #lauren bowman
    print("The Music Career Game!")

    def door1():
        print("Door 1: Private Piano Teacher")
        print ("You are teaching a student, but notice the piano bench is wobbly. What do you do next?")
        print ("1. Fix the bench before playing with a wrench.")
        print ("2. Swap out the bench for a chair.")
        print ("3. Ignore that the bench is broken, hop on the bench and play violently.")
   
        choice = input ("Choose 1,2, or 3: ")
        if choice == "1":
            print("You fix the bench and have a great lesson!")
        elif choice == "2":
            print ("The student learns discipline and becomes a great pianist. The parents help you by donating a new piano bench to you a week later.")
        elif choice == "3":
            print("The bench breaks, you fall, hit the back of your head on your floor and die.")
        else:
            print("Invalid choice. You wasted time and the lesson ended.")

    def door2():
        print("Door 2: Street performer")
        print(" You are playing at 3rd Street Promenade when a rival musician tries to take your spot. What do you do next? ")
        print ("1. Perform a duet together.")
        print ("2. Play louder to drown them out and attract more of a crowd.")
        print ("3. Physically attack the rival.")
   
        choice = input ("Choose 1, 2, or 3:")
        if choice == "1":
            print ("The crowd loves it! You both make a lot of money and become friends.")
        elif choice == "2":
            print ("You win the crowd over with your amazing skills.")
        elif choice == "3": 
            print ("The rival pulls out a knife and you die after being attacked.")
        else:
            print("Invalid choice. The rival steals your spot.")

    def door3():
        print("Door 3: Music Producer" )
        print (" Your high-teach studio console sparks during a big recording session. What do you do next?")
        print ("1. Call an electrician to fix it.")
        print ("2. Grab the live wires with bare hands.")
        print ("3. Switch to working on your laptop.")
   
        choice = input("Choose 1,2, or 3: ")
        if choice == "1":
            print ("The console gets fixed safely and you finish the album.")
        elif choice == "2":
            print ("You get electrocuted by high voltage and die.")
        elif choice == "3":
            print ("You finish the song on your computer thanks to your knowledge of music tech and production software and win a Grammy!")
        else: 
            print ("Invalid choice. You lose the project file.")

    def door4():
        print("Door 4: High School Band Director")
        print ("Right before a big championship, the band is out of tune. What do you do next?")
        print ("1. Tune every instrument carefully.")
        print ("2. Give an inspiring pep talk.")
        print ("3. Scold the band for being irresponsible.")

        choice = input("Choose 1,2, or 3: ")
        if choice == "1":
            print ("The band plays perfectly and wins 1st place because you took the time to tune them!")
        elif choice == "2":
            print ("The pep talk motivates them to play their best, but they didn't win the competition.")
        elif choice == "3":
            print ("The stress kills you and you have a heart attack on the football field right after they play.")
        else:
            print ("Invalid choice. The band misses their turn.")

    def door5():
        print("Door 5: Touring Musician")
        print("You are on stage at a huge rock concert with pyrotechnics going off. What do you do next?")
        print("1. Stay in your area onstage and play your solo.")
        print("2. Jump directly into the live flame cannons.")
        print("3. Jump off the stage into the crowd.")

        choice = input("Choose 1,2, or 3: ")
        if choice == "1":
            print("Your solo goes viral and you become famous!")
        elif choice == "2":
            print("You catch on fire and die instantly.")
        elif choice == "3":
            print("The crowd catches you and carries you around, then back onto the stage!")
        else:
            print ("Invalid choice. You miss your turn to play your solo.")

    def door6():
        print("Door 6: Wedding Singer")
        print("You are singing and playing guitar at a wedding reception and your break a string. What do you do? You are supposed to play for 2 hours.")
        print("1. You play all the songs on the guitar with the broken string, revoicing everything.")
        print("2. You see a covered piano sitting in the recpeiton hall, uncover it and show off your piano and singing skills!")
        print("3. You decide to restring your guitar because you forgot your string winder.")
    
        choice = input("Choose 1,2, or 3: ")
        if choice == "1":
            print("You amaze the bride, groom and other wedding guests. A few months later, the groom hires you to teach him how to play guitar!")
        elif choice == "2":
            print("A wedding guest who is also a musician, is impressed with your multi-instrumental music skills and hires you to play gigs with an 80's cover band.")
        elif choice == "3":
            print ("Trying to rush, and under a lot of pressure, you pop a steel string and it slices your neck open. You're bleeding heavily and have to leave the wedding to go to the emergency room to get stiches. You lose out on money from the gig and you can't play until your neck is healed.")
        else:
            print("Invalid choice, you end up not getting the wedding gig and need to look for more opportunities to perform.")

    def game():
        playing = True
        while playing:
            print("------------------------------------------------------")
            print("Welcome to the game of Music Careers! Choose wisely!")
            print("1. Private Piano Teacher~")
            print("2. Street Performer~")
            print("3. Music Producer~")
            print("4. High School Band Director~")
            print("5. Touring Musician~")
            print("6. Wedding Singer~")

            door = input ("Hello! Pick a door (#1-6): ")

            if door == "1":
                door1()
            elif door == "2":
                door2()
            elif door == "3":
                door3()
            elif door == "4":
                door4()
            elif door == "5":
                door5()
            elif door == "6":
                door6()
            else:
                print ("Door choice invalid.")

            playagain = input("Do you want to play again? (yes or no)?")
            if playagain == "no":
                playing = False
                print("Thank you for playing, this is the end of the game!")
                print("======================================================")

    game()



def room11():
    #room11
    #Timothy Duong
    first_decision_results = []
    first_decision_results.append("You woke up late again! This was the last straw. You got fired from work. Restart the game.")
    first_decision_results.append("You brush your teeth, shower, and get dressed. Time to go to work!")
    first_decision_results.append("Oops, it turns out that you don't have sick days left. Restart the game.")
    second_decision_results = []
    second_decision_results.append("It took too long to ride to work and you were late again! You got fired. Restart the game.")
    second_decision_results.append("There is an ongoing strike and the bus got delayed. You got fired from work for being late. Restart the game.")
    second_decision_results.append("You got to work just on time!")
    third_decision_results = []
    third_decision_results.append("You got to your classroom right before the bell rang!")
    third_decision_results.append("The copy machine jammed, and caused you go be late. You got fired. Restart the game.")
    third_decision_results.append("Your coworker spent too much time talking and now you're late and got fired. Restart the game.")
    fourth_decision_results = []
    fourth_decision_results.append("Later, one of your students' parents filed a complaint. You got fired. Restart the game.")
    fourth_decision_results.append("Unfortunately, an administrator decided to evaluate your lesson today. You got fired. Restart.")
    fourth_decision_results.append("The lesson went fine though could have been better.")
    fifth_decision_results = []
    fifth_decision_results.append("It's a little awkward buying lunch with the students but you're not hungry anymore.")
    fifth_decision_results.append("You didn't make it back on time. You got fired. Restart the game.")
    fifth_decision_results.append("You got too hungry to teach effectively during an important evaluation. You got fired. Restart.")

    time.sleep(1)
    print()
    print("Survive a Day of Work!")
    time.sleep(1)
    def main_menu():
        print()
        name = input("Please enter your name: ")
        time.sleep(0.5)
        print()
        print("Hello", name, "it's morning and you have just woken up. What do you do?")
        time.sleep(1)
        print("1. Press the snooze button on your alarm")
        time.sleep(0.3)
        print("2. Get ready to go to work")
        time.sleep(0.3)
        print("3. Call in sick")
        time.sleep(0.5)
        return name

    def hint():
        choice = ""
        while choice != "yes" and choice != "no":
            choice = input("Would you like a hint? yes/no: ")
            time.sleep(0.3)
            if choice == "yes":
                time.sleep(0.5)
                print("Choose the answer that would most likely get you through the work day.")
                time.sleep(1)
            elif choice != "no":
                time.sleep(0.5)
                print("You must answer with yes or no")
                time.sleep(0.5)

    def first_decision():
        choice = int(input("What do you choose? "))
        time.sleep(0.5)
        if choice == 1:
            print(first_decision_results[0])
            time.sleep(0.5)
            return "restart"
        elif choice == 2:
            print(first_decision_results[1])
            time.sleep(0.5)
            return "continue"
        elif choice == 3:
            print(first_decision_results[2])
            time.sleep(0.5)
            return "restart"

    def second_decision(name):
        print()
        print("How will you go to work today,", name)
        time.sleep(0.5)
        print("1. Ride your bike to work")
        time.sleep(0.3)
        print("2. Take the bus to work")
        time.sleep(0.3)
        print("3. Drive to work")
        time.sleep(0.5)
        choice = int(input("What do you choose? "))
        time.sleep(0.5)
        if choice == 1:
            print(second_decision_results[0])
            time.sleep(0.5)
            return "restart"
        elif choice == 2:
            print(second_decision_results[1])
            time.sleep(0.5)
            return "restart"
        elif choice == 3:
            print(second_decision_results[2])
            time.sleep(0.5)
            return "continue"

    def third_decision(name):
        print()
        print("You are now at work. What do you do next,", name)
        time.sleep(0.5)
        print("1. Go to your classroom")
        time.sleep(0.3)
        print("2. Go make copies")
        time.sleep(0.3)
        print("3. Chat with a coworker")
        time.sleep(0.5)
        choice = int(input("What do you choose? "))
        time.sleep(0.5)
        if choice == 1:
            print(third_decision_results[0])
            time.sleep(0.5)
            return "continue"
        elif choice == 2:
            print(third_decision_results[1])
            time.sleep(0.5)
            return "restart"
        elif choice == 3:
            print(third_decision_results[2])
            time.sleep(0.5)
            return "restart"

    def fourth_decision():
        print()
        print("You are now in your classroom, and you realize you forgot to plan for today's lessons. What do you do?")
        time.sleep(0.5)
        print("1. Play a movie and give the students a free day")
        time.sleep(0.3)
        print("2. Make up a lesson on the spot")
        time.sleep(0.3)
        print("3. Use last year's lesson")
        time.sleep(0.5)
        choice = int(input("What do you choose? "))
        time.sleep(0.5)
        if choice == 1:
            print(fourth_decision_results[0])
            time.sleep(0.5)
            return "restart"
        elif choice == 2:
            print(fourth_decision_results[1])
            time.sleep(0.5)
            return "restart"
        elif choice == 3:
            print(fourth_decision_results[2])
            time.sleep(0.5)
            return "continue"

    def fifth_decision(name):
        print()
        print("It is now lunchtime, and you realized you forgot to bring your lunch. What do you do next,", name)
        time.sleep(0.5)
        print("1. Buy lunch from the cafeteria")
        time.sleep(0.3)
        print("2. Drive to Chipotle to buy some food")
        time.sleep(0.3)
        print("3. Decide to not eat anything and try to make it to the end of the day")
        time.sleep(0.5)
        choice = int(input("What do you choose? "))
        time.sleep(0.5)
        if choice == 1:
            print(fifth_decision_results[0])
            time.sleep(0.5)
            return "continue"
        elif choice == 2:
            print(fifth_decision_results[1])
            time.sleep(0.5)
            return "restart"
        elif choice == 3:
            print(fifth_decision_results[2])
            time.sleep(0.5)
            return "restart"

    def ending(name):
        time.sleep(1)
        for i in range(10):
            if i%2 == 0:
                print("               CONGRATULATIONS")
            else:
                print()
            time.sleep(0.2)
        time.sleep(0.5)
        print(name, "you made it through the day without getting fired! You won the game!")
        for i in range(10):
            if i%2 == 0:
                print()
            else:
                print("               CONGRATULATIONS")
            time.sleep(0.2)

    play_again = "yes"
    while play_again == "yes":
        name = main_menu()
        hint()
        first_result = first_decision()
        if first_result != "restart":
            second_result = second_decision(name)
            if second_result != "restart":
                third_result = third_decision(name)
                if third_result != "restart":
                    fourth_result = fourth_decision()
                    if fourth_result != "restart":
                        fifth_result = fifth_decision(name)
                        if fifth_result != "restart":
                            ending(name)

        play_again = input("Would you like to play again? ")    

def room12():
    #Ceiry Molina
    #room12
    print("Ceiry's Game!")

    opt1 = ["Choose you Jedi:","1.Luke Skywalker","2.Obi Wan","3.Ahsoka"]

    opt2 = ["How do you want to eqip your compasnion:","1.Jedi Robes","2.Clome Armor","3.Mandalorian Cape"]

    opt3 = ["What mission do you want  to begin:","1.Explore a New Planet", "2.Battle the Empire","3.Attend a Galactic Celebration"]

    opt4 = ["Do you wish to upgrade your companion's Force abilities?:","1.No", "2.Increase Training","3.Master the Force"]

    opt5 = ["The Empire is attacking! How do you wish to proceed?:","1.Fight alongside your companion","2.Face the enemy alone","3.Stay back and watch"]

    opt6 = ["While on a mission you find a box! How do you wish to proceed?:","1.Open it", "2.Ignore it","3.Inspect it"]

    redo_game = ["Do you want to play again?","1.Yes","2.No"]
    again = 1 
    while(again ==1):
        print("Welcome, young Padawan! Your Star Wars adventure begins now. May the Force be with you!")

    #Level1
        for item in opt1:
            print(item)

        starter_choice = int(input("Pick a number 1-3:"))

        if starter_choice ==1:
            print("Luke Skywalker joins your journey! His courage and determination will guide you through the galaxy.")

        if starter_choice ==2:
            print("A wise choice. Obi Wan is ready to share the wisdom of the Jedi Order")

        if starter_choice ==3:
            print("Excellent choice! Ahsoka is prepared to face% any challenge and protect the galaxy")
        
        print("Before beginning your mission, let's prepare you companion!")

    #Level2
        for item in opt2:
            print(item)
    
        dress_choice = int(input("Pick a number 1-3:"))

        if dress_choice ==1:
            print("Classic Jedi style! Your companion is prepared for an honorable mission across the stars.")

        if dress_choice ==2:
            print("Battle ready! Your companion looks prepared to take on Imperial forces.")
        if dress_choice ==3:
            print("An impressive look! Your companion stands out as a true galactic hero.")

    #Level3 
        for item in opt3:
            print(item)

        journey = int(input("Pick a number 1-3:"))

        if journey ==1:
            print("Adventure awaits! Discover hidden worlds, ancient secrets, and new allies throughout7 the galaxy.")

        if journey ==2:
            print("The battle begins! Use strategy, teamwork, and the Force to defeat the Empire")

        if journey ==3: 
            print("A celebration across the galaxy! Show off your companion and enjoy the festivities")

    #Level4
        for item in opt4:
            print(item)

        evolution = int(input("Pick a number 1-3:"))

        if evolution ==1:
            print("Your companion remains as they are. Remember true strength comes from within")

        if evolution ==2:
            print("Training complete!Your companion has grown stronger and gained new Force abilities")

        if evolution ==3:
            print("Force mastery achieved! Your companion has reached their highest potential and become a legendary hero")

    #Level5

        for item in opt5:
            print(item)

        attack = int(input("Pick a number 1-3:"))

        if attack ==1:
            print("Together you fight! The force is strongest when allies stand side by side;")

        if attack ==2:
            print("Bravery is admirable, but teamwork is the Jedi way. Facing the enemy alone is risky.")

        if attack ==3:
            print("Standing aside while others fight is not the Jedi path. Heroes help those in need!")

    #Level6 

        for item in opt6:
            print(item)

        box_choice = int(input("Pick a number 1-3:"))

        if box_choice ==1:
            print("Congrats you found a purple light saber!!")

        if box_choice ==2:
            print("You leave the box alone very safe choice!")

        if box_choice ==3:
            print("You find a green light saber, very good choice!")

    #End Game 
        for item in redo_game:
            print(item)

        again = int(input("Please enter 1 or 2:"))

def room13():
    #room13
    #Muhammad Mahmood
    print("Fallout 389")

def room14():
    #room14
    # Jeff Yock
    # CTC389-151
    # Final Project
    # Best Student Ever

    qstn1 = ["Study for the test", "Play video games", "Watch TV"]
    ansr1a = ["You feel tired but you know the test is important.", "You deserve a break!", "Your hear the theme song from your favorite TV show."]
    ansr1b = ["You study a little before bed.", "You play video games until midnight.", "You go to the family room and watch TV before bed."]

    qstn2 = ["Study a litte more before school.", "Pretend to be sick.", "Make a plan to cheat."]
    ansr2a = ["You decide it might be a good idea to review more before school.", "You burp the smelliest burp you can burp.", "It's too late to study now."]
    ansr2b = ["You study a little at breakfast and in the car.", "Then you moan 'Mom. I dont feel so good.'", "You heard there's a kid at school that sells test answers."]

    qstn3 = ["Buy the cheat sheet.", "Say 'No thanks' and walk to class.", "Warn the teacher about the cheat sheet."]
    ansr3a = ["The kid says 'Five bucks, pal.'", "You shake your head, say 'No thanks,' and hurry to class.", "You hurry to the classroom and tell your teacher what happened."]
    ansr3b = ["You think it's too much money but buy it anyway.", "The kid laughs and says 'OK, enjoy your F!'", "She thanks you and says 'Hmmm, I think those cheaters will get a little surprise today.'"]

    qstn4 = ["Try to help.", "Watch and laugh.", "Go to a different bathroom."]
    ansr4a = ["You feel afraid but want to help. You say 'Stop!' and start running to go tell an adult.", "You always wanted big friends. They seem so cool.", "You feel bad but don't want any more problems today."]
    ansr4b = ["The big kids get worried, let the kid go, and run off in the other direction.", "You start laughing too and ask if you can help flush.", "You pretend you didn't see or hear anything and walk away."]

    qstn5 = ["Peek at your neighbor's test.", "Try doing the math problem on scratch paper.", "Just guess."]
    ansr5a = ["Your desk partner finished his test super fast and is smiling the biggest smile.", "You decide to try modeling the problems on scratch paper. It really helps!", "You're totally lost on this test and regret not studying."]
    ansr5b = ["He didn't cover his paper and you decide to copy all of his answers.", "You remember how to solve these kinds of problems and finish just in time.", "You just cross you fingers and start guessing."]

    def firstQ (sentName):
      print(" ")
      print(sentName, "you had a long hard day at school.")
      print("It's Thursday night and you have one day left before the weekend.")
      print("But you know that Friday is test day.")
      print("You should study but you feel super tired.")
      print("What should you do?")
      count = 1
      for i in qstn1:
        print(count, i)
        count = count + 1
      choice = int(input("Enter 1, 2, or 3: "))
      choice = choice - 1
      print(ansr1a[choice])
      print(ansr1b[choice])
      choice = choice + 1
      if choice == 1:
          points1 = 30
      elif choice == 2:
          points1 = -10
      elif choice == 3:
          points1 = 0
      return (points1)
          
    def secondQ (sentName):
      print(" ")
      print("You hear your mom calling.", sentName, "wake up! It's time for school.")
      print("You quickly get dressed but feel worried about your test")
      print("Maybe you could study a little more.")
      print("Or maybe it's time for a new plan.")
      print("What should you do?")
      count = 1
      for i in qstn2:
        print(count, i)
        count = count + 1
      choice = int(input("Enter 1, 2, or 3: "))
      choice = choice - 1
      print(ansr2a[choice])
      print(ansr2b[choice])
      choice = choice + 1
      if choice == 1:
          points2 = 20
      elif choice == 2:
          print("Your mom feels your forehead, and decides to take you to the doctor.")
          print("The doctor gives you a PAINFUL SHOT with a GIANT NEEDLE!")
          print("Now you REALLY feel sick.")
          print(" ")
          points2 = -500
      elif choice == 3:
          points2 = -30
      return (points2)

    def thirdQ (sentName):
      print(" ")
      print("When you get to school lots of kids are hanging out waiting for the gate to open.")
      print("One of the older kids sees you and walks over.")
      print("He says, 'Hey", sentName, "do you wanna buy the answers for your Math test today?'")
      print("What should you do?")
      count = 1
      for i in qstn3:
        print(count, i)
        count = count + 1
      choice = int(input("Enter 1, 2, or 3: "))
      choice = choice - 1
      print(ansr3a[choice])
      print(ansr3b[choice])
      choice = choice + 1
      if choice == 1:
          print("As soon start looking at the test answers, you feel a tap on your shoulder.")
          print("You turn around and it's the PRINCIPAL!")
          print("He takes the you and the cheat sheet straight to his office and CALLS YOUR MOM!")
          print(" ")
          points3 = -500
      elif choice == 2:
          points3 = 10
      elif choice == 3:
          points3 = 20
      return (points3)

    def fourthQ (sentName):
      print(" ")
      print("You still feel nervous about the test so you ask if you can use the restroom first.")
      print("The teacher says, 'OK", sentName, "but be quick. We are about to start the test.")
      print("You hurry out to the closest restroom but when you go in you see three older kids bullying a little kid.")
      print("They are trying to put him into the toilet. They are laughing so hard they dont see you.")
      print("What should you do?")
      count = 1
      for i in qstn4:
        print(count, i)
        count = count + 1
      choice = int(input("Enter 1, 2, or 3: "))
      choice = choice - 1
      print(ansr4a[choice])
      print(ansr4b[choice])
      choice = choice + 1
      if choice == 1:
          points4 = 10
      elif choice == 2:
          print("With all the laughing you don't notice the school safety officer come into the restroom.")
          print("You and all the big kids get SUSPENDED FOR BULLYING!")
          print("Your parents are VERY ANGRY and DISAPPOINTED.")
          print(" ")
          points4 = -500
      elif choice == 3:
          points4 = 0
      return (points4)
      
    def fifthQ (sentName):
      print(" ")
      print("It's finally time for the Math test.")
      print("You write", sentName, "on the top of your paper and begin.")
      print("It starts out easy but gets harder and harder.")
      print("You get stuck on a few problems and time is running out.")
      print("What should you do?")
      count = 1
      for i in qstn5:
        print(count, i)
        count = count + 1
      choice = int(input("Enter 1, 2, or 3: "))
      choice = choice - 1
      print(ansr5a[choice])
      print(ansr5b[choice])
      choice = choice + 1
      if choice == 1:
          print("After the test, the teacher announces she had heard there was a cheat sheet being sold on campus.")
          print("So she changed all the answers so anyone who used it would get every question wrong instead!")
          print("Your neighbor stops smiling and starts crying. They used the cheat sheet and know they got a ZERO!")
          print("And since you copied him... SO DID YOU!")
          points5 = -500
      elif choice == 2:
          points5 = 20
      elif choice == 3:
          points5 = -20
      return (points5)

    def results(score):
      if score == 100:
        print("Your grade is A+ and you made great choices today")
        print("You truly are the BEST STUDENT EVER!")
        print("Congratulations, you got the best ending!")
      elif score == 90:
        print("Your grade is A")
        print("So close! You did very good today but there is one better ending.")
      elif score == 80:
        print("Your grade is B")
        print("You did good today but there are better endings.")
      elif score == 70:
        print("Your grade is C")
        print("You did OK today but you should try again.")
      elif score == 60:
        print("Your grade is D")
        print("You barely passed! You should definitely try again.")
      elif score < 60:
        print("Your grade is F! You need to think about your choices. Try again!")
 
    print("You quickly scan the room noting the doors are all the same but the number plates are not.")  
    print("You wish you had time to make a more calculated decision but the water is rising surprisingly fast.")
    print("For some reason your eyes are drawn to the colorful plate for Room 14")
    print("Without thinking much more about it, you rush to the door, turn the handle, and enter.")
    print(" ")
    print("Closing the door behind you is diffcult as the water is rushing in, but you finally get it shut.")
    print("As you turn around, you are shocked to see a near perfect copy of your childhood bedroom.")
    print("The only difference is a bizzare object in the center of the room.")
    print("It is a smooth white cylinder about four feet tall and eight inches in diameter.")
    print("There appears to be some sort of stylus or pen sitting on top.")
    print("The base of the cylinder sits in a slight depression in a circle of small holes.")
    print("The water that entered with you is quickly draining through them.")
    print(" ")
    print("Though you feel disoriented by the room's appearance, you approach the cylinder.")
    print("Inscribed in the circular top, in colorful Comis Sans, is the following message... ")
    print("Will you play Best Student Ever? Check yes or no.")
    print("Beneath that are two crudely drawn squares that are marked 'yes' and 'no' in lower case letters.")
    print("You somehow feel it necessary to use the stylus to check one of the boxes.")

    play = input("Which box do you check? Type yes or no: ")
    if play == "no":
        print(" ")
        print("Thinking this whole situation is just too absurd, you scoff and check the 'no' box.")
        print("You instantly regret it as you hear ominous creaking getting louder from the door behind you.")
        print("As the cylinder sinks down into the depression, you notice the illusion of your childhood bedroom fading.")
        print("You turn just in time to see the door burst and the flood waters of your doom rushing in.")
      
    else:
       print(" ")
       print("Thinking that the only way out of this bizarre situation is to be proactive, you check the 'yes' box.")
       print("You feel odd as the cylinder sinks down into the depression and disappears.") 
       print("You are shocked to notice you are getting smaller and YOUNGER!")
       print("As you continue regressing, your mind gets foggy and you vaguely begin to remember a forgotton memory.")
       print("You were seven years old and were struggling with making good choices.")
       print("Your last fully cognizant thought is of a very critical day at school and a very important test.")
  
       while play == "yes":  
        score1 = 0
        score2 = 0
        score3 = 0
        score4 = 0
        score5 = 0
        scoreTot = 0
        print(" ")
        print ("Somehow you feel you've done this before...")
        print ("Never having heard of 'deja vu' at age seven, you think it's odd but otherwise ignore it.")
        print ("All week you've been lectured about good choices and bad choices.")
        print("you look at your just completed homework on your desk and notice you forgot to put your name on it.")
        print("You write your name on the top and consider what to do next.")
        plyrName = input("(Type in your name): ")
        print(" ")
        score1 = firstQ(plyrName)
        score2 = secondQ(plyrName)
        if score2 > -100:
          score3 = thirdQ(plyrName)
          if score3 > -100:
            score4 = fourthQ(plyrName)
            if score4 > -100:
              score5 = fifthQ(plyrName)
              scoreTot = scoreTot + score1 + score2 + score3 + score4 + score5
              if scoreTot < 0:
                scoreTot = 0
              print(" ")
              print ("The teacher says,'I have graded all the tests.'")
              print (plyrName, "your test score is", scoreTot)
              results(scoreTot)
              print(" ")
        play = input("Would you like to relive this day again? Type yes or no: ")
    print("Game Over")


def room15():
    #room15
    #Jitender Rajpoot
    print("Final Destination.")
   # def room15():
    #room15
    #Jitender Rajpoot
    print("Good choice. You've avoided drowning in the previous room.")
    userName = input("Enter your name: ")

    def play_game():

      print("Hi ", userName, ", welcome to 'Final Destination'--an interactive experience in which you navigate death, I mean, navigate your way to the moon and back to Earth. Safe journey!")
      points = 0        #new feature keep score for correct decisions
      #decision 1
      print("Choose your spacecraft:")

      spacecraft = ["Space Shuttle", "Solar Shuttle", "Prototype Shuttle"]    #list feature
      index = 0
      for item in spacecraft:               #loop to print list items with their index+1
        index = index+1
        print(index, item)

      choice1 = input("Enter 1, 2, or 3: ")

      if choice1 == "1":
        print("Sorry, rocket fuel prices are unaffordable. This shuttle can't fly to the moon. Flooding from the main room blocks your exit, so you can't escape and drown to deaty, Sorry, Game over!")
      elif choice1 == "2":
        points = points + 10            #add points for correct decision
        print("Great choice! Sun's fusion will power you to the moon. Points: ", points)
        #Decision 2
        print("Choose your flight path:")

        flightPath = ["Lunar Orbit", "Fly to Moon and back", "Land on Moon"]
        index = 0
        for item in flightPath:
          index = index + 1
          print(index, item)

        choice2 = input("Enter 1, 2, or 3: ")

        if choice2 == "1":
          print("The shuttle remains in an infinite loop rotating around the moon. Sorry, you die due to dehydration after 88 days. Game over!")
        elif choice2 == "2":
          print("You returned back to Earth but never stepped on the Moon.")
          print("Although you technically saw the Moon from close range, you return to Room 15, which is flooded. You valiantly struggle but succumb to a drowning death after 33 minutes. Sorry, Game over!")
        elif choice2 == "3":
          points = points + 20
          print("Well done! You made it to the Moon. Now let's explore, but first let's nourish your body. Points: ", points)
          #Decision 3
          print("What do you want to eat?")

          nourishment = ["High energy food", "Freeze dried meal", "Canned tuna and peppers with aioli"]
          index = 0
          for item in nourishment:
            index = index + 1
            print(index, item)

          choice3 = input("Enter 1, 2, or 3: ")

          if choice3 == "1":
            print("This food has too many calories. Unfortunately your heart can't handle your low blood pressure but high blood glucose levels.")
            print("Your heart decides to give up rather than continue the torture. Sorry, you die. Game over!")
          elif choice3 =="2":
            points = points + 30
            print("These items have an unsavory flavor and undesirable texture but exactly what your body needs. Points: ", points)
            #Decision 4
            print("Now let's find an activity to do. What would you like?")

            activity = ["Collect Moon Rocks", "Conduct Chemical Experiments", "Take Photographs"]
            index = 0
            for item in activity:
              index = index + 1
              print(index, item)

            choice4 = input("Enter 1, 2, or 3: ")

            if choice4 == "1":
              points = points + 40
              print("This was your best move! You've found rare Moon Diamonds, which will pay for the next 3 generations of your family. Points:", points)
              print("You should head back to Earth and enjoy your wealth. Where do you want to land?")

              landing = ["Ocean landing", "Desert Landing", "Landing Pad"]
              index = 0
              for item in landing:
                index = index + 1
                print(index, item)

              choice5 = input("Enter 1, 2, or 3: ")
              if choice5 == "1":
                points = points + 50
                print("You win! Ocean was the safest and least dangerous space to re-enter Earth. Enjoy your Moon Diamonds! Points: ", points)
              elif choice5 == "2":
                print("The ambient temprature above the desert combined with heat from your re-entry velocity disintegrated the shuttle.")
                print("Everything including you and the Moon Diamonds dissolved into the thin air. Sorry, game over!")
              elif choice5 == "3":
                print("The booster engines to decelerate the shuttle in order to land malfunctioned and accelerated instead.")
                print("At the sound of speed, you died alongside a Sonic boom. Sorry, game over!")

            elif choice4 == "2":
              print("Sorry, the gases released from the chemical reactions are poisonous.")
              print("From an allergic reaction, our sweat pores extract every drop of blood from you leaving you dead. Sorry, game over!")
            elif choice4 == "3":
              print("The batteries aren't meant to operate in Moon's extreme temperatures. The camera explodes severing your cranial nerves.")
              print("So you feel no pain, but take 72 hours to take your last breath. Sorry, game over!")

          elif choice3 == "3":
            print("This was the worst choice. All items were infected with botulinum toxin.")
            print("You died a slow suffocating death from paralysis of your lungs. Sorry, game over!")
      elif choice1 == "3":
        print("Sorry, the Prototype wasn't tested properly. It exploded midflight. Sorry, you die. Game over!")


    play_game()

    play_again = input("Do you want to try navigating to the moon and back again? Type 'yes' or 'no': ")

    while play_again == "yes":
      play_game()
      play_again = input("Would you like to try again? ")
    else:
      print("Thanks for trying 'Final Destination.' Safe travels!", userName)

def room16():
    #room16
    # Moshe Molcho
    print("Escape the Possessed Math Classroom")
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
def room17():
    #room17
    #Josue Zamora
    print("Two Minute Drill")

def room18():
   #room18
    #Cesar Cano
    print("Dark Gengar.")

def room19():
    #Patricia Flores
    print("Star Wars")

def room20():
    #room20
    #Benson Chau
    print("Big Bang Theory Sim")

def room21():
    #room21
    #Dawei Sun
    print("The Lost Jade Pendant")


def room22():
    #room22
    #Rogelio Jeronimo
    print("Playing in the Fun House.")

def room23():
    #room23    
    # Mario Magallanes

    game = 1
    option = 0
    name = input("Greetings, What is your name?: ")
    print ("")
    print (name, "You are about to enter the video game labyrinth. You will go through 6 chambers.")
    print ("Each chamber will have items or fighters for you to select.")
    print ("Chose carefully. The outcome can be to advance, to reset, or to die for.")

#chamber 1 
    while game != 0:
        if game == 1:
            print("")
            print("****************")
            print ("Welcome to the Game of Zelda Chamber.")
            print (" 1 The Ocarina of Time ")
            print (" 2 Master Sword ")
            print (" 3 Hyland Shield ")
            print ("****************")
            print (name)
            option = int(input("Please make your selection: "))

            if option == 1:
                print ("The Ocarina of Time will let you move forward")
                game = 2
        
            elif option == 2:
                print ("The Master Sword will let you try again")
                game = 1
        
            elif  option == 3:
                print ("The Hyland Shield will kill you")
                game = 0 

#chamber 2 
        if game == 2:
            print("")
            print("****************")
            print ("Welcome to the Mario World Chamber.")
            print (" 1 Koopa ")
            print (" 2 Goomba ")
            print (" 3 Shy Guy ")
            print ("****************")
            print (name)
            option = int(input("Please make your selection: "))

            if option == 1:
                print ("You defeated Koopa. Move Forward")
                game = 3
        
            elif option == 2:
                print ("It is a tie! Try again")
                game = 2
        
            elif  option == 3:
                print ("The Shy Guy was too much for you!")
                game = 1 

#chamber 3 
        if game == 3:
            print("")
            print("****************")
            print ("Welcome to the Contra Chamber.")
            print (" 1 Spear Gun ")
            print (" 2 Laser Gun ")
            print (" 3 Rapid Fire ")
            print ("****************")
            print (name)
            option = int(input("Please make your selection: "))

            if option == 1:
                print ("The Spear Gun is a keeper. Move Forward")
                game = 4
        
            elif option == 2:
                print ("The Laser Gun is defective, Try again")
                game = 3
        
            elif  option == 3:
                print ("Rapid Fire Gun exploded in your hand. Try Again!!")
                game = 1 

#chamber 4 
        if game == 4:
            print("")
            print("****************")
            print ("Welcome to the Pac-Man Chamber.")
            print (" 1 Blinky ")
            print (" 2 Pinky ")
            print (" 3 Inky ")
            print (" 4 Clyde ")
            print ("****************")
            print (name)
            option = int(input("Please make your selection: "))

            if option == 1 or option == 2:
                print ("You defeated Blinky or Pinky. Move Forward")
                game = 5
        
            elif option == 3:
                print ("It is a tie! Try again")
                game = 4
        
            elif  option == 4:
                print ("The Shy Guy was too much for you!")
                game = 0 

#chamber 5 
        if game == 5:
            print("")
            print("****************")
            print ("Welcome to the Street Fighter Chamber.")
            print (" 1 Hadouken ")
            print (" 2 Shoryuken ")
            print (" 3 Sonic Boom ")
            print ("****************")
            print (name)
            option = int(input("Please make your selection: "))

            if option == 1:
                print ("The Hadouken served you well! Move to the next level")
                game = 6
        
            elif option == 2:
                print ("It is a tie! Try again")
                game = 2
        
            elif  option == 3:
                print ("The Sonic Boom took you off!")
                game = 0 

#chamber 6 
        if game == 6:
            print("")
            print("****************")
            print ("Welcome to the Castlevania's Chamber. Select your opennet Trevor Belmont!")
            print (" 1 Count Dracula")
            print (" 2 Medusa ")
            print (" 3 Death ")
            print ("****************")
            print (name)
            option = int(input("Please make your selection: "))

            if option == 1:
                print ("You defeated the game!!!")
                print (name)
                game = int(input("Enter 1 if you wan to play again and 0 to end the game: "))
        
            elif option == 2:
                print ("It is a tie! Try again")
                game = 6
        
            elif  option == 3:
                print (name)
                print ("Since you had an honorable defeat. Death will grant you a second cahnce!")
                game = 1 

        if game == 0: 
            print("")
            print ("You lost your life! Thank you for playing")
            print (name)
            game = int(input(" Enter 1 if you wish to play again. 0 if you don't:  "))

def room24():
    #room24
    print("This door is locked.")

def room25():
    #room25
    print("This door is locked.")

def room26():
    #room26
    #Janelle Piva
    print("The Haunted School.")

def room27():
    #room27
    print("This door is locked.")

def room28():
    #room28
    #Vicky Kong
    print("Journey to K-Pop Concert")
    print("You are going to a K-Pop concert soon. Let's see how prepared you are to go the concert!")

    name=input("What is your name super fan?")

    x="yes"

    while(x=="yes"):
        play=True

        #part 1
        print("Hello",name,"! before we start heading out, you need to choose an outfit!")
        print("1. Comfy outfit")
        print("2. Silly Costume")
        print("3. Nice outfit")
        y=int(input("Enter the number to choose your outfit!"))

        if(y==1):
            print("Nice choice! Being confortable is important to having fun at a concert!")
        if(y==2):
            print("All the fans around you will love your fit and take pictures with you! Everyone is having a good laugh.")
        if(y==3):
            print("You look really nice! Slayyyy!")

        #part 2
        print("Now that you have an outfit, let's pack your concert bag!")
        concertitems=["phone","portable battery","tickets","wallet","bottle of water","keys","portable fan","lightstick","polaroid","freebies"]
        print("In your concert bag, you have included:")
        for i in concertitems:
            print(i)
        print("Oh no! Your concert bag is full! You will need to take an item out.")
        print("1. Lightstick")
        print("2. Polaroid")
        print("3. Freebies")
        z=int(input("Enter the number to take out that item:"))

        if(z==1):
            print("You can't go to a K-Pop concert without a lightstick! You are not able to go to the concert anymore.")
            x=input("Would you like to play again?")
            play=False

        if(z==2):
            print("Good choice! You are not able to take a polaroid into the venue anyways. It is best to not bring it.")

        if(z==3):
            print("You must bring your freebies! It is K-pop culture to give out freebies to other fans.")
            x=input("Would you like to play again?")
            play=False

        #part 3
        if(x=="yes" and play): 
            print("Now that you are ready, let's plan out on when you should arrive to the venue!")
            print("1. 12pm")
            print("2. 5pm")
            print("3. 8pm")
            a=int(input("Enter the number for the time you plan to arrive at the venue:"))

            if(a==1):
                print("That is a bit early, but you got to exchange a lot of freebies with other fans!")

            if(a==2):
                print("5pm is a good time! You have enough time to find parking and line up to get inside the venue!")

            if(a==3):
                print("You are late! The concert has already started! You did not make it to the concert.")
                x=input("Would you like to play again?")
                play=False

        #part 4
        if(x=="yes" and play):
            print("Let's decide how you would get to the venue.")
            print("1. Driving")
            print("2. Public Transportation")
            print("3. Walking")
            b=int(input("Enter the number for your means of transportation:"))

            if(b==1):
                print("Not the best option in my opinion. Hope you are okay with paying for parking!")

            if(b==2):
                print("Public transportation is the best!")

            if(b==3):
                print("Walking is not a good option especially if you live far from the venue. You did not make it to the concert.")
                x=input("Would you like to pay again?")
                play=False

        #part 5
        if(x=="yes" and play):
            print("You have made it to the venue! Let's decide what you should do before going inside!")
            print("1. Use the restroom")
            print("2. Get food! Yum!")
            print("3. Buy merch!")
            c=int(input("Enter the number for the activity you want to do:"))

            if(c==1):
                print("Use the restroom inside the venue! The portable restrooms are so dirty!")
                x=input("Would you like to play again?")

            if(c==2):
                print("Yes! Eat before going in! The food inside the venue is overpriced.")
                print("Have fun at the concert!")
                x=input("Would you like to play again?")

            if(c==3):
                print("Yes! Buy some merch to commemorate tonight!")
                print("Have fun at the concert!")
                x=input("Would you like to play again?")

    print("Thank you for playing!")

def room29():
    #room29
    print("This door is locked.")

def room30():
    #room30
    #Tonya McIntyre
    print("Wise One")
    

def room31():
    #room31
    #Karl Kottman
    print("Musical Odyssey")


    psychsongs = ["'Time of the Season'","'Hung up on a Dream'","'Maybe After He's Gone'","'I am the Walrus'","'Blue Jay Way'","'Strawberry Fields Forever'","'Purple Haze'","'Hey Joe'","'The Wind Cries Mary'","'The End' by The Doors","'In-A-Gadda-Da-Vida' by Iron Butteryfly","'Shangri-la' by The Kinks"]

    punksongs = ["'Bombshell'","'Caution'","'Sound System'","'Gacked on Anger'","'GFY'","'Got You'","'Triumph of the Swill'","'Macho Insecurity'","'Take This Job and Shove It'","'New Noise'by Refused","'Don't Light My Fire' by Otoboke Beaver","'Waiting Room' by Fugazi"]

    indiesongs = ["'Shady Lane'","'Type Slowly'","'Stereo'","'Pedestrian at Best'","'Depreston'","'Nobody Really Cares If You Don't Go to the Party'","'Stupidity Tries'","'Happiness/The Gondola Man'","'Somebody That I Used To Know'","'All Caps'by MF Doom'","'Respiration' by Black Star","'Ghostwriter' by RJD2"]

    def psychedelia():
        print("You've entered the psychedelic room where you find a turntable and the following three records:")

        print("1. 'Odessey and Oracle' by The Zombies")
        print("2. 'Magical Mystery Tour' by The Beatles")
        print("3. 'Are You Experienced' by Jimi Hendrix")

        psychalbum = int(input("Enter the number of the album you want to play:"))

        if (psychalbum == 1):
            print("You're getting lost in the sound of The Zombies and can't get enought, especially of these three tracks:")

            print("1.", psychsongs[0])
            print("2.", psychsongs[1])
            print("3.", psychsongs[2])

            psychsong1 = int(input("Enter the number of the song you want to listen to on repeat:"))

            if (psychsong1 == 2):
                print("You've reached a dream-like state. Do you want to:")

                print("1. ...keep dreaming?")
                print("2. ...listen to more music?")
                print("3. ...wake up?")

                whatnext = int(input("Enter the number of your choice:"))

                if (whatnext == 2):
                    print("Great! What song will you listen to next?")

                    print("1.", psychsongs[9])
                    print("2.", psychsongs[10])
                    print("3.", psychsongs[11])

                    finalsong = int(input("Enter the number of your song choice:"))

                    if (finalsong == 1):
                        print("This song is too long! Sadly, you can't finish your musical odyssey,", name,".")

                    elif (finalsong == 2):
                        print("This song is too long! Sadly, you can't finish your musical odyssey,", name,".")

                    else:
                        print("Congratulations! You've reached Shangri-la and completed your musical odyessey! Enjoy your newfound enlightenment!")
            

                elif (whatnext == 1):
                    print("You slept too long! Sadly, your musical odyessy is over,", name,".")

                else:
                    print("You've awakened from your psychedelic experience and are ready for something new.")
                    musical_odyssey()


            else:
                print("Listening to too much of The Zombies has turned you into a Zombie! Now you can't stop listening! Sadly, your musical odyssey has come to a premature end,", name,".")

        

        elif (psychalbum == 2):
            print("You love the mystery tour! Which song will you repeat?")

            print("1.", psychsongs[3])
            print("2.", psychsongs[4])
            print("3.", psychsongs[5])

            psychsong2 = int(input("Enter the number of the song you want to repeat:"))

            if (psychsong2 == 1):
                print("You've turned into a walrus! Sadly, you can't finish your musical odyssey like this,", name,"!")
        
            else:
                print("Excellent choice! But now it's time to try listening to something different.")
                punk()

        else:
            print("You're experienced now! Which song do you want to hear again?")

            print("1.", psychsongs[6])
            print("2.", psychsongs[7])
            print("3.", psychsongs[8])

            psychsong3 = int(input("Enter the number of the song you want to repeat:"))

            if (psychsong3 == 1):
                print("You got lost in the haze and have to start over.")
            else:
                print("Excellent choice! But now it's time to try listening to something different.")
                indie()


    def punk():
        print("You've entered a disheveled room with a turntable and the following three records:")

        print("1. 'Operation Ivy' by Operation Ivy")
        print("2. 'Amyl and The Sniffers' by Amyl and The Sniffers")
        print("3. 'Bedtime for Democracy' by Dead Kennedys")

        punkalbum = int(input("Enter the number of the album you want to play:"))

        if (punkalbum == 1):
            print("You loved this classic album! Which song do you want to listen to again?")

            print("1.", punksongs[0])
            print("2.", punksongs[1])
            print("3.", punksongs[2])

            punksong1 = int(input("Enter the number of the song you want to repeat:"))

            if (punksong1 == 2):
                print("Since you liked", punksongs[1],", you might like one of these songs:")

                print("1.", punksongs[9])
                print("2.", punksongs[10])
                print("3.", punksongs[11])

                punksong4 = int(input("Enter the number of the song you want to hear:"))

                if (punksong4 == 1):
                    print("You're ready for a new beat.")
                    psychedelia()

                elif (punksong4 == 2):
                    print("Great song! But now you need something slower.")
                    indie()

                elif (punksong4 == 3):
                    print("You waited too long. Sadly, your musical odyssey has ended,", name,".")

            else:
                print("You got too pumped up! Time for something slower.")
                indie()


        if (punkalbum == 2):
            print("You can't get enough of Amyl! Which track do you want to listen to again?")

            print("1.", punksongs[3])
            print("2.", punksongs[4])
            print("3.", punksongs[5])

            punksong2 = int(input("Enter the number of the song you want to repeat:"))

            if (punksong2 == 3):
                print("Great song! But time for a change of pace.")
                psychedelia()

            else:
                print("Alright, let's take it down a notch.")
                indie()

        if (punkalbum == 3):
            print("Nice choice! Which song did you like the best?")

            print("1.", punksongs[6])
            print("2.", punksongs[7])
            print("3.", punksongs[8])

            punksong3 = int(input("Enter the number of your choice:"))

            if (punksong3 == 3):
                print("You quit your job! Now you have more time for music! Let's try another room.")
                psychedelia()

            elif (punksong3 == 2):
                print("It's great you're not too macho! Now let's listen to something different.")
                indie()

            elif (punksong3 == 1):
                print("I'm afraid the swill has triumphed. Sadly, your musical odyssey has come to an end,", name,".")





    def indie():
        print("You've entered a hip room with a turntable and the following three records:")

        print("1. 'Brighten the Corners' by Pavement")
        print("2. 'Sometimes I Sit and Think, and Sometimes I Just Sit' by Courtney Barnett")
        print("3. 'Figure 8' by Elliot Smith")

        indiealbum = int(input("Enter the number of the album you want to play:"))

        if (indiealbum == 1):
            print("Did you catch all the lyrics? Which song on the album deserves another listen?")

            print("1.", indiesongs[0])
            print("2.", indiesongs[1])
            print("3.", indiesongs[2])

            indiesong1 = int(input("Enter the number of the song you want to hear again:"))

            if (indiesong1 == 1):
                print("Great choice! Be sure to listen to it's B-side, 'Harness Your Hopes', as well before you move on to the next room.")
                punk()

            elif (indiesong1 == 3):
                print("What a classic indie rock song! Want to listen to a classic indie hip-hop track?")

                print("1.", indiesongs[9])
                print("2.", indiesongs[10])
                print("3.", indiesongs[11])

                indiesong4 = int(input("Enter the number of the track you want to hear:"))

                if (indiesong4 == 1):
                    print("MF Doom will let you continue your musical odyssey.")
                    psychedelia()

                else:
                    print("Hope you enjoyed that tune! Now it's time for something different.")
                    punk()

            else:
                print("'Stereo' broke your stereo. Sadly, your musical odyssey has come to an early end,", name,".")


        if (indiealbum == 2):
            print("Which song on the album deserves another listen?")

            print("1.", indiesongs[3])
            print("2.", indiesongs[4])
            print("3.", indiesongs[5])

            indiesong2 = int(input("Enter the number of the song you want to hear again:"))

            if (indiesong2 == 1):
                print("This song is definitely more than pedestrian. Continue your musical odyssey.")
                psychedelia()

            elif (indiesong2 == 2):
                print("Nice choice, but a bit depressing. Time to liven things up!")
                punk()

            else:
                print("Unfortunately, nobody really cares if you finish your musical odyessey. Goodbye,", name,".")


        if (indiealbum == 3):
            print("Such a good album! Which track do you want to hear again?")

            print("1.", indiesongs[6])
            print("2.", indiesongs[7])
            print("3.", indiesongs[8])

            indiesong3 = int(input("Enter the number of the song you want to repeat:"))

            if (indiesong3 == 2):
                print("'Happiness' made you too sad to continue your musical odyssey. Maybe you can try again when you feel better.")

            elif (indiesong3 == 1):
                print("Stupidity succeeded! You want to listen to more. Step into the next room.")
                punk()

            else:
                print("You've moved on and no longer care about your musical odyssey. Maybe you'll try again if you change your mind.")

            
    def musical_odyssey():
        print("Before you are three doors named as follows:")

        print("1. Psychedelia")
        print("2. Punk")
        print("3. Indie")

        choice1 = int(input("What number door will you enter?:"))

        if (choice1 == 1):
            psychedelia()

        elif (choice1 == 2):
            punk()

        elif (choice1 == 3):
            indie()

    name = input("Welcome to the Land of Rock! What is your name?:")

    print("Hello,", name,"! You are about to embark on a musical odyssey. To fully complete this experience, you must choose the right path forward. But there is only one path that will take you all the way, so choose wisely.")

    while True:
        answer = input("Whether it's your first time or you're coming back for more, are you ready to embark on a musical odyssey?:")
        if (answer == "yes"):
            musical_odyssey()

        else:
            break



def room32():
    #room32
    print("This door is locked.")

def room33():
    #room33
    print("This door is locked.")

def room34():
    #room34
    print("This door is locked.")

def room35():
    #room35
    print("This door is locked.")

def room36():
    #room36
    print("This door is locked.")

def room37():
    #room37
    print("This door is locked.")

def room38():
    #room38
    print("This door is locked.")

def room39():
    #room39
    print("This door is locked.")

def room40():
    #room40
    print("This door is locked.")

def room41():
    #room41
    print("This door is locked.")

def room42():
    #room42
    print("This door is locked.")

def room43():
    #room43
    print("This door is locked.")

def room44():
    #room44
    print("This door is locked.")

def room45():
    #room45
    print("This door is locked.")

def room46():
    #room46
    print("This door is locked.")

def room47():
    #room47
    print("This door is locked.")

def room48():
    #room48
    print("This door is locked.")

def room49():
    #room49
    print("This door is locked.")

def room50():
    #room50
    #garrett poppe
    print("Game Title: Best Game Ever!")


#main program

mainChoice = 0

print("____________________________________")
print("")
print("Welcome to the role playing game!")
time.sleep(1)
print(".....")
time.sleep(1)
print("....")
time.sleep(1)
print("...")
time.sleep(1)
print("..")
time.sleep(1)
print(".")
time.sleep(1)
print("You wake up and find yourself in the center of a massive room.")
print("You do not know how you arrived here, but you look around and realize you are at the center of the room.")
print("The walls of this circular room are made of many doors.")
print("Each door has a finely crafted number plate. It appears there are 50 doors.")
print("All of a sudden, the room starts to fill with water. You must act quickly before the room floods and you drown.")
mainChoice = int(input("You decide you're going to exit through one of the doors. Which door number do you choose? "))

if mainChoice == 1:
    room1()
elif mainChoice == 2:
    room2()
elif mainChoice == 3:
    room3()
elif mainChoice == 4:
    room4()
elif mainChoice == 5:
    room5()
elif mainChoice == 6:
    room6()
elif mainChoice == 7:
    room7()
elif mainChoice == 8:
    room8()
elif mainChoice == 9:
    room9()
elif mainChoice == 10:
    room10()
elif mainChoice == 11:
    room11()
elif mainChoice == 12:
    room12()
elif mainChoice == 13:
    room13()
elif mainChoice == 14:
    room14()
elif mainChoice == 15:
    room15()
elif mainChoice == 16:
    room16()
elif mainChoice == 17:
    room17()
elif mainChoice == 18:
    room18()
elif mainChoice == 19:
    room19()
elif mainChoice == 20:
    room20()
elif mainChoice == 21:
    room21()
elif mainChoice == 22:
    room22()
elif mainChoice == 23:
    room23()
elif mainChoice == 24:
    room24()
elif mainChoice == 25:
    room25()
elif mainChoice == 26:
    room26()
elif mainChoice == 27:
    room27()
elif mainChoice == 28:
    room28()
elif mainChoice == 29:
    room29()
elif mainChoice == 30:
    room30()
elif mainChoice == 31:
    room31()
elif mainChoice == 32:
    room32()
elif mainChoice == 33:
    room33()
elif mainChoice == 34:
    room34()
elif mainChoice == 35:
    room35()
elif mainChoice == 36:
    room36()
elif mainChoice == 37:
    room37()
elif mainChoice == 38:
    room38()
elif mainChoice == 39:
    room39()
elif mainChoice == 40:
    room40()
elif mainChoice == 41:
    room41()
elif mainChoice == 42:
    room42()
elif mainChoice == 43:
    room43()
elif mainChoice == 44:
    room44()
elif mainChoice == 45:
    room45()
elif mainChoice == 46:
    room46()
elif mainChoice == 47:
    room47()
elif mainChoice == 48:
    room48()
elif mainChoice == 49:
    room49()
elif mainChoice == 50:
    room50()
else:
    print("That was the wrong choice....")
    time.sleep(1)
    print("You have perished.")


print("____________________________________")
print("")
time.sleep(2)
print(".")
time.sleep(2)
print("..")
time.sleep(2)
print("...")
time.sleep(2)
print("....")
time.sleep(2)
print(".....")
time.sleep(2)
print("You wake up and realize this was all a dream.")


