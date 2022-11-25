# Programmed by Kenneth Mallabo
# C15494052
# For the Lab Assessment Part 1 for the Software Development module
# This program is small text adventure game

import random

class Game:
    # initialise the variables
    def __init__(self, cm, cn):
        self.combatMode = cm
        self.characterName = cn

    # main menu selection function/mutator method
    def menuSelect(self):
        print("Press 1 to start game")
        print("Press 2 to exit game")
        while True:
            selection = input("Enter value here: ")
            if selection == "1":
                print("Starting Game")
                value = input("Please enter 1 if you wish to get into a dialog scenario or 2 for just combat:\n")
                if value == "1":
                    self.combatMode = 0
                    print("You have chosen story mode")
                    break
                elif value == "2":
                    self.combatMode = 1
                    print("You have chosen combat mode only")
                    break
                else:
                    print("Incorrect input detected, please choose 1 or 2")

            elif selection == "2":
                print("Exiting Game")
                exit()
            else:
                print("Incorrect input detected, please choose 1 or 2")

    # function to add the character's name/mutator method
    def addName(self):
        self.characterName = input("Enter your character's name:\n")

class Scenario(Game):
    # initialise with inheritance from Game class
    def __init__(self, combatMode, characterName, num):
        super().__init__(combatMode, characterName)
        self.talker = None
        self.noOfEnemy = num
        self.movement = None
        self.loot = None
        self.playerHealth = 100
        # a list enemy names and their health
        self.listEnemy = []

    # function to print statements out if you picked combat/dialog
    def startScenario(self):
        # dialog only
        if self.combatMode == 0:
            print("Welcome to Fodlan, a continent recovering from a recent devastating war")
            print("Disillusioned soldiers have turned to banditry")
            print("Be careful whilst on your journey")
        # no dialog, all combat
        elif self.combatMode == 1:
            print("Welcome to Fodlan, a continent that is experiencing complete societal collapse")
            print("A devastating plague has wiped out most of the population")
            print("The only survivors are deranged, prepare for unending struggle")

    # function on where to move/mutator method
    def moveScenario(self):
        while True:
            print("To the north is the savage mountains, filled with man eating heathens.")
            print("To the south lies the unforgiving desert where slavery has yet to be expelled.")
            print("To the west engulfs the seemingly endless seas, privateers and pirates are a dime a dozen here.")
            print("To the east where land is yet to be charted, here be dragons?")
            self.movement = input("Where do you want to venture forth?\n")

            if self.movement == "north":
                print(f"{self.characterName} had trekked north in the snowy mountains")
                self.movement = "north"
                break
            elif self.movement == "south":
                print(f"{self.characterName} had journeyed towards the sandy south")
                self.movement = "south"
                break
            elif self.movement == "west":
                print(f"{self.characterName} had sailed the western seas")
                self.movement = "west"
                break
            elif self.movement == "east":
                print(f"{self.characterName} have travelled to the far east")
                self.movement = "east"
                break
            else:
                print(f"Incorrect location has been inputted , what is {self.movement} anyway?")

    # function to create enemies to fight/mutator method
    def generateNumEnemy(self):
        # create up to 3 enemies
        self.noOfEnemy = random.randint(2, 3) #Bug?: if used 1 to 5, sometimes 0 gets used
        print(self.noOfEnemy)
        for x in range(1, self.noOfEnemy):
            if self.movement == "north":
                self.enemyName = "Chaos Marauder"
                self.listEnemy.append([self.enemyName + str(x), 80])
            elif self.movement == "south":
                self.enemyName = "Slaver"
                self.listEnemy.append([self.enemyName + str(x), 20])
            elif self.movement == "west":
                self.enemyName = "Pirate"
                self.listEnemy.append([self.enemyName + str(x), 40])
            else:
                self.enemyName = "Ninja"
                self.listEnemy.append([self.enemyName + str(x), 60])
        self.noOfEnemy = self.noOfEnemy - 1

    # function to create npc/mutator method
    def generateNPC(self):
        if self.movement == "north":
            self.talker = "Greg the Chaos Marauder"
            self.loot = 100
        elif self.movement == "south":
            self.talker = "Jack the Slaver"
            self.loot = 150
        elif self.movement == "west":
            self.talker = "Buggy the Pirate"
            self.loot = 125
        else:
            self.talker = "Nin the Ninja"
            self.loot = 125

