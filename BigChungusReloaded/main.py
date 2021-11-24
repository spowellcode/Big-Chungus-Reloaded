#Sam Powell 11/21/2021


import pygame

pygame.init() #initalizes the pygame library
pygame.display.set_caption('Big Chungus Reloaded')

screen = pygame.display.set_mode((800, 600)) #Window size

PlayerMapLocationX = 0 #X location of player on map
PlayerMapLocationY = 0 #Y location of player on map

mapgenerateCurrentXPos = 0
mapgenerateCurrentYPos = 0

maprowcount = 0
mapcolumnscount = 0

gametilesize = 125 #Pixel width and height of tile

StepIncrements = 1 #How many pixels the player moves

tilearray = [] #List where tiles are stored

SpriteFacingRight = 1  # 1 the sprite is facing left. 0 the sprite is facing right

keyflag = 0

blockflagN = 0
blockflagS = 0
blockflagW = 0
blockflagE = 0

class Sprite: #Sprite class

    playerX = 300 #X corodinates of where the player is drawn on screen
    playerY = 200 #Y corodinates of where the player is drawn on screen

    def player(self): #Class function to draw player on screen

        if SpriteFacingRight == 0:
            spriteimg = pygame.image.load('chungusright.png')
            self.spriteimg = pygame.transform.scale(spriteimg, (125, 230))
        if SpriteFacingRight == 1:
            spriteimg = pygame.image.load('chungusleft.png')
            self.spriteimg = pygame.transform.scale(spriteimg, (125, 230))

        screen.blit(self.spriteimg, (self.playerX, self.playerY)) #Actual draw function


class grasstile:
    block = 0
    tileposX = 0
    tileposY = 0
    tileimg = pygame.image.load('grasstile.png')
    tileimg = pygame.transform.scale(tileimg, (gametilesize, gametilesize))

    def drawtile(self):
        screen.blit(self.tileimg, (self.tileposX + PlayerMapLocationX, self.tileposY + PlayerMapLocationY))


class rocktile:
    block = 1
    tileimg = pygame.image.load('rocktile.png')
    tileimg = pygame.transform.scale(tileimg, (gametilesize, gametilesize))
    def drawtile(self):
        self.tileposX
        self.tileposY
        screen.blit(self.tileimg, (self.tileposX + PlayerMapLocationX, self.tileposY + PlayerMapLocationY))

class projectile:
    projectileimg = pygame.image.load('pepsileft.png')
    projectileimg = pygame.transform.scale(projectileimg, (458, 249))
    def fire(self):
        speed = 5
        screen.blit(self.projectileimg, (PlayerMapLocationX, PlayerMapLocationY))

p1 = Sprite() #Sprite object

#Map - each row of map is a list
row1 = [rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile()]
row2 = [rocktile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), rocktile()]
row3 = [rocktile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), rocktile()]
row4 = [rocktile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), rocktile()]
row5 = [rocktile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), rocktile()]
row6 = [rocktile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), rocktile()]
row7 = [rocktile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), rocktile()]
row8 = [rocktile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), rocktile()]
row9 = [rocktile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), rocktile()]
row10 = [rocktile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), rocktile()]
row11 = [rocktile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), rocktile()]
row12 = [rocktile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), rocktile()]
row13 = [rocktile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), rocktile()]
row14 = [rocktile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), rocktile()]
row15 = [rocktile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), rocktile()]
row16 = [rocktile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), rocktile()]
row17 = [rocktile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), rocktile()]
row18 = [rocktile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), rocktile()]
row19 = [rocktile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), grasstile(), rocktile()]
row20 = [rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile(),rocktile()]



