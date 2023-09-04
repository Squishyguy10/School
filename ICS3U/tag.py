from cmu_graphics import *


# TAG - Made by Aaron & Jaydon
# Updated Journal Log: "https://docs.google.com/document/d/14VXmkgwVo6yt_2gct9HunMQ6mP7ptVh23gwvJ0bWZ9A/edit"


# Use arrow keys to navigate through the menu and press space to interact


import random, math

# Initialize some global variables
app.stepsPerSecond = 60
app.scale = 1
app.numPlayers = 2
app.it = random.randint(0,app.numPlayers-1)
app.players = []
app.colours = ["dodgerBlue", "cyan", "yellow", "purple"]
app.clockTime = 6000
app.mode = 0
app.chosenMap = 0
app.level = 0
app.level_changed = True


# Homescreen music
app.homepageMusic = Sound("cmu://591418/22987385/Homepage.mp3")
app.homepageMusic.play(loop=True)



# Jumping Movement
def vert_jump(keys):
    # p1 (blue)
    if keys == 'w' and app.jumps[0] > 0:
        app.jumpSound.play(restart=True)
        app.velY[0] = -app.jumpPower[0]*(math.sqrt(app.scale))
        app.jumps[0] -= 1
    
    # p2 (cyan)
    if keys == 'up' and app.jumps[1] > 0:
        app.jumpSound.play(restart=True)
        app.velY[1] = -app.jumpPower[1]*(math.sqrt(app.scale))
        app.jumps[1] -= 1
    
    # p3 (yellow)
    if keys == 'i' and app.jumps[2] > 0:
        app.jumpSound.play(restart=True)
        app.velY[2] = -app.jumpPower[2]*(math.sqrt(app.scale))
        app.jumps[2] -= 1

    # p4 (purple) - Needs numlock
    if keys == '8' and app.jumps[3] > 0:
        app.jumpSound.play(restart=True)
        app.velY[3] = -app.jumpPower[3]*(math.sqrt(app.scale))
        app.jumps[3] -= 1



# Side Movement
def side_movement(keys):
    # p1 (blue)
    if 'a' in keys:
        if app.velX[0] > -app.itSpeed[0]*app.maxSpeed:
            app.velX[0] -= app.accel
        app.key[0] = True
    elif 'd' in keys:
        if app.velX[0] < app.itSpeed[0]*app.maxSpeed:
            app.velX[0] += app.accel
        app.key[0] = True


    # p2 (cyan)
    if 'left' in keys:
        if app.velX[1] > -app.itSpeed[1]*app.maxSpeed:
            app.velX[1] -= app.accel
        app.key[1] = True
    elif 'right' in keys:
        if app.velX[1] < app.itSpeed[1]*app.maxSpeed:
            app.velX[1] += app.accel
        app.key[1] = True
        
        
    # p3 (yellow)
    if 'j' in keys:
        if app.velX[2] > -app.itSpeed[2]*app.maxSpeed:
            app.velX[2] -= app.accel
        app.key[2] = True
    elif 'l' in keys:
        if app.velX[2] < app.itSpeed[2]*app.maxSpeed:
            app.velX[2] += app.accel
        app.key[2] = True
    
    
    # p4 (purple) - Needs numlock
    if '4' in keys:
        if app.velX[3] > -app.itSpeed[3]*app.maxSpeed:
            app.velX[3] -= app.accel
        app.key[3] = True
    elif '6' in keys:
        if app.velX[3] < app.itSpeed[3]*app.maxSpeed:
            app.velX[3] += app.accel
        app.key[3] = True



