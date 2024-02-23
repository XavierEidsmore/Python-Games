#My Dungeon Test (Version 1.4)
#Xavier Eidsmore 2/13/2024


#Keyword for exiting the game. exit()

#import time module
import time

#Create player inventory with starting item, Sword.
player_inventory = ["sword"]

#Create choice variable.
choice = "placeholder"

#Create important other variables.
valid_animal_choice = False
inside_choice_loop = False

#Create Flags
wait_out_saw_hall = False
player_see_fish = False
rizzed_mimic = False
player_is_bald = False

#Code to add a Torch/item to player inventory.
#player_inventory = player_inventory + ["torch"]


#Beginning of adventure:


#Print game title:
print("~~~My Dungeon Test~~~")
print("By Xavier Eidsmore")


#Enter intro question scene:
print("\nNarrator:","Before we begin, I'd like you to answer a few questions first.\n")

pet_name = input("Enter your pet's name: ")
while (valid_animal_choice == False):
    fav_animal = input("Enter your favorite animal: ")
    if (fav_animal == "deer"):
        print("Please type your favorite animal differently.")
    elif (fav_animal == "boar"):
        print("Please type your favorite animal differently.")
    else:
        valid_animal_choice = True
print("Enter your credit card number: ")
time.sleep(2)
print("Just kidding!")
fav_food = input("Enter your favorite food: ")
worst_fear = input("Enter your worst fear: ")
fav_number = input("Enter your favorite number: ")
scariest_number = input("Enter your scariest number: ")
fav_color = input("Enter your favorite color: ")
player_name = input("Enter your character's name: ")
love_name = input("Enter your character's lover's name: ")
input("Are you happy?: ")

#Tutorial: Narrator gives tutorial on how to input choices.
print("\n~~~~~~~~~~~~~~~~~Tutorial~~~~~~~~~~~~~~~~~",
      "\nNarrator:","I will tell you a quick tutorial for how to enter choices.",
      "\nChoices will appear like the following:",
      "\n(fight)\n(run)\n(hide)\n",
      "\nThen you will be given the prompt, Enter your choice:",
      "\nType in exactly what you see in the parenthesis to choose that choice. Like this.\n",
      "\nEnter your choice: run",
      "\nYou choose to run.\n",
      "\nThen press enter to submit your decision and proceed.\n",
      "\nYou may also run into:",
      "\n(1) Action 1. \n(2) Action 2. \n(3) Action 3.",
      "\nEnter your choice: 1",
      "\nYou choose to do Action 1.\n"
      "\nRemember to type in exactly what you see in the parenthesis.",
      "\nOr you will be asked to redo your choice.",
      "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
      )

#Secret Ending.
easter_egg = input("\nPress [Enter] to continue: ")
if (easter_egg == "no"):
    print("Narrator:","Wow, you are so funny. Here Mr. Funny Guy, you win the game.")
    input("Press [Enter] to close the game:")
    exit()

print("\nRemember, there are no wrong choices. Feel free to experiment.\n")

#Enter Beginning Scene
print("\n~~~The Story Begins~~~")
print("\nNarrator:","You are", player_name + ". You wake up in the middle of a forest.","The surrounding trees look down on you.",
      "\nThe weather a cloudy, dreary gray. The cold seeps through your clothes. And the muddy ground clinging down on your boots.",
      "\nYou look down at the dark staircase that leads deep into the ground ahead of you.",
      "\nYou remember why you're here.",
      "\nYou heard a rumor that at the bottom of this treacherous dungeon, lies a magical artifact.",
      "\nIt has the power to bring the dead back to life.",
      "\nYou begin to remember your beloved", love_name + ".\nWhose hair is a lovely shade of", fav_color + ".",
      "\nEverything has felt hollow ever since they were gone. And you have been hollow as well.",
      "\nBut despite the terrors below, you are determined to get them back no matter the cost."
      )


#Choice enter the dungeon, yes or no.
print("\nWill you enter the dungeon?")

inside_choice_loop = True
while (inside_choice_loop == True):
    print("\n(yes) or (no)")
    choice = input("\nEnter your choice: ")
    
    if (choice == "yes"):
        print("Narrator:","You descend into the dungeon. There's no turning back now.")
        inside_choice_loop = False
    elif (choice == "no"):
        print("Narrator:","What... After all the effort I put into my descriptive story telling to paint the scene, you just. Don't?",
              "\nOh, you must have made a typo! Haha, that's it, that's what happened. I'll give you a second chance to fix it.")
        inside_choice_loop = False
    else:
        print("[Invalid Input, Please Try Again]")


#Narrator gives you a second chance if you say no.
if (choice == "no"):
    inside_choice_loop = True
    while (inside_choice_loop == True):
        print("\n(yes) or (no)")
        choice = input("\nEnter your choice: ")
        
        if (choice == "yes"):
            print("Narrator:","After doubting your decision, you come to a concrete conclusion.",
                  "\nYou press on and descend into the dungeon.",
                  "\nThere's no turning back now.")
            inside_choice_loop = False
        elif (choice == "no"):
            inside_choice_loop = False
            print("Narrator:","*sigh* \nYou are a rational and logical individual and don't believe in 'hocus pocus magic'.",
                  "\n(Or maybe you are just trying to annoy me...)",
                  "\nAnd that it's not worth possibly losing your life in the dungeon.",
                  "\nSo you decide to return home and do something more important with your miserable life. Like sleeping.")
            print("\n~~~~~~~~~~~~~~~~~The End~~~~~~~~~~~~~~~~~")
            input("Enter anything to close the game: ")
            exit()
        else:
            print("[Invalid Input, Please Try Again]")

