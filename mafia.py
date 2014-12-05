#mafia

from random import *

sheriff1 = 0
sheriff2 = 1
mafia1 = 2
mafia2 = 2
mafia3 = 2
doctor = 3

numplayers = 15


def playOnce(playerslist):
    """Plays one game of mafia using the list of players, returns
    1 if the town wins and 0 if the mafia wins
    Optimal strategy:
        After the first night, one of the sheriffs reveals who they are.
        The doctor protects that person every night.
        The town only kills someone if the sheriff tells them to.
        The sheriff only kills someone after discovering they are in the mafia.
        The sheriff always reveals what they learned the night before.
        The mafia kills whoever the sheriff last revealed.
        Whenever a mafia member is killed, they try to kill the sherif the next
        night.
        Once the sheriff is dead, the town kills people at random.
    Possible imporvements: force mafia to guess which sheriff to kill
        on the second night"""
    players = []
    for i in playerslist:
        players.append(i)
    done = False
    firstnight = True
    secondnight = False
    sheriffalive = True
    lastidentified = 0 #position in the list of the last person investigated
    while not done:
        #print(players)
        #night time is first
        #mafia kills someone
        if firstnight or not sheriffalive:
            killdone = False
            while not killdone:
                victim = randint(0,len(players)-1)
                if players[victim] != 0 and players[victim] != 2:
                    #dont kill the key sherif or mafia members
                    
                    if players[victim] != 3:
                        #doctor protects themself if its the first night
                        players.pop(victim)
                    killdone = True
            firstnight = False
            secondnight = True
        elif foundmafia: #try to kill the sheriff
            if players.count(3) == 0: #doctor is dead
                players.pop(players.index(0)) #kill the sheriff
                sheriffalive = False
        else: #mafia should always kill a known innocent if possible
            players.pop(lastidentified)

            
        #sheriffs pick someone they have not picked before at random
        sheriffsdone = False
        foundmafia = False
        if sheriffalive:
            while not sheriffsdone:
                inspected = randint(0,len(players)-1)
                if players[inspected] == 2:
                    foundmafia = True
                    sheriffsdone = True
                elif (players[inspected] == 3 or players[inspected] == 5
                      or players[inspected] == 1):
                    sheriffsdone = True
                    lastidentified = inspected

                
        #then day time
        if foundmafia:
            players.pop(inspected)
        if not sheriffalive:
            players.pop(randint(0,len(players)-1))
        #check if the game is over
        if players.count(2) >= len(players)/2.0:
            done = True
            return 0 #mafia wins
        if players.count(2) == 0:
            done = True
            return 1 #town wins

def randomPlay(playerslist):
    """Plays one game of mafia using the list of players, returns
    1 if the town wins and 0 if the mafia wins
    Simulates when both sheriffs and 2 mafia members die"""
    players = []
    for i in playerslist:
        players.append(i)
    done = False
    sheriffalive = True
    foundmafia = False
    lastidentified = 0 #position in the list of the last person investigated
    while not done:
        #print(players)
        #night time is first
        #mafia kills someone
        killdone = False
        while not killdone:
            victim = randint(0,len(players)-1)
            if players[victim] != 0 and players[victim] != 2:
                #dont kill the key sherif or mafia members
                
                if players[victim] != 3:
                    #doctor protects themself if its the first night
                    players.pop(victim)
                killdone = True

        players.pop(randint(0,len(players)-1))
        #check if the game is over
        if players.count(2) >= len(players)/2.0:
            done = True
            return 0 #mafia wins
        if players.count(2) == 0:
            done = True
            return 1 #town wins

def oneMafia(playerslist):
    """Plays one game of mafia using the list of players, returns
    1 if the town wins and 0 if the mafia wins
    Simulates when both sheriffs and 2 mafia members die"""
    players = []
    for i in playerslist:
        players.append(i)
    done = False
    firstnight = False
    secondnight = False
    sheriffalive = False
    lastidentified = 0 #position in the list of the last person investigated
    while not done:
        #print(players)
        #night time is first
        #mafia kills someone
        if firstnight or not sheriffalive:
            killdone = False
            while not killdone:
                victim = randint(0,len(players)-1)
                if players[victim] != 0 and players[victim] != 2:
                    #dont kill the key sherif or mafia members
                    
                    if players[victim] != 3:
                        #doctor protects themself if its the first night
                        players.pop(victim)
                    killdone = True
            firstnight = False
            secondnight = True
        elif foundmafia: #try to kill the sheriff
            if players.count(3) == 0: #doctor is dead
                players.pop(players.index(0)) #kill the sheriff
                sheriffalive = False
        else: #mafia should always kill a known innocent if possible
            players.pop(lastidentified)

            
        #sheriffs pick someone they have not picked before at random

                
        #then day time

        players.pop(randint(0,len(players)-1))
        #check if the game is over
        if players.count(2) >= len(players)/2.0:
            done = True
            return 0 #mafia wins
        if players.count(2) == 0:
            done = True
            return 1 #town wins


playerslist = [sheriff1,sheriff2,mafia1,mafia2,mafia3,doctor]
for i in range(numplayers - 6):
    playerslist.append(5)

onemafia = [mafia1,doctor]
for i in range(numplayers - 10):
    onemafia.append(5)

equallist = [sheriff1,sheriff2,mafia1,mafia2,doctor]
for i in range(numplayers - 5):
    equallist.append(5)



def sim(game,playerslist,times):
    mafiawins = 0
    townwins = 0
    for i in range (times): #max 10000000, any more and it could take hours
        x = game(playerslist)
        if x == 1:
            townwins += 1
        else:
            mafiawins += 1

    print("Town won " + str(townwins) + " times")
    print("Mafia won " + str(mafiawins) + " times")
    if mafiawins != 0:
        print ("Town won " + str(100*townwins/float(mafiawins+townwins)) + "%")
    else:
        print ("Town won 100%")
            
        
