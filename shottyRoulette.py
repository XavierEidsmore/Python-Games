#Birdshot Roulette (Based on Buckshot Roulette by Mike Klubnika)
#By Xavier Eidsmore
#2/15/2024 - 2/16/2024

#Import random number generator module
import random

#Code for generating random number in a range
#random.randint(0,100)
#Chance values: 0 = 0% 50 = 50% 100 = 100%
#Chance roller
"""
chance = random.randint(0,100)
print(chance)
"""

#Game begins

#Title
print("~~~Birdshot Roulette~~~ (Based on Buckshot Roulette by Mike Klubnika)",
      "\nBy Xavier Eidsmore")

print("\n---Start Game---")
dev_tool_used = False

player_name = input("Enter your name: ")

#[DEV TOOL] Set game number
#game_number_counter = int(input("[Dev Tool] Enter the Game Number (1-3): "))
#dev_tool_used = True

print("\nYou woke up. As it turned out, that was the worst mistake of your life.")

#Pause
input("\nPress [Enter] to continue: ")

print("\nYou stumble out of the bathroom stall. And into the room at the back of the booming club party.")

#Pause
input("\nPress [Enter] to continue: ")

#Player encounts The Dealer
print("\nThe Dealer: "+player_name+", you know how this whole game works. ;)",
      "\nI deal, you die. And maybe I die if you're lucky.",
      "\n*shotgun cocks* It's shotgunning time. >:)"
      )
print(player_name+": Aight, bet.")

#Pause
input("\nPress [Enter] to continue: ")

if (dev_tool_used == False):
    game_number_counter = 1

#Setup list
player_items = []
dealer_items = []