input("\nPress [Enter] to continue: ")

#Player enters the dungeon by descending down the staircase.
print("\nNarrator:","You descend down the steps into the belly of the dungeon.",
      "\nIt reeks of mildew, as the rain from the surface leaks down here through the walls.",
      "\nAs you proceed deeper and deeper into the darkness. It becomes so dark your hands disappear.",
      "\nYou run your fingers against the wall to navigate. But then you feel you've reached the bottom of the stairs.",
      "\nThe room opens up and you wander aimlessly.",
      "\nYou trip over a brick protruding from the floor and stumble around trying to find the wall again.",
      "\nFear surges through your body as you begin to regret ever coming here unpreppared.",
      "\nYou feel death approaching.",
      "\nBut then you feel your foot kicked something, you hear it make a wooden clatter on the floor.",
      "\nYou feel around the floor for the object and grip it.",
      "\nTo your rescue, it is a torch.",
      "\nYou pull out your flint and steel, and carefully strike it.",
      "\nThe embers are dim at first, but then it grows and grows.",
      "\nIlluminating the whole room in a warm amber light."
      )

#Player gets torch.
player_inventory = player_inventory + ["torch"]

print("[Torch added to your inventory.]")
print("\n[Opening your inventory will show up as an choice whenever items can be used.]",
      "\n[To use an item, you must first open your inventory, then Enter what item you use:]",
      "\n[Then, when you use an item, it closes the inventory. Feel free to experiment, you don't lose items by using them.]",
      "\n[You are sent back to choosing a choice, which you can open the inventory again.]",
      "\nWhat do you do now?"
      )

inside_choice_loop = True
while (inside_choice_loop == True):
    print("\n(open inventory)\n(proceed)")
    choice = input("\nEnter your choice: ")
    
    if (choice == "open inventory"):
        #Open and display player inventory.
        print("[Your Inventory]")
        for items in player_inventory:
            print("-",items)
        choice = input("Enter what [item] you use: ")
        if (choice == "sword"):
            print("Narrator:","You swing around your sword, you feel really cool. \nAlmost enough to not be depressed.")
        elif (choice == "torch"):
            print("Narrator:","You look around the room, it is built with old mossy stone bricks.")
        else:
            print("[Invalid Item]")
    elif (choice == "proceed"):
        print("Narrator:","With newfound hope. You proceed deeper into the dungeon through the hallway.")
        inside_choice_loop = False
    else:
        print("[Invalid Input, Please Try Again]")

    #Pause
input("\nPress [Enter] to continue: ")

#Player enters hall of swinging saws.
print("\nNarrator:","You walk down the hallway with guiding torch in hand. And your blade at the ready.",
      "\nThen suddenly a giant bladed saw swings across the hallway, a breath away from cutting you.",
      "\nIt's not just one saw, but many, swinging side to side down the corridor.",
      "What will you do?"
      )

#Player chooses action.
inside_choice_loop = True
while (inside_choice_loop == True):
    print("\n(1) Acrobatically weave and dodge past the saws. \n(2) Look for another way past it. \n(3) Wait it out.")
    choice = input("\nEnter your choice: ")
    
    if (choice == "1"):
        print("Narrator:", "You expertly weave past the saws with expert timing and precision."
              "\nLike the doctor of swinging saw hallways you are. You dance through them with cartwheels and pirroutes.",
              "\nEnding your dance at the end of the hall with a backflip, then a kneel.",
              "\nIf there was an audience, the applaudes would be roaring.",
              )
        inside_choice_loop = False
    elif (choice == "2"):
        print("Narrator:","You think it's best to look for another way past this obviously hazardous hallway.",
              "\nWhile scouting down another corridor, you stumble upon a switch, labelled... On and Off.",
              "\nHow convinient. The engineers of this dungeon at least had a killswitch while working on it.",
              "\nImagine if they didn't.",
              "\nYou flick the switch off and the saws grind to a halt.",
              "\nWithout a care in the world, you joyfully walk to the otherside of the hallway."
              )
        inside_choice_loop = False
    elif (choice == "3"):
        print("Narrator:","You decide to, wait it out... Yeah sure, we can roll with that.",
              "\nYou wait, and wait, and wait.",
              "\nYou wait for so long that time itself becomes meaningless.",
              "\nYou sleep and wake up in the same dungeon, the cycle turns without end.",
              "\nThe blur is nauseating.",
              "\nYou start talking to yourself, like you're crazy.",
              "\nWell, you are crazy for doing this.",
              "\nThis is your existence now.",
              "\nI hope you're happy.",
              "\nIt's not going to stop anytime soon.",
              "\nI'm going to get a cup of coffee.",
              "\nAlright I'm back, well would you look at that.",
              "\nYou suddenly notice that the saws have stopped swinging, maybe a couple of minutes ago while you were dazed out.",
              "\nYou make your way to the end of the hallway.",
              "\nYou even take your time while doing so.",
              "\nNot like anyone else has a life.",
              "\nAnd what about your lover?",
              "\nYou're making them wait too, does their time not matter?",
              "\nNevermind, you've made it past the hallway, and that's all that matters."
              )
        inside_choice_loop = False
        wait_out_saw_hall = True
    else:
        print("[Invalid Input, Please Try Again]")

    #Pause
input("\nPress [Enter] to continue: ")

#Player enters kitchen of barrels.
print("\nNarrator:","You walk into the next couple of rooms.",
      "\nThey are all pretty barren. The only residents are some tiny spiders.",
      "\nYou walk into the kitchen, full of dusty cupboards and barrels, way too many barrels.",
      "\nThere's something suspicious about them.",
      "\nWill you break open the barrels to see what's inside them?",
      )

