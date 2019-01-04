import pygame,random,sys,time
from pygame.locals import *                     # 這個模組含有許多 pygame 會用到的常數
from pygame import mixer

WINDOWWIDTH  = 1200                             # 設定視窗大小
WINDOWHEIGHT = 600
BACKGROUNDCOLOR = (255, 255, 255)               # 設定視窗背景顔色
Running = True

def waitForPressKey():                          # 等待使用者按鍵
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:              # 直接關閉程式視窗
                pygame.quit()
            if event.type == KEYDOWN:               
                return

def waitForYN():                                # 等待使用者按y/n鍵
    global Running    
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:       # 直接關閉程式視窗
                pygame.quit()    
        keys = pygame.key.get_pressed()         # 檢查按鍵被按
        if keys[pygame.K_y]:                    # 按下 y             
            Running = True
            return
        if keys[pygame.K_n]:                    # 按下 n             
            Running = False
            return
                
def drawText(text, font, surface, x, y):        # 繪製文字到視窗中
    textobj = font.render(text, 1, (128, 0, 128))
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj,textrect)

mixer.init()                                    # 建立 Soumd 物件
mixer.music.load('drum.mp3')                    # 設定背景音樂
mixer.music.play()

pygame.init()                                   # 初始化 pygame
font  = pygame.font.SysFont(None,60)            # None:使用系統預字型
font2 = pygame.font.SysFont(None,30)            # None:使用系統預字型
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT+40))    
pygame.display.set_caption("太鼓達人")          # 設定視窗標題
screen.fill(BACKGROUNDCOLOR) 
image = pygame.image.load("logo_taiko.png")     # 載入圖片
screen.blit(image,(0,0))                        # 繪製圖片
drawText('Press a key to start.', font, screen, 400,600)
pygame.display.update()

waitForPressKey()                               # 等待使用者按鍵

while Running: 

    mixer.music.load('drum.mp3')                    # 載入背景音樂
    mixer.music.play()
    
    background = pygame.Surface(screen.get_size())  # 建立畫布
    background.fill(BACKGROUNDCOLOR)                # 顯示畫布為白色
    image = pygame.image.load("drum_Basemap.png")   # 載入圖片
    background.blit(image,(0,0))                    # 繪製圖片

    drums = []
	#new_drums = []                                 #在按下space的時候append進去節奏的時間點 (watch line 94)
    new_drums = [1207, 1319, 1423, 1519, 1663, 1767, 1879, 1999, 2111, 2223]  #上面按完之後得結果 ##但這邊目前只能先玩一次然後複製貼上節奏時間
    for i in range(8):
        drum = pygame.Rect(1000 + 50*i,220,50,50)   # 存放 Rect 物件，記錄鼓的位置及大小
                                                                        # 利用 random.randint 產生整數亂數
                                                                        # 改變鼓出現的時間
        image = pygame.image.load("drum.png")                           # 載入背景圖片
        drum_image = pygame.transform.scale(image, (50,50))             # 重新設定鼓的大小
        drums.append(drum)

    good = pygame.Rect(335,190,150,50)                                  # 存放 Rect 物件，記錄鼓的位置及大小    
    image = pygame.image.load("good.png")                               # 載入背景圖片
    good_image = pygame.transform.scale(image, (100,100))               # 重新設定鼓的大小    

      
    dx = 8                                          # 鼓移動的間隔
    score = 0                                       # 得分  
    clock = pygame.time.Clock()                     # 建立時間元件物件
    startTime=time.time()
    endTime = time.time()
    timing = 0
 
    while (endTime-startTime <= 30):                # 設定遊戲時間
        clock.tick(30)                              # 設定while迴圈每秒執行30次
        timing += 1
        for event in pygame.event.get():
            if event.type == QUIT:                  # 關閉程式視窗
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
              if event.key == 32:
               # print("space")                                 #這邊是append節奏的地方
               # drum = pygame.Rect(375 + 8 * timing,220,50,50)
               # new_drums.append(375 + 8 * timing)
               pass   
			   

        screen.blit(background,(0,0))               # 重繪視窗
       
        # for i in range(8):
            # drums[i].left -= dx                                 # 改變水平位置        
            # if(drums[i].left <= 350 ):                          # 到達左邊界        
                # drums[i].left = 1200 + i*100 + random.randint(0,30)    
            
            # keys = pygame.key.get_pressed()                     # 檢查按鍵被按        
            # if(drums[i].left <= 400 and keys[pygame.K_SPACE]):  # 空白鍵被按
                # score += 1   
                # screen.blit(good_image, good) 
            # screen.blit(drum_image, drums[i])                   # 繪製圖片
			
        for i in range(len(new_drums)):                           #顯示新的節奏
            new_drums[i] -= dx                                       
            if(new_drums[i] <= 350 ):                                  
              new_drums[i] = -100
            screen.blit(drum_image, pygame.Rect(new_drums[i],220,50,50))
        
        msgstr1 = str(score)                            # 分數
        msg1 = font.render(msgstr1,True,(255,0,0))      # 第1個參數是顯示的文字；第2個參數:True比較平滑；第3個參數是字體的颜色。
        screen.blit(msg1,(200,220))                     # 顯示分數
        pygame.display.update()                         # 更新視窗
        endTime = time.time()
   
    # 遊戲結束，停止播放背景音樂，顯示分數
    pygame.mixer.music.stop()
    gameOverSound = pygame.mixer.Sound('gameover.wav')
    gameOverSound.play()
    print(new_drums)

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT+40)) 
    screen.fill(BACKGROUNDCOLOR) 
    image = pygame.image.load("score_Basemap.png")  # 載入圖片
    background.blit(image,(0,0))                    # 繪製圖片
    screen.blit(background,(0,0))                   # 重繪視窗
    
    if score >= 100 and score < 300:
        level = "Good!"            # 分數 100~299 Good!
    elif score >= 300:
        level = "Excellent!"       # 分數 >300 Excellent!
    else:
        level = "OK!"              # 分數 <100 OK!

    msgstr1 = "YOUR SCORE : " + str(score)  
    msg1 = font.render(msgstr1,True,(255,0,0))      # 第1個參數是顯示的文字；第2個參數:True比較平滑；第3個參數是字體的颜色。
    screen.blit(msg1,(550,200))                     # 顯示分數
    msg2 = font.render(level,True,(0,128,128))
    screen.blit(msg2,(550,250)) 
    pygame.display.update()                         # 更新視窗
  
    drawText('PLAY AGAIN (y/n)?', font, screen, 480, 600)    
    pygame.display.update()
    # 按下y鍵再玩一次，n鍵離開。
    waitForYN()
        
gameOverSound.stop()
pygame.quit()