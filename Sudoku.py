import pygame, os
from tkinter import *
from tkinter import messagebox

#märgin, kus kohas avaneb pygame'i aken kuvaril
x=50
y=50
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (x,y)

pygame.init()

global ekraaniPind
ekraaniPind = pygame.display.set_mode( (720, 720) )

global heli
heli = False

#sudokud
lihtneSudoku = [[7,0,0,0,0,0,6,0,1],[0,0,9,7,0,0,0,0,0],[0,0,0,0,5,0,9,3,0],[8,6,0,0,3,0,0,0,0],[4,0,3,0,0,0,0,0,9],[0,0,0,0,4,0,0,2,3],[0,8,5,0,2,0,0,0,0],[0,0,0,0,7,8,1,0,0],[9,0,1,0,0,0,0,0,9]]
lihtneLahendus = [[7,5,8,3,9,2,6,4,1],[3,4,9,7,1,6,5,8,2],[1,2,6,8,5,4,9,3,7],[8,6,2,9,3,7,4,1,5],[4,1,3,2,8,5,7,6,9],[5,9,7,6,4,1,8,2,3],[6,8,5,1,2,9,3,7,4],[2,3,4,5,7,8,1,9,6],[9,7,1,4,6,3,2,5,8]]

mediumSudoku = [[0,8,0,0,0,0,7,0,0],[5,0,0,4,6,0,1,0,0],[0,0,0,0,2,0,0,4,0],[0,4,0,3,0,0,0,9,1],[6,0,0,0,0,0,0,0,8],[2,9,0,0,0,8,0,7,0],[0,1,0,0,9,0,0,0,0],[0,0,4,0,8,3,0,0,5],[0,0,6,0,0,0,0,2,0]]
mediumLahendus = [[4,8,2,9,3,1,7,5,6],[5,3,9,4,6,7,1,8,2],[1,6,7,8,2,5,3,4,9],[8,4,5,3,7,6,2,9,1],[6,7,1,2,4,9,5,3,8],[2,9,3,1,5,8,6,7,4],[3,1,8,5,9,2,4,6,7],[7,2,4,6,8,3,9,1,5],[9,5,6,7,1,4,8,2,3]]

hardSudoku = [[8,1,0,0,6,3,0,0,0],[3,0,0,0,0,0,0,0,7],[0,0,7,0,0,4,0,0,0],[0,0,0,0,0,8,3,0,0],[0,0,2,0,0,0,6,0,0],[0,0,4,9,0,0,0,0,0],[0,0,0,5,0,0,7,0,0],[4,7,0,0,0,0,0,0,5],[0,0,0,2,7,0,0,9,4]]
hardLahendus = [[8,1,9,7,6,3,4,5,2],[3,4,6,1,5,2,9,8,7],[2,5,7,8,9,4,1,3,6],[7,9,5,6,2,8,3,4,1],[1,8,2,4,3,5,6,7,9],[6,3,4,9,1,7,5,2,8],[9,2,8,5,4,6,7,1,3],[4,7,1,3,8,9,2,6,5],[5,6,3,2,7,1,8,9,4]]

võimatuSudoku = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
võimatuLahendus = [[3,4,8,1,5,6,7,9,2],[6,2,9,3,7,4,8,5,1],[1,7,5,8,9,2,3,6,4],[4,6,7,2,3,1,9,8,5],[2,8,3,5,6,9,1,4,7],[9,5,1,7,4,8,6,2,3],[5,1,4,9,8,3,2,7,6],[8,3,6,4,2,7,5,1,9],[7,9,2,6,1,5,4,3,8]]



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
    #tagasi
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
                mänguekraan(lihtneSudoku,lihtneLahendus, "sudokupohieasy.png")
                break
            elif evendiasukoht(210,530,205,295,eventx,eventy):
                mänguekraan(mediumSudoku, mediumLahendus, "sudokupohimedium.png")
                break
            elif evendiasukoht(210,530,350,445,eventx,eventy):
                mänguekraan(hardSudoku, hardLahendus, "sudokupohihard.png")
                break
            elif evendiasukoht(210,530,500,590,eventx,eventy):
                mänguekraan(võimatuSudoku, võimatuLahendus, "sudokupohiextreme.png")
                break
            elif evendiasukoht(39,195,617,696,eventx,eventy):
                homescreen()
                break

def kontrollija(sudoku, lahendus):
    if sudoku == lahendus:
        return True
    else:
        return False

