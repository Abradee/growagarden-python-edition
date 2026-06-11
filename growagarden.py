import time
import random

# Startup

print("Welcome to Grow a Garden PYTHON EDITION")
print("(c) Abradee 2025")

# Setup variables

grownitems = []
inventory = ["carrot"]
plantingitems = []
money = 0
carrotValue = 10
carrot = "carrot"



# Main command loop

while True:
    
    cmd = input("Type 'help' for help: ").strip().lower()

    if cmd == "help":
        print("Commands:")
        print("sell - allows you to sell items")
        print("help - shows this screen")
        print("quit - exits the game")
        print("plant - plants all")
        print("shop - opens the shop")
        
    if cmd == "shop":
        
        print("====SHOP====")
        

    elif cmd == "sell":
        if grownitems:
            if carrot in grownitems:
                money += carrotValue
                print("Money: ", money)
            print("You sold:", grownitems.pop(0))
            print("Items left:", grownitems)
        else:
            print("You have nothing to sell!")
    
    if cmd == "plant":
        print("Planting: ", inventory)
        plantingitems.append("carrot")
        if carrot in inventory:
            plantingitems.remove("carrot")
            print("0%")
            time.sleep(1)
            print("10%")
            time.sleep(1)
            print("20%")
            time.sleep(1)
            print("30%")
            time.sleep(1)
            print("40%")
            time.sleep(1)
            print("50%")
            time.sleep(1)
            print("60%")
            time.sleep(1)
            print("70%")
            time.sleep(1)
            print("80%")
            time.sleep(1)
            print("90%")
            time.sleep(1)
            print("100%")
            print("Your carrot is fully grown! Sell it with the command 'sell'")
            grownitems.append("carrot")
        else:
            print("You have no items to plant!")
        
        

    if cmd == "quit":
        print("Thanks for playing! Goodbye.")
        break  # Exit the loop and end the program

   

