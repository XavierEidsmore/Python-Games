#Cyber Pirate Defender
#By Xavier Eidsmore 2/23/2024-

import random

#Add Functions to simplify coding.

#Digibucks
player_digibucks = 0

#Create Shop List
shop_item_list = ["Cyber Patch (Item: Use it to gain 50 HP)"]

#Player Attack list = d6 rolls
player_attack_list = ["Cyber Saber Slash (Roll: 3)"]

#Player Item Inventory
player_items = []

#Equipment Buffs
equipment_roll_buffs = 0
equipment_extra_rolls = 0

dialogue_start_day = ["Intro day 1",
                      "Intro day 2",
                      "Intro Day 3",
                      "Intro day 4",
                      "Intro day 5",
                      "Intro day 6",
                      "Intro day 7",
                      "Intro day 8",
                      "Intro day 9",
                      "Intro day 10",
                      "Intro day 11",
                      "Intro day 12",
                      "Intro day 13",
                      "Intro day 14",
                      "Intro day 15"]
dialogue_end_day = ["",""]

#Functions:

#Player Enters Shop Menu #Add Equipment Later #Fix how player_digibucks is local variable. And buying stuff in shop, doesn't affect your digibucks after you leave.
def player_enter_shop(temp_digibucks):

    print("You fly your cyber spaceship away from HQ, and down the southern street to a quiet side of cyberspace."
          "\nYou walk behind a skyscraper and into a Digi weapons shop."
          "\nBehind the counter an ai clerk waves at you."
          "\nAutoClerk: [Greetings "+player_name+". What would you like to purchase today?]")

    #Add Items to shop as days go on.
    if (day_number == 3):
        shop_item_list.append("Data Revolver (Static Damage: 10, DigiCost: 3)")
    if (day_number == 7):
        shop_item_list.append("Cyberwhale Barrage (Roll: 2, AoE, DigiCost: 10)")

    if (day_number == 10):
        shop_item_list.append("The PAYload (Static Damage: 99, AoE, DigiCost: 99)")
    

    #Player Choice Loop
    inside_shop_choice_loop = True
    while (inside_shop_choice_loop == True):
        #Display Items available
        print("------------------------------")
        print("\n[For Sale]")
    
        item_counter = 0
        for item in shop_item_list:
            item_counter += 1
            print("("+str(item_counter)+") DigiPrice:",(10 * (item_counter ** 2)),"\t",item,)
            
        print("(exit) to exit inventory.")
        print("\nYour Digibucks:",temp_digibucks)

        #Player chooses Item to buy. #Add option to steal for 25% chance to get caught and instant gameover.
        item_buy = input("Choose Item To Buy: ")

        if (item_buy == "exit"):
            print("You exit the shop.\n")
            inside_shop_choice_loop = False

        elif (item_buy.isdigit()):
            item_buy = int(item_buy)
            item_buy = item_buy - 1

            if (item_buy >= 0 and item_buy < len(shop_item_list)):
                if (shop_item_list[item_buy] == "Cyber Patch (Item: Use it to gain 50 HP)" and temp_digibucks >= 10):
                    print("You Buy a Cyber Patch.")
                    temp_digibucks -= 10
                    print("-10 DigiBucks")
                    player_items.append("Cyber Patch (Item: Use it to gain 50 HP)")
                    print("Your Items:",player_items)
                        
                elif (shop_item_list[item_buy] == "Data Revolver (Static Damage: 10, DigiCost: 3)"
                      and "Data Revolver (Static Damage: 10, DigiCost: 3)" not in player_attack_list
                      and temp_digibucks >= 40):
                    print("You Buy the Attack, Data Revolver.")
                    temp_digibucks -= 40
                    print("-40 DigiBucks")
                    player_attack_list.append("Data Revolver (Static Damage: 10, DigiCost: 3)")
                    print("Your Attacks:",player_attack_list)

                elif (shop_item_list[item_buy] == "Cyberwhale Barrage (Roll: 2, AoE, DigiCost: 10)"
                      and "Cyberwhale Barrage (Roll: 2, AoE, DigiCost: 10)" not in player_attack_list
                      and temp_digibucks >= 90):
                    print("You Buy the Attack, Cyberwhale Barrage.")
                    temp_digibucks -= 90
                    print("-90 DigiBucks")
                    player_attack_list.append("Cyberwhale Barrage (Roll: 2, AoE, DigiCost: 10)")
                    print("Your Attacks:",player_attack_list)

                elif (shop_item_list[item_buy] == "The PAYload (Static Damage: 99, AoE, DigiCost: 99)"
                      and "The PAYload (Static Damage: 99, AoE, DigiCost: 99)" not in player_attack_list
                      and temp_digibucks >= 160):
                    print("You Buy the Attack, the PAYload.")
                    temp_digibucks -= 160
                    print("-160 DigiBucks")
                    player_attack_list.append("The PAYload (Static Damage: 99, AoE, DigiCost: 99)")
                    print("Your Attacks:",player_attack_list)

                else:
                    print("[Item does not exist in shop,you are don't have enough Digibucks to purchase, or you already have that attack.]")

            else:
                print ("[Invalid Input.]")
        else:
            print ("[Invalid Input.]")

    return(temp_digibucks)