#Begin Death Games
while (game_number_counter <= 3):
    #Death game begins
    print("\n---Game #"+str(game_number_counter)+"---")
    #Game 1
    if (game_number_counter == 1):
        player_life = 3
        dealer_life = 3
        print("""Dealer: In this game, the goal is to reduce your opponent's life to 0.
    -There are 2 types of shells randomly loaded into this gun. Red and gray.
    -Reds are filled with birdshot, and will damage the reciever's life. Grays are blank.
    -You can choose to shoot me with this gun, or shoot yourself.
    -Both will end your turn.
    -If you shoot me, I will take the damage if it's a red shell.
    -But if you shoot yourself with a gray shell, you skip your opponent's next turn.""")
        #Pause
        input("\nPress [Enter] to continue: ")

    #Game 2 (Items are introduced)
    elif (game_number_counter == 2):
        player_life = 5
        dealer_life = 5
        print("Dealer: It's time to switch it up.",player_name,";)",
              "\n*shotgun cocks*"
              )
    #Game 3 (Final Deathmatch)
    elif (game_number_counter == 3):
        player_life = 7
        dealer_life = 7
        print("Dealer: It's time to get serious.",player_name,">:)",
              "\n*shotgun cocks* But would you lose?\n"+player_name+": Nah, i'd win."
              )

    while (player_life > 0 and dealer_life > 0):
        print("\n--------------------------------------------------------------------------------------------------------",
              "\nYou hear the Dealer excitedly loading the shotgun with shells then cocks it."
              )
    
        shotgun_magazine = []

        number_of_red_shells = 0
        number_of_gray_shells = 0

        player_turn_skipped = False
        dealer_turn_skipped = False

        player_turn_skip_gray = False
        dealer_turn_skip_gray = False

        player_handcuffed = False
        dealer_handcuffed = False

        dealer_knows_chamber_shell = "none"

        #Player and dealer gets items
        #Magnifying glass: 0-10
        #Handcuffs: 11-30
        #Beer: 31-60
        #Cigarettes: 61-80
        #Saw: 81-100
        if (game_number_counter >= 2):
            #player gets 2 items.
            if (game_number_counter == 2):
                #player and dealer gets 2 items.
                number_of_items = 2
                
            elif (game_number_counter == 3):
                #player and dealer gets 4 items
                number_of_items = 4

            #Give items
            for y in range(number_of_items):
                item_chance = random.randint(1,100)
                if (item_chance > 80):
                    #Add Saw
                    player_items.append("Saw")
                elif (item_chance > 60):
                    #Add Cigarettes
                    player_items.append("Cigarettes")
                elif (item_chance > 30):
                    #Add Beer
                    player_items.append("Beer")
                elif (item_chance > 10):
                    #Add Handcuffs
                    player_items.append("Handcuffs")
                elif (item_chance > 0):
                    #Add Magnifying Glass
                    player_items.append("Magnifying glass")

            for z in range(number_of_items):
                item_chance = random.randint(1,100)
                if (item_chance > 80):
                    #Add Saw
                    dealer_items.append("Saw")
                elif (item_chance > 60):
                    #Add Cigarettes
                    dealer_items.append("Cigarettes")
                elif (item_chance > 30):
                    #Add Beer
                    dealer_items.append("Beer")
                elif (item_chance > 10):
                    #Add Handcuffs
                    dealer_items.append("Handcuffs")
                elif (item_chance > 0):
                    #Add Magnifying Glass
                    dealer_items.append("Magnifying glass")

        if (game_number_counter >= 2):
            print("\nSections of the tables unfold revealing rising trays that dump items on both sides of the tables.")
            print("\nThe Dealer: You've been dealt the items:",player_items,"\n\nI've been dealt:",dealer_items)

        #Shotgun loading and setup stuff
        #Set chance for red shell, and gray shell
        chance_for_red_shell = 50 #red shell: 0-50 gray shell: 51-100

        #set Shotgun Capacity
        if (game_number_counter == 1):
            shotgun_magazine_capacity = random.randint(2,3)

        elif(game_number_counter == 2):
            shotgun_magazine_capacity = random.randint(3,6)

        elif(game_number_counter == 3):
            shotgun_magazine_capacity = random.randint(4,8)

        #Load mandatory 1 red and 1 gray shell
        #load red shell
        shotgun_magazine.append("red shell")
        number_of_red_shells += 1
        #load gray shell
        shotgun_magazine.append("gray shell")
        number_of_gray_shells += 1

        #load shotgun randomly
        for x in range(shotgun_magazine_capacity - 2):
            chance = random.randint(1,100)
            if (chance <= chance_for_red_shell):
                #load red shell
                shotgun_magazine.append("red shell")
                number_of_red_shells += 1
            
            if (chance > chance_for_red_shell):
                #load gray shell
                shotgun_magazine.append("gray shell")
                number_of_gray_shells += 1

        #Shuffle shotgun magazine
        random.shuffle(shotgun_magazine)

        #Choose plural for shell or shells.
        if (number_of_red_shells == 1):
            plural_red_shells = "shell"
        else:
            plural_red_shells = "shells"
            
        if (number_of_gray_shells == 1):
            plural_gray_shells = "shell"
        else:
            plural_gray_shells = "shells"
            
        #Print how many shells and how many are red or gray
        print("\nThe Dealer: There are",number_of_red_shells,"red",plural_red_shells,"and",
              number_of_gray_shells,"gray",plural_gray_shells,"loaded into the shotgun randomly."
              )

        gun_not_empty = True
        #Inside loop of player and dealer's turn, until magazine runs out.
        while (gun_not_empty == True and player_life > 0 and dealer_life > 0):

