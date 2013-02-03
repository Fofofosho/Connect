import math, sys, pygame
pygame.init()

class GridSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, BACKGROUND_COLOR, squareSize, state):
        pygame.sprite.Sprite.__init__(self)
        self.stateList = ["empty", "full", "start_node", "end_node", "wall", "portal1", "portal2", "item", "laser", "laserTurret", "laservert", "potionlaser", "potionlaservert"]
        
        self.BACKGROUND_COLOR = BACKGROUND_COLOR
        self.GRID_THICKNESS = 1
        self.GRID_COLOR = (255, 255, 255)
        self.circleSize = squareSize[0] / 2, squareSize[1] / 2
        self.squareSize = squareSize
        
        self.state = self.stateList[state]
        self.laserOn = False
        
        self.image = pygame.Surface((squareSize[0], squareSize[1]))
        self.image.convert
        self.image.fill(self.BACKGROUND_COLOR)
        self.rect = self.image.get_rect()
        self.rect.centerx = x + (squareSize[0] / 2)
        self.rect.centery = y + (squareSize[1] / 2)
        
        #Draw the borders
        pygame.draw.line(self.image, self.GRID_COLOR, (0, 0), (squareSize[0]-1, 0), self.GRID_THICKNESS)
        pygame.draw.line(self.image, self.GRID_COLOR, (0, 0), (0, squareSize[1]-1), self.GRID_THICKNESS)
        pygame.draw.line(self.image, self.GRID_COLOR, (squareSize[0]-1, 0), (squareSize[0]-1, squareSize[1]-1), self.GRID_THICKNESS)
        pygame.draw.line(self.image, self.GRID_COLOR, (0, squareSize[1]-1), (squareSize[0]-1, squareSize[1]-1), self.GRID_THICKNESS)
        
    def initialize(self):
        if (self.state == "start_node"):
            pygame.draw.circle(self.image, (232, 118, 0), (self.circleSize[0], self.circleSize[1]), self.circleSize[0]/2)
        elif (self.state == "end_node"):    
            pygame.draw.circle(self.image, (137, 207, 240), (self.circleSize[0], self.circleSize[1]), self.circleSize[0]/2)
        elif (self.state == "wall"):
            self.image.fill((255, 255, 255))
        elif (self.state == "portal1" or self.state == "portal2"):
            pygame.draw.circle(self.image, (234, 2, 40), (self.circleSize[0], self.circleSize[1]), self.circleSize[0]/2, 1)
        elif (self.state == "item" or self.state == "potionlaser" or self.state == "potionlaservert"):
            IMAGE_DIMENSIONS = (32, 36)
            self.picture = pygame.Surface(IMAGE_DIMENSIONS)
            self.pictureImage = pygame.image.load("Graphics/potion.png")
            self.picture.blit(self.pictureImage, (0, 0))
            self.picture = pygame.transform.scale(self.picture, (self.squareSize[0] / 2, self.squareSize[1] / 2))
            self.image.blit(self.picture, (self.squareSize[0] / 2 - self.picture.get_width() / 2, self.squareSize[1] / 2 - self.picture.get_height() / 2))
        elif (self.state == "laserTurret"):
            IMAGE_DIMENSIONS = (32, 32)
            self.picture = pygame.Surface(IMAGE_DIMENSIONS)
            self.pictureImage = pygame.image.load("Graphics/laserTurret.png")
            self.picture.blit(self.pictureImage, (0, 0))
            self.picture = pygame.transform.scale(self.picture, (self.squareSize[0] / 2, self.squareSize[1] / 2))
            self.image.blit(self.picture, (self.squareSize[0] / 2 - self.picture.get_width() / 2, self.squareSize[1] / 2 - self.picture.get_height() / 2))
            
    def shootLazer(self):
        if (self.laserOn):
            self.image.fill(self.BACKGROUND_COLOR)
            pygame.draw.line(self.image, self.GRID_COLOR, (0, 0), (self.squareSize[0]-1, 0), self.GRID_THICKNESS)
            pygame.draw.line(self.image, self.GRID_COLOR, (0, 0), (0, self.squareSize[1]-1), self.GRID_THICKNESS)
            pygame.draw.line(self.image, self.GRID_COLOR, (self.squareSize[0]-1, 0), (self.squareSize[0]-1, self.squareSize[1]-1), self.GRID_THICKNESS)
            pygame.draw.line(self.image, self.GRID_COLOR, (0, self.squareSize[1]-1), (self.squareSize[0]-1, self.squareSize[1]-1), self.GRID_THICKNESS)
            if (self.state == "potionlaser" or self.state == "potionlaservert"):
                IMAGE_DIMENSIONS = (32, 36)
                self.picture = pygame.Surface(IMAGE_DIMENSIONS)
                self.pictureImage = pygame.image.load("Graphics/potion.png")
                self.picture.blit(self.pictureImage, (0, 0))
                self.picture = pygame.transform.scale(self.picture, (self.squareSize[0] / 2, self.squareSize[1] / 2))
                self.image.blit(self.picture, (self.squareSize[0] / 2 - self.picture.get_width() / 2, self.squareSize[1] / 2 - self.picture.get_height() / 2))
            self.laserOn = False
        elif (self.state == "potionlaser" or self.state == "potionlaservert"):
            self.image = pygame.Surface((self.squareSize[0], self.squareSize[1]))
            pygame.draw.line(self.image, self.GRID_COLOR, (0, 0), (self.squareSize[0]-1, 0), self.GRID_THICKNESS)
            pygame.draw.line(self.image, self.GRID_COLOR, (0, 0), (0, self.squareSize[1]-1), self.GRID_THICKNESS)
            pygame.draw.line(self.image, self.GRID_COLOR, (self.squareSize[0]-1, 0), (self.squareSize[0]-1, self.squareSize[1]-1), self.GRID_THICKNESS)
            pygame.draw.line(self.image, self.GRID_COLOR, (0, self.squareSize[1]-1), (self.squareSize[0]-1, self.squareSize[1]-1), self.GRID_THICKNESS)
            LASER_DIMENSIONS = (32, 20)
            self.laserGraphic = pygame.image.load("Graphics/laser.png")
            self.image.blit(self.laserGraphic, (self.squareSize[0] / 2 - LASER_DIMENSIONS[0] / 2, self.squareSize[1] / 2 - LASER_DIMENSIONS[1] / 2))
            if (self.state == "potionlaservert"):
                self.image = pygame.transform.rotate(self.image, 90)
            self.laserOn = True
        else:
            IMAGE_DIMENSIONS = (32, 20)
            self.picture = pygame.image.load("Graphics/laser.png")
            self.image.blit(self.picture, (self.squareSize[0] / 2 - IMAGE_DIMENSIONS[0] / 2, self.squareSize[1] / 2 - IMAGE_DIMENSIONS[1] / 2))
            if (self.state == "laservert"):
                self.image = pygame.transform.rotate(self.image, 90)
            self.laserOn = True
            
    def fill(self, color):
        self.image.fill(color)
        pygame.draw.line(self.image, self.GRID_COLOR, (0, 0), (self.squareSize[0]-1, 0), self.GRID_THICKNESS)
        pygame.draw.line(self.image, self.GRID_COLOR, (0, 0), (0, self.squareSize[1]-1), self.GRID_THICKNESS)
        pygame.draw.line(self.image, self.GRID_COLOR, (self.squareSize[0]-1, 0), (self.squareSize[0]-1, self.squareSize[1]-1), self.GRID_THICKNESS)
        pygame.draw.line(self.image, self.GRID_COLOR, (0, self.squareSize[1]-1), (self.squareSize[0]-1, self.squareSize[1]-1), self.GRID_THICKNESS)
        if (self.state != "laservert"):
            self.state = self.stateList[1]
        
        
