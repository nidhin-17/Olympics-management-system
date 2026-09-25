from playeradd import addplayer
from searchplayer import search
from prizeupdation import prizeupdate
from removeplayer import remove
from topplayer import playertop
from country import topcountry
y='yes'
while y=="yes":
    print("................olympics...............")
    print("1:To add a player")
    print("2:To search a player")
    print("3:To update a player")
    print("4:To remove player")
    print("5:To view players")
    print("6:To view countries")
    choice = input("enter the choice mentioned above:")
    if choice=='1':
        addplayer()
    elif choice=='2':
        search()
    elif choice=='3':
        prizeupdate()
    elif choice=='4':
        remove()
    elif choice=='5':
        playertop()
    elif choice=='6':
        topcountry()
    else:
        print("enter the valid choice")
    n = input("enter yes for continue:")
    y = n.lower()