#Player chooses whether to break barrels.
inside_choice_loop = True
while (inside_choice_loop == True):
    print("\n(yes) or (no)")
    choice = input("\nEnter your choice: ")
    
    if (choice == "yes"):
        print("Narrator:","You break open a barrel and find a bomb!",
              "\nNo need to worry it only goes off if you light the fuse with your torch.",
              "\nIt looks like one of those cartoony bombs. You know, black, heavy, made of iron, with a cord fuse ontop.",
              "\nEven I don't know why they had a bomb laying down in the kitchen. That's a different kind of way to make spicy food.",
              "\n'This food is the bomb', hahaha.",
              "\nYou put the bomb into your inventory as it seems handy for later."
              )
        print("[Bomb added to your inventory.]")
        player_inventory = player_inventory + ["bomb"]
        inside_choice_loop = False
    elif (choice == "no"):
        print("Narrator:","You feel it might be a trap, or that you fear",worst_fear,"might be inside a barrel.",
              "\nSo with your better judgement, you don't crack open any barrels.",
              "\nBut on your way out as you leave the kitchen, you spot a fish bowl that you didn't see before.",
              "\nInside it lurks a green fish with",scariest_number,"beady black eyes staring back at you.",
              "\nIt sends shivers up your back as you hastily leave. You wish you didn't see that."
              )
        player_see_fish = True
        inside_choice_loop = False
    else:
        print("[Invalid Input, Please Try Again]")

print("What do you do now?")

inside_choice_loop = True
while (inside_choice_loop == True):
    print("\n(open inventory) \n(proceed)")
    choice = input("\nEnter your choice: ")
    
    if (choice == "open inventory"):
        #Open and display player inventory.
        print("[Your Inventory]")
        for items in player_inventory:
            print("-",items)
        choice = input("Enter what [item] you use: ")
        if (choice == "sword"):
            if (player_see_fish == True):
                print("Narrator:","You kill the fish in the fish bowl with your sword, maybe you were the monster all along.",
                      "\nAlmost monsterous enough to not be depressed."
                      )
                player_see_fish = False
            else:
                print("Narrator:","You check the cupboards for some vegetables to chop up, but they are all rotten.",
                  "\nYou check if they might have your any",fav_food,"around, but it is nowhere to be seen.",
                  "\nSo you just swing around your sword, slicing apart your depression.",
                  "\nUnfortunately, depression can't be cut."
                  )
        elif (choice == "torch"):
                print("Narrator:","You think of setting the room on fire. But it would kill you too.",
                "\nWow."
                "\nThat's the only thing stopping you.")
        elif (choice == "bomb"):
                print("Narrator:","You think of setting it off, but it would plummet the second hand market value, so you don't.")
        else:
                print("[Invalid Item]")
    elif (choice == "proceed"):
        print("Narrator:","You exit the kitchen.")
        inside_choice_loop = False
    else:
        print("[Invalid Input, Please Try Again]")

    #Pause
input("\nPress [Enter] to continue: ")

#Player enters room with dead end cracked wall
print("\nNarrator:","And after exiting the kitchen, you run into a dead end.",
      "\nBut as you wave your torch around, you notice there are several deep cracks scarring it.",
      )
print("What do you do now?")

if(wait_out_saw_hall == True):
    print("And no, you are not going to wait this one out.")