class Combat(Scenario):
    # initialise with inheritance from Scenario class
    def __init__(self, playerHealth, characterName, combatMode, listEnemy):
        super().__init__(playerHealth, characterName, combatMode)
        self.user = characterName
        self.listEnemies = [listEnemy]
        self.aliveEnemies = len(self.listEnemies[0])
        self.scoreNumEnemies = len(self.listEnemies[0])
        self.scoreEnemyType = self.listEnemies[0][0][0]

    # accessor method to get aliveEnemies for Score class
    def getAliveEnemies(self):
        return self.aliveEnemies

    # accessor method to get scoreNumEnemies for Score class
    def getScoreNumEnemies(self):
        return self.scoreNumEnemies

    # accessor method to get scoreEnemyType for Score class
    def getScoreEnemyType(self):
        return self.scoreEnemyType

    # accessor method to get aliveEnemies for printing
    def getEnemy(self):
        print(self.aliveEnemies)
        for x in range(0, self.aliveEnemies):
            print(f"Enemy: {self.listEnemies[0][x][0]} Health: {self.listEnemies[0][x][1]}\n")

    # function to attack enemies/ mutator method
    def attack(self):
        enemyCounter = self.aliveEnemies
        while True:
            target = input("Who to attack? (Choose number)\n")
            target = int(target) - 1
            try:
                if self.listEnemies[0][target][1] > 0:
                    self.listEnemies[0][int(target)][1] = self.listEnemies[0][int(target)][1] - 20
                    print(f"{self.listEnemies[0][target][0]}'s health has dropped to {self.listEnemies[0][target][1]}!")
                    break
                else:
                    print(f"{self.listEnemies[0][target][0]} is already dead!")
            except:
                print("Incorrect target has been chosen")

        # check if the target is dead
        if self.listEnemies[0][target][1] <= 0:
            print(f"{self.listEnemies[0][target][0]} has died!")

        # check if all enemies are dead
        for x in range(0, self.aliveEnemies):
            if self.listEnemies[0][x][1] <= 0:
                enemyCounter = enemyCounter - 1
                if enemyCounter == 0:
                    print("All enemies has been slayed!")
                    self.aliveEnemies = 0

    # function for the all of the enemies to attack the player/ mutator method
    def enemyAttack(self):
        for x in range(0, len(self.listEnemies[0])):
            if self.listEnemies[0][x][1] > 0:
                self.playerHealth = self.playerHealth - 10
                print(f"{self.listEnemies[0][x][0]} has attacked {self.user}")
                print(f"{self.user}'s health has dropped to {self.playerHealth}!")
        # check if the player runs out of health, exit program if true
        if self.playerHealth <= 0:
            print(f"{self.user} has died!")
            exit()

    # override string method to show the status of the player
    def __str__(self):
        return f"Hero:{self.user}, Health:{self.playerHealth}"

class Dialog(Scenario):
    # initialise with inheritance from Scenario class
    def __init__(self, movement, NPC, characterName):
        super().__init__(movement, NPC, characterName)
        self.user = characterName
        self.location = movement
        self.talker = NPC

    # function to print out statements depending on who the NPC is
    def npcDialog(self):
        if self.talker == "Greg the Chaos Marauder":
            print(f"{self.talker}: Hello there {self.user}, you wish to die?")
        elif self.talker == "Jack the Slaver":
            print(f"{self.talker}: You look like you will fetch a good price...")
        elif self.talker == "Buggy the Pirate":
            print(f"{self.talker}: Give me your money or your life!")
        else:
            print(f"{self.talker}: ...")

class Score:
    # Implementing the 1:0..M aggregation relationship between Combat and Score
    def __init__(self, aE, sNE, sET):
        self.aliveEnemies = aE
        self.scoreNumEnemies = sNE
        self.scoreEnemyType = sET
        self.combats = [self.aliveEnemies, self.scoreNumEnemies, self.scoreEnemyType]

    # function to add more data to the combats list/mutator method
    def addCombat(self, alive, scoreNum, scoreType):
        self.combats.append(alive)
        self.combats.append(scoreNum)
        self.combats.append(scoreType)

    # function calculate the total score/ mutator method
    def calculateScore(self):
        combatCount = len(self.combats)
        print(self.combats)
        # checking if there is only 1 object inserted in list
        if combatCount == 3:
            dead = self.combats[1] - self.combats[0]
            print(f"Dead: {dead}")
            score = dead * 10
            if self.combats[2] == "Chaos Marauder1":
                score = score * 8
            elif self.combats[2] == "Slaver1":
                score = score * 2
            elif self.combats[2] == "Pirate1":
                score = score * 4
            elif self.combats[2] == "Ninja1":
                score = score * 6
            return score
        # checking if there is 2 objects in the list
        elif combatCount == 6:
            dead1 = self.combats[1] - self.combats[0]
            dead2 = self.combats[4] - self.combats[3]
            score = dead1 + dead2 * 10
            if self.combats[2] == "Chaos Marauder1":
                score = score * 8
            elif self.combats[2] == "Slaver1":
                score = score * 2
            elif self.combats[2] == "Pirate1":
                score = score * 4
            elif self.combats[2] == "Ninja1":
                score = score * 6

            if self.combats[5] == "Chaos Marauder1":
                score = score * 8
            elif self.combats[5] == "Slaver1":
                score = score * 2
            elif self.combats[5] == "Pirate1":
                score = score * 4
            elif self.combats[5] == "Ninja1":
                score = score * 6
            return score