#Player turn-------------------------------------------------------------------------------------------
            
            #Your turn.
            print("\n---------------------------------------------------------------------------------------------------------",
                  "\nIt's your turn.\n")
            if (player_turn_skipped == True):
                print("Your turn is skipped since the gun is empty.")
            shotgun_damage = 1
            if (dealer_handcuffed == True):
                print("The handcuffs fall off the Dealer.")
            if (player_handcuffed == True):
                print("Your turn is skipped since you're handcuffed.")
            dealer_handcuffed = False

            if (player_turn_skip_gray == True):
                print("The Dealer skips your turn.")
            dealer_turn_skip_gray = False
            
            dealer_knows_chamber_shell = "none"
            #Choose whether to shoot yourself or the dealer. Or use items.
            #Print Possible Choices
            inside_choice_loop = True
            while (inside_choice_loop == True and player_turn_skipped == False and player_handcuffed == False and player_turn_skip_gray == False):
                print("\nYour Life:",player_life,
                      "\nThe Dealer's life:",dealer_life,
                      "\n\n[Choose what to do.]",
                      "\n(1) Shoot the dealer.",
                      "\n(2) Shoot yourself",
                      "\n(3) Use an item"
                      )
                choice = input("\nEnter your choice: ")

                #Choose to shoot the Dealer
                if (choice == "1"):
                    if (len(shotgun_magazine) == 0):
                        print("You pull the trigger, and it clicks, echoing through the empty magazine.")
                        print("\nThe Dealer: The shotgun is empty. Time to put in new shells.")
                        inside_choice_loop = False
                        gun_not_empty = False
                        dealer_turn_skipped = True

                    elif (shotgun_magazine[0] == "red shell"):
                        print("You choose to shoot the dealer.")
                        print("You pull the trigger, and with a BANG!! Your shot hits The Dealer blasting him into the darkness.",
                              "\nThen he floats back to the table with a grin.",
                              "\n[Dealer life -"+str(shotgun_damage)+"]"
                              )
                        #Damage dealer
                        dealer_life -= shotgun_damage
                        if (dealer_life <= 0):
                            player_turn_skipped = True
                            dealer_turn_skipped = True

                        #Shell is removed from magazine
                        del shotgun_magazine[0]
                        inside_choice_loop = False

                    elif (shotgun_magazine[0] == "gray shell"):
                        print("You choose to shoot the dealer.")
                        print("You pull the trigger, it clicks. Nothing happens.")
                    
                        #Shell is removed from magazine
                        del shotgun_magazine[0]
                        inside_choice_loop = False

                #Choose to shoot yourself
                elif (choice == "2"):
                    if (len(shotgun_magazine) == 0):
                        print("You pull the trigger, and it clicks, echoing through the empty magazine.")
                        print("\nThe Dealer: The shotgun is empty. Time to put in new shells.")
                        inside_choice_loop = False
                        gun_not_empty = False
                        dealer_turn_skipped = True
                    
                    elif (shotgun_magazine[0] == "red shell"):
                        print("You choose to shoot yourself.")
                        print("You pull the trigger, and with a BANG!! Your shot blows a smoking hole through your skull.",
                              "\nYou die, but then it's not long you are brought back to life by a blurry doctor with a defibilator.",
                              "\n[Your life -"+str(shotgun_damage)+"]"
                              )
                        #Damage player
                        player_life -= shotgun_damage
                        if (player_life <= 0):
                            player_turn_skipped = True
                            dealer_turn_skipped = True

                        #Shell is removed from magazine
                        del shotgun_magazine[0]
                        inside_choice_loop = False

                    elif (shotgun_magazine[0] == "gray shell"):
                        print("You choose to shoot yourself.")
                        print("You pull the trigger, it clicks. Nothing happens.",
                              "You skip the Dealer's next turn."
                              )

                        dealer_turn_skip_gray = True
                    
                        #Shell is removed from magazine
                        del shotgun_magazine[0]
                        inside_choice_loop = False

                #Choose to use an item
                elif (choice == "3"):

                    inside_item_choice_loop = True
                    while (inside_item_choice_loop == True):
                        print("\n[Your Items:]")
            
                        if (len(shotgun_magazine) < 1):
                            print("[No Shell in Chamber. Beer and Magnifying Glass cannot be used]")
                            
                        for item_index in range(len(player_items)):
                            print("("+str(item_index)+")", player_items[item_index])

                        print("(exit) To exit item list.")

                        player_item_number_choice = input("Enter which item you use: ")

                        if (player_item_number_choice.isalpha() == True):
                            if(player_item_number_choice == "exit"):
                                inside_item_choice_loop = False
                            else:
                                print("\n[Incorrect Input]")

                        elif (player_item_number_choice.isdigit()):
                            if (int(player_item_number_choice) <= (len(player_items) - 1) and int(player_item_number_choice) >= 0):
                                player_item_choice = player_items[int(player_item_number_choice)]

                                if (player_item_choice == "Saw"):
                                    print("You pick up the saw and frantically saw it back and forth against the barrel.",
                                          "\nIt falls against the concrete floor, clattering.",
                                          "\nThe shotgun is now sawed off. A shot with a red shell deals 2 damage instead of 1 this turn.")
                                    del player_items[int(player_item_number_choice)]
                                    shotgun_damage = 2

                                elif (player_item_choice == "Cigarettes"):
                                    print("You pull out a light and smoke the cigarettes. You gain 1 life.")
                                    del player_items[int(player_item_number_choice)]
                                    player_life += 1

                                elif (player_item_choice == "Beer" and len(shotgun_magazine) > 0):
                                    print("You crack open a beer and chug it down. Then you cock the shotgun, ejecting the shell from the chamber."
                                          "\nThe shell ejected was a",shotgun_magazine[0]+".")
                                    del player_items[int(player_item_number_choice)]
                                    #Shell is removed from magazine
                                    del shotgun_magazine[0]

                                elif (player_item_choice == "Handcuffs" and dealer_handcuffed == False):
                                    print("You hand the handcuffs to the Dealer, he puts them on his hands. Skipping his next turn.")
                                    del player_items[int(player_item_number_choice)]
                                    dealer_handcuffed = True
                                elif (player_item_choice == "Handcuffs" and dealer_handcuffed == True):
                                    print("You can't use the Handcuffs, the dealer is already handcuffed.")

                                elif(player_item_choice == "Magnifying glass" and len(shotgun_magazine) > 0):
                                    print("You break the magnifying glass against the table and look into the chamber of the shotgun."
                                          "\nYou see that a",shotgun_magazine[0],"is currently in the chamber.")
                                    del player_items[int(player_item_number_choice)]

                            else:
                                print("\n[There's no item with that number.]")

                        else:
                            print("\n[Incorrect Input]")



                #If input is incorrect
                else:
                    print("[Incorrect Input]")

            #Pause
            input("\nPress [Enter] to continue: ")

            print("\nYour Life:",player_life,
                  "\nThe Dealer's life:",dealer_life,)
        