# For iterating through menu
def arrow_itr(keys):
    # Up and Down
    if keys == 'up' and app.select > 0:
        app.settings[app.select].size = 35
        app.settings[app.select].opacity = 90
        app.select -= 1
        app.settings[app.select].size = 40
        app.settings[app.select].opacity = 100
        app.selectSound.play(restart=True)
        
    elif keys == 'down' and app.select < 5:
        app.settings[app.select].size = 35
        app.settings[app.select].opacity = 90
        app.select += 1
        app.settings[app.select].size = 40
        app.settings[app.select].opacity = 100
        app.selectSound.play(restart=True)


    # SPACE for instructions
    if app.select == 0:
        if keys == 'space':
            app.confirmSound.play(restart=True)
            level_change(1)
    
    # Left and Right for selecting
    elif app.select == 1:
        if keys == 'left' and app.numPlayers > 2:
            app.numPlayers -= 1
            app.settings[1].value = "Players:  < " + str(app.numPlayers) + " >"
            app.selectSound.play(restart=True)
        elif keys == 'right' and app.numPlayers < 4:
            app.numPlayers += 1
            app.settings[1].value = "Players:  < " + str(app.numPlayers) + " >"
            app.selectSound.play(restart=True)
        
    elif app.select == 2:
        if keys == 'left' and app.clockTime > 6000:
            app.clockTime -= 6000
            app.settings[2].value = "Timer:  < " + str(math.ceil(app.clockTime/60)) + " >"
            app.selectSound.play(restart=True)
        elif keys == 'right' and app.clockTime < 18000:
            app.clockTime += 6000
            app.settings[2].value = "Timer:  < " + str(math.ceil(app.clockTime/60)) + " >"
            app.selectSound.play(restart=True)
            
    elif app.select == 3:
        if keys == 'left' and app.chosenMap > 0:
            app.chosenMap -= 1
            app.settings[3].value = "Map:  < A >"
            app.selectSound.play(restart=True)
        elif keys == 'right' and app.chosenMap < 1:
            app.chosenMap += 1
            app.settings[3].value = "Map:  < B >"
            app.selectSound.play(restart=True)
            
    elif app.select == 4:
        if keys == 'left' and app.mode > 0:
            app.mode -= 1
            app.settings[4].value = "Mode:  < TAG >"
            app.selectSound.play(restart=True)
        elif keys == 'right' and app.mode < 1:
            app.mode += 1
            app.settings[4].value = "Mode:  < KING >"
            app.selectSound.play(restart=True)

    # SPACE for start
    elif app.select == 5:
        if keys == 'space':
            app.confirmSound.play(restart=True)
            level_change(2)
            
            

# Function to scale and reposition the camera
# Note: Camera position is based on midpoint of the farthest out players (based on map)
#       while scaling is based on characters' distance from edge of canvas
def cameraReposition():
    # Compare old and current camera position to detect scaling
    oldCamX = app.cameraX
    oldCamY = app.cameraY
    
    # Find max distance from farthest players
    app.minX = math.inf
    app.minY = math.inf
    app.maxX = -math.inf
    app.maxY = -math.inf

    for i in range(app.numPlayers):
        app.minX = min(app.minX, app.mapPosX[i])
        app.minY = min(app.minY, app.mapPosY[i])
        app.maxX = max(app.maxX, app.mapPosX[i])
        app.maxY = max(app.maxY, app.mapPosY[i])
    
    # Calculate midpoint for new camera position
    app.cameraX = (app.minX+app.maxX)/2
    app.cameraY = (app.minY+app.maxY)/2
    disX = abs(app.maxX-app.minX)
    disY = abs(app.maxY-app.minY)
    
    app.minPlayerX = math.inf
    app.minPlayerY = math.inf
    app.maxPlayerX = -math.inf
    app.maxPlayerY = -math.inf
    
    # Detect distance from the edge of canvas for scaling
    for i in range(app.numPlayers):
        app.minPlayerX = min(app.minPlayerX, app.players[i].centerX)
        app.minPlayerY = min(app.minPlayerY, app.players[i].centerY)
        app.maxPlayerX = max(app.maxPlayerX, app.players[i].centerX)
        app.maxPlayerY = max(app.maxPlayerY, app.players[i].centerY)
    

    dX = oldCamX - app.cameraX
    dY = oldCamY - app.cameraY
    
    # New scaling factor
    dScale = pythonRound(max(disX,disY), 4)
    
    app.originalScale = app.scale
    
    # Scaling when players are moving to sides of screen
    if(app.minPlayerX <= 50 or app.maxPlayerX >= 350 or app.minPlayerY <= 50 or app.maxPlayerY >= 350):
        app.originalScale = app.scale
        app.scale = pythonRound(1/(dScale*0.0032), 4)
        # Cap scale to 1 (Fix for "The Cannon")
        if app.scale > 1:
            app.scale = 1
        
    # Move and scale players
    for i in range(len(app.players)):
        app.players[i].centerX+=dX*app.scale
        app.players[i].centerY+=dY*app.scale
        
        if(app.minPlayerX <= 50 or app.maxPlayerX >= 350 or app.minPlayerY <= 50 or app.maxPlayerY >= 350):
            app.players[i].width = (app.players[i].width/app.originalScale)*app.scale
            app.players[i].height = (app.players[i].height/app.originalScale)*app.scale
            app.players[i].centerX = 200+((app.mapPosX[i]-app.cameraX)*app.scale)
            app.players[i].centerY = 200+((app.mapPosY[i]-app.cameraY)*app.scale)
        
        
    # Move and scale map
    for i in range(len(app.currMap)):
        app.currMap[i].centerX+=dX*app.scale
        app.currMap[i].centerY+=dY*app.scale
        
        if app.minPlayerX <= 50 or app.maxPlayerX >= 350 or app.minPlayerY <= 50 or app.maxPlayerY >= 350:
            app.currMap[i].width = (app.currMap[i].width/app.originalScale)*app.scale
            app.currMap[i].height = (app.currMap[i].height/app.originalScale)*app.scale
            app.currMap[i].centerX = 200+((app.mapX[i]-app.cameraX)*app.scale)
            app.currMap[i].centerY = 200+((app.mapY[i]-app.cameraY)*app.scale)


    
