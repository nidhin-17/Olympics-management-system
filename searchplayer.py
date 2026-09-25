import csv
def search():
    with open("olympics.csv",'r') as oly:
        cr=csv.reader(oly)
        playerid=input("enter the player_id:")
        list=[]
        for i in cr:
            list.append(i[0])
        if playerid not in list:
            print("player not found")
    with open("olympics.csv", 'r') as oly:
        cr = csv.reader(oly)
        for i in cr:
            if i!=[]:
                if i[0]==playerid:
                    print("Details of the player searched")
                    print('player_id', '::', 'player_name', '::', 'country', '::', 'Item', '::', 'Gold', '::', 'silver',
                          '::', 'bronze', '::', 'points')
                    for x in i:
                        print(x,end='::')
                    print()