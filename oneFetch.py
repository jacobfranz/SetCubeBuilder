import requests
import json


f = open("cardnames.txt", "w+")

#get the json blob for the entire set
response = requests.get("https://api.scryfall.com/cards/search?order=cmc&q=set%3Adom")
fetch = response.json()


#get the correct json blob
for x in fetch.items():
    item = x

#switch to the list of cards rather than the first part of the blob
cardList = item[1]

#get an individual card
#card = cardList[0]
#print(type(card))


number = int(input("How many copies do you want of each Mythic? "))
f.write('Mythics \n')
f.write('\n')
print()

for card in cardList:
    if card['rarity'] == 'mythic':
        f.write(str(number))
        f.write(' ')
        f.write(card['name'])
        f.write('\n')


number = int(input("How many copies do you want of each Rare? "))
f.write('Rares \n')
f.write('\n')
print()

for card in cardList:
    if card['rarity'] == 'rare':
        f.write(str(number))
        f.write(' ')
        f.write(card['name'])
        f.write('\n')


number = int(input("How many copies do you want of each Uncommon? "))
f.write('Uncommons \n')
f.write('\n')
print()

for card in cardList:
    if card['rarity'] == 'uncommon':
        f.write(str(number))
        f.write(' ')
        f.write(card['name'])
        f.write('\n')


number = int(input("How many copies do you want of each Common? "))
f.write('Commons \n')
f.write('\n')
print()

for card in cardList:
    if card['rarity'] == 'common':
        f.write(str(number))
        f.write(' ')
        f.write(card['name'])
        f.write('\n')



f.close()


