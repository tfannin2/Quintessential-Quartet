def createPointStore():
    #Make the inventory
    global inventory
    inventory = []
    inventory.append(["Baseball Hat", "25 points"])
    inventory.append(["Tie", "30 points"])
    inventory.append(["Hair Bow", "30 points"])
    inventory.append(["Bow Tie", "50 points"])

def visitPointStore():

    #determine amount of points user has
    global points

    #Display shopkeep and opening message
    print("Hello there! We have many wares that will \n")
    print("make your dog the talk of the town!\n")
    #clear screen somehow.
    print("What would you like?")

    #Print list of items for purchase
    global inventory
    for item in inventory:
        print(item[0] + ":" + "\t\t" + item[1])
    

createPointStore()
visitPointStore()