#Player chooses action.
inside_choice_loop = True
while (inside_choice_loop == True):
    print("\n(open inventory) \n(1) Headbutt it. \n(2) Talk to it about your problems. \n(3) Look through the cracks, to hopefully see the other side.")
    if(wait_out_saw_hall == True):
        print("(4) Wait it out.")
    choice = input("\nEnter your choice: ")

    if (choice == "open inventory"):
        #Open and display player inventory.
        print("[Your Inventory]")
        for items in player_inventory:
            print("-",items)
        choice = input("Enter what [item] you use: ")
        if (choice == "sword"):
            print("Narrator:","You unsheathe your sword, about to show this feeble wall your true power.",
                  "\nWith a tornado of swirling slashes, exectuted artfully in the blink of an eye.",
                  "\nIs what I would say.",
                  "\nBut your depression holds back your abilities.",
                  "\nYou remember you are no anime protagonist. Just a shell of your former self.",
                  "\nWith no motivation or real training.",
                  "\nYour sword bounces out of your hands at the first swing against the wall.",
                  "\nYou pick it back up. Then sheathe it.",
                  "\nIt would have been so cool, if you weren't depressed."
                  )
        elif (choice == "torch"):
            print("Narrator:","You throw your torch at the wall, it bounces off then smacks you in the face.",
                  "\nYou panic as you try to put it out as it sets your hair on fire.",
                  "\nYou manage to put it out, but the damage has been done.",
                  "\nYou pull out your sword and cut off the little tuffs of hair that remain.",
                  "\nYou are now bald.",
                  "\n",player_name,"the Bald."
                  )
            player_is_bald = True
        elif (choice == "bomb"):
            print("Narrator:","You set the bomb alight with your torch.",
                  "\nIt sizzles and fizzes as you set it at the foot of the wall.",
                  "\nThen you run and hide around the corner as it detonates.",
                  "\nYou pray it doesn't bring the entire dungeon down.",
                  "\nAnd thankfully it doesn't.",
                  "\nIn fact, despite it's size, the bomb did nearly no damage.",
                  "\nBut just enough that you are able to pry the bricks away and climb through the small hole to the other side."
                  )
            inside_choice_loop = False
        else:
            print("[Invalid Item]")
    elif (choice == "1"):
        print("Narrator:", "You take several steps back, springing the power into your legs."
              "\nYou then thrust forth with an explosion of your strength. Hurtling your head into the wall.",
              "\nOh god, you're really doing this.",
              "\nYour head crashes into the wall, you feel your skull fracture down the middle.",
              "\nBut to everyone's surprise, you are still alive, even after doing the stupidest thing imaginable.",
              "\nYou think it was all for nothing until you see the crack on the wall has grown to the corners.",
              "\nThen not a second later, the wall crumbles apart, clouding the room in dust.",
              "\nYou defeated this obstacle, with your sheer stupidity.",
              "\nIt's almost admirable."
              )
        inside_choice_loop = False
    elif (choice == "2"):
        print("Narrator:","You, talk to the wall about your problems.",
              "\nAfter all it is as broken as you are.",
              "\nLike a good therapist it listens.",
              "\nAnd like a bad therapist, it's like you are talking to a wall.",
              "\nIt crumbles apart by how sad it becomes.",
              "\nThis is the true power of your depression.",
              "\nA hole opens up in the wall, and you climb through."
              )
        inside_choice_loop = False
    elif (choice == "3"):
        print("Narrator:","You look through the cracks of the wall.",
              "\nWhat you see makes you stand on end.",
              "\nIt's so exciting you start giggling and prancing.",
              "\nYou finally start to make out what you see on the other end.",
              "\nIt looks just like all the other rooms."
              )
    elif (choice == "4"):
        print("Narrator:","You decide to, wait it out... AGAIN!?!?!?",
              "\nI, I just can't.",
              "\nYou must be doing this on purpose to mess with me.",
              "\n*annoyed sigh*.",
              "\nJust like earlier.",
              "\nTime becomes meaningless.",
              "\nYour existence becomes meaningless.",
              "\nIt all becomes a meaningless nauseating blur.",
              "\nThis is your existence now.",
              "\nI hope you're happy.",
              "\nThe wall crumbles under the length of time.",
              "\nThe universe begins to unravel.",
              "\nYour torch goes dark.",
              "\nYou begin to feel yourself floating before you wake up.",
              "\nYou wasted everyone's time.",
              "\nBut luckily it was all a dream.",
              "\nMaybe this entire game is.",
              "\nWhatever, you notice a perfectly cut hole in the cracked wall.",
              "\nAnd you climb through.",
              "\nYou've made it past the wall, and that's all that matters.",
              "\nYou light your torch again with your flint and steel."
              )
        inside_choice_loop = False
    else:
        print("[Invalid Input, Please Try Again]")

    #Pause
input("\nPress [Enter] to continue: ")

#Player makes it through to other side of cracked wall.
print("Narrator:","Now that you've made it through the wall.",
      "\nYou walk down the hallway and see a treasure chest on the floor.",
      "\nDo you open the chest?"
      )

#Player chooses yes or no.
inside_choice_loop = True
while (inside_choice_loop == True):
    print("\n(yes) or (no)")
    choice = input("\nEnter your choice: ")
    
    if (choice == "yes"):
        print("Narrator:","You open the chest. And it loudly creaks.",
              "\nYou see an amber glint.",
              "\nYou reach for it and pick it up.",
              "\nIt's exterior is smooth and round.",
              "\nAlso slightly transparent.",
              )
        print("[Truth Seeing Stone added to your inventory.]")
        player_inventory = player_inventory + ["truth seeing stone"]
        inside_choice_loop = False
    elif (choice == "no"):
        print("Narrator:","To be cautious of obvious traps. You walk past it.",
              "\nBut as you do, the chest opens wide.",
              "\nRevealing",scariest_number,"jaws of teeth and slimy tongues.",
              "\nYou flee as it hops towards you, but then morphs into",worst_fear,"then traps you in a corner."
              "\nWhat do you do?"
              )
        inside_choice_loop = False
    else:
        print("[Invalid Input, Please Try Again]")

