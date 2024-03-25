import pygame as pygame

def drawCenterLine():
    global screenWidth, screenHeight
    pygame.draw.line(window, white, (screenWidth//2, 0), (screenWidth//2, screenHeight))

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
    
    if ballLocation[0] < 0:
        ballSpeedx = -ballSpeedx
        scoreB = scoreB + 1
    
    if ballLocation[1] < 0:
        ballSpeedy = -ballSpeedy
    
    if ballLocation[1] > screenHeight:
        ballSpeedy = -ballSpeedy
        
    ballLocation[0] = ballLocation[0] + ballSpeedx
    ballLocation[1] = ballLocation[1] + ballSpeedy
    ball = pygame.draw.circle(window, white, ballLocation, radius, 0) 
    
def MovePaddle():
    global PadASpeed, PadA
    """
    Moves the paddle up and down but not off the screen
    """
    
    if PadA.top <= 0:
        print("Top of Screen")
        PadA = PadA.move(0,2)
        PadASpeed = 0
    #Add Bottom of Paddle Code here
        
    PadA = PadA.move(0, PadASpeed)
    pygame.draw.rect(window, white, PadA)

timer = pygame.time.Clock()

screenWidth = 1000
screenHeight = 600

window = pygame.display.set_mode([screenWidth, screenHeight])

ballSpeedx = 1
ballSpeedy = -1
black = (0,0,0)
white = (255, 255, 255)
radius = 20
ballLocation=[500, 300]
ball = pygame.Rect(ballLocation, (radius, radius))

PadA = pygame.Rect((0,150), (50,300))
PadASpeed = 0

scoreA=0
scoreB=0

pygame.font.init()
font = pygame.font.Font(None,24)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                PadASpeed = -2
            if event.key == pygame.K_DOWN:
                PadASpeed = 2
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                PadASpeed = 0
            if event.key == pygame.K_DOWN:
                PadASpeed = 0
    if PadA.colliderect(ball):
        ballSpeedx = -ballSpeedx
    timer.tick(60)
    window.fill(black)
    MoveBall()
    MovePaddle()
    drawCenterLine()
    drawScore(font)
    pygame.display.flip()
    
    #check quit event
    #check up, down, spacebar event