# OnStep function for our main code :)
def onStep():
    # Initialize level when screen is changed
    if app.level_changed:
        level_init()
    
    # Game screen
    if app.level == 2:
        # Variable to use later on
        app.gravity = 0.8*app.scale
        app.accel = 0.45*app.scale
        app.maxSpeed = 5*app.scale
        
        # X-Deceleration
        for i in range(app.numPlayers):
            if(not app.key[i]):
                if app.velX[i] < -app.accel*0.5:
                    app.velX[i] += app.accel*0.5
                elif app.velX[i] > app.accel*0.5:
                    app.velX[i] -= app.accel*0.5
                else:
                    app.velX[i] = 0
            
            # Move player relative to angle of platform
            app.players[i].centreX += app.velX[i]*(math.sin(math.radians(app.players[i].rotateAngle+90)))
            app.mapPosX[i] += app.velX[i]*(math.sin(math.radians(app.players[i].rotateAngle+90)))
            app.players[i].centreY -= app.velX[i]*(math.cos(math.radians(app.players[i].rotateAngle+90)))
            app.mapPosY[i] -= app.velX[i]*(math.cos(math.radians(app.players[i].rotateAngle+90)))
          
            # X-Collision (relative to player angle)
            for part in app.currMap:
                if app.players[i].hitsShape(part):
                    app.players[i].centreX -= app.velX[i]*(math.sin(math.radians(app.players[i].rotateAngle+90)))
                    app.mapPosX[i] -= app.velX[i]*(math.sin(math.radians(app.players[i].rotateAngle+90)))
                    app.players[i].centreY += app.velX[i]*(math.cos(math.radians(app.players[i].rotateAngle+90)))
                    app.mapPosY[i] += app.velX[i]*(math.cos(math.radians(app.players[i].rotateAngle+90)))
                
            # Y-hitbox
            app.players[i].centreY += app.velY[i]
            app.mapPosY[i] += app.velY[i]
            
            # Map collision
            for part in app.currMap:
                if app.players[i].hitsShape(part):
                    if app.velY[i] > 0 and app.velY[i] != app.gravity:
                        app.players[i].rotateAngle = part.rotateAngle
                        # app.players[i].centreY += 15*app.scale
                        # app.mapPosY[i] += 15*app.scale
                        app.jumps[i] = app.jumpStartingAmount
                        if part.fill == 'gold':
                            if i == app.it:
                                app.itSpeed[i] = 1.71
                            else:
                                app.itSpeed[i] = 1.5
                        else:
                            if i == app.it:
                                app.itSpeed[i] = 1.14
                            else:
                                app.itSpeed[i] = 1
                                
                    if app.players[i].hitsShape(part):
                        if app.velY[i] > 0:
                            while app.players[i].hitsShape(part):
                                app.players[i].centreY -= 0.15*app.scale
                                app.mapPosY[i] -= 0.15*app.scale
                            
                            
                        elif app.velY[i] < 0:
                            while app.players[i].hitsShape(part):
                                app.players[i].centreY += 0.15*app.scale
                                app.mapPosY[i] += 0.15*app.scale
                            
                        app.velY[i] = -(app.gravity)
                        
                        
                        break
            
            # Check if players are airborne
            if abs(app.velY[i]) > 5*app.gravity:
                if abs(app.velX[i]) > app.maxSpeed:
                    app.velX[i] == app.maxSpeed
                if i == app.it:
                    app.itSpeed[i] = 1.14
                else:
                    app.itSpeed[i] = 1
                app.players[i].rotateAngle=0
                
                # Decrease jumps
                if app.jumps[i] == app.jumpStartingAmount:
                    app.jumps[i] = app.jumpStartingAmount-1
                
            # Y-acceleration
            app.velY[i] += app.gravity
            
            # To detect if key has been pressed
            app.key[i] = False
        
        # Scale and reposition camera
        cameraReposition()

        # To decrease clock
        if app.clockTime > 0:
            app.clockTime -= 1
            app.clock.value = math.ceil(app.clockTime/60)
            
            # Tagging feature
            for i in range(app.numPlayers):
                if i != app.it and app.itCooldown<=-30:
                    if(app.players[app.it].hitsShape(app.players[i])):
                        app.tagSound.play()
                        app.itSpeed[app.it] = 1
                        app.itCooldown=200
                        app.it = i
                        app.players[app.it].toFront()
                        app.itSpeed[app.it] = 1.14
                        break
                        
            
            # Move "it" triangle
            app.itLabel.centreX = app.players[app.it].centreX
            app.itLabel.bottom = app.players[app.it].centerY-30*app.scale
            app.itTimer.value = math.ceil(app.itCooldown/60)
            
            if app.musicTimer > 0:
                app.musicTimer -= 1
            else:
                app.gameMusic.play(loop=True)
            
            # Display timer above player after tagging
            if app.itCooldown > 180:
                app.itTimer.value = "TAG!"
                app.itCooldown-=1
            elif app.itCooldown > 0:
                app.itCooldown-=1
            elif app.itCooldown > -30:
                app.itTimer.value = "GO!"
                app.itCooldown-=1
            else:
                app.itTimer.value = ""
                
        # Change level when clock hits 0
        else:
            level_change(1)