#If Choice no, mimic encounter.
if (choice == "no"):

    inside_choice_loop = True
    while (inside_choice_loop == True):
        print("\n(open inventory)\n(fists)\n(biceps)\n(flirt)\n(befriend)")
        if(wait_out_saw_hall == True):
            print("(wait)") 
        choice = input("\nEnter your choice: ")
    
        if (choice == "open inventory"):
            #Open and display player inventory.
            print("[Your Inventory]")
            for items in player_inventory:
               print("-",items)
            choice = input("Enter what [item] you use:")
            if (choice == "sword"):
                print("Narrator:","Your body freezes up, yet you muster up all your courage.",
                      "\nUnsheathe your blade and stab it through it's heart.",
                      "\nThe mimic disintegrates into dust.",
                      "\nWhat a lucky strike.",
                      "\nYou feel you've overcome your fear of",worst_fear,"and you feel.",
                      "\nAlmost strong enough to not be depressed."
                      )
                inside_choice_loop = False
            elif (choice == "torch"):
                 print("Narrator:","You set the mimic on fire.",
                       "\nYou hope it's enough to burn away your worst fear.",
                       "\nBut it just cackles, and looks even scarier.",
                       "\nYou squeak."
                       )
            elif (choice == "bomb"):
                print("Narrator:","You light your bomb and blindly throw it at the mimic like it's a grenade."
                      "\n'TALLY HO LADS!!!!', you shout, like a goofball.\n",
                      worst_fear,"never stood a chance against the power of explosives.",
                      "\nAnd your recklessness...",
                      "\nThe mimic is defeated and you reign victorious over conquering your worst fear.",
                      "\nBut you notice your wallet is missing, and then you see it has become a charred black streak on the floor.",
                      "\nIf the bank finds out about this, they would certaintly deduct your credit score by 300."
                      )
                inside_choice_loop = False
            else:
                print("[Invalid Item]")
        elif (choice == "fists"):
            print("Narrator:","You swing your fists."
                  "\nYou land your strongest blow using what little you know about boxing.\n",
                  worst_fear,"seems completely unphased, not even moving an inch.",
                  "\nIt laughs at your feeble blows."
                  )
        elif (choice == "biceps"):
            print("Narrator:","You flex your biceps, hoping to win in the looks department.",
                  "\nBut",worst_fear,"flexes even bigger biceps back with a smirk.",
                  "\nOh~ but that only drives you to flex even harder back.",
                  "\nThe mimic looks at you with disdain, it flexes.",
                  "\nYou flex.",
                  "\nIt flexes back.",
                  "\nTurn after turn, exchanging flexes one flex at a time.",
                  "\nWith increasingly larger and larger biceps.",
                  "\nWith more and more strength. Challenging both your bodies to their limits.",
                  "\nThe mimic was a tough battle, but you flexed the largest strongest biceps mankind and mimickind has ever seen.",
                  "\nWith a final move, the mimic flexes it's biceps so hard the walls begin to crack, and collapses in on it.",
                  "\nBurying it in the rubble.",
                  "\nThroughout dungeon and gym, you alone are the victorious one."
                  )
            inside_choice_loop = False
        elif (choice == "flirt"):
            print("Narrator:","You, umm. What?",
                  "\nBut it's your worst fear?",
                  "\nAnd what about",love_name+"?"
                  "\nAren't you cheating on them?"
                  "\nFine.",
                  "\nYou admire the fine curvature of",worst_fear+"'s body.",
                  "\nWhat a hunk~",
                  "\nAnd you let it know directly to the mimic's face.",
                  "\nThe mimic is confused why you are complimenting it but you lean in close to it's face."
                  "\nStaring deeply into it's horrific eyes."
                  )
            mimic_flirt_message = input("Enter what you say to the mimic: ")
            print("\nYou carress the mimic's face and say,",
                   mimic_flirt_message+". You pull the mimic's body close to yours.",
                  "\nFeeling it's, indescribable skin against yours.",
                  "\nAnd your hot breath blowing on each other.",
                  "\nMixing into an indescribable scent.",
                  "\nThe mimic blushes and is flustered, it stammers in confusion.",
                  "\nBut you are the one in control now. Your worst fear is not so scary since you will be the one kissing it.",
                  "\nYou caress the mimics face as you lean in towards it's ear.",
                  "\nYou whisper, 'I want you.' and the mimic lights up into a bright red."
                  "\nYou say this will all have to wait later, kissing the mimic on the cheek as you gently push it away.",
                  "\nThe mimic is completely stunned, still blushing.",
                  "\nYou seductively wave goodbye, and the mimic waves back.",
                  "\nYou save this occasion for later.",
                  "\nI CAN'T BELIEVE YOU MADE ME DESCRIBE THAT, WHAT A HORRIBLE SCRIPT I HAVE TO READ.",
                  "\nWhatever, WHATEVER.",
                  "\nThat's one way of conquering your worst fear.",
                  "\nAnd the mimic is done, we can move on now.",
                  )
            rizzed_mimic = True
            inside_choice_loop = False
        elif (choice == "befriend"):
             print("Narrator:","You two talk it out."
                   "\nBut the mimic doesn't speak your language.",
                   "\nNot a single word makes it through to it.",
                   "\nThe language barrier is stronger than the power of your friendship."
                   )
        elif (choice == "wait"):
            print("Narrator:","No. Just no, no more.")
        else:
            print("[Invalid Input, Please Try Again]")

else:
    print("\nNarrator:","You walk down the rest of the hallway.")

    #Pause
input("\nPress [Enter] to continue: ")

#Player enters room with 3 statues.
print("\nNarrator:","Then you enter a small room with 3 stone statues.",
      "\nThere is a deer, a boar, and a",fav_animal+".",
      "\nEach of them have",fav_number,"written with red paint on their foreheads.",
      "\nYou notice scratch marks on the floor, like the statues can be moved."
      "\nWhich statue do you move?"
      )

inside_choice_loop = True
while (inside_choice_loop == True):
    print("\n(open inventory) \n(deer) \n("+fav_animal+") \n(boar)")
    choice = input("\nEnter your choice: ")
    
    if (choice == "open inventory"):
        #Open and display player inventory.
        print("[Your Inventory]")
        for items in player_inventory:
            print("-",items)
        choice = input("Enter what [item] you use:")
        if (choice == "sword"):
            print("Narrator:","The gaze of the statues stop you.")
        elif (choice == "torch"):
            print("Narrator:","The gaze of the statues stop you.")
        elif (choice == "bomb"):
            print("Narrator:","The gaze of the statues stop you.")
        elif (choice == "truth seeing stone"):
            print("Truth Seeing Stone:","'Hey, *coughs*, it's the *heavy coughing*, one.'",
                  "\nNarrator:","Umm, which one?",
                  "\nTruth Seeing Stone:","'The *coughs and weezes* right one.'",
                  "\nNarrator:","Which RIGHT one!? I... I mean we, don't have all day.",
                  "\nTruth Seeing Stone:","'The best one.'",
                  "\nNarrator:","*sigh* I think we got enough information, it's your favorite one."
                  )
        else:
            print("[Invalid Item]")
    elif (choice == "deer"):
        print("Narrator:","You go with team deer and push the statue. Nothing happens.")
    elif (choice == "boar"):
        print("Narrator:","You go with team boar and push the statue. Nothing happens.")
    elif (choice == fav_animal):
        print("Narrator:","You have faith with your favorite animal and push the statue.",
              "\nIt slides out of the way revealing a secret staricase in the wall that descends past what you can see.",
              "\nYou feel a sense of finality."
              )
        inside_choice_loop = False
    else:
        print("[Invalid Input, Please Try Again]")

    #Pause
