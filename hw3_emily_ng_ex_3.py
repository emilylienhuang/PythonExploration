'''
Homework 3, Exercise 3
Emily Ng
2/18/2023
This exercise saves an inventory in a dictionary.
There are functions to print the inventory, add an item, and delete an item.
'''

def printInventory(inventory):
    print('The current inventory: ')
    for key in inventory:
        print('{} has {} in stock.'.format(key, inventory[key]))
    print()

def addItem(inventory, item):
    if item in inventory:
        #increment item inventory already in inventory
        inventory[item] += 1
    else:
        #add the item to the inventory if it's not there
        inventory[item] = 1

def deleteItem(inventory,item):

    if inventory[item] == 0:
        #error no more to delete
        print('Error: There is no more {} to remove.'.format(item))
    else:
        #otherwise just take one out of the inventory
        inventory[item] -= 1


def main():
    #test inventory
    inventory= {'Hand Sanitizer': 10, 'Soap': 6, 'Kleenex': 22, 'Lotion': 16, 'Razors': 12}

    #test print
    printInventory(inventory)

    #test add item
    addItem(inventory, 'Advil')

    printInventory(inventory)

    addItem(inventory, 'Advil')

    printInventory(inventory)

    addItem(inventory, 'Lotion')

    printInventory(inventory)

    #test delete item
    print('Taking out one bar of soap until there are none left...')

    while inventory['Soap'] != 0:
        deleteItem(inventory, 'Soap')
        printInventory(inventory)

    print('Trying to remove another bar of soap...')
    deleteItem(inventory,'Soap')
    printInventory(inventory)
main()