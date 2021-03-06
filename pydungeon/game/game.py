import pygame, sys, os
import colors as c

class Game:
    def __init__(self):
        pygame.init()

        self.data_path = os.path.join(os.path.dirname(__file__),'../assets')
        self.display = pygame.display.set_mode( (400, 300), 0, 32)
        pygame.display.set_caption('pydungeon')
        
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.display.fill(c.grey)
        
        self.w_img = pygame.image.load(os.path.join(self.data_path, 'w.png'))
        self.v1_img = pygame.image.load(os.path.join(self.data_path, 'v1.png'))
        self.v2_img = pygame.image.load(os.path.join(self.data_path, 'v2.png'))
        self.h_img = pygame.image.load(os.path.join(self.data_path, 'h.png'))
        self.m_img = pygame.image.load(os.path.join(self.data_path, 'm.png'))
        self.r_img = pygame.image.load(os.path.join(self.data_path, 'r.png'))
    
    def set_map(self, level):
        self.l = level
    
    def update(self, paramDict):
        self.display.fill(c.grey)
        
        framex = 20
        framey = 50
        blocksize = 32
        cursorx = framex
        cursory = framey
        
        ###            
        
        self.display.blit(self.w_img, (cursorx, cursory) )
        cursorx += blocksize
        
        for i in range( len(self.l.map[0] ) ):
            self.display.blit(self.w_img, (cursorx, cursory) )
            cursorx += blocksize
        cursory += blocksize
        cursorx = framex
        
        for i in range( len( self.l.map ) ):
            self.display.blit(self.w_img, (cursorx, cursory) )
            cursorx += blocksize
            for j in range( len( self.l.map[i] ) ):
                if str(self.l.map[i][j]) == 'H':
                    self.display.blit(self.h_img, (cursorx, cursory) )
                elif str(self.l.map[i][j]) == 'v':
                    self.display.blit(self.v1_img, (cursorx, cursory) )
                elif str(self.l.map[i][j]) == 'V':
                    self.display.blit(self.v2_img, (cursorx, cursory) )
                elif str(self.l.map[i][j]) == 'm':
                    self.display.blit(self.m_img, (cursorx, cursory) )
                elif str(self.l.map[i][j]) == 'R':
                    self.display.blit(self.r_img, (cursorx, cursory) )
                cursorx += blocksize                
            cursory += blocksize
            cursorx = framex
                
            for k in range( len(self.l.map[0])+1 ):
                self.display.blit(self.w_img, (cursorx, cursory) )
                cursorx += blocksize
            cursory += blocksize
            cursorx = framex
        
        ###
        
        self.updateHealth(paramDict['health'])
        self.updateTurn(paramDict['turn'])
        
        try:
            x = paramDict['alert']
            if x:
                if x == 1: #hero dies
                    self.alertMessage('Hero is dead')
                elif x == 2: #level ends
                    self.alertMessage('Level Complete')
        except:
            pass
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
            

    def alertMessage(self, msg):
        textSurface = self.font.render(msg, True, c.black, c.grey)
        textRect = textSurface.get_rect()
        textRect.midtop = (200, 75)
        self.display.blit(textSurface, textRect)
            
    def updateHealth(self, h):
        textSurface = self.font.render('HEALTH: ' + str(h), True, c.white, c.grey)
        textRect = textSurface.get_rect()
        textRect.topleft = (5, 5)
        self.display.blit(textSurface, textRect)
    
    def updateTurn(self, t):
        textSurface = self.font.render('TURN: ' + str(t), True, c.white, c.grey)
        textRect = textSurface.get_rect()
        textRect.topright = (395, 5)
        self.display.blit(textSurface, textRect)
            
    def quit(self):
        pygame.quit()
