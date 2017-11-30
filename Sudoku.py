import pygame
pygame.init()

global ekraaniPind
ekraaniPind = pygame.display.set_mode( (720, 720) )

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
    ekraaniPind.fill(valge)
    #Taust
    pilt("puit.jpg",0,0)
    
    #Suur kõlar
    pilt("kõlarmutetud.png", 200, 200)
    
    #Tagasi nupp
    tekstKastis("Tagasi", "Bauhaus 93",50,70,660)
    
    pygame.display.flip()
    
    a = 1
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        eventx, eventy = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pilt("puit.jpg",0,0)
            tekstKastis("Tagasi", "Bauhaus 93",50,70,660)
            if evendiasukoht(60,600,60,600,eventx,eventy) and a % 2 == 1:
                pilt("kõlarsees.png", 200,200)
                pygame.display.flip()
                muusika("helilaul.mp3")
                a += 1
            elif evendiasukoht(60,600,60,600,eventx,eventy) and a % 2 != 1:
                pilt("kõlarmutetud.png",200,200)
                pygame.mixer.music.stop()
                pygame.display.flip()
                
                a += 1
            elif evendiasukoht(60,230,660,720,eventx,eventy):
                homescreen()
                break
                    
                heli = True

def kuidasmängida():   #siin on pooleli
    ekraaniPind.fill(valge)
    #Taust
    pilt("puit.jpg",0,0)
    #Juhend
    pilt("sudokujuhend.png",0,0)
    
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
    tekstKastis("SuDoKu", "Bauhaus 93", 100, 200, 120)
    
    #Mängima
    tekstKastis("Mängima", "Bauhaus 93", 70, 225, 250)
    
    #Settings nupp
    tekstKastis("Sätted", "Bauhaus 93", 50, 300, 400)
    
    #Raskusastmed
    tekstKastis("Raskusastmed", "Bauhaus 93", 50, 220, 465)
    
    #Abimehike
    pilt("küsimärk.png",620,620)
    
    pygame.display.flip()
    
    #Panen heli, kui vajutatakse sisse
    heli = False

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  #vasakklikk = 1
            eventx, eventy = pygame.mouse.get_pos()
            if evendiasukoht(295,450,400,450,eventx,eventy):
                print((eventx, eventy))
                settinguteScreen()
                break
            elif evendiasukoht(220,520,250,330,eventx,eventy): #mängima
                print(eventx,eventy)
            elif evendiasukoht(215,530,470,515,eventx,eventy): #raskusastmed
                print(eventx,eventy)
            elif evendiasukoht(620,720,620,720,eventx,eventy):
                kuidasmängida()
                break
            else:
                continue

homescreen()