#Before game begins, player creates character name.
player_name = input("Enter your character's name: ")

#29 Days, interrogation on the 30th.
for day_counter in range(29):
    day_number = day_counter + 1

    print("------------------------------")
    print("DAY ["+str(day_number)+"]")
    print("------------------------------")
    #Start Day

    #Intro Dialogue
    print(dialogue_start_day[day_counter])

    #Player Enters Shop
    print("------------------------------")
    player_digibucks = player_enter_shop(player_digibucks)

    
    #Battle Start
    print("------------------------------")
    enemies_in_battle = []
    enemies_hp = []
    number_of_enemies = 0
    player_hp = 100


    #Generate Basic Enemy
    if (day_number == 1):
        enemy_number_pirate_basic = 1

    elif (day_number == 2):
        enemy_number_pirate_basic = 2

    elif (day_number < 10):
        enemy_number_pirate_basic = 3
        
    elif (day_number < 15):
        enemy_number_pirate_basic = 4
        
    elif (day_number < 20):
        enemy_number_pirate_basic = 5
        
    elif (day_number < 30):
        enemy_number_pirate_basic = 7
        
    enemy_hp_pirate_basic = 3 + day_number
    
    for enemy_counter_basic in range(enemy_number_pirate_basic):
        enemies_in_battle.append("Pirate #"+str(enemy_counter_basic + 1)) #List of enemies
        enemies_hp.append(enemy_hp_pirate_basic) #List of enemy hp corresponding with enemy, enemy 1 at index 0 has hp at index 0.

        number_of_enemies += 1 #for digibuck drops

    #Generate Pirate Captain Enemy
    if (day_number >= 5):
        enemy_number_pirate_boss = 1
        enemy_hp_pirate_boss = 30 + day_number
        for enemy_counter_boss in range(enemy_number_pirate_boss):
            enemies_in_battle.append("Pirate Captain") #List of enemies
            enemies_hp.append(enemy_hp_pirate_boss) #List of enemy hp corresponding with enemy, enemy 1 at index 0 has hp at index 0.

            number_of_enemies += 3 #for digibuck drops

    #Generate Pirate First Mate Enemy
    if (day_number >= 8):
        enemy_number_pirate_first_mate = 1
        enemy_hp_pirate_first_mate = 20 + day_number
        for enemy_counter_first_mate in range(enemy_number_pirate_first_mate):
            enemies_in_battle.append("Pirate First Mate") #List of enemies
            enemies_hp.append(enemy_hp_pirate_first_mate) #List of enemy hp corresponding with enemy, enemy 1 at index 0 has hp at index 0.

            number_of_enemies += 2 #for digibuck drops

    #Generate Pirate Parrot Enemy
    if (day_number >= 10):
        enemy_number_pirate_parrot = 1
        enemy_hp_pirate_parrot = 3 + day_number
        for enemy_counter_parrot in range(enemy_number_pirate_parrot):
            enemies_in_battle.append("Pirate Cyber Parrot") #List of enemies
            enemies_hp.append(enemy_hp_pirate_parrot) #List of enemy hp corresponding with enemy, enemy 1 at index 0 has hp at index 0.

            number_of_enemies += 5 #for digibuck drops

    while (len(enemies_in_battle) > 0):
        #Print enemies in battle and their hp.
        print("[Enemies in Battle]")
        for x in range(len(enemies_in_battle)):
            print("("+str(x + 1)+")",enemies_in_battle[x],
                    "HP:", enemies_hp[x])
        print("------------------------------")
        

        player_turn = True
        while (player_turn == True):
            print("Your HP:",player_hp)
            print("Your DigiBucks:",player_digibucks)
            print("\n[Your Actions]")
            print("(1) Attack\n(2) Item")
            player_action = input("\nChoose Action: ")

            #Player Attacks
            if (player_action == "1"):

                #Print Attack list
                for y in player_attack_list:
                    if (y == "Cyber Saber Slash (Roll: 3)"):
                        print("(1)",y)
                    elif (y == "Data Revolver (Static Damage: 10, DigiCost: 3)"):
                        print("(2)",y)
                    elif (y == "Cyberwhale Barrage (Roll: 2, AoE, DigiCost: 10)"):
                        print("(3)",y)
                    elif (y == "The PAYload (Static Damage: 99, AoE, DigiCost: 99)"):
                        print("(4)",y)

                #Choose attack
                choose_attack_loop = True
                while (choose_attack_loop == True):
                    player_attack_choice = input("\nChoose Attack: ")
                      
                    if (player_attack_choice == "1"):
                        #Cyber Saber Slash (Roll 3)
                        player_attack_name = "Cyber Saber Slash"
                        attack_rolls = 3
                        player_aoe_attack = False
                        player_static_attack = False
                        player_static_attack_damage = 0
                          
                        choose_attack_loop = False

                    elif (player_attack_choice == "2"):
                        #"Data Revolver (Static Damage: 10, DigiCost: 3)"
                        player_digibucks -= 3
                        print("-3 DigiBucks")
                        
                        player_attack_name = "Data Revolver"
                        attack_rolls = 0
                        player_aoe_attack = False
                        player_static_attack = True
                        player_static_attack_damage = 10
                          
                        choose_attack_loop = False

                    elif (player_attack_choice == "3"):
                        #Cyberwhale Barrage (Roll 2, AoE, DigiCost: 10)
                        player_digibucks -= 10
                        print("-10 DigiBucks")
                        
                        player_attack_name = "Cyberwhale Barrage"
                        attack_rolls = 2
                        player_aoe_attack = True
                        player_static_attack = False
                        player_static_attack_damage = 0
                          
                        choose_attack_loop = False

                    elif (player_attack_choice == "4" and player_digibucks >= 99):
                        #The PAYload (Static Damage: 99, AoE, DigiCost: 99)
                        player_digibucks -= 99
                        print("-99 DigiBucks")

                        print("You drop the Bomb.")
                        player_attack_name = "The PAYload"
                        attack_rolls = 0
                        player_aoe_attack = True
                        player_static_attack = True
                        player_static_attack_damage = 99

                          
                        choose_attack_loop = False
                          
                    else:
                        print("[Invalid Input or Lacking DigiBucks for attack cost.]")

            #Player uses Items              
            if (player_action == "2"):
                item_counter = 0
                for current_item in player_items:
                    item_counter += 1
                    print("("+str(item_counter)+")",current_item)

                print("(exit) to exit inventory.")

                inside_item_choice_loop = True
                while (inside_item_choice_loop == True):
                    player_item_choice = input("\nChoose Item: ")

                    if (player_item_choice == "exit"):
                        print("You exit your inventory.\n")
                        inside_item_choice_loop = False

                    elif (player_item_choice.isdigit()):
                        player_item_choice = int(player_item_choice)
                        player_item_choice = player_item_choice - 1

                        if (player_item_choice >= 0 and player_item_choice < len(player_items)):
                            if (player_items[player_item_choice] == "Cyber Patch (Item: Use it to gain 50 HP)"):
                                print("You use the Cyber Patch, you gain 50 HP.")
                                player_hp += 50
                                print("Your HP:",player_hp)
                                del player_items[player_item_choice]

                            else:
                                print("[Item does not exist in inventory.]")

                        else:
                            print ("[Invalid Input.]")
                    else:
                        print ("[Invalid Input.]")
                
                
            #Attack Damage Calulcations
            if (player_action == "1"):
                      
                if (player_aoe_attack == True):
                    #AoE enemy select
                    print("\nYou use",player_attack_name,"on every enemy.")

                else:
                    #Single Enemy Select
                    choose_enemy_to_attack_loop = True
                    while (choose_enemy_to_attack_loop == True):
                        enemy_select = input("\nChoose Which Enemy To Attack: ")

                        if (enemy_select.isdigit() == True):
                            enemy_select = int(enemy_select)
                            if (enemy_select <= len(enemies_in_battle) and enemy_select > 0):
                                choose_enemy_to_attack_loop = False
                            else:
                                print("[Invalid Input]")
                                  
                        else:
                            print("[Invalid Input]")

                    enemy_select = enemy_select - 1
                    print("\nYou use",player_attack_name,"on",enemies_in_battle[enemy_select])

                      

                print("------------------------------")

                if (player_static_attack == True):
                    damage = player_static_attack_damage

                else:
                    #Roll d6s
                    player_dice_roll_number = attack_rolls + equipment_extra_rolls
                    dice_roll_multiplier = 1 + equipment_roll_buffs
                    print("Rolling",player_dice_roll_number,"d6s...\n")
                    damage = 0
                    total_roll = 0
                    for z in range(player_dice_roll_number):
                        dice_roll = random.randint(1,6)
                              
                        if (dice_roll == 6):
                                  print("You rolled:",dice_roll,"CRITICAL HIT (damage doubled)")
                                  dice_roll_multiplier = dice_roll_multiplier * 2
                        elif (dice_roll == 1):
                                  print("You rolled:",dice_roll,"CRITICAL FAILURE (damage halved)")
                                  dice_roll_multiplier = dice_roll_multiplier / 2
                        else:
                                  print("You rolled:",dice_roll)

                        total_roll += dice_roll

                        damage = total_roll * dice_roll_multiplier


                #Damage Enemy
                print("") #Spacer
                if (player_aoe_attack == True):
                    #Damage all hp in lists
                    for each_enemy_hp_index in range(len(enemies_hp)):
                        enemies_hp[each_enemy_hp_index] -= damage
                        print("You deal",damage,"damage to", enemies_in_battle[each_enemy_hp_index])

                    static_enemies_hp_len = len(enemies_hp)

                    #If they die
                    print("") #Spacer
                    for each_enemy_hp_index in range(static_enemies_hp_len):
                        death_counter = (static_enemies_hp_len - 1) - each_enemy_hp_index
                        if (enemies_hp[death_counter] <= 0):
                            print(enemies_in_battle[death_counter],"digital avatar defeated.")
                            del enemies_in_battle[death_counter]
                            del enemies_hp[death_counter]

                else:
                    #Damage single enemy
                    enemies_hp[enemy_select] -= damage
                    print("\nYou deal",damage,"damage to", enemies_in_battle[enemy_select],"\n")

                    #If they die
                    if (enemies_hp[enemy_select] <= 0):
                        print(enemies_in_battle[enemy_select],"digital avatar defeated.")
                        del enemies_in_battle[enemy_select]
                        del enemies_hp[enemy_select]
                

                player_turn = False
                print("------------------------------")

        #Enemy Turn
        print("It's the Pirates' Turn")
        for current_damager in enemies_in_battle:
            damage_to_player = 0
            
            #Basic Pirate Attacks
            if (current_damager.find("Pirate #") >= 0):
                print(current_damager,"attacks you.")
                print(current_damager+": Argh!")

                #rolls 1 d6 for damage
                print("They roll 1 d6...\n")
                enemy_roll = random.randint(1,6)
                print("They rolled:",enemy_roll)
                print("You take",enemy_roll,"damage.")
                player_hp -= enemy_roll

                #Damage Player
                if (player_hp <= 0):
                    print("---YOU DIED---")
                    input("Press [Enter] to close the game.")
                    exit()

            #Pirate Parrot Attacks
            elif (current_damager.find("Parrot") >= 0):
                print("Pirate Cyber Parrot: SQUAWK!!!")

            #Pirate First Mate Attacks  
            elif (current_damager.find("First Mate") >= 0):
                print(current_damager,"attacks you.")
                print("Pirate First Mate: YAHHH!!!")
                
                #rolls 2 d6 for damage
                print("They roll 2 d6s...\n")
                for placeholder in range(2):
                    enemy_roll = random.randint(1,6)
                    print("They rolled:",enemy_roll)
                    damage_to_player += enemy_roll

                #Damage player
                print("You take",damage_to_player,"damage.")
                player_hp -= damage_to_player

                if (player_hp <= 0):
                    print("---YOU DIED---")
                    input("Press [Enter] to close the game.")
                    exit()    

            #Pirate Captain Attacks  
            elif (current_damager.find("Captain") >= 0):
                print(current_damager,"attacks you.")
                print("Pirate Captain: YARRGGHH!!")
                
                #rolls 3 d6 for damage
                print("They roll 3 d6s...\n")
                for placeholder in range(3):
                    enemy_roll = random.randint(1,6)
                    print("They rolled:",enemy_roll)
                    damage_to_player += enemy_roll

                #Damage player
                print("You take",damage_to_player,"damage.")
                player_hp -= damage_to_player

                if (player_hp <= 0):
                    print("---YOU DIED---")
                    input("Press [Enter] to close the game.")
                    exit()

            #Pause
            input("Press [Enter] to continue: ")
            print("------------------------------")
                          
                                

    print("All pirates defeated. End of battle.")

    #Pause
    input("Press [Enter] to continue: ")

    print("------------------------------")

    #print drops and digibucks.
    digibucks_loot = (number_of_enemies * day_number) + random.randint(0,100)
    print("The pirates dropped",digibucks_loot,"DigiBucks!"
          "\nBut this is the company's loot."
          "\nPE3P swoops by and sucks up the loot with it's tractor beam."
          "\nYou recieve your daily wage of 50 DigiBucks.")
    player_digibucks += 50
    print("Your current balance:", player_digibucks)