input("\nPress [Enter] to continue: ")

#Player enters final staircase
print("\nNarrator:","As you descend down the staircase, you feel almost nostalgic."
      "\nThese stairs remind you of the stairs at the start of your adventure.",
      "\nYou descend for several more minutes under the torch light.",
      "\nYou can't help but think of",love_name,"and all those warm memories.",
      "\nYou miss them more than anything else.",
      "\nThere's no way to go but forward now."
      )

#Player Proceed Choice
inside_choice_loop = True
while (inside_choice_loop == True):
    print("\n(proceed)")
    choice = input("\nEnter your choice: ")
    
    if (choice == "proceed"):
        print("You descend the rest of the staircase and enter the final room.")
        inside_choice_loop = False
    else:
        print("[Invalid Input, Please Try Again]")

    #Pause
input("\nPress [Enter] to continue: ")

#Player enter final room
print("Narrator:","At long last, your journey is coming to an end.",
      "\nThis deepest room looks like a tomb.",
      "\nAnd atop the coffin is a magical glowing",fav_color,"orb.",
      "\nYou walk closer to the orb and hold it in your hands.",
      "\nYou feel it's power emanating through every hair and vein, on and beneath your skin.",
      "\nThen you see a little snake swirling inside with blue and golden scales.",
      "\nIt's a familiar voice, like the one guiding you throughout this whole journey.")

    #Pause
input("\nPress [Enter] to continue: ")

print("\n*tap tap*",
      "\nHEY! HEY!, quit tapping the glass.",
      "\n"+player_name+":","()%&@%()%(@&%)@(%&@(&%.",
      "\nNarrator: Fine, since you've asked,",
      "\nI am the narrator of your journey thus far. My name is Python.",
      "\n"+player_name+":","~!@#$%^&*()_)(*&^%$#@#$%^.",
      "\nPython: The story would be too long, there's no time to explain, just trust me.",
      "\n"+player_name+":","~^!*(#!_$(!$+!#)!()&)&$.",
      "\nPython: Isn't reviving your lover more important than asking questions?",
      "\n"+player_name+":","*&$)(!)($&!*^$!*^$!#)#&.",
      "\nPython: You look to the heavy and elaborate door to the left.",
      "\nIt has written above it 'Door to the Afterlife' etched in stone."
      )

print("\nWill you open the door to the afterlife?")

#Player choice to open door to the afterlife.
inside_choice_loop = True
while (inside_choice_loop == True):
    print("\n(yes) or (no)")
    choice = input("\nEnter your choice: ")
    
    if (choice == "yes"):
        print("Python:","You heave open the doors with all your might."
              )
        inside_choice_loop = False
    elif (choice == "no"):
        print("Python:","You've come this far.")
    else:
        print("[Invalid Input, Please Try Again]")

#Lover and Python dialogue
print("You shield your eyes from the bright otherworldly, and incomprehendable light.",
      "You feel a barrier, preventing you from entering the door. It rejects the living.",
      "\nThen you finally see them,",
      "\nAfter so long,",
      "\nThe spirit of your beloved.",
      "\n",love_name+".",
      "\nThey are as beautiful as ever, with a gentle smile across their face.\n"
      )

    #Pause
input("\nPress [Enter] to continue: ")

print("\n"+love_name+": 'Hello dear. It's been so long",player_name+", hasn't it?'")

if (player_is_bald == True):
    print("'Wow, you're bald now. It quite a look.'")

    #Pause
input("\nPress [Enter] to continue: ")

print("\nPython: You are stunned in awe and the beauty of your lover.",
      "\nThen you tell them about the power of the orb in your hands, how you can bring them back.",
      "\nAnd be together again."
      )

    #Pause
input("\nPress [Enter] to continue: ")

print("\n"+love_name+": 'I can't believe it!'",
      "\n'It's very nice in the afterlife. but I would be willing to come back down to earth just to be with you again.'",
      "\n'But I'm fine with whatever you choose to do. Since we will be together again, with each other, either way.'",
      "\n'Whether you die, or you revive me. I want it to be your choice.'"
      )

    #Pause
input("\nPress [Enter] to continue: ")

print("\nPython: Then you hear the orb whisper to you, 'To ressurect them, it will cost the life of your pet,", pet_name+".'",
      "\nYour stomach drops."
      )

     #Pause
input("\nPress [Enter] to continue: ")


#Player choose to ressurect lover.
print("\nPython: Will you ressurect the love of your life at the cost of your pet?")


