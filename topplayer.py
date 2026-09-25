import csv
def playertop():
    with open("olympics.csv",'r') as olympics:
        olyr=csv.reader(olympics)
        l=[]
        for i in olyr:
            l.append(int(i[7]))
        l.sort()
        l=l[-1::-1]
        print('player_id', '::', 'player_name', '::', 'country', '::', 'Item', '::', 'Gold', '::',
              'silver',
              '::', 'bronze', '::', 'points')
        for j in l:
            with open("olympics.csv", 'r') as olympics:
                olyr1 = csv.reader(olympics)
                for x in olyr1:
                    if j==int(x[7]):
                        for i in x:
                             print(i,end="::")
                        print()