def mänguekraan(sudoku,lahendus, väljak):#poolik
    #ekraani atribuudid
    valik = 0
    ekraaniPind.fill(valge)
    pilt(väljak,0,0)
    #tagasi
    tekstKastis("Tagasi", "Bauhaus 93", 50, 50, 620)
    #kontrolli nupp
    tekstKastis("Kontrolli", "Bauhaus 93", 40, 550, 115)
    clock = pygame.time.Clock()
    
    if heli:
        muusika("helilaul1.mp3")
    
    while True:
        event = pygame.event.poll()
        eventx, eventy = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print(eventx, eventy)
            if evendiasukoht(21,222,595,694,eventx,eventy):
                raskusastmed()
                break
            elif evendiasukoht(527,720,89,190,eventx,eventy):
                if kontrollija(sudoku, lahendus):
                    if heli:
                        muusika("celebration.mp3")
                    else:
                        continue
                else:
                    if heli:
                        muusika
                    Tk().wm_withdraw()
                    messagebox.showinfo("Harjuta veel, nub", "Sa oled kõik valesti teinud!!!")
               
            #sudoku ruudud 1.rida   
            if evendiasukoht(61,106,64,107,eventx,eventy):
                valik = 0,0
            if evendiasukoht(110,156,64,107,eventx,eventy):
                valik = 0,1
            if evendiasukoht(160,205,64,107,eventx,eventy):
                valik = 0,2
            if evendiasukoht(211,256,64,107,eventx,eventy):
                valik = 0,3
            if evendiasukoht(260,305,64,107,eventx,eventy):
                valik = 0,4
            if evendiasukoht(310,353,64,107,eventx,eventy):
                valik = 0,5
            if evendiasukoht(361,406,64,107,eventx,eventy):
                valik = 0,6
            if evendiasukoht(412,457,64,107,eventx,eventy):
                valik = 0,7
            if evendiasukoht(462,503,64,107,eventx,eventy):
                valik = 0,8
            
            #sudoku ruudud 2.rida
            if evendiasukoht(61,106,113,158,eventx,eventy):
                valik = 1,0
            if evendiasukoht(110,156,113,158,eventx,eventy):
                valik = 1,1
            if evendiasukoht(160,205,113,158,eventx,eventy):
                valik = 1,2
            if evendiasukoht(211,256,113,158,eventx,eventy):
                valik = 1,3
            if evendiasukoht(260,305,113,158,eventx,eventy):
                valik = 1,4
            if evendiasukoht(310,353,113,158,eventx,eventy):
                valik = 1,5
            if evendiasukoht(361,406,113,158,eventx,eventy):
                valik = 1,6
            if evendiasukoht(412,457,113,158,eventx,eventy):
                valik = 1,7
            if evendiasukoht(462,503,113,158,eventx,eventy):
                valik = 1,8
                
            #sudoku ruudud 3.rida
            if evendiasukoht(61,106,164,207,eventx,eventy):
                valik = 2,0
            if evendiasukoht(110,156,164,207,eventx,eventy):
                valik = 2,1
            if evendiasukoht(160,205,164,207,eventx,eventy):
                valik = 2,2
            if evendiasukoht(211,256,164,207,eventx,eventy):
                valik = 2,3
            if evendiasukoht(260,305,164,207,eventx,eventy):
                valik = 2,4
            if evendiasukoht(310,353,164,207,eventx,eventy):
                valik = 2,5
            if evendiasukoht(361,406,164,207,eventx,eventy):
                valik = 2,6
            if evendiasukoht(412,457,164,207,eventx,eventy):
                valik = 2,7
            if evendiasukoht(462,503,164,207,eventx,eventy):
                valik = 2,8
            
            #sudoku ruudud 4.rida
            if evendiasukoht(61,106,215,259,eventx,eventy):
                valik = 3,0
            if evendiasukoht(110,156,215,259,eventx,eventy):
                valik = 3,1
            if evendiasukoht(160,205,215,259,eventx,eventy):
                valik = 3,2
            if evendiasukoht(211,256,215,259,eventx,eventy):
                valik = 3,3
            if evendiasukoht(260,305,215,259,eventx,eventy):
                valik = 3,4
            if evendiasukoht(310,353,215,259,eventx,eventy):
                valik = 3,5
            if evendiasukoht(361,406,215,259,eventx,eventy):
                valik = 3,6
            if evendiasukoht(412,457,215,259,eventx,eventy):
                valik = 3,7
            if evendiasukoht(462,503,215,259,eventx,eventy):
                valik = 3,8
                
            #sudoku ruudud 5.rida
            if evendiasukoht(61,106,265,308,eventx,eventy):
                valik = 4,0
            if evendiasukoht(110,156,265,308,eventx,eventy):
                valik = 4,1
            if evendiasukoht(160,205,265,308,eventx,eventy):
                valik = 4,2
            if evendiasukoht(211,256,265,308,eventx,eventy):
                valik = 4,3
            if evendiasukoht(260,305,265,308,eventx,eventy):
                valik = 4,4
            if evendiasukoht(310,353,265,308,eventx,eventy):
                valik = 4,5
            if evendiasukoht(361,406,265,308,eventx,eventy):
                valik = 4,6
            if evendiasukoht(412,457,265,308,eventx,eventy):
                valik = 4,7
            if evendiasukoht(462,503,265,308,eventx,eventy):
                valik = 4,8
                
            #sudoku ruudud 6.rida
            if evendiasukoht(61,106,315,357,eventx,eventy):
                valik = 5,0
            if evendiasukoht(110,156,315,357,eventx,eventy):
                valik = 5,1
            if evendiasukoht(160,205,315,357,eventx,eventy):
                valik = 5,2
            if evendiasukoht(211,256,315,357,eventx,eventy):
                valik = 5,3
            if evendiasukoht(260,305,315,357,eventx,eventy):
                valik = 5,4
            if evendiasukoht(310,353,315,357,eventx,eventy):
                valik = 5,5
            if evendiasukoht(361,406,315,357,eventx,eventy):
                valik = 5,6
            if evendiasukoht(412,457,315,357,eventx,eventy):
                valik = 5,7
            if evendiasukoht(462,503,315,357,eventx,eventy):
                valik = 5,8
            
            #sudoku ruudud 7.rida
            if evendiasukoht(61,106,364,408,eventx,eventy):
                valik = 6,0
            if evendiasukoht(110,156,364,408,eventx,eventy):
                valik = 6,1
            if evendiasukoht(160,205,364,408,eventx,eventy):
                valik = 6,2
            if evendiasukoht(211,256,364,408,eventx,eventy):
                valik = 6,3
            if evendiasukoht(260,305,364,408,eventx,eventy):
                valik = 6,4
            if evendiasukoht(310,353,364,408,eventx,eventy):
                valik = 6,5
            if evendiasukoht(361,406,364,408,eventx,eventy):
                valik = 6,6
            if evendiasukoht(412,457,364,408,eventx,eventy):
                valik = 6,7
            if evendiasukoht(462,503,364,408,eventx,eventy):
                valik = 6,8
                
            #sudoku ruudud 8.rida
            if evendiasukoht(61,106,413,458,eventx,eventy):
                valik = 7,0
            if evendiasukoht(110,156,413,458,eventx,eventy):
                valik = 7,1
            if evendiasukoht(160,205,413,458,eventx,eventy):
                valik = 7,2
            if evendiasukoht(211,256,413,458,eventx,eventy):
                valik = 7,3
            if evendiasukoht(260,305,413,458,eventx,eventy):
                valik = 7,4
            if evendiasukoht(310,353,413,458,eventx,eventy):
                valik = 7,5
            if evendiasukoht(361,406,413,458,eventx,eventy):
                valik = 7,6
            if evendiasukoht(412,457,413,458,eventx,eventy):
                valik = 7,7
            if evendiasukoht(462,503,413,458,eventx,eventy):
                valik = 7,8
                
            #sudoku ruudud 8.rida
            if evendiasukoht(61,106,463,505,eventx,eventy):
                valik = 8,0
            if evendiasukoht(110,156,463,505,eventx,eventy):
                valik = 8,1
            if evendiasukoht(160,205,463,505,eventx,eventy):
                valik = 8,2
            if evendiasukoht(211,256,463,505,eventx,eventy):
                valik = 8,3
            if evendiasukoht(260,305,463,505,eventx,eventy):
                valik = 8,4
            if evendiasukoht(310,353,463,505,eventx,eventy):
                valik = 8,5
            if evendiasukoht(361,406,463,505,eventx,eventy):
                valik = 8,6
            if evendiasukoht(412,457,463,505,eventx,eventy):
                valik = 8,7
            if evendiasukoht(462,503,463,505,eventx,eventy):
                valik = 8,8
                
            #numbrid valikust
            if evendiasukoht(62,108,522,566,eventx,eventy):
                a,b = valik
                sudoku[a][b] = 1
                #numbrite blitimine 1.rida
                if a == 0 and b == 0:
                    tekstKastis("1", "Comic Sans", 45, 75, 75)
                if a == 0 and b == 1:
                    tekstKastis("1", "Comic Sans", 45, 125, 75)
                if a == 0 and b == 2:
                    tekstKastis("1", "Comic Sans", 45, 175, 75)
                if a == 0 and b == 3:
                    tekstKastis("1", "Comic Sans", 45, 225, 75)
                if a == 0 and b == 4:
                    tekstKastis("1", "Comic Sans", 45, 275, 75)
                if a == 0 and b == 5:
                    tekstKastis("1", "Comic Sans", 45, 325, 75)
                if a == 0 and b == 6:
                    tekstKastis("1", "Comic Sans", 45, 375, 75)
                if a == 0 and b == 7:
                    tekstKastis("1", "Comic Sans", 45, 425, 75)
                if a == 0 and b == 8:
                    tekstKastis("1", "Comic Sans", 45, 475, 75)
                #2.rida
                if a == 1 and b == 0:
                    tekstKastis("1", "Comic Sans", 45, 75, 125)
                if a == 1 and b == 1:
                    tekstKastis("1", "Comic Sans", 45, 125, 125)
                if a == 1 and b == 2:
                    tekstKastis("1", "Comic Sans", 45, 175, 125)
                if a == 1 and b == 3:
                    tekstKastis("1", "Comic Sans", 45, 225, 125)
                if a == 1 and b == 4:
                    tekstKastis("1", "Comic Sans", 45, 275, 125)
                if a == 1 and b == 5:
                    tekstKastis("1", "Comic Sans", 45, 325, 125)
                if a == 1 and b == 6:
                    tekstKastis("1", "Comic Sans", 45, 375, 125)
                if a == 1 and b == 7:
                    tekstKastis("1", "Comic Sans", 45, 425, 125)
                if a == 1 and b == 8:
                    tekstKastis("1", "Comic Sans", 45, 475, 125)
                #3.rida
                if a == 2 and b == 0:
                    tekstKastis("1", "Comic Sans", 45, 75, 175)
                if a == 2 and b == 1:
                    tekstKastis("1", "Comic Sans", 45, 125, 175)
                if a == 2 and b == 2:
                    tekstKastis("1", "Comic Sans", 45, 175, 175)
                if a == 2 and b == 3:
                    tekstKastis("1", "Comic Sans", 45, 225, 175)
                if a == 2 and b == 4:
                    tekstKastis("1", "Comic Sans", 45, 275, 175)
                if a == 2 and b == 5:
                    tekstKastis("1", "Comic Sans", 45, 325, 175)
                if a == 2 and b == 6:
                    tekstKastis("1", "Comic Sans", 45, 375, 175)
                if a == 2 and b == 7:
                    tekstKastis("1", "Comic Sans", 45, 425, 175)
                if a == 2 and b == 8:
                    tekstKastis("1", "Comic Sans", 45, 475, 175)
                #4.rida
                if a == 3 and b == 0:
                    tekstKastis("1", "Comic Sans", 45, 75, 225)
                if a == 3 and b == 1:
                    tekstKastis("1", "Comic Sans", 45, 125, 225)
                if a == 3 and b == 2:
                    tekstKastis("1", "Comic Sans", 45, 175, 225)
                if a == 3 and b == 3:
                    tekstKastis("1", "Comic Sans", 45, 225, 225)
                if a == 3 and b == 4:
                    tekstKastis("1", "Comic Sans", 45, 275, 225)
                if a == 3 and b == 5:
                    tekstKastis("1", "Comic Sans", 45, 325, 225)
                if a == 3 and b == 6:
                    tekstKastis("1", "Comic Sans", 45, 375, 225)
                if a == 3 and b == 7:
                    tekstKastis("1", "Comic Sans", 45, 425, 225)
                if a == 3 and b == 8:
                    tekstKastis("1", "Comic Sans", 45, 475, 225)
                #5.rida
                if a == 4 and b == 0:
                    tekstKastis("1", "Comic Sans", 45, 75, 275)
                if a == 4 and b == 1:
                    tekstKastis("1", "Comic Sans", 45, 125, 275)
                if a == 4 and b == 2:
                    tekstKastis("1", "Comic Sans", 45, 175, 275)
                if a == 4 and b == 3:
                    tekstKastis("1", "Comic Sans", 45, 225, 275)
                if a == 4 and b == 4:
                    tekstKastis("1", "Comic Sans", 45, 275, 275)
                if a == 4 and b == 5:
                    tekstKastis("1", "Comic Sans", 45, 325, 275)
                if a == 4 and b == 6:
                    tekstKastis("1", "Comic Sans", 45, 375, 275)
                if a == 4 and b == 7:
                    tekstKastis("1", "Comic Sans", 45, 425, 275)
                if a == 4 and b == 8:
                    tekstKastis("1", "Comic Sans", 45, 475, 275)
                #6.rida
                if a == 5 and b == 0:
                    tekstKastis("1", "Comic Sans", 45, 75, 325)
                if a == 5 and b == 1:
                    tekstKastis("1", "Comic Sans", 45, 125, 325)
                if a == 5 and b == 2:
                    tekstKastis("1", "Comic Sans", 45, 175, 325)
                if a == 5 and b == 3:
                    tekstKastis("1", "Comic Sans", 45, 225, 325)
                if a == 5 and b == 4:
                    tekstKastis("1", "Comic Sans", 45, 275, 325)
                if a == 5 and b == 5:
                    tekstKastis("1", "Comic Sans", 45, 325, 325)
                if a == 5 and b == 6:
                    tekstKastis("1", "Comic Sans", 45, 375, 325)
                if a == 5 and b == 7:
                    tekstKastis("1", "Comic Sans", 45, 425, 325)
                if a == 5 and b == 8:
                    tekstKastis("1", "Comic Sans", 45, 475, 325)
                #7.rida
                if a == 6 and b == 0:
                    tekstKastis("1", "Comic Sans", 45, 75, 375)
                if a == 6 and b == 1:
                    tekstKastis("1", "Comic Sans", 45, 125, 375)
                if a == 6 and b == 2:
                    tekstKastis("1", "Comic Sans", 45, 175, 375)
                if a == 6 and b == 3:
                    tekstKastis("1", "Comic Sans", 45, 225, 375)
                if a == 6 and b == 4:
                    tekstKastis("1", "Comic Sans", 45, 275, 375)
                if a == 6 and b == 5:
                    tekstKastis("1", "Comic Sans", 45, 325, 375)
                if a == 6 and b == 6:
                    tekstKastis("1", "Comic Sans", 45, 375, 375)
                if a == 6 and b == 7:
                    tekstKastis("1", "Comic Sans", 45, 425, 375)
                if a == 6 and b == 8:
                    tekstKastis("1", "Comic Sans", 45, 475, 375)
                #8.rida
                if a == 7 and b == 0:
                    tekstKastis("1", "Comic Sans", 45, 75, 425)
                if a == 7 and b == 1:
                    tekstKastis("1", "Comic Sans", 45, 125, 425)
                if a == 7 and b == 2:
                    tekstKastis("1", "Comic Sans", 45, 175, 425)
                if a == 7 and b == 3:
                    tekstKastis("1", "Comic Sans", 45, 225, 425)
                if a == 7 and b == 4:
                    tekstKastis("1", "Comic Sans", 45, 275, 425)
                if a == 7 and b == 5:
                    tekstKastis("1", "Comic Sans", 45, 325, 425)
                if a == 7 and b == 6:
                    tekstKastis("1", "Comic Sans", 45, 375, 425)
                if a == 7 and b == 7:
                    tekstKastis("1", "Comic Sans", 45, 425, 425)
                if a == 7 and b == 8:
                    tekstKastis("1", "Comic Sans", 45, 475, 425)
                #9.rida
                if a == 8 and b == 0:
                    tekstKastis("1", "Comic Sans", 45, 75, 475)
                if a == 8 and b == 1:
                    tekstKastis("1", "Comic Sans", 45, 125, 475)
                if a == 8 and b == 2:
                    tekstKastis("1", "Comic Sans", 45, 175, 475)
                if a == 8 and b == 3:
                    tekstKastis("1", "Comic Sans", 45, 225, 475)
                if a == 8 and b == 4:
                    tekstKastis("1", "Comic Sans", 45, 275, 475)
                if a == 8 and b == 5:
                    tekstKastis("1", "Comic Sans", 45, 325, 475)
                if a == 8 and b == 6:
                    tekstKastis("1", "Comic Sans", 45, 375, 475)
                if a == 8 and b == 7:
                    tekstKastis("1", "Comic Sans", 45, 425, 475)
                if a == 8 and b == 8:
                    tekstKastis("1", "Comic Sans", 45, 475, 475)
                
            if evendiasukoht(112,156,522,566,eventx,eventy):
                a,b = valik
                sudoku[a][b] = 2
                #numbrite blitimine 1.rida
                if a == 0 and b == 0:
                    tekstKastis("2", "Comic Sans", 45, 75, 75)
                if a == 0 and b == 1:
                    tekstKastis("2", "Comic Sans", 45, 125, 75)
                if a == 0 and b == 2:
                    tekstKastis("2", "Comic Sans", 45, 175, 75)
                if a == 0 and b == 3:
                    tekstKastis("2", "Comic Sans", 45, 225, 75)
                if a == 0 and b == 4:
                    tekstKastis("2", "Comic Sans", 45, 275, 75)
                if a == 0 and b == 5:
                    tekstKastis("2", "Comic Sans", 45, 325, 75)
                if a == 0 and b == 6:
                    tekstKastis("2", "Comic Sans", 45, 375, 75)
                if a == 0 and b == 7:
                    tekstKastis("2", "Comic Sans", 45, 425, 75)
                if a == 0 and b == 8:
                    tekstKastis("2", "Comic Sans", 45, 475, 75)
                #2.rida
                if a == 1 and b == 0:
                    tekstKastis("2", "Comic Sans", 45, 75, 125)
                if a == 1 and b == 1:
                    tekstKastis("2", "Comic Sans", 45, 125, 125)
                if a == 1 and b == 2:
                    tekstKastis("2", "Comic Sans", 45, 175, 125)
                if a == 1 and b == 3:
                    tekstKastis("2", "Comic Sans", 45, 225, 125)
                if a == 1 and b == 4:
                    tekstKastis("2", "Comic Sans", 45, 275, 125)
                if a == 1 and b == 5:
                    tekstKastis("2", "Comic Sans", 45, 325, 125)
                if a == 1 and b == 6:
                    tekstKastis("2", "Comic Sans", 45, 375, 125)
                if a == 1 and b == 7:
                    tekstKastis("2", "Comic Sans", 45, 425, 125)
                if a == 1 and b == 8:
                    tekstKastis("2", "Comic Sans", 45, 475, 125)
                #3.rida
                if a == 2 and b == 0:
                    tekstKastis("2", "Comic Sans", 45, 75, 175)
                if a == 2 and b == 1:
                    tekstKastis("2", "Comic Sans", 45, 125, 175)
                if a == 2 and b == 2:
                    tekstKastis("2", "Comic Sans", 45, 175, 175)
                if a == 2 and b == 3:
                    tekstKastis("2", "Comic Sans", 45, 225, 175)
                if a == 2 and b == 4:
                    tekstKastis("2", "Comic Sans", 45, 275, 175)
                if a == 2 and b == 5:
                    tekstKastis("2", "Comic Sans", 45, 325, 175)
                if a == 2 and b == 6:
                    tekstKastis("2", "Comic Sans", 45, 375, 175)
                if a == 2 and b == 7:
                    tekstKastis("2", "Comic Sans", 45, 425, 175)
                if a == 2 and b == 8:
                    tekstKastis("2", "Comic Sans", 45, 475, 175)
                #4.rida
                if a == 3 and b == 0:
                    tekstKastis("2", "Comic Sans", 45, 75, 225)
                if a == 3 and b == 1:
                    tekstKastis("2", "Comic Sans", 45, 125, 225)
                if a == 3 and b == 2:
                    tekstKastis("2", "Comic Sans", 45, 175, 225)
                if a == 3 and b == 3:
                    tekstKastis("2", "Comic Sans", 45, 225, 225)
                if a == 3 and b == 4:
                    tekstKastis("2", "Comic Sans", 45, 275, 225)
                if a == 3 and b == 5:
                    tekstKastis("2", "Comic Sans", 45, 325, 225)
                if a == 3 and b == 6:
                    tekstKastis("2", "Comic Sans", 45, 375, 225)
                if a == 3 and b == 7:
                    tekstKastis("2", "Comic Sans", 45, 425, 225)
                if a == 3 and b == 8:
                    tekstKastis("2", "Comic Sans", 45, 475, 225)
                #5.rida
                if a == 4 and b == 0:
                    tekstKastis("2", "Comic Sans", 45, 75, 275)
                if a == 4 and b == 1:
                    tekstKastis("2", "Comic Sans", 45, 125, 275)
                if a == 4 and b == 2:
                    tekstKastis("2", "Comic Sans", 45, 175, 275)
                if a == 4 and b == 3:
                    tekstKastis("2", "Comic Sans", 45, 225, 275)
                if a == 4 and b == 4:
                    tekstKastis("2", "Comic Sans", 45, 275, 275)
                if a == 4 and b == 5:
                    tekstKastis("2", "Comic Sans", 45, 325, 275)
                if a == 4 and b == 6:
                    tekstKastis("2", "Comic Sans", 45, 375, 275)
                if a == 4 and b == 7:
                    tekstKastis("2", "Comic Sans", 45, 425, 275)
                if a == 4 and b == 8:
                    tekstKastis("2", "Comic Sans", 45, 475, 275)
                #6.rida
                if a == 5 and b == 0:
                    tekstKastis("2", "Comic Sans", 45, 75, 325)
                if a == 5 and b == 1:
                    tekstKastis("2", "Comic Sans", 45, 125, 325)
                if a == 5 and b == 2:
                    tekstKastis("2", "Comic Sans", 45, 175, 325)
                if a == 5 and b == 3:
                    tekstKastis("2", "Comic Sans", 45, 225, 325)
                if a == 5 and b == 4:
                    tekstKastis("2", "Comic Sans", 45, 275, 325)
                if a == 5 and b == 5:
                    tekstKastis("2", "Comic Sans", 45, 325, 325)
                if a == 5 and b == 6:
                    tekstKastis("2", "Comic Sans", 45, 375, 325)
                if a == 5 and b == 7:
                    tekstKastis("2", "Comic Sans", 45, 425, 325)
                if a == 5 and b == 8:
                    tekstKastis("2", "Comic Sans", 45, 475, 325)
                #7.rida
                if a == 6 and b == 0:
                    tekstKastis("2", "Comic Sans", 45, 75, 375)
                if a == 6 and b == 1:
                    tekstKastis("2", "Comic Sans", 45, 125, 375)
                if a == 6 and b == 2:
                    tekstKastis("2", "Comic Sans", 45, 175, 375)
                if a == 6 and b == 3:
                    tekstKastis("2", "Comic Sans", 45, 225, 375)
                if a == 6 and b == 4:
                    tekstKastis("2", "Comic Sans", 45, 275, 375)
                if a == 6 and b == 5:
                    tekstKastis("2", "Comic Sans", 45, 325, 375)
                if a == 6 and b == 6:
                    tekstKastis("2", "Comic Sans", 45, 375, 375)
                if a == 6 and b == 7:
                    tekstKastis("2", "Comic Sans", 45, 425, 375)
                if a == 6 and b == 8:
                    tekstKastis("2", "Comic Sans", 45, 475, 375)
                #8.rida
                if a == 7 and b == 0:
                    tekstKastis("2", "Comic Sans", 45, 75, 425)
                if a == 7 and b == 1:
                    tekstKastis("2", "Comic Sans", 45, 125, 425)
                if a == 7 and b == 2:
                    tekstKastis("2", "Comic Sans", 45, 175, 425)
                if a == 7 and b == 3:
                    tekstKastis("2", "Comic Sans", 45, 225, 425)
                if a == 7 and b == 4:
                    tekstKastis("2", "Comic Sans", 45, 275, 425)
                if a == 7 and b == 5:
                    tekstKastis("2", "Comic Sans", 45, 325, 425)
                if a == 7 and b == 6:
                    tekstKastis("2", "Comic Sans", 45, 375, 425)
                if a == 7 and b == 7:
                    tekstKastis("2", "Comic Sans", 45, 425, 425)
                if a == 7 and b == 8:
                    tekstKastis("2", "Comic Sans", 45, 475, 425)
                #9.rida
                if a == 8 and b == 0:
                    tekstKastis("2", "Comic Sans", 45, 75, 475)
                if a == 8 and b == 1:
                    tekstKastis("2", "Comic Sans", 45, 125, 475)
                if a == 8 and b == 2:
                    tekstKastis("2", "Comic Sans", 45, 175, 475)
                if a == 8 and b == 3:
                    tekstKastis("2", "Comic Sans", 45, 225, 475)
                if a == 8 and b == 4:
                    tekstKastis("2", "Comic Sans", 45, 275, 475)
                if a == 8 and b == 5:
                    tekstKastis("2", "Comic Sans", 45, 325, 475)
                if a == 8 and b == 6:
                    tekstKastis("2", "Comic Sans", 45, 375, 475)
                if a == 8 and b == 7:
                    tekstKastis("2", "Comic Sans", 45, 425, 475)
                if a == 8 and b == 8:
                    tekstKastis("2", "Comic Sans", 45, 475, 475)

            if evendiasukoht(163,205,522,566,eventx,eventy):
                a,b = valik
                sudoku[a][b] = 3
                #numbrite blitimine 1.rida
                if a == 0 and b == 0:
                    tekstKastis("3", "Comic Sans", 45, 75, 75)
                if a == 0 and b == 1:
                    tekstKastis("3", "Comic Sans", 45, 125, 75)
                if a == 0 and b == 2:
                    tekstKastis("3", "Comic Sans", 45, 175, 75)
                if a == 0 and b == 3:
                    tekstKastis("3", "Comic Sans", 45, 225, 75)
                if a == 0 and b == 4:
                    tekstKastis("3", "Comic Sans", 45, 275, 75)
                if a == 0 and b == 5:
                    tekstKastis("3", "Comic Sans", 45, 325, 75)
                if a == 0 and b == 6:
                    tekstKastis("3", "Comic Sans", 45, 375, 75)
                if a == 0 and b == 7:
                    tekstKastis("3", "Comic Sans", 45, 425, 75)
                if a == 0 and b == 8:
                    tekstKastis("3", "Comic Sans", 45, 475, 75)
                #2.rida
                if a == 1 and b == 0:
                    tekstKastis("3", "Comic Sans", 45, 75, 125)
                if a == 1 and b == 1:
                    tekstKastis("3", "Comic Sans", 45, 125, 125)
                if a == 1 and b == 2:
                    tekstKastis("3", "Comic Sans", 45, 175, 125)
                if a == 1 and b == 3:
                    tekstKastis("3", "Comic Sans", 45, 225, 125)
                if a == 1 and b == 4:
                    tekstKastis("3", "Comic Sans", 45, 275, 125)
                if a == 1 and b == 5:
                    tekstKastis("3", "Comic Sans", 45, 325, 125)
                if a == 1 and b == 6:
                    tekstKastis("3", "Comic Sans", 45, 375, 125)
                if a == 1 and b == 7:
                    tekstKastis("3", "Comic Sans", 45, 425, 125)
                if a == 1 and b == 8:
                    tekstKastis("3", "Comic Sans", 45, 475, 125)
                #3.rida
                if a == 2 and b == 0:
                    tekstKastis("3", "Comic Sans", 45, 75, 175)
                if a == 2 and b == 1:
                    tekstKastis("3", "Comic Sans", 45, 125, 175)
                if a == 2 and b == 2:
                    tekstKastis("3", "Comic Sans", 45, 175, 175)
                if a == 2 and b == 3:
                    tekstKastis("3", "Comic Sans", 45, 225, 175)
                if a == 2 and b == 4:
                    tekstKastis("3", "Comic Sans", 45, 275, 175)
                if a == 2 and b == 5:
                    tekstKastis("3", "Comic Sans", 45, 325, 175)
                if a == 2 and b == 6:
                    tekstKastis("3", "Comic Sans", 45, 375, 175)
                if a == 2 and b == 7:
                    tekstKastis("3", "Comic Sans", 45, 425, 175)
                if a == 2 and b == 8:
                    tekstKastis("3", "Comic Sans", 45, 475, 175)
                #4.rida
                if a == 3 and b == 0:
                    tekstKastis("3", "Comic Sans", 45, 75, 225)
                if a == 3 and b == 1:
                    tekstKastis("3", "Comic Sans", 45, 125, 225)
                if a == 3 and b == 2:
                    tekstKastis("3", "Comic Sans", 45, 175, 225)
                if a == 3 and b == 3:
                    tekstKastis("3", "Comic Sans", 45, 225, 225)
                if a == 3 and b == 4:
                    tekstKastis("3", "Comic Sans", 45, 275, 225)
                if a == 3 and b == 5:
                    tekstKastis("3", "Comic Sans", 45, 325, 225)
                if a == 3 and b == 6:
                    tekstKastis("3", "Comic Sans", 45, 375, 225)
                if a == 3 and b == 7:
                    tekstKastis("3", "Comic Sans", 45, 425, 225)
                if a == 3 and b == 8:
                    tekstKastis("3", "Comic Sans", 45, 475, 225)
                #5.rida
                if a == 4 and b == 0:
                    tekstKastis("3", "Comic Sans", 45, 75, 275)
                if a == 4 and b == 1:
                    tekstKastis("3", "Comic Sans", 45, 125, 275)
                if a == 4 and b == 2:
                    tekstKastis("3", "Comic Sans", 45, 175, 275)
                if a == 4 and b == 3:
                    tekstKastis("3", "Comic Sans", 45, 225, 275)
                if a == 4 and b == 4:
                    tekstKastis("3", "Comic Sans", 45, 275, 275)
                if a == 4 and b == 5:
                    tekstKastis("3", "Comic Sans", 45, 325, 275)
                if a == 4 and b == 6:
                    tekstKastis("3", "Comic Sans", 45, 375, 275)
                if a == 4 and b == 7:
                    tekstKastis("3", "Comic Sans", 45, 425, 275)
                if a == 4 and b == 8:
                    tekstKastis("3", "Comic Sans", 45, 475, 275)
                #6.rida
                if a == 5 and b == 0:
                    tekstKastis("3", "Comic Sans", 45, 75, 325)
                if a == 5 and b == 1:
                    tekstKastis("3", "Comic Sans", 45, 125, 325)
                if a == 5 and b == 2:
                    tekstKastis("3", "Comic Sans", 45, 175, 325)
                if a == 5 and b == 3:
                    tekstKastis("3", "Comic Sans", 45, 225, 325)
                if a == 5 and b == 4:
                    tekstKastis("3", "Comic Sans", 45, 275, 325)
                if a == 5 and b == 5:
                    tekstKastis("3", "Comic Sans", 45, 325, 325)
                if a == 5 and b == 6:
                    tekstKastis("3", "Comic Sans", 45, 375, 325)
                if a == 5 and b == 7:
                    tekstKastis("3", "Comic Sans", 45, 425, 325)
                if a == 5 and b == 8:
                    tekstKastis("3", "Comic Sans", 45, 475, 325)
                #7.rida
                if a == 6 and b == 0:
                    tekstKastis("3", "Comic Sans", 45, 75, 375)
                if a == 6 and b == 1:
                    tekstKastis("3", "Comic Sans", 45, 125, 375)
                if a == 6 and b == 2:
                    tekstKastis("3", "Comic Sans", 45, 175, 375)
                if a == 6 and b == 3:
                    tekstKastis("3", "Comic Sans", 45, 225, 375)
                if a == 6 and b == 4:
                    tekstKastis("3", "Comic Sans", 45, 275, 375)
                if a == 6 and b == 5:
                    tekstKastis("3", "Comic Sans", 45, 325, 375)
                if a == 6 and b == 6:
                    tekstKastis("3", "Comic Sans", 45, 375, 375)
                if a == 6 and b == 7:
                    tekstKastis("3", "Comic Sans", 45, 425, 375)
                if a == 6 and b == 8:
                    tekstKastis("3", "Comic Sans", 45, 475, 375)
                #8.rida
                if a == 7 and b == 0:
                    tekstKastis("3", "Comic Sans", 45, 75, 425)
                if a == 7 and b == 1:
                    tekstKastis("3", "Comic Sans", 45, 125, 425)
                if a == 7 and b == 2:
                    tekstKastis("3", "Comic Sans", 45, 175, 425)
                if a == 7 and b == 3:
                    tekstKastis("3", "Comic Sans", 45, 225, 425)
                if a == 7 and b == 4:
                    tekstKastis("3", "Comic Sans", 45, 275, 425)
                if a == 7 and b == 5:
                    tekstKastis("3", "Comic Sans", 45, 325, 425)
                if a == 7 and b == 6:
                    tekstKastis("3", "Comic Sans", 45, 375, 425)
                if a == 7 and b == 7:
                    tekstKastis("3", "Comic Sans", 45, 425, 425)
                if a == 7 and b == 8:
                    tekstKastis("3", "Comic Sans", 45, 475, 425)
                #9.rida
                if a == 8 and b == 0:
                    tekstKastis("3", "Comic Sans", 45, 75, 475)
                if a == 8 and b == 1:
                    tekstKastis("3", "Comic Sans", 45, 125, 475)
                if a == 8 and b == 2:
                    tekstKastis("3", "Comic Sans", 45, 175, 475)
                if a == 8 and b == 3:
                    tekstKastis("3", "Comic Sans", 45, 225, 475)
                if a == 8 and b == 4:
                    tekstKastis("3", "Comic Sans", 45, 275, 475)
                if a == 8 and b == 5:
                    tekstKastis("3", "Comic Sans", 45, 325, 475)
                if a == 8 and b == 6:
                    tekstKastis("3", "Comic Sans", 45, 375, 475)
                if a == 8 and b == 7:
                    tekstKastis("3", "Comic Sans", 45, 425, 475)
                if a == 8 and b == 8:
                    tekstKastis("3", "Comic Sans", 45, 475, 475)

            if evendiasukoht(212,256,522,566,eventx,eventy):
                a,b = valik
                sudoku[a][b] = 4
                #numbrite blitimine 1.rida
                if a == 0 and b == 0:
                    tekstKastis("4", "Comic Sans", 45, 75, 75)
                if a == 0 and b == 1:
                    tekstKastis("4", "Comic Sans", 45, 125, 75)
                if a == 0 and b == 2:
                    tekstKastis("4", "Comic Sans", 45, 175, 75)
                if a == 0 and b == 3:
                    tekstKastis("4", "Comic Sans", 45, 225, 75)
                if a == 0 and b == 4:
                    tekstKastis("4", "Comic Sans", 45, 275, 75)
                if a == 0 and b == 5:
                    tekstKastis("4", "Comic Sans", 45, 325, 75)
                if a == 0 and b == 6:
                    tekstKastis("4", "Comic Sans", 45, 375, 75)
                if a == 0 and b == 7:
                    tekstKastis("4", "Comic Sans", 45, 425, 75)
                if a == 0 and b == 8:
                    tekstKastis("4", "Comic Sans", 45, 475, 75)
                #2.rida
                if a == 1 and b == 0:
                    tekstKastis("4", "Comic Sans", 45, 75, 125)
                if a == 1 and b == 1:
                    tekstKastis("4", "Comic Sans", 45, 125, 125)
                if a == 1 and b == 2:
                    tekstKastis("4", "Comic Sans", 45, 175, 125)
                if a == 1 and b == 3:
                    tekstKastis("4", "Comic Sans", 45, 225, 125)
                if a == 1 and b == 4:
                    tekstKastis("4", "Comic Sans", 45, 275, 125)
                if a == 1 and b == 5:
                    tekstKastis("4", "Comic Sans", 45, 325, 125)
                if a == 1 and b == 6:
                    tekstKastis("4", "Comic Sans", 45, 375, 125)
                if a == 1 and b == 7:
                    tekstKastis("4", "Comic Sans", 45, 425, 125)
                if a == 1 and b == 8:
                    tekstKastis("4", "Comic Sans", 45, 475, 125)
                #3.rida
                if a == 2 and b == 0:
                    tekstKastis("4", "Comic Sans", 45, 75, 175)
                if a == 2 and b == 1:
                    tekstKastis("4", "Comic Sans", 45, 125, 175)
                if a == 2 and b == 2:
                    tekstKastis("4", "Comic Sans", 45, 175, 175)
                if a == 2 and b == 3:
                    tekstKastis("4", "Comic Sans", 45, 225, 175)
                if a == 2 and b == 4:
                    tekstKastis("4", "Comic Sans", 45, 275, 175)
                if a == 2 and b == 5:
                    tekstKastis("4", "Comic Sans", 45, 325, 175)
                if a == 2 and b == 6:
                    tekstKastis("4", "Comic Sans", 45, 375, 175)
                if a == 2 and b == 7:
                    tekstKastis("4", "Comic Sans", 45, 425, 175)
                if a == 2 and b == 8:
                    tekstKastis("4", "Comic Sans", 45, 475, 175)
                #4.rida
                if a == 3 and b == 0:
                    tekstKastis("4", "Comic Sans", 45, 75, 225)
                if a == 3 and b == 1:
                    tekstKastis("4", "Comic Sans", 45, 125, 225)
                if a == 3 and b == 2:
                    tekstKastis("4", "Comic Sans", 45, 175, 225)
                if a == 3 and b == 3:
                    tekstKastis("4", "Comic Sans", 45, 225, 225)
                if a == 3 and b == 4:
                    tekstKastis("4", "Comic Sans", 45, 275, 225)
                if a == 3 and b == 5:
                    tekstKastis("4", "Comic Sans", 45, 325, 225)
                if a == 3 and b == 6:
                    tekstKastis("4", "Comic Sans", 45, 375, 225)
                if a == 3 and b == 7:
                    tekstKastis("4", "Comic Sans", 45, 425, 225)
                if a == 3 and b == 8:
                    tekstKastis("4", "Comic Sans", 45, 475, 225)
                #5.rida
                if a == 4 and b == 0:
                    tekstKastis("4", "Comic Sans", 45, 75, 275)
                if a == 4 and b == 1:
                    tekstKastis("4", "Comic Sans", 45, 125, 275)
                if a == 4 and b == 2:
                    tekstKastis("4", "Comic Sans", 45, 175, 275)
                if a == 4 and b == 3:
                    tekstKastis("4", "Comic Sans", 45, 225, 275)
                if a == 4 and b == 4:
                    tekstKastis("4", "Comic Sans", 45, 275, 275)
                if a == 4 and b == 5:
                    tekstKastis("4", "Comic Sans", 45, 325, 275)
                if a == 4 and b == 6:
                    tekstKastis("4", "Comic Sans", 45, 375, 275)
                if a == 4 and b == 7:
                    tekstKastis("4", "Comic Sans", 45, 425, 275)
                if a == 4 and b == 8:
                    tekstKastis("4", "Comic Sans", 45, 475, 275)
                #6.rida
                if a == 5 and b == 0:
                    tekstKastis("4", "Comic Sans", 45, 75, 325)
                if a == 5 and b == 1:
                    tekstKastis("4", "Comic Sans", 45, 125, 325)
                if a == 5 and b == 2:
                    tekstKastis("4", "Comic Sans", 45, 175, 325)
                if a == 5 and b == 3:
                    tekstKastis("4", "Comic Sans", 45, 225, 325)
                if a == 5 and b == 4:
                    tekstKastis("4", "Comic Sans", 45, 275, 325)
                if a == 5 and b == 5:
                    tekstKastis("4", "Comic Sans", 45, 325, 325)
                if a == 5 and b == 6:
                    tekstKastis("4", "Comic Sans", 45, 375, 325)
                if a == 5 and b == 7:
                    tekstKastis("4", "Comic Sans", 45, 425, 325)
                if a == 5 and b == 8:
                    tekstKastis("4", "Comic Sans", 45, 475, 325)
                #7.rida
                if a == 6 and b == 0:
                    tekstKastis("4", "Comic Sans", 45, 75, 375)
                if a == 6 and b == 1:
                    tekstKastis("4", "Comic Sans", 45, 125, 375)
                if a == 6 and b == 2:
                    tekstKastis("4", "Comic Sans", 45, 175, 375)
                if a == 6 and b == 3:
                    tekstKastis("4", "Comic Sans", 45, 225, 375)
                if a == 6 and b == 4:
                    tekstKastis("4", "Comic Sans", 45, 275, 375)
                if a == 6 and b == 5:
                    tekstKastis("4", "Comic Sans", 45, 325, 375)
                if a == 6 and b == 6:
                    tekstKastis("4", "Comic Sans", 45, 375, 375)
                if a == 6 and b == 7:
                    tekstKastis("4", "Comic Sans", 45, 425, 375)
                if a == 6 and b == 8:
                    tekstKastis("4", "Comic Sans", 45, 475, 375)
                #8.rida
                if a == 7 and b == 0:
                    tekstKastis("4", "Comic Sans", 45, 75, 425)
                if a == 7 and b == 1:
                    tekstKastis("4", "Comic Sans", 45, 125, 425)
                if a == 7 and b == 2:
                    tekstKastis("4", "Comic Sans", 45, 175, 425)
                if a == 7 and b == 3:
                    tekstKastis("4", "Comic Sans", 45, 225, 425)
                if a == 7 and b == 4:
                    tekstKastis("4", "Comic Sans", 45, 275, 425)
                if a == 7 and b == 5:
                    tekstKastis("4", "Comic Sans", 45, 325, 425)
                if a == 7 and b == 6:
                    tekstKastis("4", "Comic Sans", 45, 375, 425)
                if a == 7 and b == 7:
                    tekstKastis("4", "Comic Sans", 45, 425, 425)
                if a == 7 and b == 8:
                    tekstKastis("4", "Comic Sans", 45, 475, 425)
                #9.rida
                if a == 8 and b == 0:
                    tekstKastis("4", "Comic Sans", 45, 75, 475)
                if a == 8 and b == 1:
                    tekstKastis("4", "Comic Sans", 45, 125, 475)
                if a == 8 and b == 2:
                    tekstKastis("4", "Comic Sans", 45, 175, 475)
                if a == 8 and b == 3:
                    tekstKastis("4", "Comic Sans", 45, 225, 475)
                if a == 8 and b == 4:
                    tekstKastis("4", "Comic Sans", 45, 275, 475)
                if a == 8 and b == 5:
                    tekstKastis("4", "Comic Sans", 45, 325, 475)
                if a == 8 and b == 6:
                    tekstKastis("4", "Comic Sans", 45, 375, 475)
                if a == 8 and b == 7:
                    tekstKastis("4", "Comic Sans", 45, 425, 475)
                if a == 8 and b == 8:
                    tekstKastis("4", "Comic Sans", 45, 475, 475)

            if evendiasukoht(263,304,522,566,eventx,eventy):
                a,b = valik
                sudoku[a][b] = 5
                #numbrite blitimine 1.rida
                if a == 0 and b == 0:
                    tekstKastis("5", "Comic Sans", 45, 75, 75)
                if a == 0 and b == 1:
                    tekstKastis("5", "Comic Sans", 45, 125, 75)
                if a == 0 and b == 2:
                    tekstKastis("5", "Comic Sans", 45, 175, 75)
                if a == 0 and b == 3:
                    tekstKastis("5", "Comic Sans", 45, 225, 75)
                if a == 0 and b == 4:
                    tekstKastis("5", "Comic Sans", 45, 275, 75)
                if a == 0 and b == 5:
                    tekstKastis("5", "Comic Sans", 45, 325, 75)
                if a == 0 and b == 6:
                    tekstKastis("5", "Comic Sans", 45, 375, 75)
                if a == 0 and b == 7:
                    tekstKastis("5", "Comic Sans", 45, 425, 75)
                if a == 0 and b == 8:
                    tekstKastis("5", "Comic Sans", 45, 475, 75)
                #2.rida
                if a == 1 and b == 0:
                    tekstKastis("5", "Comic Sans", 45, 75, 125)
                if a == 1 and b == 1:
                    tekstKastis("5", "Comic Sans", 45, 125, 125)
                if a == 1 and b == 2:
                    tekstKastis("5", "Comic Sans", 45, 175, 125)
                if a == 1 and b == 3:
                    tekstKastis("5", "Comic Sans", 45, 225, 125)
                if a == 1 and b == 4:
                    tekstKastis("5", "Comic Sans", 45, 275, 125)
                if a == 1 and b == 5:
                    tekstKastis("5", "Comic Sans", 45, 325, 125)
                if a == 1 and b == 6:
                    tekstKastis("5", "Comic Sans", 45, 375, 125)
                if a == 1 and b == 7:
                    tekstKastis("5", "Comic Sans", 45, 425, 125)
                if a == 1 and b == 8:
                    tekstKastis("5", "Comic Sans", 45, 475, 125)
                #3.rida
                if a == 2 and b == 0:
                    tekstKastis("5", "Comic Sans", 45, 75, 175)
                if a == 2 and b == 1:
                    tekstKastis("5", "Comic Sans", 45, 125, 175)
                if a == 2 and b == 2:
                    tekstKastis("5", "Comic Sans", 45, 175, 175)
                if a == 2 and b == 3:
                    tekstKastis("5", "Comic Sans", 45, 225, 175)
                if a == 2 and b == 4:
                    tekstKastis("5", "Comic Sans", 45, 275, 175)
                if a == 2 and b == 5:
                    tekstKastis("5", "Comic Sans", 45, 325, 175)
                if a == 2 and b == 6:
                    tekstKastis("5", "Comic Sans", 45, 375, 175)
                if a == 2 and b == 7:
                    tekstKastis("5", "Comic Sans", 45, 425, 175)
                if a == 2 and b == 8:
                    tekstKastis("5", "Comic Sans", 45, 475, 175)
                #4.rida
                if a == 3 and b == 0:
                    tekstKastis("5", "Comic Sans", 45, 75, 225)
                if a == 3 and b == 1:
                    tekstKastis("5", "Comic Sans", 45, 125, 225)
                if a == 3 and b == 2:
                    tekstKastis("5", "Comic Sans", 45, 175, 225)
                if a == 3 and b == 3:
                    tekstKastis("5", "Comic Sans", 45, 225, 225)
                if a == 3 and b == 4:
                    tekstKastis("5", "Comic Sans", 45, 275, 225)
                if a == 3 and b == 5:
                    tekstKastis("5", "Comic Sans", 45, 325, 225)
                if a == 3 and b == 6:
                    tekstKastis("5", "Comic Sans", 45, 375, 225)
                if a == 3 and b == 7:
                    tekstKastis("5", "Comic Sans", 45, 425, 225)
                if a == 3 and b == 8:
                    tekstKastis("5", "Comic Sans", 45, 475, 225)
                #5.rida
                if a == 4 and b == 0:
                    tekstKastis("5", "Comic Sans", 45, 75, 275)
                if a == 4 and b == 1:
                    tekstKastis("5", "Comic Sans", 45, 125, 275)
                if a == 4 and b == 2:
                    tekstKastis("5", "Comic Sans", 45, 175, 275)
                if a == 4 and b == 3:
                    tekstKastis("5", "Comic Sans", 45, 225, 275)
                if a == 4 and b == 4:
                    tekstKastis("5", "Comic Sans", 45, 275, 275)
                if a == 4 and b == 5:
                    tekstKastis("5", "Comic Sans", 45, 325, 275)
                if a == 4 and b == 6:
                    tekstKastis("5", "Comic Sans", 45, 375, 275)
                if a == 4 and b == 7:
                    tekstKastis("5", "Comic Sans", 45, 425, 275)
                if a == 4 and b == 8:
                    tekstKastis("5", "Comic Sans", 45, 475, 275)
                #6.rida
                if a == 5 and b == 0:
                    tekstKastis("5", "Comic Sans", 45, 75, 325)
                if a == 5 and b == 1:
                    tekstKastis("5", "Comic Sans", 45, 125, 325)
                if a == 5 and b == 2:
                    tekstKastis("5", "Comic Sans", 45, 175, 325)
                if a == 5 and b == 3:
                    tekstKastis("5", "Comic Sans", 45, 225, 325)
                if a == 5 and b == 4:
                    tekstKastis("5", "Comic Sans", 45, 275, 325)
                if a == 5 and b == 5:
                    tekstKastis("5", "Comic Sans", 45, 325, 325)
                if a == 5 and b == 6:
                    tekstKastis("5", "Comic Sans", 45, 375, 325)
                if a == 5 and b == 7:
                    tekstKastis("5", "Comic Sans", 45, 425, 325)
                if a == 5 and b == 8:
                    tekstKastis("5", "Comic Sans", 45, 475, 325)
                #7.rida
                if a == 6 and b == 0:
                    tekstKastis("5", "Comic Sans", 45, 75, 375)
                if a == 6 and b == 1:
                    tekstKastis("5", "Comic Sans", 45, 125, 375)
                if a == 6 and b == 2:
                    tekstKastis("5", "Comic Sans", 45, 175, 375)
                if a == 6 and b == 3:
                    tekstKastis("5", "Comic Sans", 45, 225, 375)
                if a == 6 and b == 4:
                    tekstKastis("5", "Comic Sans", 45, 275, 375)
                if a == 6 and b == 5:
                    tekstKastis("5", "Comic Sans", 45, 325, 375)
                if a == 6 and b == 6:
                    tekstKastis("5", "Comic Sans", 45, 375, 375)
                if a == 6 and b == 7:
                    tekstKastis("5", "Comic Sans", 45, 425, 375)
                if a == 6 and b == 8:
                    tekstKastis("5", "Comic Sans", 45, 475, 375)
                #8.rida
                if a == 7 and b == 0:
                    tekstKastis("5", "Comic Sans", 45, 75, 425)
                if a == 7 and b == 1:
                    tekstKastis("5", "Comic Sans", 45, 125, 425)
                if a == 7 and b == 2:
                    tekstKastis("5", "Comic Sans", 45, 175, 425)
                if a == 7 and b == 3:
                    tekstKastis("5", "Comic Sans", 45, 225, 425)
                if a == 7 and b == 4:
                    tekstKastis("5", "Comic Sans", 45, 275, 425)
                if a == 7 and b == 5:
                    tekstKastis("5", "Comic Sans", 45, 325, 425)
                if a == 7 and b == 6:
                    tekstKastis("5", "Comic Sans", 45, 375, 425)
                if a == 7 and b == 7:
                    tekstKastis("5", "Comic Sans", 45, 425, 425)
                if a == 7 and b == 8:
                    tekstKastis("5", "Comic Sans", 45, 475, 425)
                #9.rida
                if a == 8 and b == 0:
                    tekstKastis("5", "Comic Sans", 45, 75, 475)
                if a == 8 and b == 1:
                    tekstKastis("5", "Comic Sans", 45, 125, 475)
                if a == 8 and b == 2:
                    tekstKastis("5", "Comic Sans", 45, 175, 475)
                if a == 8 and b == 3:
                    tekstKastis("5", "Comic Sans", 45, 225, 475)
                if a == 8 and b == 4:
                    tekstKastis("5", "Comic Sans", 45, 275, 475)
                if a == 8 and b == 5:
                    tekstKastis("5", "Comic Sans", 45, 325, 475)
                if a == 8 and b == 6:
                    tekstKastis("5", "Comic Sans", 45, 375, 475)
                if a == 8 and b == 7:
                    tekstKastis("5", "Comic Sans", 45, 425, 475)
                if a == 8 and b == 8:
                    tekstKastis("5", "Comic Sans", 45, 475, 475)

            if evendiasukoht(312,355,522,566,eventx,eventy):
                a,b = valik
                sudoku[a][b] = 6
                #numbrite blitimine 1.rida
                if a == 0 and b == 0:
                    tekstKastis("6", "Comic Sans", 45, 75, 75)
                if a == 0 and b == 1:
                    tekstKastis("6", "Comic Sans", 45, 125, 75)
                if a == 0 and b == 2:
                    tekstKastis("6", "Comic Sans", 45, 175, 75)
                if a == 0 and b == 3:
                    tekstKastis("6", "Comic Sans", 45, 225, 75)
                if a == 0 and b == 4:
                    tekstKastis("6", "Comic Sans", 45, 275, 75)
                if a == 0 and b == 5:
                    tekstKastis("6", "Comic Sans", 45, 325, 75)
                if a == 0 and b == 6:
                    tekstKastis("6", "Comic Sans", 45, 375, 75)
                if a == 0 and b == 7:
                    tekstKastis("6", "Comic Sans", 45, 425, 75)
                if a == 0 and b == 8:
                    tekstKastis("6", "Comic Sans", 45, 475, 75)
                #2.rida
                if a == 1 and b == 0:
                    tekstKastis("6", "Comic Sans", 45, 75, 125)
                if a == 1 and b == 1:
                    tekstKastis("6", "Comic Sans", 45, 125, 125)
                if a == 1 and b == 2:
                    tekstKastis("6", "Comic Sans", 45, 175, 125)
                if a == 1 and b == 3:
                    tekstKastis("6", "Comic Sans", 45, 225, 125)
                if a == 1 and b == 4:
                    tekstKastis("6", "Comic Sans", 45, 275, 125)
                if a == 1 and b == 5:
                    tekstKastis("6", "Comic Sans", 45, 325, 125)
                if a == 1 and b == 6:
                    tekstKastis("6", "Comic Sans", 45, 375, 125)
                if a == 1 and b == 7:
                    tekstKastis("6", "Comic Sans", 45, 425, 125)
                if a == 1 and b == 8:
                    tekstKastis("6", "Comic Sans", 45, 475, 125)
                #3.rida
                if a == 2 and b == 0:
                    tekstKastis("6", "Comic Sans", 45, 75, 175)
                if a == 2 and b == 1:
                    tekstKastis("6", "Comic Sans", 45, 125, 175)
                if a == 2 and b == 2:
                    tekstKastis("6", "Comic Sans", 45, 175, 175)
                if a == 2 and b == 3:
                    tekstKastis("6", "Comic Sans", 45, 225, 175)
                if a == 2 and b == 4:
                    tekstKastis("6", "Comic Sans", 45, 275, 175)
                if a == 2 and b == 5:
                    tekstKastis("6", "Comic Sans", 45, 325, 175)
                if a == 2 and b == 6:
                    tekstKastis("6", "Comic Sans", 45, 375, 175)
                if a == 2 and b == 7:
                    tekstKastis("6", "Comic Sans", 45, 425, 175)
                if a == 2 and b == 8:
                    tekstKastis("6", "Comic Sans", 45, 475, 175)
                #4.rida
                if a == 3 and b == 0:
                    tekstKastis("6", "Comic Sans", 45, 75, 225)
                if a == 3 and b == 1:
                    tekstKastis("6", "Comic Sans", 45, 125, 225)
                if a == 3 and b == 2:
                    tekstKastis("6", "Comic Sans", 45, 175, 225)
                if a == 3 and b == 3:
                    tekstKastis("6", "Comic Sans", 45, 225, 225)
                if a == 3 and b == 4:
                    tekstKastis("6", "Comic Sans", 45, 275, 225)
                if a == 3 and b == 5:
                    tekstKastis("6", "Comic Sans", 45, 325, 225)
                if a == 3 and b == 6:
                    tekstKastis("6", "Comic Sans", 45, 375, 225)
                if a == 3 and b == 7:
                    tekstKastis("6", "Comic Sans", 45, 425, 225)
                if a == 3 and b == 8:
                    tekstKastis("6", "Comic Sans", 45, 475, 225)
                #5.rida
                if a == 4 and b == 0:
                    tekstKastis("6", "Comic Sans", 45, 75, 275)
                if a == 4 and b == 1:
                    tekstKastis("6", "Comic Sans", 45, 125, 275)
                if a == 4 and b == 2:
                    tekstKastis("6", "Comic Sans", 45, 175, 275)
                if a == 4 and b == 3:
                    tekstKastis("6", "Comic Sans", 45, 225, 275)
                if a == 4 and b == 4:
                    tekstKastis("6", "Comic Sans", 45, 275, 275)
                if a == 4 and b == 5:
                    tekstKastis("6", "Comic Sans", 45, 325, 275)
                if a == 4 and b == 6:
                    tekstKastis("6", "Comic Sans", 45, 375, 275)
                if a == 4 and b == 7:
                    tekstKastis("6", "Comic Sans", 45, 425, 275)
                if a == 4 and b == 8:
                    tekstKastis("6", "Comic Sans", 45, 475, 275)
                #6.rida
                if a == 5 and b == 0:
                    tekstKastis("6", "Comic Sans", 45, 75, 325)
                if a == 5 and b == 1:
                    tekstKastis("6", "Comic Sans", 45, 125, 325)
                if a == 5 and b == 2:
                    tekstKastis("6", "Comic Sans", 45, 175, 325)
                if a == 5 and b == 3:
                    tekstKastis("6", "Comic Sans", 45, 225, 325)
                if a == 5 and b == 4:
                    tekstKastis("6", "Comic Sans", 45, 275, 325)
                if a == 5 and b == 5:
                    tekstKastis("6", "Comic Sans", 45, 325, 325)
                if a == 5 and b == 6:
                    tekstKastis("6", "Comic Sans", 45, 375, 325)
                if a == 5 and b == 7:
                    tekstKastis("6", "Comic Sans", 45, 425, 325)
                if a == 5 and b == 8:
                    tekstKastis("6", "Comic Sans", 45, 475, 325)
                #7.rida
                if a == 6 and b == 0:
                    tekstKastis("6", "Comic Sans", 45, 75, 375)
                if a == 6 and b == 1:
                    tekstKastis("6", "Comic Sans", 45, 125, 375)
                if a == 6 and b == 2:
                    tekstKastis("6", "Comic Sans", 45, 175, 375)
                if a == 6 and b == 3:
                    tekstKastis("6", "Comic Sans", 45, 225, 375)
                if a == 6 and b == 4:
                    tekstKastis("6", "Comic Sans", 45, 275, 375)
                if a == 6 and b == 5:
                    tekstKastis("6", "Comic Sans", 45, 325, 375)
                if a == 6 and b == 6:
                    tekstKastis("6", "Comic Sans", 45, 375, 375)
                if a == 6 and b == 7:
                    tekstKastis("6", "Comic Sans", 45, 425, 375)
                if a == 6 and b == 8:
                    tekstKastis("6", "Comic Sans", 45, 475, 375)
                #8.rida
                if a == 7 and b == 0:
                    tekstKastis("6", "Comic Sans", 45, 75, 425)
                if a == 7 and b == 1:
                    tekstKastis("6", "Comic Sans", 45, 125, 425)
                if a == 7 and b == 2:
                    tekstKastis("6", "Comic Sans", 45, 175, 425)
                if a == 7 and b == 3:
                    tekstKastis("6", "Comic Sans", 45, 225, 425)
                if a == 7 and b == 4:
                    tekstKastis("6", "Comic Sans", 45, 275, 425)
                if a == 7 and b == 5:
                    tekstKastis("6", "Comic Sans", 45, 325, 425)
                if a == 7 and b == 6:
                    tekstKastis("6", "Comic Sans", 45, 375, 425)
                if a == 7 and b == 7:
                    tekstKastis("6", "Comic Sans", 45, 425, 425)
                if a == 7 and b == 8:
                    tekstKastis("6", "Comic Sans", 45, 475, 425)
                #9.rida
                if a == 8 and b == 0:
                    tekstKastis("6", "Comic Sans", 45, 75, 475)
                if a == 8 and b == 1:
                    tekstKastis("6", "Comic Sans", 45, 125, 475)
                if a == 8 and b == 2:
                    tekstKastis("6", "Comic Sans", 45, 175, 475)
                if a == 8 and b == 3:
                    tekstKastis("6", "Comic Sans", 45, 225, 475)
                if a == 8 and b == 4:
                    tekstKastis("6", "Comic Sans", 45, 275, 475)
                if a == 8 and b == 5:
                    tekstKastis("6", "Comic Sans", 45, 325, 475)
                if a == 8 and b == 6:
                    tekstKastis("6", "Comic Sans", 45, 375, 475)
                if a == 8 and b == 7:
                    tekstKastis("6", "Comic Sans", 45, 425, 475)
                if a == 8 and b == 8:
                    tekstKastis("6", "Comic Sans", 45, 475, 475)

            if evendiasukoht(364,404,522,566,eventx,eventy):
                a,b = valik
                sudoku[a][b] = 7
                #numbrite blitimine 1.rida
                if a == 0 and b == 0:
                    tekstKastis("7", "Comic Sans", 45, 75, 75)
                if a == 0 and b == 1:
                    tekstKastis("7", "Comic Sans", 45, 125, 75)
                if a == 0 and b == 2:
                    tekstKastis("7", "Comic Sans", 45, 175, 75)
                if a == 0 and b == 3:
                    tekstKastis("7", "Comic Sans", 45, 225, 75)
                if a == 0 and b == 4:
                    tekstKastis("7", "Comic Sans", 45, 275, 75)
                if a == 0 and b == 5:
                    tekstKastis("7", "Comic Sans", 45, 325, 75)
                if a == 0 and b == 6:
                    tekstKastis("7", "Comic Sans", 45, 375, 75)
                if a == 0 and b == 7:
                    tekstKastis("7", "Comic Sans", 45, 425, 75)
                if a == 0 and b == 8:
                    tekstKastis("7", "Comic Sans", 45, 475, 75)
                #2.rida
                if a == 1 and b == 0:
                    tekstKastis("7", "Comic Sans", 45, 75, 125)
                if a == 1 and b == 1:
                    tekstKastis("7", "Comic Sans", 45, 125, 125)
                if a == 1 and b == 2:
                    tekstKastis("7", "Comic Sans", 45, 175, 125)
                if a == 1 and b == 3:
                    tekstKastis("7", "Comic Sans", 45, 225, 125)
                if a == 1 and b == 4:
                    tekstKastis("7", "Comic Sans", 45, 275, 125)
                if a == 1 and b == 5:
                    tekstKastis("7", "Comic Sans", 45, 325, 125)
                if a == 1 and b == 6:
                    tekstKastis("7", "Comic Sans", 45, 375, 125)
                if a == 1 and b == 7:
                    tekstKastis("7", "Comic Sans", 45, 425, 125)
                if a == 1 and b == 8:
                    tekstKastis("7", "Comic Sans", 45, 475, 125)
                #3.rida
                if a == 2 and b == 0:
                    tekstKastis("7", "Comic Sans", 45, 75, 175)
                if a == 2 and b == 1:
                    tekstKastis("7", "Comic Sans", 45, 125, 175)
                if a == 2 and b == 2:
                    tekstKastis("7", "Comic Sans", 45, 175, 175)
                if a == 2 and b == 3:
                    tekstKastis("7", "Comic Sans", 45, 225, 175)
                if a == 2 and b == 4:
                    tekstKastis("7", "Comic Sans", 45, 275, 175)
                if a == 2 and b == 5:
                    tekstKastis("7", "Comic Sans", 45, 325, 175)
                if a == 2 and b == 6:
                    tekstKastis("7", "Comic Sans", 45, 375, 175)
                if a == 2 and b == 7:
                    tekstKastis("7", "Comic Sans", 45, 425, 175)
                if a == 2 and b == 8:
                    tekstKastis("7", "Comic Sans", 45, 475, 175)
                #4.rida
                if a == 3 and b == 0:
                    tekstKastis("7", "Comic Sans", 45, 75, 225)
                if a == 3 and b == 1:
                    tekstKastis("7", "Comic Sans", 45, 125, 225)
                if a == 3 and b == 2:
                    tekstKastis("7", "Comic Sans", 45, 175, 225)
                if a == 3 and b == 3:
                    tekstKastis("7", "Comic Sans", 45, 225, 225)
                if a == 3 and b == 4:
                    tekstKastis("7", "Comic Sans", 45, 275, 225)
                if a == 3 and b == 5:
                    tekstKastis("7", "Comic Sans", 45, 325, 225)
                if a == 3 and b == 6:
                    tekstKastis("7", "Comic Sans", 45, 375, 225)
                if a == 3 and b == 7:
                    tekstKastis("7", "Comic Sans", 45, 425, 225)
                if a == 3 and b == 8:
                    tekstKastis("7", "Comic Sans", 45, 475, 225)
                #5.rida
                if a == 4 and b == 0:
                    tekstKastis("7", "Comic Sans", 45, 75, 275)
                if a == 4 and b == 1:
                    tekstKastis("7", "Comic Sans", 45, 125, 275)
                if a == 4 and b == 2:
                    tekstKastis("7", "Comic Sans", 45, 175, 275)
                if a == 4 and b == 3:
                    tekstKastis("7", "Comic Sans", 45, 225, 275)
                if a == 4 and b == 4:
                    tekstKastis("7", "Comic Sans", 45, 275, 275)
                if a == 4 and b == 5:
                    tekstKastis("7", "Comic Sans", 45, 325, 275)
                if a == 4 and b == 6:
                    tekstKastis("7", "Comic Sans", 45, 375, 275)
                if a == 4 and b == 7:
                    tekstKastis("7", "Comic Sans", 45, 425, 275)
                if a == 4 and b == 8:
                    tekstKastis("7", "Comic Sans", 45, 475, 275)
                #6.rida
                if a == 5 and b == 0:
                    tekstKastis("7", "Comic Sans", 45, 75, 325)
                if a == 5 and b == 1:
                    tekstKastis("7", "Comic Sans", 45, 125, 325)
                if a == 5 and b == 2:
                    tekstKastis("7", "Comic Sans", 45, 175, 325)
                if a == 5 and b == 3:
                    tekstKastis("7", "Comic Sans", 45, 225, 325)
                if a == 5 and b == 4:
                    tekstKastis("7", "Comic Sans", 45, 275, 325)
                if a == 5 and b == 5:
                    tekstKastis("7", "Comic Sans", 45, 325, 325)
                if a == 5 and b == 6:
                    tekstKastis("7", "Comic Sans", 45, 375, 325)
                if a == 5 and b == 7:
                    tekstKastis("7", "Comic Sans", 45, 425, 325)
                if a == 5 and b == 8:
                    tekstKastis("7", "Comic Sans", 45, 475, 325)
                #7.rida
                if a == 6 and b == 0:
                    tekstKastis("7", "Comic Sans", 45, 75, 375)
                if a == 6 and b == 1:
                    tekstKastis("7", "Comic Sans", 45, 125, 375)
                if a == 6 and b == 2:
                    tekstKastis("7", "Comic Sans", 45, 175, 375)
                if a == 6 and b == 3:
                    tekstKastis("7", "Comic Sans", 45, 225, 375)
                if a == 6 and b == 4:
                    tekstKastis("7", "Comic Sans", 45, 275, 375)
                if a == 6 and b == 5:
                    tekstKastis("7", "Comic Sans", 45, 325, 375)
                if a == 6 and b == 6:
                    tekstKastis("7", "Comic Sans", 45, 375, 375)
                if a == 6 and b == 7:
                    tekstKastis("7", "Comic Sans", 45, 425, 375)
                if a == 6 and b == 8:
                    tekstKastis("7", "Comic Sans", 45, 475, 375)
                #8.rida
                if a == 7 and b == 0:
                    tekstKastis("7", "Comic Sans", 45, 75, 425)
                if a == 7 and b == 1:
                    tekstKastis("7", "Comic Sans", 45, 125, 425)
                if a == 7 and b == 2:
                    tekstKastis("7", "Comic Sans", 45, 175, 425)
                if a == 7 and b == 3:
                    tekstKastis("7", "Comic Sans", 45, 225, 425)
                if a == 7 and b == 4:
                    tekstKastis("7", "Comic Sans", 45, 275, 425)
                if a == 7 and b == 5:
                    tekstKastis("7", "Comic Sans", 45, 325, 425)
                if a == 7 and b == 6:
                    tekstKastis("7", "Comic Sans", 45, 375, 425)
                if a == 7 and b == 7:
                    tekstKastis("7", "Comic Sans", 45, 425, 425)
                if a == 7 and b == 8:
                    tekstKastis("7", "Comic Sans", 45, 475, 425)
                #9.rida
                if a == 8 and b == 0:
                    tekstKastis("7", "Comic Sans", 45, 75, 475)
                if a == 8 and b == 1:
                    tekstKastis("7", "Comic Sans", 45, 125, 475)
                if a == 8 and b == 2:
                    tekstKastis("7", "Comic Sans", 45, 175, 475)
                if a == 8 and b == 3:
                    tekstKastis("7", "Comic Sans", 45, 225, 475)
                if a == 8 and b == 4:
                    tekstKastis("7", "Comic Sans", 45, 275, 475)
                if a == 8 and b == 5:
                    tekstKastis("7", "Comic Sans", 45, 325, 475)
                if a == 8 and b == 6:
                    tekstKastis("7", "Comic Sans", 45, 375, 475)
                if a == 8 and b == 7:
                    tekstKastis("7", "Comic Sans", 45, 425, 475)
                if a == 8 and b == 8:
                    tekstKastis("7", "Comic Sans", 45, 475, 475)

            if evendiasukoht(412,457,522,566,eventx,eventy):
                a,b = valik
                sudoku[a][b] = 8
                #numbrite blitimine 1.rida
                if a == 0 and b == 0:
                    tekstKastis("8", "Comic Sans", 45, 75, 75)
                if a == 0 and b == 1:
                    tekstKastis("8", "Comic Sans", 45, 125, 75)
                if a == 0 and b == 2:
                    tekstKastis("8", "Comic Sans", 45, 175, 75)
                if a == 0 and b == 3:
                    tekstKastis("8", "Comic Sans", 45, 225, 75)
                if a == 0 and b == 4:
                    tekstKastis("8", "Comic Sans", 45, 275, 75)
                if a == 0 and b == 5:
                    tekstKastis("8", "Comic Sans", 45, 325, 75)
                if a == 0 and b == 6:
                    tekstKastis("8", "Comic Sans", 45, 375, 75)
                if a == 0 and b == 7:
                    tekstKastis("8", "Comic Sans", 45, 425, 75)
                if a == 0 and b == 8:
                    tekstKastis("8", "Comic Sans", 45, 475, 75)
                #2.rida
                if a == 1 and b == 0:
                    tekstKastis("8", "Comic Sans", 45, 75, 125)
                if a == 1 and b == 1:
                    tekstKastis("8", "Comic Sans", 45, 125, 125)
                if a == 1 and b == 2:
                    tekstKastis("8", "Comic Sans", 45, 175, 125)
                if a == 1 and b == 3:
                    tekstKastis("8", "Comic Sans", 45, 225, 125)
                if a == 1 and b == 4:
                    tekstKastis("8", "Comic Sans", 45, 275, 125)
                if a == 1 and b == 5:
                    tekstKastis("8", "Comic Sans", 45, 325, 125)
                if a == 1 and b == 6:
                    tekstKastis("8", "Comic Sans", 45, 375, 125)
                if a == 1 and b == 7:
                    tekstKastis("8", "Comic Sans", 45, 425, 125)
                if a == 1 and b == 8:
                    tekstKastis("8", "Comic Sans", 45, 475, 125)
                #3.rida
                if a == 2 and b == 0:
                    tekstKastis("8", "Comic Sans", 45, 75, 175)
                if a == 2 and b == 1:
                    tekstKastis("8", "Comic Sans", 45, 125, 175)
                if a == 2 and b == 2:
                    tekstKastis("8", "Comic Sans", 45, 175, 175)
                if a == 2 and b == 3:
                    tekstKastis("8", "Comic Sans", 45, 225, 175)
                if a == 2 and b == 4:
                    tekstKastis("8", "Comic Sans", 45, 275, 175)
                if a == 2 and b == 5:
                    tekstKastis("8", "Comic Sans", 45, 325, 175)
                if a == 2 and b == 6:
                    tekstKastis("8", "Comic Sans", 45, 375, 175)
                if a == 2 and b == 7:
                    tekstKastis("8", "Comic Sans", 45, 425, 175)
                if a == 2 and b == 8:
                    tekstKastis("8", "Comic Sans", 45, 475, 175)
                #4.rida
                if a == 3 and b == 0:
                    tekstKastis("8", "Comic Sans", 45, 75, 225)
                if a == 3 and b == 1:
                    tekstKastis("8", "Comic Sans", 45, 125, 225)
                if a == 3 and b == 2:
                    tekstKastis("8", "Comic Sans", 45, 175, 225)
                if a == 3 and b == 3:
                    tekstKastis("8", "Comic Sans", 45, 225, 225)
                if a == 3 and b == 4:
                    tekstKastis("8", "Comic Sans", 45, 275, 225)
                if a == 3 and b == 5:
                    tekstKastis("8", "Comic Sans", 45, 325, 225)
                if a == 3 and b == 6:
                    tekstKastis("8", "Comic Sans", 45, 375, 225)
                if a == 3 and b == 7:
                    tekstKastis("8", "Comic Sans", 45, 425, 225)
                if a == 3 and b == 8:
                    tekstKastis("8", "Comic Sans", 45, 475, 225)
                #5.rida
                if a == 4 and b == 0:
                    tekstKastis("8", "Comic Sans", 45, 75, 275)
                if a == 4 and b == 1:
                    tekstKastis("8", "Comic Sans", 45, 125, 275)
                if a == 4 and b == 2:
                    tekstKastis("8", "Comic Sans", 45, 175, 275)
                if a == 4 and b == 3:
                    tekstKastis("8", "Comic Sans", 45, 225, 275)
                if a == 4 and b == 4:
                    tekstKastis("8", "Comic Sans", 45, 275, 275)
                if a == 4 and b == 5:
                    tekstKastis("8", "Comic Sans", 45, 325, 275)
                if a == 4 and b == 6:
                    tekstKastis("8", "Comic Sans", 45, 375, 275)
                if a == 4 and b == 7:
                    tekstKastis("8", "Comic Sans", 45, 425, 275)
                if a == 4 and b == 8:
                    tekstKastis("8", "Comic Sans", 45, 475, 275)
                #6.rida
                if a == 5 and b == 0:
                    tekstKastis("8", "Comic Sans", 45, 75, 325)
                if a == 5 and b == 1:
                    tekstKastis("8", "Comic Sans", 45, 125, 325)
                if a == 5 and b == 2:
                    tekstKastis("8", "Comic Sans", 45, 175, 325)
                if a == 5 and b == 3:
                    tekstKastis("8", "Comic Sans", 45, 225, 325)
                if a == 5 and b == 4:
                    tekstKastis("8", "Comic Sans", 45, 275, 325)
                if a == 5 and b == 5:
                    tekstKastis("8", "Comic Sans", 45, 325, 325)
                if a == 5 and b == 6:
                    tekstKastis("8", "Comic Sans", 45, 375, 325)
                if a == 5 and b == 7:
                    tekstKastis("8", "Comic Sans", 45, 425, 325)
                if a == 5 and b == 8:
                    tekstKastis("8", "Comic Sans", 45, 475, 325)
                #7.rida
                if a == 6 and b == 0:
                    tekstKastis("8", "Comic Sans", 45, 75, 375)
                if a == 6 and b == 1:
                    tekstKastis("8", "Comic Sans", 45, 125, 375)
                if a == 6 and b == 2:
                    tekstKastis("8", "Comic Sans", 45, 175, 375)
                if a == 6 and b == 3:
                    tekstKastis("8", "Comic Sans", 45, 225, 375)
                if a == 6 and b == 4:
                    tekstKastis("8", "Comic Sans", 45, 275, 375)
                if a == 6 and b == 5:
                    tekstKastis("8", "Comic Sans", 45, 325, 375)
                if a == 6 and b == 6:
                    tekstKastis("8", "Comic Sans", 45, 375, 375)
                if a == 6 and b == 7:
                    tekstKastis("8", "Comic Sans", 45, 425, 375)
                if a == 6 and b == 8:
                    tekstKastis("8", "Comic Sans", 45, 475, 375)
                #8.rida
                if a == 7 and b == 0:
                    tekstKastis("8", "Comic Sans", 45, 75, 425)
                if a == 7 and b == 1:
                    tekstKastis("8", "Comic Sans", 45, 125, 425)
                if a == 7 and b == 2:
                    tekstKastis("8", "Comic Sans", 45, 175, 425)
                if a == 7 and b == 3:
                    tekstKastis("8", "Comic Sans", 45, 225, 425)
                if a == 7 and b == 4:
                    tekstKastis("8", "Comic Sans", 45, 275, 425)
                if a == 7 and b == 5:
                    tekstKastis("8", "Comic Sans", 45, 325, 425)
                if a == 7 and b == 6:
                    tekstKastis("8", "Comic Sans", 45, 375, 425)
                if a == 7 and b == 7:
                    tekstKastis("8", "Comic Sans", 45, 425, 425)
                if a == 7 and b == 8:
                    tekstKastis("8", "Comic Sans", 45, 475, 425)
                #9.rida
                if a == 8 and b == 0:
                    tekstKastis("8", "Comic Sans", 45, 75, 475)
                if a == 8 and b == 1:
                    tekstKastis("8", "Comic Sans", 45, 125, 475)
                if a == 8 and b == 2:
                    tekstKastis("8", "Comic Sans", 45, 175, 475)
                if a == 8 and b == 3:
                    tekstKastis("8", "Comic Sans", 45, 225, 475)
                if a == 8 and b == 4:
                    tekstKastis("8", "Comic Sans", 45, 275, 475)
                if a == 8 and b == 5:
                    tekstKastis("8", "Comic Sans", 45, 325, 475)
                if a == 8 and b == 6:
                    tekstKastis("8", "Comic Sans", 45, 375, 475)
                if a == 8 and b == 7:
                    tekstKastis("8", "Comic Sans", 45, 425, 475)
                if a == 8 and b == 8:
                    tekstKastis("8", "Comic Sans", 45, 475, 475)

            if evendiasukoht(464,504,522,566,eventx,eventy):
                a,b = valik
                sudoku[a][b] = 9
                #numbrite blitimine 1.rida
                if a == 0 and b == 0:
                    tekstKastis("9", "Comic Sans", 45, 75, 75)
                if a == 0 and b == 1:
                    tekstKastis("9", "Comic Sans", 45, 125, 75)
                if a == 0 and b == 2:
                    tekstKastis("9", "Comic Sans", 45, 175, 75)
                if a == 0 and b == 3:
                    tekstKastis("9", "Comic Sans", 45, 225, 75)
                if a == 0 and b == 4:
                    tekstKastis("9", "Comic Sans", 45, 275, 75)
                if a == 0 and b == 5:
                    tekstKastis("9", "Comic Sans", 45, 325, 75)
                if a == 0 and b == 6:
                    tekstKastis("9", "Comic Sans", 45, 375, 75)
                if a == 0 and b == 7:
                    tekstKastis("9", "Comic Sans", 45, 425, 75)
                if a == 0 and b == 8:
                    tekstKastis("9", "Comic Sans", 45, 475, 75)
                #2.rida
                if a == 1 and b == 0:
                    tekstKastis("9", "Comic Sans", 45, 75, 125)
                if a == 1 and b == 1:
                    tekstKastis("9", "Comic Sans", 45, 125, 125)
                if a == 1 and b == 2:
                    tekstKastis("9", "Comic Sans", 45, 175, 125)
                if a == 1 and b == 3:
                    tekstKastis("9", "Comic Sans", 45, 225, 125)
                if a == 1 and b == 4:
                    tekstKastis("9", "Comic Sans", 45, 275, 125)
                if a == 1 and b == 5:
                    tekstKastis("9", "Comic Sans", 45, 325, 125)
                if a == 1 and b == 6:
                    tekstKastis("9", "Comic Sans", 45, 375, 125)
                if a == 1 and b == 7:
                    tekstKastis("9", "Comic Sans", 45, 425, 125)
                if a == 1 and b == 8:
                    tekstKastis("9", "Comic Sans", 45, 475, 125)
                #3.rida
                if a == 2 and b == 0:
                    tekstKastis("9", "Comic Sans", 45, 75, 175)
                if a == 2 and b == 1:
                    tekstKastis("9", "Comic Sans", 45, 125, 175)
                if a == 2 and b == 2:
                    tekstKastis("9", "Comic Sans", 45, 175, 175)
                if a == 2 and b == 3:
                    tekstKastis("9", "Comic Sans", 45, 225, 175)
                if a == 2 and b == 4:
                    tekstKastis("9", "Comic Sans", 45, 275, 175)
                if a == 2 and b == 5:
                    tekstKastis("9", "Comic Sans", 45, 325, 175)
                if a == 2 and b == 6:
                    tekstKastis("9", "Comic Sans", 45, 375, 175)
                if a == 2 and b == 7:
                    tekstKastis("9", "Comic Sans", 45, 425, 175)
                if a == 2 and b == 8:
                    tekstKastis("9", "Comic Sans", 45, 475, 175)
                #4.rida
                if a == 3 and b == 0:
                    tekstKastis("9", "Comic Sans", 45, 75, 225)
                if a == 3 and b == 1:
                    tekstKastis("9", "Comic Sans", 45, 125, 225)
                if a == 3 and b == 2:
                    tekstKastis("9", "Comic Sans", 45, 175, 225)
                if a == 3 and b == 3:
                    tekstKastis("9", "Comic Sans", 45, 225, 225)
                if a == 3 and b == 4:
                    tekstKastis("9", "Comic Sans", 45, 275, 225)
                if a == 3 and b == 5:
                    tekstKastis("9", "Comic Sans", 45, 325, 225)
                if a == 3 and b == 6:
                    tekstKastis("9", "Comic Sans", 45, 375, 225)
                if a == 3 and b == 7:
                    tekstKastis("9", "Comic Sans", 45, 425, 225)
                if a == 3 and b == 8:
                    tekstKastis("9", "Comic Sans", 45, 475, 225)
                #5.rida
                if a == 4 and b == 0:
                    tekstKastis("9", "Comic Sans", 45, 75, 275)
                if a == 4 and b == 1:
                    tekstKastis("9", "Comic Sans", 45, 125, 275)
                if a == 4 and b == 2:
                    tekstKastis("9", "Comic Sans", 45, 175, 275)
                if a == 4 and b == 3:
                    tekstKastis("9", "Comic Sans", 45, 225, 275)
                if a == 4 and b == 4:
                    tekstKastis("9", "Comic Sans", 45, 275, 275)
                if a == 4 and b == 5:
                    tekstKastis("9", "Comic Sans", 45, 325, 275)
                if a == 4 and b == 6:
                    tekstKastis("9", "Comic Sans", 45, 375, 275)
                if a == 4 and b == 7:
                    tekstKastis("9", "Comic Sans", 45, 425, 275)
                if a == 4 and b == 8:
                    tekstKastis("9", "Comic Sans", 45, 475, 275)
                #6.rida
                if a == 5 and b == 0:
                    tekstKastis("9", "Comic Sans", 45, 75, 325)
                if a == 5 and b == 1:
                    tekstKastis("9", "Comic Sans", 45, 125, 325)
                if a == 5 and b == 2:
                    tekstKastis("9", "Comic Sans", 45, 175, 325)
                if a == 5 and b == 3:
                    tekstKastis("9", "Comic Sans", 45, 225, 325)
                if a == 5 and b == 4:
                    tekstKastis("9", "Comic Sans", 45, 275, 325)
                if a == 5 and b == 5:
                    tekstKastis("9", "Comic Sans", 45, 325, 325)
                if a == 5 and b == 6:
                    tekstKastis("9", "Comic Sans", 45, 375, 325)
                if a == 5 and b == 7:
                    tekstKastis("9", "Comic Sans", 45, 425, 325)
                if a == 5 and b == 8:
                    tekstKastis("9", "Comic Sans", 45, 475, 325)
                #7.rida
                if a == 6 and b == 0:
                    tekstKastis("9", "Comic Sans", 45, 75, 375)
                if a == 6 and b == 1:
                    tekstKastis("9", "Comic Sans", 45, 125, 375)
                if a == 6 and b == 2:
                    tekstKastis("9", "Comic Sans", 45, 175, 375)
                if a == 6 and b == 3:
                    tekstKastis("9", "Comic Sans", 45, 225, 375)
                if a == 6 and b == 4:
                    tekstKastis("9", "Comic Sans", 45, 275, 375)
                if a == 6 and b == 5:
                    tekstKastis("9", "Comic Sans", 45, 325, 375)
                if a == 6 and b == 6:
                    tekstKastis("9", "Comic Sans", 45, 375, 375)
                if a == 6 and b == 7:
                    tekstKastis("9", "Comic Sans", 45, 425, 375)
                if a == 6 and b == 8:
                    tekstKastis("9", "Comic Sans", 45, 475, 375)
                #8.rida
                if a == 7 and b == 0:
                    tekstKastis("9", "Comic Sans", 45, 75, 425)
                if a == 7 and b == 1:
                    tekstKastis("9", "Comic Sans", 45, 125, 425)
                if a == 7 and b == 2:
                    tekstKastis("9", "Comic Sans", 45, 175, 425)
                if a == 7 and b == 3:
                    tekstKastis("9", "Comic Sans", 45, 225, 425)
                if a == 7 and b == 4:
                    tekstKastis("9", "Comic Sans", 45, 275, 425)
                if a == 7 and b == 5:
                    tekstKastis("9", "Comic Sans", 45, 325, 425)
                if a == 7 and b == 6:
                    tekstKastis("9", "Comic Sans", 45, 375, 425)
                if a == 7 and b == 7:
                    tekstKastis("9", "Comic Sans", 45, 425, 425)
                if a == 7 and b == 8:
                    tekstKastis("9", "Comic Sans", 45, 475, 425)
                #9.rida
                if a == 8 and b == 0:
                    tekstKastis("9", "Comic Sans", 45, 75, 475)
                if a == 8 and b == 1:
                    tekstKastis("9", "Comic Sans", 45, 125, 475)
                if a == 8 and b == 2:
                    tekstKastis("9", "Comic Sans", 45, 175, 475)
                if a == 8 and b == 3:
                    tekstKastis("9", "Comic Sans", 45, 225, 475)
                if a == 8 and b == 4:
                    tekstKastis("9", "Comic Sans", 45, 275, 475)
                if a == 8 and b == 5:
                    tekstKastis("9", "Comic Sans", 45, 325, 475)
                if a == 8 and b == 6:
                    tekstKastis("9", "Comic Sans", 45, 375, 475)
                if a == 8 and b == 7:
                    tekstKastis("9", "Comic Sans", 45, 425, 475)
                if a == 8 and b == 8:
                    tekstKastis("9", "Comic Sans", 45, 475, 475)

                

        pygame.display.flip()

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
            if evendiasukoht(232,467,563,647,eventx,eventy):
                settinguteScreen()
                break
            elif evendiasukoht(232,467,398,480,eventx,eventy): #mängima
                raskusastmed()
                break
            elif evendiasukoht(620,720,620,720,eventx,eventy): #õpetus
                kuidasmängida()
                break
            else:
                continue

homescreen()