import sys, stdio, stdarray, shoputils

def main():
    shops = []
    prices = []
    done = False
    while not done:
        shop = shoputils.readShop()
        if shop == None:
            done == True
            break
        
        shops.append(shop)
        prices.append(shoputils.readPrices())
    
    #print('shops')
    #print(shops)
    #print('prices')
    #print(prices)
    items = []
    done = False
    while not done:
        shoplist = shoputils.readShoppingList()
        if list == None:
            break
        else:
            items.append(shoplist) 

    cheapest = shoputils.shoptimize(shops, prices, items)

    shoputils.writeShoopingList(cheapest, items)

if __name__ == '__main__': main()
