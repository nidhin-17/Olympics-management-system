import csv
import os
def addplayer():
    with open("olympics.csv","a",newline='') as olympic:
        olyw=csv.writer(olympic)
    playerid=input("enter the player id:")
    with open("olympics.csv", "r+",newline='') as olympic:
        cr=csv.reader(olympic)
        cw=csv.writer(olympic)
        filepath='olympics.csv'
        if os.path.getsize(filepath)==0:
            playername = input("enter the player name:")
            country = input("enter the player country:")
            item = input("enter the item of player:")
            gold = input("enter the gold prize:")
            silver = input("enter the silver prize:")
            bronze = input("enter the bronze prize:")
            points = (int(gold) * 5) + (int(silver) * 3) + (int(bronze) * 1)
            list = [playerid, playername, country, item, gold, silver, bronze, str(points)]
            print('player_id','::','player_name','::','country','::','Item','::','Gold','::','silver','::','bronze','::','points')
            for i in list:
                print(i,end='::')
            cw.writerow(list)
            print()
            print("player inserted succesfully")
        else:
            list=[]
            for i in cr:
                list.append(i[0])
            if playerid not in list:
                playername = input("enter the player name:")
                country = input("enter the player country:")
                item = input("enter the item of player:")
                gold = input("enter the gold prize:")
                silver = input("enter the silver prize:")
                bronze = input("enter the bronze prize:")
                points = (int(gold) * 5) + (int(silver) * 3) + (int(bronze) * 1)
                list = [playerid, playername, country, item, gold, silver, bronze, str(points)]
                print('player_id', '::', 'player_name', '::', 'country', '::', 'Item', '::', 'Gold', '::', 'silver',
                      '::', 'bronze', '::', 'points')
                for i in list:
                    print(i, end='::')
                cw.writerow(list)
                print()
                print("player inserted succesfully")
            else:
                print('enter a another playerid')