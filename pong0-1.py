import pygame as pygame

def drawCenterLine():
    global screenWidth, screenHeight
    pygame.draw.line(window, white, (screenWidth//2, 0), (screenWidth//2, screenHeight))

def resetBall():
    global ballLocation
    ballLocation = [500, 300]
        
def scoreColor():
    global scoreA, scoreB
    if scoreA > scoreB:
        text=font.render(str(scoreA), True, green)
        text=font.render(str(scoreB), True, red)
    if scoreB > scoreA:
        text=font.render(str(scoreA), True, red)
        text=font.render(str(scoreB), True, green)

def drawScore(font):
    global scoreA, scoreB
    
    text=font.render(str(scoreA), True, white)
    window.blit(text, (200, 30))
    text = font.render(str(scoreB), True, white)
    window.blit(text, (700, 30))
        
        

def MoveBall():
    global scoreA, scoreB, ballSpeedx, ballSpeedy, ballLocation, ball
    
    if ballLocation[0] > screenWidth:
        ballSpeedx = -ballSpeedx
        scoreA = scoreA + 1
        resetBall()
    
    if ballLocation[0] < 0:
        ballSpeedx = -ballSpeedx
        scoreB = scoreB + 1
        resetBall()
    
    if ballLocation[1] < 0:
        ballSpeedy = -ballSpeedy
    
    if ballLocation[1] > screenHeight:
        ballSpeedy = -ballSpeedy
        
    ballLocation[0] = ballLocation[0] + ballSpeedx
    ballLocation[1] = ballLocation[1] + ballSpeedy
    ball = pygame.draw.circle(window, white, ballLocation, radius, 0) 
    
def MovePaddle():
    global PadASpeed, PadA
    if PadA.top <= 0:
        print("Top of Screen")
        PadA = PadA.move(0,2)
        PadASpeed = 0
    if PadA.bottom >= 600:
        print("Bottom of Screen")
        PadA = PadA.move(0,-2)
        PadASpeed = 0
        
    PadA = PadA.move(0, PadASpeed)
    pygame.draw.rect(window, white, PadA)

def MovePaddleB():
    global PadBSpeed, PadB
    if PadB.top<=0:
        print("Top of screen B")
        PadB = PadB.move(0, 2)
        PadBSpeed = 0
    if PadB.bottom >= 600:
        print("Bottom of Screen B")
        PadB = PadB.move(0,-2)
        PadBSpeed = 0
        
    PadB = PadB.move(0, PadBSpeed)
    pygame.draw.rect(window, white, PadB)

timer = pygame.time.Clock()

screenWidth = 1000
screenHeight = 600

window = pygame.display.set_mode([screenWidth, screenHeight])

ballSpeedx = 6
ballSpeedy = -6
black = (0,0,0)
white = (255, 255, 255)
radius = 20
ballLocation=[500, 300]
ball = pygame.Rect(ballLocation, (radius, radius))

PadA = pygame.Rect((10,150), (15,110))
PadASpeed = 0
PadA = PadA.move(0, 2)
PadASpeed = 0

PadB = pygame.Rect((975, 150), (15, 110))
PadBSpeed = 0
PadB = PadB.move(0, 2)
PadBSpeed = 0

scoreA=0
scoreB=0

pygame.font.init()
font = pygame.font.Font(None,24)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if PadB.top <= 0:
                    PadB = PadB.move (0,5)
                    PadB = PadB = 0
                else:
                    PadBSpeed = -5
            if event.key == pygame.K_w:
                PadASpeed = -6
            if event.key == pygame.K_UP:
                PadBSpeed = -6
            if event.key == pygame.K_s:
                PadASpeed = 6
            if event.key == pygame.K_DOWN:
                PadBSpeed = 6
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                PadASpeed = 0
            if event.key == pygame.K_UP:
                PadBSpeed = 0
            if event.key == pygame.K_s:
                PadASpeed = 0
            if event.key == pygame.K_DOWN:
                PadBSpeed = 0
    if PadA.colliderect(ball):
        ballSpeedx = -ballSpeedx
    if PadB.colliderect(ball):
        ballSpeedx = -ballSpeedx
    
    timer.tick(60)
    window.fill(black)
    MoveBall()
    MovePaddle()
    MovePaddleB()
    drawCenterLine()
    drawScore(font)
    pygame.display.flip()
    
    #check quit event
    #check up, down, spacebar event