rooms = {
    'Hall': {
        'description': 'You are in the Hall. There is a door to the south.',
        'south': 'Kitchen',
        'item': 'Key'
    },
    'Kitchen': {
        'description': 'You are in the Kitchen. There is a door to the north and east.',
        'north': 'Hall',
        'east': 'Dining Room',
        'item': 'Knife'
    },
    'Dining Room': {
        'description': 'You are in the Dining Room. There is a door to the west.',
        'west': 'Kitchen',
        'item': 'Monster'
    }
} 

current_room = 'Hall'
inventory = []

while True:
    print(rooms[current_room]['description'])

    command = input("Enter your move: ").lower().split()

    if command[0] == 'go':
        direction = command[1]
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way!")

    elif command[0] == 'get':
        item = command[1].capitalize()
        if 'item' in rooms[current_room] and rooms[current_room]['item'] == item:
            inventory.append(item)
            print(f"{item} collected!")
            del rooms[current_room]['item']
        else:
            print(f"Can't get {item}.")

    elif command[0] == 'exit':
        print("Thanks for playing!")
        break

if 'item' in rooms[current_room] and rooms[current_room]['item'] == 'Monster':
    if 'Knife' in inventory:
        print("You defeated the monster!")
    else:
        print("You were eaten by the monster. Game Over.")
        breakpoint
