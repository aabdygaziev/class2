while True:
    b = input()
    if b =='hello':
        print('hello')
    elif b =='menu':
        food = ''
        drink =''
        place =''

        while not (food.lower() == 'burger' or food.lower() == 'hotdog'):
            print('burger ili hotdog?')
            food = input()
        print('do you want to drink?')
        b = input()
        if b=='yes':
            while not (drink.lower() == 'cola' or drink.lower() == 'pepsi'):
                print('Cola ili Pepsi?')
                drink = input()
        print('zdes ili na vinos')
        while not (place.lower() == 'zdes' or place.lower() == 'vinos'):
            place = input()

        print(food, drink, place)













