exec(open("./settings.py").read())


def genfood(game_display_width,game_display_height,border,thicc,translation_vector,size):
        global r    
        r = randint(0,3)
        return (randint(1,(game_display_width-border-thicc-1)/size)*size,randint(1,(game_display_height-border-thicc-1)/size)*size)

cibo = genfood(game_display_width,game_display_height,border,thicc,translation_vector,size)


def start_up():
    global gameDisplay
    global display_width
    global display_height
    global cibo 
    global game_display_width
    global game_display_height
    Pause = True 
    while Pause:
        font = pygame.font.Font("prstartk.ttf", 25)
        text = font.render( 'Press a key to start', True, (255,255,255))
        gameDisplay.blit(text,(game_display_width/2 - text.get_width()/2,game_display_height/2 + text.get_height()))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.VIDEORESIZE:
                gameDisplay = pygame.display.set_mode(event.dict['size'], RESIZABLE)
                display_width = event.dict['size'][0]
                display_height = event.dict['size'][1]
                game_display_width =  display_width - translation_vector[0]
                game_display_height =  display_height - translation_vector[1]
                for i in range (size):
                    if (game_display_width + i) % size == 0:
                        game_display_width += i
                for i in range (size):
                    if (game_display_height + i) % size == 0:
                        game_display_height += i
                cibo= (randint(0,(game_display_width-border-thicc)/size)*size,randint(0,(game_display_height-border-thicc)/size)*size)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #ESC
                    pygame.quit()
                    quit()

                else:
                    Pause = False

    
def draw_snake ():
    itersnake = iter(snake)
    next (itersnake)
    for i  in range (1,len(snake)):
        if snake[i][2] == snake[i-1][2]:
            #pygame.draw.rect(gameDisplay, green, (piece[0]+translation_vector[0], piece[1]+translation_vector[1], size-1,size-1))            
            gameDisplay.blit(pygame.transform.rotate(vertical_body, 90*(snake[i][2]%2)),(snake[i][0]+translation_vector[0], snake[i][1]+translation_vector[1]))
        elif snake[i][2] == 1 and snake[i-1][2] == 4:
            gameDisplay.blit(curva,(snake[i][0]+translation_vector[0], snake[i][1]+translation_vector[1]))
        elif snake[i][2] == 4 and snake[i-1][2] == 3:
            gameDisplay.blit(pygame.transform.rotate(curva,90),(snake[i][0]+translation_vector[0], snake[i][1]+translation_vector[1]))
        elif snake[i][2] == 3 and snake[i-1][2] == 2:
            gameDisplay.blit(pygame.transform.rotate(curva,180),(snake[i][0]+translation_vector[0], snake[i][1]+translation_vector[1]))
        elif snake[i][2] == 2 and snake[i-1][2] == 1:
            gameDisplay.blit(pygame.transform.rotate(curva, 270),(snake[i][0]+translation_vector[0], snake[i][1]+translation_vector[1]))
        elif snake[i][2] == 1:
            gameDisplay.blit(pygame.transform.rotate(curva,90),(snake[i][0]+translation_vector[0], snake[i][1]+translation_vector[1]))
        elif snake[i][2] == 4:
            gameDisplay.blit(pygame.transform.rotate(curva,180),(snake[i][0]+translation_vector[0], snake[i][1]+translation_vector[1]))
        elif snake[i][2] == 3:
            gameDisplay.blit(pygame.transform.rotate(curva,270),(snake[i][0]+translation_vector[0], snake[i][1]+translation_vector[1]))
        elif snake[i][2] == 2:
            gameDisplay.blit(pygame.transform.rotate(curva,0),(snake[i][0]+translation_vector[0], snake[i][1]+translation_vector[1]))
    
    gameDisplay.blit(pygame.transform.rotate(tail, 90*(-snake[0][2]-1)),(snake[0][0]+translation_vector[0], snake[0][1]+translation_vector[1]))

    
