import csv
def prizeupdate():
    with open("olympics.csv",'r') as oly:
        cr=csv.reader(oly)
        list=[]
        list1=[]
        for i in cr:
            if i!=[]:
                list.append(i)
        playerid=input('enter player_id for price updation:')
        for i in list:
            list1.append(i[0])
        if playerid in list1:
            gold=input('enter the gold prize:')
            silver=input('enter the silver prize:')
            bronze=input('enter the bronze prize:')
            list2=[]
            for i in list:
                if i[0]==playerid:
                    i[4]=str(int(i[4])+int(gold))
                    i[5]=str(int(i[5])+int(silver))
                    i[6]=str(int(i[6])+int(bronze))
                    i[7]=str((int(i[4])*5)+(int(i[5])*3)+(int(i[6])*1))
                    list2.append(i)
                    print('player_id', '::', 'player_name', '::', 'country', '::', 'Item', '::', 'Gold', '::', 'silver',
                          '::', 'bronze', '::', 'points')
                    for x in i:
                        print(x,end="::")
                    print()
                    print("player detail updated successfully")
                else:
                    list2.append(i)
            with open("olympics.csv", 'w',newline='') as oly:
                cw=csv.writer(oly)
                for i in list2:
                        cw.writerow(i)
        else:
            print("enter valid player_id")