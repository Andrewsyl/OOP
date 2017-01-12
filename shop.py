def show_list(shopping_list):
    count = 1
    for item in shopping_list:
        print '{} - {}'.format(count, item)
        count += 1

def add():
    shopping_list = []
    while True:
        stuff = raw_input('What do you want?: ')
        if stuff == 'show':
            show_list(shopping_list)
        elif stuff == 'remove':
            while True:
                take = raw_input('What do you want to take away?: ')
                try:
                    shopping_list.pop(int(take)-1)
                    show_list(shopping_list)
                    break
                except ValueError:
                    print 'Please enter the number of the item'

        else:
            new_stuff = stuff.split(',')
            for items in new_stuff:
                shopping_list.append(items)


add()