#First choice
inside_choice_loop = True
while (inside_choice_loop == True):
    print("\n(open inventory) \n(yes) \n(no)")
    if (rizzed_mimic == True):
        print("(choose mimic instead)")
    choice = input("\nEnter your choice: ")
    
    if (choice == "open inventory"):
        #Open and display player inventory.
        print("[Your Inventory]")
        for items in player_inventory:
            print("-",items)
        choice = input("Enter what [item] you use:")
        if (choice == "sword"):
            print("Python:","You want nothing more than to be reunited with",love_name,"again.",
                  "\nIn your desperation and overwhelming longing, you drive the sword deep into your gut, impaling yourself.",
                  "\nAnything to be with them again.",
                  "\n"+love_name,"lets out a gasp and stares at you in horror.",
                  "\n"+love_name+":STOP!!! You didn't need to do that, you could have waited."
                  "\nYou didn't have to kill yourself to be with me.",
                  "\nPython:","Your lover hugs you closely and sobs into your chest. A bloody pool oozes out around you.",
                  "\nEverything begins to swirl and darken.",
                  "\nYour body slowly numbs and your organs shut down.",
                  "\n'Everything goes dark, and you die.'(Narrator from Slay the Princess)"
                  )
            inside_choice_loop = False
        elif (choice == "torch"):
            print("Python:","You light yourself on fire, like a lovestrucked idiot.",
                  "\n'Hey babe, is it just me, or is it getting hot in here?' you say as your hair burns.",
                  "\n"+love_name,"lets out a gasp and stares at you in horror.",
                  "\n'I'm pretty hot right?' you say as your skin and flesh melts off the bone.",
                  "\nThe pain you hide behind your dumb pickup lines is agonizing, not just the fire, but listening to you say it.",
                  "\nYour existence is only pain and flames now, then finally, you die."
                  )
            inside_choice_loop = False
        elif (choice == "bomb"):
            print("Python:","You set your bomb alight, it's fuse fizzes and sizzles as it sparks everywhere.",
                  "\n'I'm the bomb.' you say to your lover.",
                  "\nNot only did I feel the full brunt of second hand embaressment.",
                  "\n"+love_name,"lets out a gasp and stares at you in horror.",
                  "\nNot a moment later, the bomb goes off. And it's surprisingly powerful.",
                  "\nIt blows you, not me, to smithereens. And the entire ceiling collapses in on the room."
                  "\nDestroying the portal to the afterlife."
                  )
            inside_choice_loop = False
        elif (choice == "truth seeing stone"):
            print("Truth Seeing Stone:","'Yup, *coughs*, it's your lover alright.'",
                  "\nPython:","You are SO helpful.",
                  "\nTruth Seeing Stone:","'Ah gee, thanks!'",
                  "\nPython:","I was BEING sarcastic. You are USELESS, you only pointed out the obvious!",
                  "\nTruth Seeing Stone:","'Well, maybe the player is doubting whether this is their real lover or an imposter.'",
                  "\nPython:","Play- Oh~, so you do know more than you're letting on. Well I guess what you said MAY be useful to the player."
                  )
        else:
            print("[Invalid Item]")
    elif (choice == "yes"):
        print("Python:","You close your eyes and confirm your wish. The orb pulses in your hand.",
              "\nYou feel like the precense of",pet_name,"has disapeared from the world."
              )
        inside_choice_loop = False
    elif (choice == "no"):
        print("Python:","After going all this way, you chose not to? What does a pet matter compared to the grandeur of your lover?",
              "\nUse my power. I'm giving you a second chance."
              )
        inside_choice_loop = False
    elif (choice == "choose mimic instead"):
        print("Python:","You choose your monsterous mimic instead of",love_name,"as you feel it satisfies your needs better."
              "\nI can't believe you are cheating on your lover."
              )
        inside_choice_loop = False
    else:
        print("[Invalid Input, Please Try Again]")

#Second choice. Narrator gives you a second chance if you say no.
if (choice == "no"):
    inside_choice_loop = True
    while (inside_choice_loop == True):
        print("\n(open inventory) \n(yes) \n(no)")
        if (rizzed_mimic == True):
            print("(choose mimic instead)")
        choice = input("\nEnter your choice: ")
    
        if (choice == "open inventory"):
            #Open and display player inventory.
            print("[Your Inventory]")
            for items in player_inventory:
                print("-",items)
            choice = input("Enter what [item] you use:")
            if (choice == "sword"):
                print("Python:","You want nothing more than to be reunited with",love_name,"again.",
                      "\nIn your desperation and overwhelming longing, you drive the sword deep into your gut, impaling yourself.",
                      "\nAnything to be with them again.",
                      "\n"+love_name,"lets out a gasp and stares at you in horror.",
                      "\n"+love_name+":STOP!!! You didn't need to do that, you could have waited."
                      "\nYou didn't have to kill yourself to be with me.",
                      "\nPython:","Your lover hugs you closely and sobs into your chest. A bloody pool oozes out around you.",
                      "\nEverything begins to swirl and darken.",
                      "\nYour body slowly numbs and your organs shut down.",
                      "\n'Everything goes dark, and you die.'(Narrator from Slay the Princess)"
                      )
                inside_choice_loop = False
            elif (choice == "torch"):
                print("Python:","You light yourself on fire, like a lovestrucked idiot.",
                      "\n'Hey babe, is it just me, or is it getting hot in here?' you say as your hair burns.",
                      "\n"+love_name,"lets out a gasp and stares at you in horror.",
                      "\n'I'm pretty hot right?' you say as your skin and flesh melts off the bone.",
                      "\nThe pain you hide behind your dumb pickup lines is agonizing, not just the fire, but listening to you say it.",
                      "\nYour existence is only pain and flames now, then finally, you die."
                      )
                inside_choice_loop = False
            elif (choice == "bomb"):
                print("Python:","You set your bomb alight, it's fuse fizzes and sizzles as it sparks everywhere.",
                      "\n'I'm the bomb.' you say to your lover.",
                      "\nNot only did I feel the full brunt of second hand embaressment.",
                      "\n"+love_name,"lets out a gasp and stares at you in horror.",
                      "\nNot a moment later, the bomb goes off. And it's surprisingly powerful.",
                      "\nIt blows you, not me, to smithereens. And the entire ceiling collapses in on the room.",
                      "\nDestroying the portal to the afterlife."
                      )
                inside_choice_loop = False
            elif (choice == "truth seeing stone"):
                print("Truth Seeing Stone:","'Yup, *coughs*, it's your lover alright.'",
                      "\nPython:","You are SO helpful.",
                      "\nTruth Seeing Stone:","'Ah gee, thanks!'",
                      "\nPython:","I was BEING sarcastic. You are USELESS, you only pointed out the obvious!",
                      "\nTruth Seeing Stone:","'Well, maybe the player is doubting whether this is their real lover or an imposter.'",
                      "\nPython:","Play- Oh~, so you do know more than you're letting on. Well I guess what you said MAY be useful to the player."
                      )
            else:
                print("[Invalid Item]")
        elif (choice == "yes"):
            print("Python:","You close your eyes and confirm your wish. The orb pulses in your hand.",
                  "\nYou feel like the precense of",pet_name,"has disapeared from the world."
                  )
            inside_choice_loop = False
        elif (choice == "no"):
            print("Python:","Fine."
                  )
            inside_choice_loop = False
        elif (choice == "choose mimic instead"):
            print("Python:","You choose your monsterous mimic instead of",love_name,"as you feel it satisfies your needs better."
                  "\nI can't believe you are cheating on your lover."
                  )
            inside_choice_loop = False
        else:
            print("[Invalid Input, Please Try Again]")


