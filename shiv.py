def drawFont(ofx,ofy,fx,fy,count,moveText,k,j,i,running,screenVar):
    if count % 12 == 0:
        if k < len(script):
            if j < len(script[k]):
                if i < len(script[k][j]):
                    if script[k][j][i] != "~":
                        if screenVar:
                            screen.blit(screenshot,(100,100))
                        character = consolas.render(floweyScript[k][j][i],True,WHITE)
                        screen.blit(character,(fx,fy))
    if count % 120 == 0:
        musicChannel.play(sound)
    display.flip()
    return fx,fy,count,moveText,k,j,i,running,screenVar

def update(fx,fy,count,moveText,k,j,i,running):
    if script[k][j][i] == "~":
        fx = ofx
        fy += 20
        moveText = False
    else:
        screenVar = True
    if moveText:
        fx += 10
    if count % 12 == 0:
        if not i+1 == len(script[k][j]):
            i+=1
            moveText = True
            screenVar = True
        else:
            i = 0
            if not j+1 == len(floweyScript[k]):
                j+=1
            else:
                j = 0
                if not k+1 == len(floweyScript):
                    k+=1
                    fx = ofx
                    fy = ofy
                    moveText = False
                    screenVar = False
                else:
                    running = False
    count += 1
    display.flip()
    screenshot = screen.copy().subsurface(ofx,ofy,800,100)
    return fx,fy,count,moveText,k,j,i,running

def make3D(text):
    script = text.readlines()
    box = []
    sentence = []
    word = []
    for i in script:
        for j in i:
            if j.isalpha() or j == "?" or j == "!" or j == "'" or j == "," or j == "." or j == "~":
                word.append(j)
            else:
                if len(word)>0:
                    sentence.append(word)
                    word =  []
        box.append(sentence)
        sentence = []
    return box

# ofx is original ofx, aka starting font x position
# same for ofy
#fx and fy is current font position
#sound is the osund effect of the person whos talking
#movetext is a boolean that checks if you need to move the next letter over
#k j and i are counters
# have this in a while running loop
# also when you call this function do fx,fy,count,moveText,k,j,i,running = update(fx,fy,count,moveText,k,j,i,running)
#
