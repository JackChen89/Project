import pygame,random,sys,time
from pygame.locals import *                     # 這個模組含有許多 pygame 會用到的常數
from pygame import mixer

WINDOWWIDTH  = 895                              # 設定視窗大小
WINDOWHEIGHT = 596
BACKGROUNDCOLOR = (255, 255, 255)               # 設定視窗背景顔色

def waitForPressKey():                          # 等待使用者按鍵
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:              # 直接關閉程式視窗
                pygame.quit()
            if event.type == KEYDOWN:               
                return

def waitForESC():                               # 等待使用者按ESC鍵
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:              # 直接關閉程式視窗
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:       # 按下 ESC 鍵離開                    
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
font = pygame.font.SysFont(None, 50)            # None:使用系統預字型
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))    
pygame.display.set_caption("太鼓達人")          # 設定視窗標題

# 顯示起始畫面，告知玩家按下任意鍵開始遊戲
screen.fill(BACKGROUNDCOLOR)                    # 顯示畫布為白色
drawText('Taiko', font, screen, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press a key to start.', font, screen, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()                         # 顯示畫布為白色
waitForPressKey()                               # 等待使用者按鍵

background = pygame.Surface(screen.get_size())  # 建立畫布
background = background.convert()               # 畫布建立副本，加快畫布顯示速度
background.fill(BACKGROUNDCOLOR)                # 顯示畫布為白色

image = pygame.image.load("drum_Basemap.png")   # 載入圖片
image.convert()                                 # 畫布建立副本，加快畫布顯示速度
background.blit(image,(0,0))                    # 繪製圖片

drums = []
for i in range(6):
    drum = pygame.Rect(890+i*150+random.randint(30,50),180,60,60)   # 存放 Rect 物件，記錄鼓的位置及大小
                                                                    # 利用 random.randint 產生整數亂數
    image = pygame.image.load("drum.png")           # 載入背景圖片
    drum_image = pygame.transform.scale(image, (60,60)) # 重新設定鼓的大小
    drums.append(drum)
        
dx = 10                                         # 鼓運動速度
score = 0                                       # 得分
clock = pygame.time.Clock()                     # 建立時間元件物件

startTime=time.time()
endTime = time.time()

while (endTime-startTime <= 30):                 # 設定遊戲時間
    clock.tick(30)                              # 設定while迴圈每秒執行30次
    for event in pygame.event.get():
        if event.type == QUIT:                  # 關閉程式視窗
            pygame.quit()
    
    screen.blit(background,(0,0))               # 清除繪圖視窗
    
    for i in range(6):
        drums[i].left -= dx                             # 改變水平位置
        
        if(drums[i].left <= 190 ):                      # 到達左邊界        
            drums[i].left = screen.get_width()                  
            
        keys = pygame.key.get_pressed()                 # 檢查按鍵被按
        
        if(drums[i].left <= 250 and keys[pygame.K_SPACE]):  # 空白鍵被按
            score += 1   
        screen.blit(drum_image, drums[i])                   # 繪製圖片
    
    msgstr1 = str(score)                            # 繪製分數
    msg1 = font.render(msgstr1,True,(255,0,0))      # 第一個參數是顯示的文字；第一個參數:True比較平滑；第一個參數是字體的颜色。
    screen.blit(msg1,(60,200))                      # 繪製的位置
    pygame.display.update()                         # 繪製 Surface 物件到螢幕上
    endTime=time.time()
 
# 遊戲結束，停止播放背景音樂，顯示"Game Over"
pygame.mixer.music.stop()
gameOverSound = pygame.mixer.Sound('gameover.wav')
gameOverSound.play()
drawText('GAME OVER                     Press ESC to exit.', font, screen, 200, 275)
pygame.display.update()

# 按下 ESC 鍵離開遊戲
waitForESC()
gameOverSound.stop()
pygame.quit()