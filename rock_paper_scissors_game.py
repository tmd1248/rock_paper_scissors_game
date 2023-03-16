import pygame;
from pygame.locals import *
# global variables used in a couple of functions 
fstam = 12
tstam = 12
kstam = 8

#This might end up geting depreciated. I only need to update it all at once at the start of the game
def set_status(player_data, player_class, health, stamina, poisoned, stunned): 
    player_data["Class"] = player_class
    player_data["Health"] = health 
    player_data["Stamina"] = stamina
    player_data["Poisoned"] = poisoned
    player_data["Stunned"] = stunned
#This function is intended to calculate damage based upon player offense and defense. 
def gameCalculations(p1data, p2data, p1offense, p2offense, p1defense, p2defense):
    #If someone is stunned they can't take a turn. could technically lead to taking a match hostage, but it doesn't do any damage so it's 
    #also kind of pointless. descriptions for each attack and defense are down in the main gameplay loop
    if p1data["Stunned"] == False:
        #match case based on offense and defense 
        match p1offense:
            case 1:
                if p2defense == 7 and p1data["Stamina"] >= 2:
                    p2data["Health"] = p2data["Health"] - 2
                    p1data["Stamina"] = p1data["Stamina"] - 2
                elif p2defense == 8 and p1data["Stamina"] >= 2:
                    p2data["Health"] = p2data["Health"] - 4
                    p1data["Stamina"] = p1data["Stamina"] - 2
            case 2:
                if p2defense == 7 and p1data["Stamina"] >= 3:
                    p2data["Health"] = p2data["Health"] - 2
                    p1data["Stamina"] = p1data["Stamina"] - 3
                elif p2defense == 9 and p1data["Stamina"] >= 3:
                    p2data["Health"] = p2data["Health"] - 6
                    p1data["Stamina"] = p1data["Stamina"] - 3
                elif p1data["Stamina"] >= 3: 
                    p2data["Health"] = p2data["Health"] - 4
                    p1data["Stamina"] = p1data["Stamina"] - 3
            case 3:
                #would like to use a nested match statement here, but it doesn't like that so we're doing if/else instead
                if p1data["Class"] == "Fighter":
                    if p2defense != 8 and p1data["Stamina"] >= 2:
                        p2data["Health"] = p2data["Health"] - 6
                        p1data["Stamina"] = p1data["Stamina"] - 2
                    #not working. don't know why 
                elif p1data["Class"] == "Thief":
                    if p2defense != 8 and p1data["Stamina"] >= 4:
                         p2data["Poisoned"] == True  
                         p1data["Stamina"] = p1data["Stamina"] - 4 
                #not working, don't know why
                else: 
                    if p2defense != 8 and p1data["Stamina"] >= 1:
                        p2data["Stunned"] == True
                        p1data["Stamina"] = p1data["Stamina"] - 1
            case 4:
                if p1data["Class"] == "Fighter":
                    p1data["Stamina"] = fstam
                elif p1data["Class"] == "Thief":
                    p1data["Stamina"] = tstam   
                else: 
                    p1data["Stamina"] = kstam
    #Identical to the p1 values 
    if p2data["Stunned"] == False:
        match p2offense:
            case 1:
                if p1defense == 7 and p2data["Stamina"] >= 2:
                    p1data["Health"] = p1data["Health"] - 2
                    p2data["Stamina"] = p2data["Stamina"] - 2
                elif p1defense == 8 and p2data["Stamina"] >= 2:
                    p1data["Health"] = p1data["Health"] - 4
                    p2data["Stamina"] = p2data["Stamina"] - 2
            case 2:
                if p1defense == 7 and p2data["Stamina"] >= 3:
                    p1data["Health"] = p1data["Health"] - 2
                    p2data["Stamina"] = p2data["Stamina"] - 3
                elif p1defense == 9 and p2data["Stamina"] >= 3:
                    p1data["Health"] = p1data["Health"] - 6
                    p2data["Stamina"] = p2data["Stamina"] - 3
                elif p2data["Stamina"] >= 3: 
                    p1data["Health"] = p1data["Health"] - 4
                    p2data["Stamina"] = p2data["Stamina"] - 3
            case 3:
                if p2data["Class"] == "Fighter":
                    if p1defense != 8 and p2data["Stamina"] > 2:
                        p1data["Health"] = p1data["Health"] - 6
                        p2data["Stamina"] = p2data["Stamina"] - 2
                elif p2data["Class"] == "Thief":
                    if p1defense != 8:
                         p1data["Poisoned"] == True  
                         p2data["Stamina"] = p2data["Stamina"] - 4 
                else: 
                    if p1defense != 8 and p2data["Stamina"] > 1:
                        p1data["Stunned"] == True
                        p2data["Stamina"] = p2data["Stamina"] - 1
            case 4:
                if p2data["Class"] == "Fighter":
                    p2data["Stamina"] = fstam
                elif p2data["Class"] == "Thief":
                    p2data["Stamina"] = tstam   
                else: 
                    p2data["Stamina"] = kstam
    #finally, this adds some ongoing status effect checks to make sure that stun wears off properly and poison damage is accounted for 
    #Known issue. Poison and stun do not currently work
    if p1data["Poisoned"] == True:
        p1data["Health"] = p1data["Health"] - 2
    if p2data["Poisoned"] == True:
        p2data["Health"] = p2data["Health"] - 2
    if p1data["Stunned"] == True and p2offense != 8:
        p1data["Stunned"] = False
    if p2data["Stunned"] == True and p1offense != 8:
        p2data["Stunned"] = False    
    



