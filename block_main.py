import pygame,sys,math
pygame.init()
screen = pygame.display.set_mode((1300,1200))
Main_image=pygame.image.load('Image1_.png')
arrow_img0=pygame.image.load('arrow7_.png')
arrow_img1=pygame.image.load('arrow5_.png')
brick_img1=pygame.image.load('brick4.png')
timer=pygame.time.Clock()
screen.fill('violet')
teta,delta=5,0 
X0,Y0=100,1000
X1,Y1=900,Y0
Point0=(X0,Y0)
Width=5
dX=0
q=1
while True:
    teta=teta+0.5*q
    if teta>30:
        q=0
    X2,Y2=X0,Y0-(X1-X0)* math.tan(3.14159/180*teta)
    X3,Y3=X0+delta,Y2+delta*math.tan(teta*3.14159/180)
    dX=dX+1
    if teta<30:
        dX=0
    X=X3+dX
    Y=Y3+dX*math.tan(teta*3.14159/180)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    screen.fill('violet')
    brick_img2=pygame.transform.rotate(brick_img1,-teta)
    arrow_img2=pygame.transform.rotate(arrow_img1,-teta)
    rect_brick=brick_img2.get_rect(topleft=(X,Y-42))
    rect_arrow0=arrow_img0.get_rect(center=(X+55,Y+10))
    rect_arrow=arrow_img2.get_rect(center=(X+55,Y+10))
    Point1=(X1,Y1)
    Point2=(X2,Y2)
    pygame.draw.polygon(screen, 'blue', (Point0,Point1,Point2))
    screen.blit(brick_img2,rect_brick)
    screen.blit(arrow_img0,rect_arrow0)
    screen.blit(arrow_img2,rect_arrow)
    screen.blit(Main_image,(400,70))
    #pygame.draw.rect(screen,'gold',rect_brick,5)
    if X>700:
        dX,teta,q=0,10,1
    timer.tick(50)
    pygame.display.update()
    
