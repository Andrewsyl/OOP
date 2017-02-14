directions = {
    'left': (-1, 0),
    'right': (1, 0),
    'forward': (0, -1),
    'back': (0, 1),
}

locations = {
    (0, 0): 'Cave',
    (0, 1): 'Village',
    (1, 0): 'Building',
    (0, 1): 'Midgar'
}

description = {
    (0, 0): "A BIG DARK HOUSE WITH NO LIGHTS",
    (0, 1): 'A LAKE USED FOR DUMPING RUBBISH',
    (1, 0): 'A SUNNY PARK FULL OF PEOPLE',
    (1, 1): 'A MARKET FULL OF FOOD STALLS',
}

items = {
    (0, 0): 'candle stick',
    (0, 1): 'rubber duck',
    (1, 0): 'football',
    (1, 1): 'bag of chips',
}

position = (0, 0)

# direction = raw_input('forward, back, left ,right?: ')

inventory = []

while True:

    location = locations[position]
    description1 = description[position]
    stuff = items[position]
    # mapo = map[position]

    print 'You are at the %s' % location
    print '%s' % description1
    # print '%s' % mapo

    Choice = raw_input('You find a %s. Do you pick it up? YES/NO\n' % stuff).upper()
    if Choice == 'YES':
        if stuff in inventory:
            print "You aleady have one of those"
            continue
        else:
            print "You picked up the %s" % stuff
            inventory.append(stuff)
    # elif stuff in inventory:
    #     print "You already have one of those"
    #     continue
    elif Choice == "DROP ITEM":
        i = raw_input("which item?: ")
        for j in inventory:
            if j == i:
                inventory.remove(i)
        print "You dropped %s" % i
    else:
        print "You leave the %s and keep going" % stuff

    valid_directions = {}
    for k, v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1])
        possible_location = locations.get(possible_position)

        if possible_location:
            print 'to the %s is a %s' % (k, possible_location)
            valid_directions[k] = possible_position
    print "Inventory: %s" % inventory

    direction = raw_input('which direction do you want to go?\n')
    new_position = valid_directions.get(direction)
    if new_position:
        position = new_position
    else:
        print "You walked into a fence"

print inventory
print "You collected all the items, well done!"