class Action:
    def __init__(self, scenario):
        # Implementing the 1:1 aggregation relationship between Scenario and Action classes
        self.Scenario = scenario
        self.score = 0

    # function to steal loot from NPC/ mutator method
    def steal(self):
        while True:
            if self.Scenario.talker == "Greg the Chaos Marauder":
                attemptSteal = random.randint(0, 1)
            elif self.Scenario.talker == "Jack the Slaver":
                attemptSteal = random.randint(0, 2)
            elif self.Scenario.talker == "Buggy the Pirate":
                attemptSteal = random.randint(0, 3)
            else:
                attemptSteal = random.randint(0, 4)
            # if it is 0, then the program will shutdown
            if attemptSteal == 0:
                print(f"{self.Scenario.talker} has caught {self.Scenario.characterName} trying to steal!")
                print("Game over")
                break
            else:
                self.score = self.score + self.Scenario.loot
                print(f"{self.Scenario.characterName} has successfully stolen from {self.Scenario.talker}!")
            print(f"Stolen amount of goods {self.score}")
        exit()


game1 = Game(None, None)    # creates game1 object
# run functions from Game class
game1.addName()
game1.menuSelect()

comScenario = Scenario(game1.combatMode, game1.characterName, 0)    # creates comScenario1 object
# run functions from Scenario class
comScenario.startScenario()
comScenario.moveScenario()
comScenario.generateNumEnemy()

# checks if this is combat only
if comScenario.combatMode == 1:
    playerCombat = Combat(comScenario.playerHealth, comScenario.characterName, comScenario.combatMode, comScenario.listEnemy)   # creates playerCombat object
    # continue to loop if there is at least 1 enemies alive
    while playerCombat.aliveEnemies > 0:
        # run functions from Combat class
        playerCombat.getEnemy()
        playerCombat.attack()
        playerCombat.enemyAttack()
        print(playerCombat)     # print the overridden string to show player name and current health
    scoring = Score(playerCombat.getAliveEnemies(), playerCombat.getScoreNumEnemies(), playerCombat.getScoreEnemyType())
    print(f"Total score: {scoring.calculateScore()}")

    print("Congratulations! Do you wish to have another adventure?")
    choice = input("1 for yes or 2 for no\n")
    if choice == "1":
        comScenario2 = Scenario(game1.combatMode, game1.characterName, 0)       # creates comScenario2 object
        # run functions from Scenario class
        comScenario2.moveScenario()
        comScenario2.generateNumEnemy()

        if comScenario2.combatMode == 1:
            playerCombat2 = Combat(comScenario2.playerHealth, comScenario2.characterName, comScenario2.combatMode,
                                   comScenario2.listEnemy)      # creates playerCombat2 object
            # continue to loop if there is at least 1 enemies alive
            while playerCombat2.aliveEnemies > 0:
                # run functions from Combat class
                playerCombat2.getEnemy()
                playerCombat2.attack()
                playerCombat2.enemyAttack()
                print(playerCombat2)
        scoring.addCombat(playerCombat2.getAliveEnemies(), playerCombat2.getScoreNumEnemies(),
                          playerCombat2.getScoreEnemyType())    # run function to add more score data to already existing list
        print(f"Total score: {scoring.calculateScore()}")

# checks if this is dialog only
elif comScenario.combatMode == 0:
    print("Do you wish to steal from them or just talk to them?")
    choice = input("1 for stealing or press any other key for talking\n")
    if choice == "1":
        comScenario.generateNPC()               # run function to create NPC depending on location
        playerAction = Action(comScenario)      # create playerAction object
        print(f"{playerAction.Scenario.talker} is the target for theft")
        playerAction.steal()                    # run function to attempt thievery
    else:
        comScenario.generateNPC()               # run function to create NPC depending on location
        playerDialog = Dialog(comScenario.movement, comScenario.talker, comScenario.characterName)  # create playerDialog object
        playerDialog.npcDialog()                # run function to print out dialog