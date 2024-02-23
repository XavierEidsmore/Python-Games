print("~~~Crafting Sim~~~",
      "\nCraft two things together."
      )

#Default is both 0.5
item_one_divider_ratio = 0.6
item_two_divider_ratio = 0.4

inside_choice_loop = True
while (inside_choice_loop == True):
    item_one = input("Enter thing 1: ")
    item_two = input("Enter thing 2: ")
    item_one_length = int(len(item_one) * item_one_divider_ratio)
    item_two_length = int(len(item_two) * item_two_divider_ratio)
    print("\nCrafting...\n",item_one[:item_one_length]+item_two[item_two_length:],
          "\n")
    #print(item_one_length,item_two_length)