def drawGame(gameDisplay,game_display_width,game_display_height,border,translation_vector,thicc,x,y,snake,cibo,size): 
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    font = pygame.font.Font("prstartk.ttf", 50)
    text = font.render( str(len(snake)-4), True, white)
    gameDisplay.fill(black)    
    pygame.draw.line(gameDisplay, blue, (border+translation_vector[0],border+translation_vector[1]), (game_display_width-border+translation_vector[0],border+translation_vector[1]),thicc)
    pygame.draw.line(gameDisplay, blue, (border+translation_vector[0],game_display_height-border+translation_vector[1]), (game_display_width-border+translation_vector[0],game_display_height-border+translation_vector[1]),thicc)
    pygame.draw.line(gameDisplay, blue, (border+translation_vector[0],border+translation_vector[1]), (border+translation_vector[0],game_display_height-border+translation_vector[1]),thicc)        
    pygame.draw.line(gameDisplay, blue, (game_display_width-border+translation_vector[0],border+translation_vector[1]), (game_display_width-border+translation_vector[0],game_display_height-border+translation_vector[1]),thicc)
    gameDisplay.blit(pygame.transform.rotate(head,(-direction+1)*90),(x+translation_vector[0],y+translation_vector[1]))
    #pygame.draw.rect(gameDisplay, green, (x+translation_vector[0],y+translation_vector[1],size-1,size-1))        
    gameDisplay.blit(food[r],(cibo[0]+translation_vector[0], cibo[1]+translation_vector[1]))
    #pygame.draw.rect(gameDisplay, white, (cibo[0]+translation_vector[0], cibo[1]+translation_vector[1],size,size))
    gameDisplay.blit(text,(game_display_width/2 - text.get_width()/2,translation_vector[1]/2 - text.get_height()/2+ (border+thicc) / 2))
    draw_snake()
    pygame.display.update()
    
def pause():
    global gameDisplay
    global display_width
    global display_height
    global cibo 
    global game_display_width
    global game_display_height
    Pause = True
    while Pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.VIDEORESIZE:
                gameDisplay = pygame.display.set_mode(event.dict['size'], RESIZABLE)
                display_width = event.dict['size'][0]
                display_height = event.dict['size'][1]
                game_display_width =  display_width - translation_vector[0]
                game_display_height =  display_height - translation_vector[1]
                for i in range (size):
                    if (game_display_width + i) % size == 0:
                        game_display_width += i
                for i in range (size):
                    if (game_display_height + i) % size == 0:
                        game_display_height += i
                cibo= (randint(0,(game_display_width-border-thicc)/size)*size,randint(0,(game_display_height-border-thicc)/size)*size)
                drawGame(gameDisplay,game_display_width,game_display_height,border,translation_vector,thicc,x,y,snake,cibo,size)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #ESC
                    pygame.quit()
                    quit()

                if event.key == pygame.K_q:
                    Pause = False
start_up()
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        elif event.type == pygame.VIDEORESIZE:
            gameDisplay = pygame.display.set_mode(event.dict['size'], RESIZABLE)
            display_width = event.dict['size'][0]
            display_height = event.dict['size'][1]
            game_display_width =  display_width - translation_vector[0]
            game_display_height =  display_height - translation_vector[1]
            for i in range (size):
                if (game_display_width + i) % size == 0:
                    game_display_width += i
            for i in range (size):
                if (game_display_height + i) % size == 0:
                    game_display_height += i
            cibo= (randint(0,(game_display_width-border-thicc)/size)*size,randint(0,(game_display_height-border-thicc)/size)*size)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #ESC
                pygame.quit()
                quit()
                
            if event.key == pygame.K_LEFT and direction != 3:
                x_change = -size
                y_change = 0
                direction = 1
                    
            if event.key == pygame.K_RIGHT and direction != 1:
                x_change = size
                y_change = 0
                direction = 3

                    
            if event.key == pygame.K_UP and direction != 4:
                y_change = -size
                x_change = 0
                direction = 2
                    
            if event.key == pygame.K_DOWN and direction != 2:
                y_change = size
                x_change = 0
                direction = 4
            if event.key == pygame.K_q:
                pause()
                
        #if event.type == pygame.KEYUP:
         #   if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    #x_change = 0
        #    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #        y_change = 0
    
    
    if time.clock()-t0 > speed:
        t0 = time.clock()
        
        if direction != 0:
        
            for i in range (len(snake)-1):
                snake [i] = snake [i+1]
            
            snake[len(snake)-1] = (x,y,direction)
            x += x_change
            y += y_change
        
            for piece in snake:
                if (piece[0], piece[1]) == (x,y):
                    pygame.quit()
                    quit()
                
        if x == cibo[0] and y == cibo[1]:
            snake.insert(0,(-100,-100,0))
            cibo = genfood(game_display_width,game_display_height,border,thicc,translation_vector,size)            
            #speed -= 0.01
    
        if x > game_display_width - border+thicc - size:
            x = border+thicc
    
        elif  x < border+thicc:
            x = game_display_width - border-thicc - size
        
        if y > game_display_height -border+thicc- size:
            y = border+thicc
        
        elif y < border+thicc:
            y = game_display_height -border-thicc- size
        
        drawGame(gameDisplay,game_display_width,game_display_height,border,translation_vector,thicc,x,y,snake,cibo,size)
quit()
        

    