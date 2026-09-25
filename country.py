import csv
def topcountry():
    with open("olympics.csv",'r') as oly:
        cr=csv.reader(oly)
        list=[]
        list1=[]
        list2=[]
        list3=[]
        for i in cr:
            if i!=[]:
                list.append(i)
        for i in list:
            list1.append(i[2])
        for x in list1:
            gold=0
            silver=0
            bronze=0
            point=0
            for i in list:
                if i[2]==x:
                    gold=gold+int(i[4])
                    silver=silver+int(i[5])
                    bronze=bronze+int(i[6])
                    point=point+int(i[7])
                    l=[i[2],gold,silver,bronze,point]
            if l not in list2:
                list2.append(l)
    for i in list2:
        list3.append(i[4])
    list3.sort()
    list3=list3[-1::-1]
    print("country","::","gold","::","silver","::","bronze")
    for x in list3:
        for i in list2:
            if x==i[4]:
                for x in i:
                    print(x,end="::")
                print()


