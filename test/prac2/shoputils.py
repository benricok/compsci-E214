import sys, stdio, stdarray

def readShop():
    if stdio.hasNextLine():
        a = stdio.readString()
        if a == 'ENDSHOPS':
            return None
        else:
            return a
    else:
        return None

def readPrice():
    if stdio.hasNextLine():
        a = stdio.readString()
        if a == 'ENDPRICES':
            return None
        else:
            name = a
            price = stdio.readFloat()
            return [name, price]
    else:
        return None

def readPrices():
    prices = []
    done = False
    while not done:
        a = readPrice()
        if a == None:
            return prices
        prices.append(a)

def readShoppingList():
    shoppingList = []
    done = False
    while not done:
        if stdio.hasNextLine():
            #try:
                a = stdio.readLine()
            #except ValueError:
            #    print('Error reading')

            if a == 'ENDLIST':
                if len(shoppingList) == 0:
                    return None
                else:
                    return shoppingList
            else:
                #print(a)
                shoppingList.append(a)

def shoptimize(shops, prices, items):
    length = len(items)
    cheapest = [''] * length
    
    for idx, item in enumerate(items):
        low = 1000000000
        for shopidx, price in enumerate(prices):
            if item == price[0]:
                if low > price[1]:
                    low == price[1]
                    cheapest[idx] = shop[shopidx]

    return cheapest

def witeShoppingList(shops, items):
    if not len(shops) == len(items):
        stdio.writef('ERROR: arrays shops and items not same length\n')

    for idx, item in enumerate(items):
        if shops[idx] == '':
            stdio.writeln(f'{item}: NOWHERE IN STOCK')
        stdio.writeln(f'{item}: {shops[idx]}')
