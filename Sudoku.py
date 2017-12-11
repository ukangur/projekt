import pygame
import os

#märgin, kus kohas avaneb pygame'i aken kuvaril
x=50
y=50
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (x,y)
pygame.init()

global ekraaniPind
ekraaniPind = pygame.display.set_mode( (720, 720) )

global heli
heli = False

#defineerin värve
must = (0,0,0)
valge = (255,255,255)
punane = (255,0,0)
roheline = (0,255,0)
kollane = (255,255,0)
sinine = (0,0,255)
helesinine = (0,255,255)
hall = (211,211,211)

def tekstikast(xkoord, ykoord, laius, kõrgus, värv):
    kast = pygame.Rect(xkoord, ykoord, laius, kõrgus)
    pygame.draw.rect(ekraaniPind, värv, kast)

def tekstKastis(sisu, fondistiil, suurus, xkoord, ykoord):
    logoTekst = sisu
    logoFont = pygame.font.SysFont(fondistiil, suurus)
    logoPilt = logoFont.render(logoTekst, False, (0,0,0))
    ekraaniPind.blit(logoPilt, (xkoord,ykoord))

def pilt(pildiNimi, xkoord, ykoord):
    pildike = pygame.image.load(pildiNimi)
    ekraaniPind.blit(pildike, (xkoord,ykoord))

def evendiasukoht(xmin, xmax, ymin, ymax, eventx, eventy):
    if eventx >= xmin and eventx <= xmax and eventy >= ymin and eventy <= ymax:
        return True
    else:
        return False

def muusika(laulunimi):
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.music.load(laulunimi)
    pygame.mixer.music.play()
    
def settinguteScreen():
    global heli
    
    ekraaniPind.fill(valge)
    #Taust
    pilt("seaded.jpg",0,0)
    #Suur kõlar
    if heli == False:
        pilt("kõlarmutetud.png",280,275)
    else:
        pilt("kõlarsees.png",280,275)
    #Tagasi nupp
    tekstKastis("Tagasi", "Bauhaus 93",50,45,630)
    
    pygame.display.flip()
    
    a = 1
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            break

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            eventx, eventy = pygame.mouse.get_pos()
            print(eventx, eventy)
            pilt("seaded.jpg",0,0)
            tekstKastis("Tagasi", "Bauhaus 93",50,45,630)
            if evendiasukoht(202,551,242,495,eventx,eventy) and a % 2 == 1:
                pilt("kõlarsees.png",280,275)
                pygame.display.flip()
                muusika("helilaul.mp3")
                heli = True
                a += 1
            elif evendiasukoht(202,551,242,495,eventx,eventy) and a % 2 != 1:
                pilt("kõlarmutetud.png",280,275)
                pygame.mixer.music.stop()
                pygame.display.flip()
                heli = False
                a += 1
            elif evendiasukoht(39,195,617,696,eventx,eventy):
                homescreen()
                break
                    
                heli = True

def kuidasmängida():
    ekraaniPind.fill(valge)
    #Taust
    pilt("info.jpg",0,0)
    #Tagasi nupp
    tekstKastis("Tagasi", "Bauhaus 93", 50, 45, 630)
    
    pygame.display.flip()
    
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        eventx, eventy = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if evendiasukoht(39,195,617,696,eventx,eventy):
                homescreen()
                break

def raskusastmed():
    #ekraani atribuudid
    ekraaniPind.fill(valge)
    pilt("raskusastmed1.jpg", 0, 0)
    #raskusastmed
    tekstKastis("Lihtne", "Bauhaus 93", 50, 300, 75)
    tekstKastis("Raskem", "Bauhaus 93", 50, 290, 225)
    tekstKastis("Veel raskem", "Bauhaus 93", 50, 240, 370)
    tekstKastis("Võimatu", "Bauhaus 93", 50, 280, 520)
    tekstKastis("Tagasi", "Bauhaus 93", 50, 45, 630)
    
    pygame.display.flip()
    
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  #vasakklikk = 1
            eventx, eventy = pygame.mouse.get_pos()
            print(eventx, eventy)
            if evendiasukoht(210,530,55,145,eventx,eventy):
                homescreen()
                break
            elif evendiasukoht(210,530,205,295,eventx,eventy):
                homescreen()
                break
            elif evendiasukoht(210,530,350,445,eventx,eventy):
                homescreen()
                break
            elif evendiasukoht(210,530,500,590,eventx,eventy):
                homescreen()
                break
            elif evendiasukoht(39,195,617,696,eventx,eventy):
                homescreen()
                break
    

def mänguekraan():             #poolik
    #ekraani atribuudid
    ekraaniPind.fill(valge)
    pilt("sudokugrid.png",50,50)
    
    pygame.display.flip()
    
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        
def homescreen():
    #ekraani atribuudid
    pygame.display.set_caption("SuDoKu   By Uq and Erki")
    ekraaniPind.fill(valge)
    #Taust
    pilt("puit.jpg",0,0)
    #Sudoku logo
    tekstKastis("SuDoKu", "Bauhaus 93", 100, 185, 150)
    #Nimed logo all
    tekstKastis("Erik Mukk & Uku Kangur", "Bauhaus 93", 35, 165, 260)
    #Mängima
    tekstKastis("Mängima", "Bauhaus 93", 55, 237, 407)
    #Settings nupp
    tekstKastis("Sätted", "Bauhaus 93", 55, 275, 575)
    #Abimehike
    pilt("küsimärk.png",620,620)
    
    pygame.display.flip()
    
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  #vasakklikk = 1
            eventx, eventy = pygame.mouse.get_pos()
            print(eventx, eventy)
            if evendiasukoht(232,467,563,647,eventx,eventy):
                settinguteScreen()
                break
            elif evendiasukoht(232,467,398,480,eventx,eventy): #mängima
                raskusastmed()
                break
            elif evendiasukoht(620,720,620,720,eventx,eventy): #how to nupp
                kuidasmängida()
                break
            else:
                continue

homescreen()