#Dealer turn-------------------------------------------------------------------------------------------
            
            #Dealer's turn.
            print("\n--------------------------------------------------------------------------------------------------------",
                  "\nIt's The Dealer's turn.\n")
            if (dealer_turn_skipped == True):
                print("The Dealer's turn is skipped since the gun is empty.")
            shotgun_damage = 1
            if (player_handcuffed == True):
                print("The handcuffs fall off your hands.")
            if (dealer_handcuffed == True):
                print("The Dealer's turn is skipped since he's handcuffed.")
            player_handcuffed = False

            if (dealer_turn_skip_gray == True):
                print("You skip The Dealer's turn.")
            player_turn_skip_gray = False

            #Dealer chooses whether to shoot you or himself. Or use items.
            #Print Possible Choices
            dealer_inside_choice_loop = True
            while (dealer_inside_choice_loop == True and dealer_turn_skipped == False and dealer_handcuffed == False and dealer_turn_skip_gray == False):

                #Dealer choice decider
                if (game_number_counter == 1):
                    dealer_choice = random.randint(1,3) #doesn't choose items.
                    
                elif (game_number_counter == 2):
                    dealer_choice = random.randint(1,6) #chooses items some of time
                    
                elif (game_number_counter == 3):
                     dealer_choice = random.randint(1,20) #chooses items most of the time

                if (len(shotgun_magazine) == 1):
                    dealer_knows_chamber_shell = shotgun_magazine[0]
                    

                #Dealer Choice Decider overrides if knows chamber shell
                if (dealer_knows_chamber_shell == "red shell"):
                    dealer_choice = 1 #Shoots you
                elif (dealer_knows_chamber_shell == "gray shell"):
                    dealer_choice = 3 #Shoots himself

                #Dealer Choose to shoot the Player
                if (dealer_choice == 1 or dealer_choice == 2):
                    print("The Dealer: I choose to shoot you.")
                    if (len(shotgun_magazine) == 0):
                        print("He pulls the trigger, and it clicks, echoing through the empty magazine.")
                        print("\nThe Dealer: The shotgun is empty. Time to put in new shells.")
                        dealer_inside_choice_loop = False
                        gun_not_empty = False
                        player_turn_skipped = True
                        dealer_knows_chamber_shell = "none"

                        #Pause
                        input("\nPress [Enter] to continue: ")
                    
                    elif (shotgun_magazine[0] == "red shell"):
                        print("He pulls the trigger, and with a BANG!! 'FIRE IN THE HOLE!!!!!' His shot nails you in the chest.",
                              "\nYou die, but then it's not long you are brought back to life by a blurry doctor with a defibilator.",
                              "\n[Your life -"+str(shotgun_damage)+"]"
                              )
                        #Damage player
                        player_life -= shotgun_damage
                        if (player_life <= 0):
                            player_turn_skipped = True
                            dealer_turn_skipped = True

                        #Shell is removed from magazine
                        del shotgun_magazine[0]
                        dealer_inside_choice_loop = False
                        dealer_knows_chamber_shell = "none"

                        #Pause
                        input("\nPress [Enter] to continue: ")

                    elif (shotgun_magazine[0] == "gray shell"):
                        print("He pulls the trigger, it clicks. Nothing happens.")
                    
                        #Shell is removed from magazine
                        del shotgun_magazine[0]
                        dealer_inside_choice_loop = False
                        dealer_knows_chamber_shell = "none"

                        #Pause
                        input("\nPress [Enter] to continue: ")


                #Dealer Choose to shoot himself
                elif (dealer_choice == 3):
                    print("The Dealer: I choose to shoot myself.")
                    if (len(shotgun_magazine) == 0):
                        print("He pulls the trigger, and it clicks, echoing through the empty magazine.")
                        print("\nThe Dealer: The shotgun is empty. Time to put in new shells.")
                        dealer_inside_choice_loop = False
                        gun_not_empty = False
                        player_turn_skipped = True
                        dealer_knows_chamber_shell = "none"

                        #Pause
                        input("\nPress [Enter] to continue: ")
                    
                    elif (shotgun_magazine[0] == "red shell"):
                        print("He pulls the trigger, and with a BANG!! His shot blasts himself into the darkness.",
                              "\nThen he floats back to the table with a grin.",
                              "\n[Dealer life -"+str(shotgun_damage)+"]"
                              )
                        #Damage dealer
                        dealer_life -= shotgun_damage
                        if (dealer_life <= 0):
                            player_turn_skipped = True
                            dealer_turn_skipped = True

                        #Shell is removed from magazine
                        del shotgun_magazine[0]
                        dealer_inside_choice_loop = False
                        dealer_knows_chamber_shell = "none"

                        #Pause
                        input("\nPress [Enter] to continue: ")
                    elif (shotgun_magazine[0] == "gray shell"):
                        print("He pulls the trigger, it clicks. Nothing happens.",
                              "He skips your next turn."
                              )
                        player_turn_skip_gray = True
                    
                        #Shell is removed from magazine
                        del shotgun_magazine[0]
                        dealer_inside_choice_loop = False
                        dealer_knows_chamber_shell = "none"

                        
                        #Pause
                        input("\nPress [Enter] to continue: ")
                    
                #Dealer Choose to use an item
                elif (dealer_choice > 3 and len(dealer_items) > 0 and len(shotgun_magazine) > 0):
                    print("The Dealer: I choose to use an item.")

                    #Setup dealer item choice variable
                    dealer_item_choice = "placeholder"
                    #Dealer Item Decider
                    #Prioritizes handcuffs, magnifying glass, then saws. Lastly cigarettes if he's low
                    if (("Handcuffs" in dealer_items) and len(shotgun_magazine) > 0 and player_handcuffed == False):
                        dealer_item_choice = "Handcuffs"
                        dealer_item_number_choice = dealer_items.index(dealer_item_choice)
                        print("The Dealer stretches his hand across the table and handcuffs your hands. Skipping your next turn.")
                        del dealer_items[int(dealer_item_number_choice)]
                        player_handcuffed = True

                    elif (("Magnifying glass" in dealer_items) == True and len(shotgun_magazine) > 0 and dealer_knows_chamber_shell == "none"):
                        dealer_item_choice = "Magnifying glass"
                        dealer_item_number_choice = dealer_items.index(dealer_item_choice)
                        print("He looks into the chamber of the shotgun with a magnifying glass,"
                              "\nthen breaks it and tosses it away into the darkness.")
                        del dealer_items[dealer_item_number_choice]
                        
                        #He see that the shell currently in the chamber.
                        dealer_knows_chamber_shell = shotgun_magazine[0]

                    elif (("Saw" in dealer_items) and len(shotgun_magazine) > 0 and shotgun_damage == 1):
                        dealer_item_choice = "Saw"
                        dealer_item_number_choice = dealer_items.index(dealer_item_choice)
                        print("He picks up the saw and with a single slash.",
                              "\nThe barrel falls against the concrete floor, clattering.",
                              "\nThe shotgun is now sawed off. A shot with a red shell deals 2 damage instead of 1 this turn.")
                        del dealer_items[dealer_item_number_choice]
                        shotgun_damage = 2

                    elif (("Cigarettes" in dealer_items) == True):
                        dealer_item_choice = "Cigarettes"
                        dealer_item_number_choice = dealer_items.index(dealer_item_choice)
                        print("He pulls out a light and smokes the cigarettes. The Dealer gains 1 life.")
                        del dealer_items[dealer_item_number_choice]
                        dealer_life += 1
                        
                    elif (("Beer" in dealer_items) == True and len(shotgun_magazine) > 0):
                        dealer_item_choice = "Beer"
                        dealer_item_number_choice = dealer_items.index(dealer_item_choice)
                        print("He cracks open a beer and chugs it down. Then he cocks the shotgun, ejecting the shell from the chamber."
                              "\nThe shell ejected was a",shotgun_magazine[0]+".")
                        del dealer_items[dealer_item_number_choice]
                        #Shell is removed from magazine
                        del shotgun_magazine[0]


                    #Pause
                    input("\nPress [Enter] to continue: ")


    #Print winner

    #If player wins
    if(player_life > dealer_life):
        print("---------------------------------------------------------------------------------------------------------",
              "\nYou Win!")
        game_number_counter += 1
    
        #Pause
        input("\nPress [Enter] to continue: ")
        print("\n---------------------------------------------------------------------------------------------------------")

    #If dealer wins
    elif(dealer_life > player_life):
        print("---------------------------------------------------------------------------------------------------------"),
        print("You died.")
        print("\n---GAME OVER---")
        input("\nPress [Enter] to quit.")
        exit()


#End of game.
money_won = random.randint(1,200000)
print("\nThe Dealer pulls out and gives you a briefcase full of money, Yipee!!",
      "\nYou drive away in the back of a taxi car into the night."
      "\nYou won: $"+str(format(money_won,',.2f'))+"!!!"
      )
      
print("\nThank you for playing!!")

input("Press [Enter] to quit.")
exit()
