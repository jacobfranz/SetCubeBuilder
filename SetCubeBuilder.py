import requests
import json


totalCards = 0

def getNames(fetch, number, f):
    #get the correct json blob

    global totalCards

    for x in fetch.items():
        item = x

    #switch to the list of cards rather than the first part of the blob
    cardList = item[1]

    #get an individual card
    #card = cardList[0]
    #print(type(card))

    #f = open("cardnames.txt", "a+")

    print(len(cardList))

    for card in cardList:
        #if card['promo_types'] != 'planeswalkerdeck':
        #print(type(card))

        if 'promo_types' not in card:
            totalCards = totalCards + number
            f.write(str(number))
            f.write(' ')
            f.write(card['name'])
            f.write('\n')

setCode = input('What set code corresponds to the set you are using for your cube? Ex: DOM ')
print()


f = open("cardnames.txt", "w+")

response = requests.get('https://api.scryfall.com/cards/search?order=set&q=set%3A{}+rarity%3Am+not%3Apwdeck'.format(setCode))
fetch = response.json()

number = int(input("How many copies do you want of each Mythic? "))
f.write('Mythics \n')
getNames(fetch, number, f)
f.write('\n')
print()

response = requests.get("https://api.scryfall.com/cards/search?order=set&q=set%3A{}+rarity%3Ar+not%3Apwdeck".format(setCode))
fetch = response.json()

number = int(input("How many copies do you want of each Rare? "))
f.write('Rares \n')
getNames(fetch, number, f)
f.write('\n')
print()

response = requests.get("https://api.scryfall.com/cards/search?order=set&q=set%3A{}+rarity%3Au+not%3Apwdeck".format(setCube())
fetch = response.json()

number = int(input("How many copies do you want of each Uncommon? "))
f.write('Uncommons \n')
getNames(fetch, number, f)
f.write('\n')
print()

response = requests.get("https://api.scryfall.com/cards/search?order=set&q=set%3A{}+rarity%3Ac+not%3Apwdeck+-t%3Abasic".format(setCube())
fetch = response.json()

number = int(input("How many copies do you want of each Common? "))
f.write('Commons \n')
getNames(fetch, number, f)
f.write('\n')
print('You need ' + str(totalCards) + ' cards.')


f.close()