# OnKeyPress for menu, instructions, and jumping (in main screen)
def onKeyPress(keys):
    if app.level == 0:
        arrow_itr(keys)
        
    elif app.level == 1:
        if keys == 'space':
            app.confirmSound.play(restart=True)
            level_change(-1)
    
    elif app.level == 2:
        vert_jump(keys)



# OnKeyPress for player movement
def onKeyHold(keys):
    if app.level == 2:
        side_movement(keys)



# To initialize a screen
def level_init():
    # Home screen
    if app.level == 0:
        app.image = Image("cmu://591458/22995744/ohdreaam.jpg", 0, 0, width=400, height=400)
        app.selectSound = Sound("cmu://591418/22987205/Select.mp3")
        app.confirmSound = Sound("cmu://591418/22987288/Confirm.mp3")
        
        Label("TAG", 200, 50, size=70, fill="white", font="orbitron", border='black', borderWidth=2, bold=True)
        
        app.select = 0
        Label("Interact with", 330, 45, size=15, font="orbitron", bold=True, rotateAngle=320, fill="red")
        Label("Arrow Keys", 340, 60, size=15, font="orbitron", bold=True, rotateAngle=320, fill="red")
        Label("& SPACE", 350, 75, size=15, font="orbitron", bold=True, rotateAngle=320, fill="red")
        
        # Interactable settings
        app.settings = [
            Label("Instructions", 200, 120, size=40, fill="white", font="orbitron", border='black', borderWidth=1.5, bold=True),
            Label("Players:  < " + str(app.numPlayers) + " >", 200, 165, size=35, fill="white", font="orbitron", border='black', borderWidth=1.5, opacity=90, bold=True),
            Label("Timer:  < " + str(math.ceil(app.clockTime/60)) + " >", 200, 210, size=35, fill="white", font="orbitron", border='black', borderWidth=1.5, opacity=90, bold=True),
            Label("Map:  < A >", 200, 255, size=35, fill="white", font="orbitron", border='black', borderWidth=1.5, opacity=90, bold=True),
            Label("Mode:  < TAG >", 200, 300, size=35, fill="white", font="orbitron", border='black', borderWidth=1.5, opacity=90, bold=True),
            Label("START", 200, 370, size=35, fill="white", font="orbitron", border='black', borderWidth=1.5, opacity=90, bold=True)
        ]
        if app.chosenMap == 1:
            app.settings[3].value = "Map:  < B >"
        if app.mode == 1:
            app.settings[4].value = "Mode:  < KING >"
        
        
    # Instructions screen
    elif app.level == 1:
        app.image = Image("cmu://591458/22995744/ohdreaam.jpg", 0, 0, width=400, height=400)
        Label("Instructions", 200, 50, size=50, fill="white", font="orbitron", border='black', borderWidth=2, bold=True)
        
        Label("Press SPACE", 305, 355, size=15, font="orbitron", bold=True, rotateAngle=320, fill="yellow")
        Label("To Go Back", 315, 365, size=15, font="orbitron", bold=True, rotateAngle=320, fill="yellow")

        Label("Blue: WASD", 200, 100, size=30,fill="white", font="orbitron", border='black', borderWidth=1.5, bold=True)
        Label("Cyan: Arrow Keys", 200, 135, size=30,fill="white", font="orbitron", border='black', borderWidth=1.5, bold=True)
        Label("Yellow: IJKL", 200, 170, size=30,fill="white", font="orbitron", border='black', borderWidth=1.5, bold=True)
        Label("Purple: 8456 (Numlock)", 200, 205, size=30,fill="white", font="orbitron", border='black', borderWidth=1.5, bold=True)
        
        if(app.mode == 0):
            Label("Don't be IT when", 200, 260, size=35, fill=rgb(230, 75, 60), font="orbitron", border='black', borderWidth=1.5, opacity=90, bold=True)
            Label("the timer runs out!", 200, 300, size=35, fill=rgb(230, 75, 60), font="orbitron", border='black', borderWidth=1.5, opacity=90, bold=True)
        
        elif(app.mode == 1):
            Label("Be IT when", 200, 260, size=35, fill=rgb(230, 75, 60), font="orbitron", border='black', borderWidth=1.5, opacity=90, bold=True)
            Label("the timer runs out!", 200, 300, size=35, fill=rgb(230, 75, 60), font="orbitron", border='black', borderWidth=1.5, opacity=90, bold=True)

        # To go back
        app.back = Label("Back", 200, 370, size=40, fill="white", font="orbitron", border='black', borderWidth=2, bold=True)
        
        
    # Game screen
    elif app.level == 2:
        # Stop homepage music and start game music
        app.homepageMusic.pause()
        
        # Initialize more global variables
        app.background = "lightGreen"
        app.key = [False,False,False,False]
        app.itSpeed = [1,1,1,1]
        app.itSpeed[app.it] = 1.14
        app.itCooldown = 180
        
        # Position and velocity
        app.velX = [0,0,0,0]
        app.velY = [0,0,0,0]
        app.posX = [0,0,0,0]
        app.posY = [0,0,0,0]
        
        # Jumps
        app.jumpStartingAmount = 2
        app.jumpPower = [15,15,15,15]
        app.jumps = [app.jumpStartingAmount,app.jumpStartingAmount,app.jumpStartingAmount,app.jumpStartingAmount]
        
        app.cameraX = 200
        app.cameraY = 200
        
        # App.maps is for all the maps
        app.currMap = []
        
        if app.chosenMap == 0:
            # Map A (1)
            app.currMap = [
                # Platforms
                Rect(app.cameraX*app.scale,(app.cameraY+185)*app.scale,1075*app.scale,30*app.scale,fill='saddleBrown',align='center'),
                Rect((app.cameraX-140)*app.scale,(app.cameraY+70)*app.scale,160*app.scale,20*app.scale,fill='saddleBrown',rotateAngle=25,align='center'),
                Rect((app.cameraX+50)*app.scale,(app.cameraY+20)*app.scale,150*app.scale,20*app.scale,fill='saddleBrown',align='center'),
                Rect((app.cameraX+600)*app.scale,(app.cameraY+400)*app.scale,875*app.scale,30*app.scale,fill='saddleBrown',align='center'),
                Rect((app.cameraX+700)*app.scale,(app.cameraY+50)*app.scale,600*app.scale,20*app.scale,fill='gold',align='center'),
                Rect((app.cameraX-300)*app.scale,(app.cameraY+400)*app.scale,200*app.scale,20*app.scale,fill='gold',rotateAngle=-25,align='center'),
                
                # Borders
                Line(-400*app.scale,-275*app.scale, -400*app.scale, 875*app.scale, lineWidth=150, fill="saddleBrown"),
                Line(-400*app.scale, -200*app.scale, 1200*app.scale, -200*app.scale, lineWidth=150, fill="saddleBrown"),
                Line(1200*app.scale, -275*app.scale, 1200*app.scale, 875*app.scale, lineWidth=150, fill="saddleBrown"),
                Line(-400*app.scale, 800*app.scale, 1200*app.scale, 800*app.scale, lineWidth=150, fill="saddleBrown")
            ]
        
        elif app.chosenMap == 1:
            # Map B (2)
            app.currMap = [
                # The commented code below is a lot of other paltforms we planned on adding, but it became way too laggy with everything
                
                # Platforms
                # Rect((app.cameraX-670)*app.scale,(app.cameraY-300)*app.scale,300*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                Rect((app.cameraX-240)*app.scale,(app.cameraY-370)*app.scale,260*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                Rect((app.cameraX+60)*app.scale,(app.cameraY-370)*app.scale,350*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                # Rect((app.cameraX+370)*app.scale,(app.cameraY-370)*app.scale,260*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                # Rect((app.cameraX+950)*app.scale,(app.cameraY-310)*app.scale,350*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                
                # Rect((app.cameraX-950)*app.scale,(app.cameraY-150)*app.scale,170*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                Rect((app.cameraX-370)*app.scale,(app.cameraY-100)*app.scale,260*app.scale,35*app.scale,fill='saddleBrown',align='center',rotateAngle=15),
                # Rect((app.cameraX-0)*app.scale,(app.cameraY-110)*app.scale,390*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                # Rect((app.cameraX+470)*app.scale,(app.cameraY-160)*app.scale,275*app.scale,35*app.scale,fill='saddleBrown',align='center',rotateAngle=-30),
                # Rect((app.cameraX+930)*app.scale,(app.cameraY-40)*app.scale,560*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                
                Rect((app.cameraX-860)*app.scale,(app.cameraY-80)*app.scale,90*app.scale,35*app.scale,fill='saddleBrown',align='center',rotateAngle=-15),
                Rect((app.cameraX-470)*app.scale,(app.cameraY+100)*app.scale,600*app.scale,35*app.scale,fill='saddleBrown',align='center',rotateAngle=30),
                ### Center
                Rect((app.cameraX-0)*app.scale,(app.cameraY+50)*app.scale,300*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                ###
                # Rect((app.cameraX+210)*app.scale,(app.cameraY+120)*app.scale,215*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                # Rect((app.cameraX+510)*app.scale,(app.cameraY+220)*app.scale,260*app.scale,35*app.scale,fill='saddleBrown',align='center',rotateAngle=30),
                
                # Rect((app.cameraX+1050)*app.scale,(app.cameraY+190)*app.scale,350*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                # Rect((app.cameraX-1004)*app.scale,(app.cameraY+45)*app.scale,50*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                # Rect((app.cameraX-978)*app.scale,(app.cameraY+150)*app.scale,90*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                # Rect((app.cameraX-630)*app.scale,(app.cameraY+330)*app.scale,300*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                Rect((app.cameraX-210)*app.scale,(app.cameraY+360)*app.scale,215*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                
                # Rect((app.cameraX+50)*app.scale,(app.cameraY+310)*app.scale,170*app.scale,35*app.scale,fill='saddleBrown',align='center',rotateAngle=-30),
                # Rect((app.cameraX+260)*app.scale,(app.cameraY+400)*app.scale,215*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                # Rect((app.cameraX+840)*app.scale,(app.cameraY+390)*app.scale,215*app.scale,35*app.scale,fill='saddleBrown',align='center',rotateAngle=15),
                # Rect((app.cameraX-890)*app.scale,(app.cameraY+450)*app.scale,170*app.scale,35*app.scale,fill='saddleBrown',align='center',rotateAngle=45),
                # Rect((app.cameraX-514)*app.scale,(app.cameraY+555)*app.scale,300*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                
                # Rect((app.cameraX-240)*app.scale,(app.cameraY+555)*app.scale,300*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                # Rect((app.cameraX+40)*app.scale,(app.cameraY+555)*app.scale,300*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                # Rect((app.cameraX+590)*app.scale,(app.cameraY+550)*app.scale,260*app.scale,35*app.scale,fill='saddleBrown',align='center',rotateAngle=-30),
                # Rect((app.cameraX+970)*app.scale,(app.cameraY+570)*app.scale,170*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                # Rect((app.cameraX-935)*app.scale,(app.cameraY+650)*app.scale,170*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                
                # Rect((app.cameraX-630)*app.scale,(app.cameraY+710)*app.scale,170*app.scale,35*app.scale,fill='saddleBrown',align='center',rotateAngle=15),
                # Rect((app.cameraX-240)*app.scale,(app.cameraY+665)*app.scale,390*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                # Rect((app.cameraX+160)*app.scale,(app.cameraY+710)*app.scale,130*app.scale,35*app.scale,fill='saddleBrown',align='center',rotateAngle=-30),
                # Rect((app.cameraX+350)*app.scale,(app.cameraY+690)*app.scale,130*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                # Rect((app.cameraX+760)*app.scale,(app.cameraY+665)*app.scale,90*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                
                # Rect((app.cameraX+1130)*app.scale,(app.cameraY-680)*app.scale,130*app.scale,35*app.scale,fill='saddleBrown',align='center'),
                
                # Borders
                Line(-850*app.scale,-400*app.scale, -850*app.scale, 800*app.scale, lineWidth=150, fill="saddleBrown"),
                Line(-925*app.scale, -400*app.scale, 750*app.scale, -400*app.scale, lineWidth=150, fill="saddleBrown"),
                Line(675*app.scale, -400*app.scale, 675*app.scale, 800*app.scale, lineWidth=150, fill="saddleBrown"),
                Line(-800*app.scale, 725*app.scale, 675*app.scale, 725*app.scale, lineWidth=150, fill="saddleBrown")
            ]
            
            
        app.mapX = [platform.centerX for platform in app.currMap]
        app.mapY = [platform.centerY for platform in app.currMap]
        
        
        # Player's positions without scaling
        app.mapPosX = [app.cameraX-90,app.cameraX-30,app.cameraX+30,app.cameraX+90]
        app.mapPosY = [app.cameraY-30,app.cameraY-30,app.cameraY-30,app.cameraY-30]
        
        # Create players
        for i in range(app.numPlayers):
            face = Group(
                Rect(app.mapPosX[i]+8*app.scale,app.mapPosY[i]-5*app.scale,4*app.scale,12*app.scale,fill='black',align='centre'),
                Rect(app.mapPosX[i]-8*app.scale,app.mapPosY[i]-5*app.scale,4*app.scale,12*app.scale,fill='black',align='centre')
            )
            create_player = Group(
                Rect(app.mapPosX[i],app.mapPosY[i],36*app.scale,40*app.scale,fill=app.colours[i],border='black',borderWidth=2*app.scale, align="centre"),
                Rect(app.mapPosX[i],app.mapPosY[i],40*app.scale,36*app.scale,fill=app.colours[i], border='black',borderWidth=2*app.scale, align="centre"),
                Rect(app.mapPosX[i],app.mapPosY[i],32*app.scale,36*app.scale,fill=app.colours[i], align="centre"),
                Rect(app.mapPosX[i],app.mapPosY[i],40*app.scale,40*app.scale,fill=None,align='centre'),
                face
            )
            app.players.append(create_player)
        
        # "it" label
        app.itTimer = Label(math.ceil(app.itCooldown/60), 0, -66*app.scale, size=33*app.scale, fill='white', border='black', borderWidth=1, bold=True, font='orbitron')
        
        app.itLabel = Group(
            Polygon(-15*app.scale,-45*app.scale,15*app.scale,-45*app.scale,0,-32*app.scale,fill="white",border="black",borderWidth=1.5*app.scale),
            app.itTimer
        )
        
        # clock label
        app.clock = Label(math.ceil(app.clockTime/60), 200, 30, size=35, fill='white', border='black', borderWidth=1.5, bold=True, font='orbitron')
        
        
        # Music/sound effects
        app.jumpSound = Sound("cmu://591418/22987131/Jump.mp3")
        app.tagSound = Sound("cmu://591418/22987155/Tag.mp3")
        app.gameMusic = Sound("cmu://591418/22987550/Game.mp3")
        app.gameStartMusic = Sound("cmu://591418/22987552/GameStart.mp3")
        app.musicTimer=234
        app.gameStartMusic.play()
        
    
    # Winner screen
    elif app.level == 3:
        app.background = rgb(150, 240, 110)
        app.gameMusic.pause()
        
        app.victoryMusic = Sound("cmu://591418/22987597/Victory.mp3")
        app.victoryMusic.play()
        
        # Create podium
        podium1 = Group(
            Rect(200,300,144,240,fill='gold',border='black',borderWidth=2, align="centre"),
            Rect(200,300,160,216,fill='gold', border='black',borderWidth=2, align="centre"),
            Rect(200,300,140,216,fill='gold', align="centre"),
            
            Rect(200,240,40,55,fill=rgb(247,233,142), align="centre"),
            Rect(200,240,55,40,fill=rgb(247,233,142), align="centre"),
            
            Label(1,197.5,240,fill='white',size=35,font='orbitron',align='center',bold=True,border='black',borderWidth=1.5)
        )
        
        Rect(0,381,400,19,fill='saddleBrown')
        
        # Set character's position on the podium
        app.startingVals1 = [200, 175, 155, 130]
        app.startingVals2 = [30, 85, 315, 370]
        notIT=0
        
        for i in range(app.numPlayers):
            # If the mode is set to "TAG"
            if app.mode == 0:
                # Players who won :)
                if app.it != i:
                    face = Group(
                        Rect(app.startingVals1[app.numPlayers-2]+(45*notIT)+8,156,4,12,fill='black',align='centre'),
                        Rect(app.startingVals1[app.numPlayers-2]+(45*notIT)-8,156,4,12,fill='black',align='centre')
                    )
                    create_player = Group(
                        Rect(app.startingVals1[app.numPlayers-2]+(45*notIT),161,36,40,fill=app.colours[i],border='black',borderWidth=2, align="centre"),
                        Rect(app.startingVals1[app.numPlayers-2]+(45*notIT),161,40,36,fill=app.colours[i], border='black',borderWidth=2, align="centre"),
                        Rect(app.startingVals1[app.numPlayers-2]+(45*notIT),161,32,36,fill=app.colours[i], align="centre"),
                        Rect(app.startingVals1[app.numPlayers-2]+(45*notIT),161,40,40,fill=None,align='centre'),
                        face
                    )
                    notIT+=1
                
                # Player who is "IT" goes on the floor :(
                else:
                    face = Group(
                        Rect(358,356,4,12,fill='black',align='centre'),
                        Rect(342,356,4,12,fill='black',align='centre')
                    )
                    create_player = Group(
                        Rect(350,361,36,40,fill=app.colours[i],border='black',borderWidth=2, align="centre"),
                        Rect(350,361,40,36,fill=app.colours[i], border='black',borderWidth=2, align="centre"),
                        Rect(350,361,32,36,fill=app.colours[i], align="centre"),
                        Rect(350,361,40,40,fill=None,align='centre'),
                        face
                    )
                    
            # If the mode is set to "KING"
            elif app.mode == 1:
                # Losers go on the floor :(
                if app.it != i:
                    face = Group(
                        Rect(app.startingVals2[i]+8,356,4,12,fill='black',align='centre'),
                        Rect(app.startingVals2[i]-8,356,4,12,fill='black',align='centre')
                    )
                    create_player = Group(
                        Rect(app.startingVals2[i],361,36,40,fill=app.colours[i],border='black',borderWidth=2, align="centre"),
                        Rect(app.startingVals2[i],361,40,36,fill=app.colours[i], border='black',borderWidth=2, align="centre"),
                        Rect(app.startingVals2[i],361,32,36,fill=app.colours[i], align="centre"),
                        Rect(app.startingVals2[i],361,40,40,fill=None,align='centre'),
                        face
                    )
                # Whoever is the "IT" (the KING) goes on top :)
                else:
                    face = Group(
                        Rect(208,156,4,12,fill='black',align='centre'),
                        Rect(192,156,4,12,fill='black',align='centre')
                    )
                    create_player = Group(
                        Rect(200,161,36,40,fill=app.colours[i],border='black',borderWidth=2, align="centre"),
                        Rect(200,161,40,36,fill=app.colours[i], border='black',borderWidth=2, align="centre"),
                        Rect(200,161,32,36,fill=app.colours[i], align="centre"),
                        Rect(200,161,40,40,fill=None,align='centre'),
                        face
                    )
                
                
    # To check if level has been changed recently
    app.level_changed = False
        


# Function to change levels
def level_change(n):
    app.level += n
    app.level_changed = True
    app.group.clear()
    

cmu_graphics.run()