def main():
    #lots of variables initialized up here for use later
    pygame.init()
    size = width, height = 1200, 1000
    running = True
    #pygame screen and font established here 
    screen = pygame.display.set_mode(size)
    font = pygame.font.SysFont(None, 24)
    #pygame color library
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    p1label = font.render('Player 1', True, RED)
    p2label = font.render('Player 2', True, RED)
    fimage = pygame.image.load("Fighter.png")
    timage = pygame.image.load("Thief.png")
    kimage = pygame.image.load("Knight.png")
    bgroundfight = pygame.image.load("Fight!.png")
    bgroundwin = pygame.image.load("Victory.png")
    #empty variables for when a class is chosen 
    p1classlabel = ""
    p2classlabel = ""
    #gameplay instructions are stored here 
    gstartlabel = font.render('Choose your class, 1 for fighter, 2 for Thief, 3 for Knight', True, RED)
    fighterlabel = font.render('Fighter: HP 10, SP 12. a good all-arounder', True, RED)
    thieflabel = font.render('Thief: HP 8, SP 12. Can poison foes.', True, RED)
    knightlabel = font.render('Knight: HP 12, SP 8. Can stun foes', True, RED)
    strikelabel = font.render('1: Strike. Anticipate a dodge. 2 SP for 4 HP', True, BLUE)
    ripostelabel = font.render('2: Riposte. Anticipate a parry. 3 SP for 4 HP, 6 if parry', True, BLUE)
    fspeciallabel = font.render('3: Fighter special move, breaks a block. 2 SP for 6 HP', True, YELLOW)
    tspeciallabel = font.render('3: Thief special move. poisons foe to take 2 HP per turn, 4 SP', True, GREEN)
    kspeciallabel = font.render('3: Knight special move. Stuns an opponent next turn', True, WHITE)
    waitlabel = font.render("4: Do not attack, regenerating all SP", True, BLUE)
    blocklabel = font.render("7: Block a Strike or Riposte, reduce damage by half", True, BLUE)
    dodgelabel = font.render("8: Dodge a special move, negating it", True, BLUE)
    parrylabel = font.render("9: Parry a Strike, negating all damage", True, BLUE)
    #location of player 1 and 2 on the screen 
    p1position = (20, 20)
    p2position = (500, 20)
    while running:
        #tracker variables for game progression
        p1chose = False
        p2chose = False
        #player data dictionaries 
        p1data = dict()
        p2data = dict()
        #game size 

        #another tracker variable 
        game_ongoing = True
        #game instructions are written to the screen here 
        screen.fill(BLACK)
        screen.blit(p1label, p1position)
        screen.blit(p2label, p2position)
        screen.blit(gstartlabel, (100, 70))
        screen.blit(fighterlabel, (20, 120))
        screen.blit(thieflabel, (20, 150))
        screen.blit(knightlabel, (20, 180))
        screen.blit(bgroundfight, (50, 300))
        pygame.display.update()
        #main gameplay loop begins

        #have player 1 choose a class 
        while p1chose == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    p1chose = True
                    p2chose = True
                elif event.type == KEYDOWN:
                    if event.key == K_1:
                        set_status(p1data, "Fighter", 10, fstam, False, False)
                        p1class = fimage
                        p1chose = True
                    elif event.key == K_2:
                        set_status(p1data, "Thief", 8, tstam, False, False)
                        p1class = timage
                        p1chose = True
                    elif event.key == K_3:
                        set_status(p1data, "Knight", 12, kstam, False, False)
                        p1class = kimage
                        p1chose = True
            if "Class" in p1data:
                p1classlabel = font.render(p1data["Class"], True, RED)
                screen.blit(p1classlabel, (20, 48))
                screen.blit(p1class, (220, 320))
            pygame.display.update()
        #same for player 2 
        while p2chose == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    p2chose = True
                elif event.type == KEYDOWN:
                    if event.key == K_1:
                        set_status(p2data, "Fighter", 10, fstam, False, False)
                        p2class = fimage
                        p2chose = True
                    elif event.key == K_2:
                        set_status(p2data, "Thief", 8, tstam, False, False)
                        p2class = timage
                        p2chose = True
                    elif event.key == K_3:
                        set_status(p2data, "Knight", 12, kstam, False, False)
                        p2class = kimage
                        p2chose = True
            if "Class" in p2data:
                p2classlabel = font.render(p2data["Class"], True, RED)
                screen.blit(p2classlabel, (500, 48))
                screen.blit(p2class, (650, 320))
            pygame.display.update()
        #make sure nothing executes if the button to close the window has been clicked 
        if running == False:
            break
        #problems start here. The game sometimes won't close on its own, and never initiates the actual calculations 
        while game_ongoing == True:
            #should end the loop whenever someone reaches zero health, haven't actually made it that far 
            if p1data["Health"] <= 0 or p2data["Health"] <= 0:
                break
            #establishing variables to be used later
            p1offense = 0
            p2offense = 0
            p1defense = 0
            p2defense = 0
            p1choseoffense = False
            p2choseoffense = False
            p1chosedefense = False
            p2chosedefense = False
            p1stats = font.render(str(p1data["Health"]) + "HP / " + str(p1data["Stamina"]) + "SP / " + "Poisoned " + str(p1data["Poisoned"]) + " / Stunned " + str(p1data["Stunned"]), True, RED)
            p2stats = font.render(str(p2data["Health"]) + "HP / " + str(p2data["Stamina"]) + "SP / " + "Poisoned " + str(p2data["Poisoned"]) + " / Stunned " + str(p2data["Stunned"]), True, RED)
            #start each loop by making sure only relevant things are on the screen 
            screen.fill(BLACK)
            screen.blit(p1stats, (20, 65))
            screen.blit(p2stats, (500, 65))
            screen.blit(p1label, p1position)
            screen.blit(p2label, p2position)
            p1instructions = font.render("Player 1: Choose an offensive and defensive tactic", True, RED)
            screen.blit(p1instructions, (200, 900))
            screen.blit(p1classlabel, (20, 48))
            screen.blit(p2classlabel, (500, 48))
            screen.blit(strikelabel, (20, 90))
            screen.blit(ripostelabel, (20, 120))
            screen.blit(bgroundfight, (50, 300))
            screen.blit(p1class, (220, 320))
            screen.blit(p2class, (650, 320))
            #checks player classes and only provides relevant information 
            if p1data["Class"] == "Fighter" or p2data["Class"] == "Fighter":
                screen.blit(fspeciallabel,(20, 150))
            if p1data["Class"] == "Thief" or p2data["Class"] == "Thief":
                screen.blit(tspeciallabel,(20, 180))
            if p1data["Class"] == "Knight" or p2data["Class"] == "Knight":
                screen.blit(kspeciallabel,(20, 210))
            screen.blit(waitlabel, (20, 240))
            screen.blit(blocklabel, (500, 90))
            screen.blit(parrylabel, (500, 120))
            screen.blit(dodgelabel, (500, 150))
            pygame.display.update()
            #make sure each loop that p1 has to choose again
            p1chose = False
            #p1 should need to go through this loop twice, once to pick an offensive option, once to pick a defensive option 
            while p1chose == False:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            game_ongoing = False
                            p1chose = True
                        elif event.type == KEYDOWN:
                            if event.key == K_1:
                                p1offense = 1
                                p1choseoffense = True
                            elif event.key == K_2:
                                p1offense = 2
                                p1choseoffense = True
                            elif event.key == K_3:
                                p1offense = 3
                                p1choseoffense = True
                            elif event.key == K_4:
                                p1offense = 4
                                p1choseoffense = True
                            elif event.key == K_7:
                                p1defense = 7
                                p1chosedefense = True
                            elif event.key == K_8:
                                p1defense = 8
                                p1chosedefense = True
                            elif event.key == K_9:
                                p1defense = 9
                                p1chosedefense = True
                            #should be a new if statement, disregarding what's above 
                if p1choseoffense == True and p1chosedefense == True:
                    break
            #get out of the loop if the x has been clicked 
            if game_ongoing == False:
                break
            #should be identical to the code above 
            p2chose = False 
            screen.fill(BLACK)
            screen.blit(p1stats, (20, 65))
            screen.blit(p2stats, (500, 65))
            screen.blit(p1label, p1position)
            screen.blit(p2label, p2position)
            p2instructions = font.render("Player 2: Choose an offensive and defensive tactic", True, RED)
            screen.blit(p2instructions, (200, 900))
            screen.blit(p1classlabel, (20, 48))
            screen.blit(p2classlabel, (500, 48))
            screen.blit(bgroundfight, (50, 300))
            screen.blit(p1class, (220, 320))
            screen.blit(p2class, (650, 320))
            screen.blit(strikelabel, (20, 90))
            screen.blit(ripostelabel, (20, 120))
            #checks player classes and only provides relevant information 
            if p1data["Class"] == "Fighter" or p2data["Class"] == "Fighter":
                screen.blit(fspeciallabel,(20, 150))
            if p1data["Class"] == "Thief" or p2data["Class"] == "Thief":
                screen.blit(tspeciallabel,(20, 180))
            if p1data["Class"] == "Knight" or p2data["Class"] == "Knight":
                screen.blit(kspeciallabel,(20, 210))
            screen.blit(waitlabel, (20, 240))
            screen.blit(blocklabel, (500, 90))
            screen.blit(parrylabel, (500, 120))
            screen.blit(dodgelabel, (500, 150))
            pygame.display.update()
            while p2chose == False:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            game_ongoing = False
                            p1chose = True
                            p2chose = True
                        elif event.type == KEYDOWN:
                            if event.key == K_1:
                                p2offense = 1
                                p2choseoffense = True
                            elif event.key == K_2:
                                p2offense = 2
                                p2choseoffense = True
                            elif event.key == K_3:
                                p2offense = 3
                                p2choseoffense = True
                            elif event.key == K_4:
                                p2offense = 4
                                p2choseoffense = True
                            elif event.key == K_7:
                                p2defense = 7
                                p2chosedefense = True
                            elif event.key == K_8:
                                p2defense = 8
                                p2chosedefense = True
                            elif event.key == K_9:
                                p2defense = 9
                                p2chosedefense = True
                if p2choseoffense == True and p2chosedefense == True:
                    break
            #if we get out of these calculations it should update the dictionaries with new information
            gameCalculations(p1data, p2data, p1offense, p2offense, p1defense, p2defense)
        screen.fill(BLACK)
        game_ongoing = False
        congratulations = None
        screen.blit(bgroundwin, (50, 300))
        if p1data["Health"] <= 0: 
            congratulations = font.render("Well done, Player 2", True, RED)
            screen.blit(p1class, (400, 360))
        elif p2data["Health"] <= 0:
            congratulations = font.render("Well done, Player 1", True, RED)
            screen.blit(p2class, (400, 360))
        if congratulations is not None:
            screen.blit(congratulations, (20, 20))
            instructions = font.render("Press 1 for a new game", True, RED)
            screen.blit (instructions, (500, 20))
        else: 
            break
        pygame.display.update()
        newgame = False
        while newgame == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(newgame)
                    running = False
                    newgame = True
                elif event.type == KEYDOWN:
                    if event.key == K_1:
                        newgame = True
    pygame.quit()

        

main()