class OutOfMovesMessage(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.text = "Out of moves"
        self.font = pygame.font.SysFont("None", 120)
        self.image = self.font.render(self.text, 1, (255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = screen[0] / 2
        self.rect.centery = screen[1] / 2
        
class ZappedMessage(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.text = "You've been zapped!"
        self.font = pygame.font.SysFont("None", 80)
        self.image = self.font.render(self.text, 1, (255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = screen[0] / 2
        self.rect.centery = screen[1] / 2
        
class WinMessage(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.text = "You win!"
        self.font = pygame.font.SysFont("None", 120)
        self.image = self.font.render(self.text, 1, (255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = screen[0] / 2
        self.rect.centery = screen[1] / 2

class MovementsNumMessage(pygame.sprite.Sprite):
    def __init__(self, screen, movements):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("None", 24)
        self.text = "Moves: %d" % movements
        self.image = self.font.render(self.text, 1, (255, 0, 0))
        self.rect = self.image.get_rect()
        
    def update(self, movements):
        self.text = "Moves: %d" % movements
        self.image = self.font.render(self.text, 1, (255, 0, 0))
    
   
def level(currentLEV):
    #0 = "empty", 1 = "full", 2 = "start_node", 3 = "end_node", 4 = "wall", 5 = "portal1", 6 = "portal2", 7 = "item",
    #8 = "laser", 9 = "laser turret", 10 = "laservert", 11 = "potionlaser", 12 = "potionlaservert"
    if (currentLEV == 1):
        return ([[2, 4, 0, 6, 0,
                  0, 4, 0, 4, 0,
                  0, 4, 7, 0, 0,
                  0, 5, 0, 0, 0,
                  0, 0, 0, 0, 3],
                 [5, 5, 7, 4]])
        
    if (currentLEV == 2):
        return ([[4, 2, 0, 0, 0, 4,
                  5, 4, 4, 4, 0, 0,
                  0, 4, 7, 0, 4, 0,
                  0, 4, 0, 0, 0, 0,
                  0, 4, 0, 4, 4, 0,
                  0, 0, 0, 6, 3, 4],
                 [6, 6, 11, 10]])
        
    if (currentLEV == 3):
        return ([[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                  4, 2, 0, 4, 0, 0, 0, 4, 0, 0, 0, 0, 4, 4,
                  4, 4, 0, 0, 0, 4, 0, 4, 8, 8, 8, 11, 8, 9,
                  4, 4, 0, 4, 4, 0, 7, 0, 0, 4, 4, 4, 0, 4,
                  4, 0, 4, 0, 0, 4, 0, 4, 4, 0, 0, 0, 0, 4,
                  4, 0, 7, 0, 0, 0, 0, 4, 4, 0, 0, 7, 5, 4,
                  4, 4, 4, 0, 0, 4, 4, 0, 10, 0, 4, 4, 4, 4,
                  9, 8, 8, 8, 4, 0, 0, 0, 10, 4, 0, 0, 0, 4,
                  4, 4, 4, 7, 4, 0, 4, 7, 10, 4, 8, 11, 8, 9,
                  9, 8, 8, 8, 4, 11, 8, 8, 9, 4, 0, 4, 0, 4,
                  4, 0, 0, 0, 4, 0, 0, 0, 10, 0, 0, 4, 0, 4,
                  4, 0, 4, 4, 4, 0, 0, 0, 4, 0, 4, 0, 0, 4,
                  4, 6, 4, 4, 4, 0, 0, 7, 0, 4, 3, 0, 4, 4,
                  4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                 [14, 14, 12, 10]])
        
def drawLevel(SCREEN_SIZE, grid, gridDimensions, BACKGROUND_COLOR, mapImage):
    gridGroup = pygame.sprite.Group()
    
    if (SCREEN_SIZE[0] > SCREEN_SIZE[1]):
        PLAYING_AREA_OFFSET = (SCREEN_SIZE[0] - SCREEN_SIZE[1]) / 2 #Makes each grid a square
        SQUARE_OFFSET = (SCREEN_SIZE[1]%gridDimensions[1]) / 2 #So we don't have a small gap depending on size
        squareSize = (SCREEN_SIZE[1]/gridDimensions[0], SCREEN_SIZE[1]/gridDimensions[1]) #Size of the individual squares
        #Create the grid
        for x in range(0, gridDimensions[0]):
            for y in range(0, gridDimensions[1]):
                grid[x][y] = GridSprite(PLAYING_AREA_OFFSET + (x*(squareSize[0]-1)), SQUARE_OFFSET + (y*(squareSize[1]-1)), BACKGROUND_COLOR, squareSize, mapImage[0][y*gridDimensions[1] + x])
                gridGroup.add(grid[x][y])
                grid[x][y].initialize();
    else:
        PLAYING_AREA_OFFSET = (SCREEN_SIZE[1] - SCREEN_SIZE[0]) / 2
        squareSize = (SCREEN_SIZE[0]/gridDimensions[0], SCREEN_SIZE[0]/gridDimensions[1])
        for x in range(0, gridDimensions[0]):
            for y in range(0, gridDimensions[1]):
                grid[x][y] = GridSprite(SQUARE_OFFSET + (x*(squareSize[0]-1)), PLAYING_AREA_OFFSET + (y*(squareSize[1]-1)), BACKGROUND_COLOR, squareSize, mapImage[0][y*gridDimensions[1] + x])
                gridGroup.add(grid[x][y])
                grid[x][y].initialize();
                
    return gridGroup
                         
                               
def boundary(playerPOS, gridDIM, direction):
    if (direction == "LEFT" and playerPOS[0] == 0):
        return False
    elif (direction == "UP" and playerPOS[1] == 0):
        return False
    elif (direction == "RIGHT" and playerPOS[0] == gridDIM[0]-1):
        return False
    elif (direction == "DOWN" and playerPOS[1] == gridDIM[1]-1):
        return False
    else:
        return True
    
    
def main():
    SCREEN_SIZE = 640, 400
    BACKGROUND_COLOR = 0, 0, 0
    
    currentLevel = 1
    mapImage = level(currentLevel)
    movementCounter = mapImage[1][2]
    gridDimensions = (mapImage[1][0], mapImage[1][0])
    playerPOS = [0,0]
    playing = True 
    
    outOfMovesMessage = OutOfMovesMessage(SCREEN_SIZE)
    zappedMessage = ZappedMessage(SCREEN_SIZE)
    winMessage = WinMessage(SCREEN_SIZE)
    messageGroup = pygame.sprite.Group()
    
    movesMessage = MovementsNumMessage(SCREEN_SIZE, movementCounter)
    movementGroup = pygame.sprite.Group(movesMessage)
    
    grid = [[0 for x in xrange(gridDimensions[1])] for x in xrange(gridDimensions[0])]
    
    #Create grid based on screen size and grid dimensions
    gridGroup = drawLevel(SCREEN_SIZE, grid, gridDimensions, BACKGROUND_COLOR, mapImage)
    
    #Screen stuff
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Connect")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BACKGROUND_COLOR)
    screen.blit(background, (0, 0))
    
    allSprites = pygame.sprite.Group(gridGroup)
    
    clock = pygame.time.Clock()
    while playing:  #Main game loop
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (messageGroup.has(winMessage)):
                    playing = False 
                messageGroup.remove(outOfMovesMessage, zappedMessage)
                if event.key == pygame.K_LEFT:
                    if (boundary(playerPOS, gridDimensions, "LEFT")):
                        if (grid[playerPOS[0]-1][playerPOS[1]].state != "wall" and grid[playerPOS[0]-1][playerPOS[1]].state != "full"):
                            if (movementCounter > 0):
                                movementCounter -= 1
                                gCounter = 0
                                for g in mapImage[0]:
                                    gCounter += 1
                                    if (g == 8 or g == 10 or g == 11 or g == 12):
                                        grid[gCounter % gridDimensions[0] - 1][(int)(math.floor(gCounter/gridDimensions[1]))].shootLazer()
                        if (grid[playerPOS[0]-1][playerPOS[1]].state == "empty"):
                            playerPOS[0] -= 1
                            grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                        elif (grid[playerPOS[0]-1][playerPOS[1]].state == "end_node"):
                            allSprites.clear(screen, background)
                            if (currentLevel == 3):
                                messageGroup.add(winMessage)
                            else:
                                currentLevel += 1
                                mapImage = level(currentLevel)
                                movementCounter = mapImage[1][2]
                                gridDimensions = (mapImage[1][0], mapImage[1][0])
                                grid = [[0 for x in xrange(gridDimensions[1])] for x in xrange(gridDimensions[0])]
                                gridGroup = drawLevel(SCREEN_SIZE, grid, gridDimensions, BACKGROUND_COLOR, mapImage)
                                allSprites = pygame.sprite.Group(gridGroup)
                                for g in mapImage[0]:
                                    if (g == 2):
                                        playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                        playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                        elif (grid[playerPOS[0]-1][playerPOS[1]].state == "portal1"):
                            for g in mapImage[0]:
                                if (g == 6):
                                    grid[playerPOS[0]-1][playerPOS[1]].fill((87, 123, 6))
                                    playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                    playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                                    grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                        elif (grid[playerPOS[0]-1][playerPOS[1]].state == "portal2"):
                            for g in mapImage[0]:
                                if (g == 5):
                                    grid[playerPOS[0]-1][playerPOS[1]].fill((87, 123, 6))
                                    playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                    playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                                    grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                        elif (grid[playerPOS[0]-1][playerPOS[1]].state == "item" or grid[playerPOS[0]-1][playerPOS[1]].state == "potionlaser" or grid[playerPOS[0]-1][playerPOS[1]].state == "potionlaservert"):
                            playerPOS[0] -= 1
                            if (grid[playerPOS[0]][playerPOS[1]].state == "potionlaser" or grid[playerPOS[0]][playerPOS[1]].state == "potionlaservert"):
                                if (grid[playerPOS[0]][playerPOS[1]].laserOn):
                                    allSprites.clear(screen, background)
                                    mapImage = level(currentLevel)
                                    movementCounter = mapImage[1][2]
                                    gridGroup = drawLevel(SCREEN_SIZE, grid, gridDimensions, BACKGROUND_COLOR, mapImage)
                                    allSprites = pygame.sprite.Group(gridGroup)
                                    messageGroup.add(zappedMessage)
                                    for g in mapImage[0]:
                                        if (g == 2):
                                            playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                            playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                            grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                            movementCounter += mapImage[1][3]
                        elif (grid[playerPOS[0]-1][playerPOS[1]].state == "laser" or grid[playerPOS[0]-1][playerPOS[1]].state == "laservert"):
                            if (grid[playerPOS[0]-1][playerPOS[1]].laserOn == False):
                                playerPOS[0] -= 1
                                grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                            else:
                                allSprites.clear(screen, background)
                                mapImage = level(currentLevel)
                                movementCounter = mapImage[1][2]
                                gridGroup = drawLevel(SCREEN_SIZE, grid, gridDimensions, BACKGROUND_COLOR, mapImage)
                                allSprites = pygame.sprite.Group(gridGroup)
                                messageGroup.add(zappedMessage)
                                for g in mapImage[0]:
                                    if (g == 2):
                                        playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                        playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                        else:
                            print "Can not run into a wall"
                    else:
                        print "Can not go outside of grid"
                if event.key == pygame.K_UP:
                    if (boundary(playerPOS, gridDimensions, "UP")):
                        if (grid[playerPOS[0]][playerPOS[1]-1].state != "wall" and grid[playerPOS[0]][playerPOS[1]-1].state != "full"):
                            if (movementCounter > 0):
                                movementCounter -= 1
                                gCounter = 0
                                for g in mapImage[0]:
                                    gCounter += 1
                                    if (g == 8 or g == 10 or g == 11 or g == 12):
                                        grid[gCounter % gridDimensions[0] - 1][(int)(math.floor(gCounter/gridDimensions[1]))].shootLazer()
                        if(grid[playerPOS[0]][playerPOS[1]-1].state == "empty"):
                            playerPOS[1] -= 1
                            grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                        elif(grid[playerPOS[0]][playerPOS[1]-1].state == "end_node"):
                            allSprites.clear(screen, background)
                            if (currentLevel == 3):
                                messageGroup.add(winMessage)
                            else:
                                currentLevel += 1
                                mapImage = level(currentLevel)
                                movementCounter = mapImage[1][2]
                                gridDimensions = (mapImage[1][0], mapImage[1][0])
                                grid = [[0 for x in xrange(gridDimensions[1])] for x in xrange(gridDimensions[0])]
                                gridGroup = drawLevel(SCREEN_SIZE, grid, gridDimensions, BACKGROUND_COLOR, mapImage)
                                allSprites = pygame.sprite.Group(gridGroup)
                                for g in mapImage[0]:
                                    if (g == 2):
                                        playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                        playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                        elif (grid[playerPOS[0]][playerPOS[1]-1].state == "portal1"):
                            for g in mapImage[0]:
                                if (g == 6):
                                    grid[playerPOS[0]][playerPOS[1]-1].fill((87, 123, 6))
                                    playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                    playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                                    grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                        elif (grid[playerPOS[0]][playerPOS[1]-1].state == "portal2"):
                            for g in mapImage[0]:
                                if (g == 5):
                                    grid[playerPOS[0]][playerPOS[1]-1].fill((87, 123, 6))
                                    playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                    playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                                    grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                        elif (grid[playerPOS[0]][playerPOS[1]-1].state == "item" or grid[playerPOS[0]][playerPOS[1]-1].state == "potionlaser" or grid[playerPOS[0]][playerPOS[1]-1].state == "potionlaservert"):
                            playerPOS[1] -= 1
                            if (grid[playerPOS[0]][playerPOS[1]].state == "potionlaser" or grid[playerPOS[0]][playerPOS[1]].state == "potionlaservert"):
                                if (grid[playerPOS[0]][playerPOS[1]].laserOn):
                                    allSprites.clear(screen, background)
                                    mapImage = level(currentLevel)
                                    movementCounter = mapImage[1][2]
                                    gridGroup = drawLevel(SCREEN_SIZE, grid, gridDimensions, BACKGROUND_COLOR, mapImage)
                                    allSprites = pygame.sprite.Group(gridGroup)
                                    messageGroup.add(zappedMessage)
                                    for g in mapImage[0]:
                                        if (g == 2):
                                            playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                            playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                            grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                            movementCounter += mapImage[1][3]
                        elif (grid[playerPOS[0]][playerPOS[1]-1].state == "laser" or grid[playerPOS[0]][playerPOS[1]-1].state == "laservert"):
                            if (grid[playerPOS[0]][playerPOS[1]-1].laserOn == False):
                                playerPOS[1] -= 1
                                grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                            else:
                                allSprites.clear(screen, background)
                                mapImage = level(currentLevel)
                                movementCounter = mapImage[1][2]
                                gridGroup = drawLevel(SCREEN_SIZE, grid, gridDimensions, BACKGROUND_COLOR, mapImage)
                                allSprites = pygame.sprite.Group(gridGroup)
                                messageGroup.add(zappedMessage)
                                for g in mapImage[0]:
                                    if (g == 2):
                                        playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                        playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                        else:
                            print "Can not run into a wall"
                    else:
                        print "Can not go outside of grid"
                if event.key == pygame.K_RIGHT:
                    if (boundary(playerPOS, gridDimensions, "RIGHT")):
                        if (grid[playerPOS[0]+1][playerPOS[1]].state != "wall" and grid[playerPOS[0]+1][playerPOS[1]].state != "full"):
                            if (movementCounter > 0):
                                movementCounter -= 1
                                gCounter = 0
                                for g in mapImage[0]:
                                    gCounter += 1
                                    if (g == 8 or g == 10 or g == 11 or g == 12):
                                        grid[gCounter % gridDimensions[0] - 1][(int)(math.floor(gCounter/gridDimensions[1]))].shootLazer()
                        if(grid[playerPOS[0]+1][playerPOS[1]].state == "empty"):
                            playerPOS[0] += 1
                            grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                        elif(grid[playerPOS[0]+1][playerPOS[1]].state == "end_node"):
                            allSprites.clear(screen, background)
                            if (currentLevel == 3):
                                messageGroup.add(winMessage)
                            else:
                                currentLevel += 1
                                mapImage = level(currentLevel)
                                movementCounter = mapImage[1][2]
                                gridDimensions = (mapImage[1][0], mapImage[1][0])
                                grid = [[0 for x in xrange(gridDimensions[1])] for x in xrange(gridDimensions[0])]
                                gridGroup = drawLevel(SCREEN_SIZE, grid, gridDimensions, BACKGROUND_COLOR, mapImage)
                                allSprites = pygame.sprite.Group(gridGroup)
                                for g in mapImage[0]:
                                    if (g == 2):
                                        playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                        playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                        elif (grid[playerPOS[0]+1][playerPOS[1]].state == "portal1"):
                            for g in mapImage[0]:
                                if (g == 6):
                                    grid[playerPOS[0]+1][playerPOS[1]].fill((87, 123, 6))
                                    playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                    playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                                    grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                        elif (grid[playerPOS[0]+1][playerPOS[1]].state == "portal2"):
                            for g in mapImage[0]:
                                if (g == 5):
                                    grid[playerPOS[0]+1][playerPOS[1]].fill((87, 123, 6))
                                    playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                    playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                                    grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                        elif (grid[playerPOS[0]+1][playerPOS[1]].state == "item" or grid[playerPOS[0]+1][playerPOS[1]].state == "potionlaser" or grid[playerPOS[0]+1][playerPOS[1]].state == "potionlaservert"):
                            playerPOS[0] += 1
                            if (grid[playerPOS[0]][playerPOS[1]].state == "potionlaser" or grid[playerPOS[0]][playerPOS[1]].state == "potionlaservert"):
                                if (grid[playerPOS[0]][playerPOS[1]].laserOn):
                                    allSprites.clear(screen, background)
                                    mapImage = level(currentLevel)
                                    movementCounter = mapImage[1][2]
                                    gridGroup = drawLevel(SCREEN_SIZE, grid, gridDimensions, BACKGROUND_COLOR, mapImage)
                                    allSprites = pygame.sprite.Group(gridGroup)
                                    messageGroup.add(zappedMessage)
                                    for g in mapImage[0]:
                                        if (g == 2):
                                            playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                            playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                            grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                            movementCounter += mapImage[1][3]
                        elif (grid[playerPOS[0]+1][playerPOS[1]].state == "laser" or grid[playerPOS[0]+1][playerPOS[1]].state == "laservert"):
                            if (grid[playerPOS[0]+1][playerPOS[1]].laserOn == False):
                                playerPOS[0] += 1
                                grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                            else:
                                allSprites.clear(screen, background)
                                mapImage = level(currentLevel)
                                movementCounter = mapImage[1][2]
                                gridGroup = drawLevel(SCREEN_SIZE, grid, gridDimensions, BACKGROUND_COLOR, mapImage)
                                allSprites = pygame.sprite.Group(gridGroup)
                                messageGroup.add(zappedMessage)
                                for g in mapImage[0]:
                                    if (g == 2):
                                        playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                        playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                        else:
                            print "Can not run into a wall"
                    else:
                        print "Can not go outside of grid"
                if event.key == pygame.K_DOWN:
                    if (boundary(playerPOS, gridDimensions, "DOWN")):
                        if (grid[playerPOS[0]][playerPOS[1]+1].state != "wall" and grid[playerPOS[0]][playerPOS[1]+1].state != "full"):
                            if (movementCounter > 0):
                                movementCounter -= 1
                                gCounter = 0
                                for g in mapImage[0]:
                                    gCounter += 1
                                    if (g == 8 or g == 10 or g == 11 or g == 12):
                                        grid[gCounter % gridDimensions[0] - 1][(int)(math.floor(gCounter/gridDimensions[1]))].shootLazer()
                        if(grid[playerPOS[0]][playerPOS[1]+1].state == "empty"):
                            playerPOS[1] += 1
                            grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                        elif(grid[playerPOS[0]][playerPOS[1]+1].state == "end_node"):
                            allSprites.clear(screen, background)
                            if (currentLevel == 3):
                                messageGroup.add(winMessage)
                            else:
                                currentLevel += 1
                                mapImage = level(currentLevel)
                                movementCounter = mapImage[1][2]
                                gridDimensions = (mapImage[1][0], mapImage[1][0])
                                grid = [[0 for x in xrange(gridDimensions[1])] for x in xrange(gridDimensions[0])]
                                gridGroup = drawLevel(SCREEN_SIZE, grid, gridDimensions, BACKGROUND_COLOR, mapImage)
                                allSprites = pygame.sprite.Group(gridGroup)
                                for g in mapImage[0]:
                                    if (g == 2):
                                        playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                        playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                        elif (grid[playerPOS[0]][playerPOS[1]+1].state == "portal1"):
                            for g in mapImage[0]:
                                if (g == 6):
                                    grid[playerPOS[0]][playerPOS[1]+1].fill((87, 123, 6))
                                    playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                    playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                                    grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                        elif (grid[playerPOS[0]][playerPOS[1]+1].state == "portal2"):
                            for g in mapImage[0]:
                                if (g == 5):
                                    grid[playerPOS[0]][playerPOS[1]+1].fill((87, 123, 6))
                                    playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                    playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                                    grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                        elif (grid[playerPOS[0]][playerPOS[1]+1].state == "item" or grid[playerPOS[0]][playerPOS[1]+1].state == "potionlaser" or grid[playerPOS[0]][playerPOS[1]+1].state == "potionlaservert"):
                            playerPOS[1] += 1
                            if (grid[playerPOS[0]][playerPOS[1]].state == "potionlaser" or grid[playerPOS[0]][playerPOS[1]].state == "potionlaservert"):
                                if (grid[playerPOS[0]][playerPOS[1]].laserOn):
                                    allSprites.clear(screen, background)
                                    mapImage = level(currentLevel)
                                    movementCounter = mapImage[1][2]
                                    gridGroup = drawLevel(SCREEN_SIZE, grid, gridDimensions, BACKGROUND_COLOR, mapImage)
                                    allSprites = pygame.sprite.Group(gridGroup)
                                    messageGroup.add(zappedMessage)
                                    for g in mapImage[0]:
                                        if (g == 2):
                                            playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                            playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                            grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                            movementCounter += mapImage[1][3]
                        elif (grid[playerPOS[0]][playerPOS[1]+1].state == "laser" or grid[playerPOS[0]][playerPOS[1]+1].state == "laservert"):
                            if (grid[playerPOS[0]][playerPOS[1]+1].laserOn == False):
                                playerPOS[1] += 1
                                grid[playerPOS[0]][playerPOS[1]].fill((87, 123, 6))
                            else:
                                allSprites.clear(screen, background)
                                mapImage = level(currentLevel)
                                movementCounter = mapImage[1][2]
                                gridGroup = drawLevel(SCREEN_SIZE, grid, gridDimensions, BACKGROUND_COLOR, mapImage)
                                allSprites = pygame.sprite.Group(gridGroup)
                                messageGroup.add(zappedMessage)
                                for g in mapImage[0]:
                                    if (g == 2):
                                        playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                                        playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                        else:
                            print "Can not run into a wall"
                    else:
                        print "Can not go outside of grid"
                            
        if (movementCounter <= 0):
            allSprites.clear(screen, background)
            mapImage = level(currentLevel)
            movementCounter = mapImage[1][2]
            gridGroup = drawLevel(SCREEN_SIZE, grid, gridDimensions, BACKGROUND_COLOR, mapImage)
            allSprites = pygame.sprite.Group(gridGroup)
            messageGroup.add(outOfMovesMessage)
            for g in mapImage[0]:
                if (g == 2):
                    playerPOS[0] = mapImage[0].index(g) % gridDimensions[0]
                    playerPOS[1] = (int)(math.floor(mapImage[0].index(g)/gridDimensions[1]))
                    
        #Update ALL THE THINGS!
        allSprites.clear(screen, background)
        movementGroup.clear(screen,background)
        messageGroup.clear(screen, background)
        
        allSprites.update()
        movementGroup.update(movementCounter)
        
        allSprites.draw(screen)
        messageGroup.draw(screen)
        movementGroup.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()