running = True
while running:

    screen.fill((0, 0, 0)) #Sets window to black (RGB)

    # Exit code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left key pressed")
                SpriteFacingRight = 0 #Changes which way the sprite is facing
                keyflag = 1 # Sets a flag so you can hold down a key. Game would crash if there was a loop here.
            if event.key == pygame.K_RIGHT:
                SpriteFacingRight = 1  #Changes which way the sprite is facing
                print("Right key pressed")
                keyflag = 2 # Sets a flag so you can hold down a key. Game would crash if there was a loop here.
            if event.key == pygame.K_UP:
                print("Up key pressed")
                keyflag = 3 # Sets a flag so you can hold down a key. Game would crash if there was a loop here.
            if event.key == pygame.K_DOWN:
                print("Down key pressed")
                keyflag = 4 # Sets a flag so you can hold down a key. Game would crash if there was a loop here.

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                print("Right key is released")
                keyflag = 0 # Deactivates keyflag when key is released. This is so the sprite stops moving
            if event.key == pygame.K_LEFT:
                print("Left key is released")
                keyflag = 0 # Deactivates keyflag when key is released. This is so the sprite stops moving
            if event.key == pygame.K_UP:
                print("Up key is released")
                keyflag = 0 # Deactivates keyflag when key is released. This is so the sprite stops moving
            if event.key == pygame.K_DOWN:
                print("Down key is released")
                keyflag = 0 # Deactivates keyflag when key is released. This is so the sprite stops moving

    for x in range(len(row1)):
        row1[x].tileposX = mapgenerateCurrentXPos
        if row1[x].tileposX > 300 and row1[x].tileposX < 500:
            blockflag = 1
        else:
            blockflag = 0
        row1[x].tileposY = 0
        row1[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row2)):
        row2[x].tileposX = mapgenerateCurrentXPos
        row2[x].tileposY = 125
        row2[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row3)):
        row3[x].tileposX = mapgenerateCurrentXPos
        row3[x].tileposY = 125*2
        row3[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row4)):
        row4[x].tileposX = mapgenerateCurrentXPos
        row4[x].tileposY = 125*3
        row4[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row5)):
        row5[x].tileposX = mapgenerateCurrentXPos
        row5[x].tileposY = 125*4
        row5[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row6)):
        row6[x].tileposX = mapgenerateCurrentXPos
        row6[x].tileposY = 125*5
        row6[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row7)):
        row7[x].tileposX = mapgenerateCurrentXPos
        row7[x].tileposY = 125*6
        row7[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row8)):
        row8[x].tileposX = mapgenerateCurrentXPos
        row8[x].tileposY = 125*7
        row8[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row9)):
        row9[x].tileposX = mapgenerateCurrentXPos
        row9[x].tileposY = 125*8
        row9[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row10)):
        row10[x].tileposX = mapgenerateCurrentXPos
        row10[x].tileposY = 125*9
        row10[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row11)):
        row11[x].tileposX = mapgenerateCurrentXPos
        row11[x].tileposY = 125*10
        row11[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row12)):
        row12[x].tileposX = mapgenerateCurrentXPos
        row12[x].tileposY = 125*11
        row12[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row13)):
        row13[x].tileposX = mapgenerateCurrentXPos
        row13[x].tileposY = 125*12
        row13[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row14)):
        row14[x].tileposX = mapgenerateCurrentXPos
        row14[x].tileposY = 125*13
        row14[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row15)):
        row15[x].tileposX = mapgenerateCurrentXPos
        row15[x].tileposY = 125*14
        row15[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row16)):
        row16[x].tileposX = mapgenerateCurrentXPos
        row16[x].tileposY = 125*15
        row16[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row17)):
        row17[x].tileposX = mapgenerateCurrentXPos
        row17[x].tileposY = 125*16
        row17[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row18)):
        row18[x].tileposX = mapgenerateCurrentXPos
        row18[x].tileposY = 125*17
        row18[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row19)):
        row19[x].tileposX = mapgenerateCurrentXPos
        row19[x].tileposY = 125*18
        row19[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    for x in range(len(row20)):
        row20[x].tileposX = mapgenerateCurrentXPos
        row20[x].tileposY = 125*19
        row20[x].drawtile()
        mapgenerateCurrentXPos = mapgenerateCurrentXPos + gametilesize
    mapgenerateCurrentXPos = 0

    if PlayerMapLocationX > 175:
        blockflagN = 1
    else:
        blockflagN = 0

    if PlayerMapLocationX < -1955:
        blockflagS = 1
    else:
        blockflagS = 0

    if PlayerMapLocationY > 200:
        blockflagE = 1
    else:
        blockflagE = 0

    if PlayerMapLocationY < -1978:
        blockflagW = 1
    else:
        blockflagW = 0

    if keyflag == 1 and blockflagN != 1:
        PlayerMapLocationX = PlayerMapLocationX + StepIncrements
    if keyflag == 2 and blockflagS != 1:
        PlayerMapLocationX = PlayerMapLocationX - StepIncrements
    if keyflag == 3 and blockflagE != 1:
        PlayerMapLocationY = PlayerMapLocationY + StepIncrements
    if keyflag == 4 and blockflagW != 1:
        PlayerMapLocationY = PlayerMapLocationY - StepIncrements

    p1.player()
    pygame.display.update()