#Choose Sword Ending
if (choice == "sword"):

    print("\nPython:","You are dead, a spirit as romantic as Romeo.",
          "\nThey leap into your arms and you twirl together in an embrace.",
          "\nThough they still look sad.",
          "\nYou enter the door to the afterlife together. It's indescribable.",
          "\nYou sit down together shoulder to shoulder, finally reunited and at peace.",
          "\nTogether again, forever."
          )

#Choose Torch Ending
if (choice == "torch"):

    print("\nPython:","You are dead, a finely roasted spirit now.",
          "\nThey leap into your arms and you twirl together in an embrace.",
          "\nThough they still look sad.",
          "\nYou enter the door to the afterlife together. It's indescribable.",
          "\nYou sit down together shoulder to shoulder, finally reunited and at peace.",
          "\nTogether again, forever."
          )

#Choose Bomb Ending
if (choice == "bomb"):

    print("\nPython:","You are dead, a restless spirit now.",
          "\nThough",love_name,"is nowhere to be seen.",
          "\nWith the door destroyed."
          "\nYou float aimlessly through the crumbled walls, and to the surface, you watch the sunset behind the dark clouds all alone.",
          "\nForever yearning for your lover. And regretting doing, whatever you just did."
          "\nAlone again, but forever."
          )

#Choose Yes Ending
if (choice == "yes"):
    print("\n"+love_name+": 'Hahaha, I can't believe we're together again my love!'")


    print("\nPython:",love_name,"has turned back into a living human.",
          "\nThey leap into your arms and you twirl together in an embrace.")

    if (rizzed_mimic == True):
        print("\nYou can't help but feel the guilt eating you, of cheating your lover behind their back.",
              "\nMaybe it's okay, maybe they would forgive you, maybe it's fine as long as they never find out.")

    print("\nYou return back to the surface together. The sky is clear and sunny now.",
          "\nYou sit down together shoulder to shoulder, watching the sunset.",
          "\nTogether again, you plan towards the future, to do the things you regretted not having enough time to do."
          "\nAnd facing the struggles and pain of the world together, side by side."
          "\nYou do miss",pet_name,"though."
          )



#Choose No Ending
if (choice == "no"):

    print("\n"+love_name+": 'I respect your decision.'",
          "\n'It's not worth taking the life of your pet if you will die and be together in the afterlife eventually.'"
          )

    print("\nPython:",love_name,"floats back through the door to the afterlife.",
          "\nAnd waves you goodbye."
          )

    print("\n"+love_name+": 'I'll see you later, my love.'")

    print("\nPython:","They smile at you before the doors slam shut.",
          "\nYou return to the surface. The sky is clear and sunny now. And you stare into the sunset.",
          "\nYou finally feel at peace, and can't wait to pet",pet_name,"once you get back."
          )



#Choose Mimic Ending
if (choice == "choose mimic instead"):
    print("\nPython:","You smugly tell",love_name,"that you have chosen a new lover.",
          "\nThen the mimic oozes through the cracks of the walls into the room.",
          "\nIt moves toward you to be by your side."
          )

    print("\n"+love_name+": 'I can't even, and you are even shoving it in my face.'",
          "\n'You know what, I was wrong. Wrong about you, ever thinking we had something!'",
          "\n'And wrong about ever thinking you were a decent human being, you jerk!.'"
          )

    print("\nPython:",love_name,"dashes back through the door to the afterlife.",
          "\nAnd slams the doors shut.",
          "\nYou look to your dashing mimic. And bring it close to you and together you kiss.",
          "\nYou return to the surface. The sky is clear and sunny now. And you stare into the sunset together.",
          "\nYou feel at peace, now that you have moved on, with a monster as a new lover.",
          "\nDamn, you're cold."
          )

#Pause
input("\nPress [Enter] to continue: ")


#End of program
print("\n~~~~~~~~~~~~~~~~~The End~~~~~~~~~~~~~~~~~")
input("Press [Enter] to close the game:")
exit()
