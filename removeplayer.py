import csv
def remove():
    with open("olympics.csv",'r') as olympics:
        cr=csv.reader(olympics)
        playerid=input("enter player_id to be removed:" )
        list=[]
        list1=[]
        for i in cr:
            if i!=[]:
                if playerid!=i[0]:
                    list.append(i)
                else:
                    print('player_id', '::', 'player_name', '::', 'country', '::', 'Item', '::', 'Gold', '::',
                          'silver',
                          '::', 'bronze', '::', 'points')
                    list1.append(i)
                    for x in list1:
                        for i in x:
                            print(i,end="::")
                    print()
                    print("player removed succesfully")
        if list1==[]:
            print("enter a valid player id")
        else:
            with open("olympics.csv", 'w',newline='') as olympics:
                cw=csv.writer(olympics)
                for j in list:
                    cw.writerow(j)