import pygame,random,sys,time
from pygame.locals import * 
from pygame import mixer
import tkinter as tk
import tkinter.font as tkf

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
mixer.music.load('C:\Users\user\Desktop\\drum.mp3')             # 設定背景音樂
mixer.music.play()

pygame.init()                                   # 初始化 pygame
font  = pygame.font.SysFont(None,60)            # None:使用系統預字型
font2 = pygame.font.SysFont(None,30)            # None:使用系統預字型
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT+40))    
pygame.display.set_caption("太鼓達人")          # 設定視窗標題
screen.fill(BACKGROUNDCOLOR) 
image = pygame.image.load('C:\Users\user\Desktop\logo_taiko.png')     # 載入圖片
screen.blit(image,(0,0))                        # 繪製圖片
drawText('Press a key to start.', font, screen, 400,600)
pygame.display.update()

waitForPressKey()                               # 等待使用者按鍵

song_list = ["find you", "red", "shape of you", "honesty", "done for me"]

while Running: 
    #用tkinter製作的歌曲選單， 輸入後按旁邊的按鈕，關閉視窗即可
    class asksong(tk.Frame):                    
      def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.create()
      def create(self):
        s = tk.NE + tk.SW
        f1 = tkf.Font(size = 32,family = "Courier New")
        f2 = tkf.Font(size = 28,family = "Courier New")
        f3 = tkf.Font(size = 14,family = "Courier New")
        self.txt = tk.Text(self,height = 1,width = 15,font = f2)
        self.txt.grid(row = 0,column = 0,columnspan = 15,sticky = s)
        self.lbl = tk.Label(self,text = "請選擇歌曲",height = 1,width = 20,font = f1)
        self.lbl.grid(row = 1,column = 0,columnspan = 20,sticky = s)
        self.btn = tk.Button(self,text = "確認",height = 1,width = 5,font = f2,command = self.clickbtn)
        self.btn.grid(row = 0,column = 16,columnspan = 5,sticky = s)
        self.btn0 = tk.Button(self,text = song_list[0],height = 1,width = 5,font = f3,command = self.clicksongbtn0)
        self.btn0.grid(row = 2,column = 0,columnspan = 5,sticky = s)
        self.btn1 = tk.Button(self,text = song_list[1],height = 1,width = 5,font = f3,command = self.clicksongbtn1)
        self.btn1.grid(row = 2,column = 5,columnspan = 5,sticky = s)
        self.btn2 = tk.Button(self,text = song_list[2],height = 1,width = 5,font = f3,command = self.clicksongbtn2)
        self.btn2.grid(row = 2,column = 10,columnspan = 5,sticky = s)
        self.btn3 = tk.Button(self,text = song_list[3],height = 1,width = 5,font = f3,command = self.clicksongbtn3)
        self.btn3.grid(row = 2,column = 15,columnspan = 5,sticky = s)

      def clickbtn(self):
        global song
        song = self.txt.get("1.0",tk.END)      #將輸入值回傳
      def clicksongbtn0(self):
        self.txt.delete("1.0", tk.END)
        self.txt.insert("1.0", song_list[0])
      def clicksongbtn1(self):
        self.txt.delete("1.0", tk.END)
        self.txt.insert("1.0", song_list[1])
      def clicksongbtn2(self):
        self.txt.delete("1.0", tk.END)
        self.txt.insert("1.0", song_list[2])
      def clicksongbtn3(self):
        self.txt.delete("1.0", tk.END)
        self.txt.insert("1.0", song_list[3])
        
    window = asksong()
    window.master.title("Song")
    window.mainloop()

    song = str(song)
    song = song.lower()
    l = len(song)
    songstr = song[0:l-1]                      #字串處理(因textbox多一個\n，並變成小寫)
    mixer.music.load('C:\Users\user\Desktop\\music\%s.mp3'%songstr) # 載入背景音樂
    mixer.music.play()
    
    background = pygame.Surface(screen.get_size())  # 建立畫布
    background.fill(BACKGROUNDCOLOR)                # 顯示畫布為白色
    image = pygame.image.load('C:\Users\user\Desktop\drum_Basemap.png')   # 載入圖片
    background.blit(image,(0,0))                    # 繪製圖片
                                
    """以下為目前歌曲的鼓(已對過節奏)，若有要增減或修改從此處"""
    if songstr == "find you":
      new_drums1 = [2114, 2858, 3146, 3298, 3618, 3866, 3970, 4074, 4178, 4746, 5186, 5658, 5954, 6242, 6490, 6754, 6986, 7394, 7874, 8090, 8186, 8410, 8538, 8890, 9050, 9234, 9650, 10114, 10426, 10586, 10994, 11242, 11410, 11898, 12114, 12282, 12946, 13282, 13738, 13794, 13850, 13906, 13962] 
      new_drums2 = [2906, 3098, 3354, 3578, 4290, 4402, 4506, 4618, 4962, 5418, 5698, 5914, 7650, 7754, 7978, 8314, 8770, 8938, 9098, 9290, 10162, 10378, 10626, 11042, 11202, 11466, 12074, 12250, 12434, 12786, 13122]
    
    elif songstr == "red":
      new_drums1 = [770, 858, 1250, 1634, 1738, 2586, 2682, 3082, 3466, 3594, 4386, 4498, 4602, 4714, 4834, 4946, 5058, 5162, 6202, 6442, 6778, 7002, 7122, 7226, 7794, 7914, 8498, 8618, 8722, 8834, 9410, 9514, 9634, 9754, 9874, 10042, 10162, 10282, 10346, 10498, 10618, 10794, 10954, 11074, 11178, 11242, 11818, 12026, 12274, 12530, 12730, 12946, 13186, 13418, 13522, 13650, 13762, 13882, 14434, 14554] 
      new_drums2 = [810, 1194, 1306, 1690, 2642, 3042, 3146, 3530, 5274, 5386, 5514, 5642, 5738, 5858, 5970, 6090, 6322, 6546, 6666, 6890, 7346, 7450, 7562, 7682, 8034, 8146, 8258, 8386, 8946, 9058, 9170, 9298, 9986, 10226, 10458, 10690, 10906, 11130, 11354, 11690, 11858, 11970, 12074, 12138, 12418, 12458, 12618, 12770, 12874, 12994, 13066, 13290, 13354, 13986, 14098, 14218, 14322]
      
    elif songstr == "shape of you":
      new_drums1 = [1863, 2135, 2199, 2439, 2511, 2727, 2919, 3103, 3335, 3391, 3623, 3695, 3911, 4111, 4303, 4375, 4447, 4527, 4599, 4663, 4751, 4815, 5479, 5615, 5711, 5775, 5895, 5999, 6671, 6743, 6847, 6911, 6983, 7047, 7119, 7191, 7855, 7999, 8151, 8303, 9055, 9207, 9647, 10079, 10319, 10463, 10543, 10687, 10831, 10903, 10975, 11039, 11423, 11711, 12167, 12447, 12607, 12863, 12919, 13127, 13199]
      new_drums2 = [1991, 2319, 2623, 2799, 3023, 3215, 3495, 3799, 3983, 4215, 4887, 4959, 5031, 5103, 5183, 5247, 5327, 5391, 6063, 6191, 6295, 6367, 6479, 6575, 7271, 7343, 7407, 7479, 7559, 7623, 7695, 7767, 8463, 8607, 8759, 8903, 9343, 9495, 9799, 9935, 10239, 10391, 10615, 10759, 11119, 11191, 11263, 11327, 11567, 11871, 12031, 12311, 12735, 13015]
    elif songstr == "honesty":
      new_drums1 = [842, 1010, 1282, 1554, 1714, 1898, 2074, 2258, 2450, 2626, 2802, 2978, 3146, 3506, 3866, 4050, 4290, 4466, 4906, 5074, 5458, 5722, 5890, 6058, 6146, 6410, 6586, 6746, 6834, 7106, 7298, 7458, 7730, 8082, 8274, 8530, 8706, 8882, 9162, 9506, 9674, 9754, 9930, 10018, 10202, 10562, 10914, 11082, 11354, 11522, 11962, 12322, 12498, 12578, 12770, 12858, 13186, 13354, 13730, 13858, 13994, 14162, 14250, 14346]
      new_drums2 = [938, 1210, 1378, 1642, 1994, 2362, 2706, 3066, 3338, 3674, 4226, 4554, 4738, 5266, 5642, 5986, 6322, 6666, 7034, 7378, 7546, 7818, 7986, 8178, 8434, 8794, 8978, 9074, 9242, 9338, 9586, 9850, 10282, 10386, 10474, 10634, 10738, 10994, 11266, 11610, 11698, 11794, 12042, 12138, 12394, 12682, 13026, 13274, 13450, 13546, 13818, 14090, 14442]
    elif songstr == "done for me":
      new_drums1 = [3634, 3834, 3962, 4282, 4474, 4682, 4810, 5002, 5122, 5258, 5386, 5706, 5898, 6026, 6226, 6426, 6554, 6666, 6730, 6938, 7066, 7266, 7458, 7586, 7778, 7978, 8290, 8426, 8690, 8810, 9010, 9146, 9330, 9602, 9722, 9978, 10314, 10426, 10554, 10898, 11090, 11218, 11346, 11474, 11602, 11730, 12050, 12250, 12362, 12434, 12626, 12818, 12954, 13146, 13266, 13402, 13530, 13794, 14042, 14170, 14298, 14362]
      new_drums2 =[3770, 4026, 4146, 4346, 4538, 4938, 5066, 5330, 5450, 5506, 5578, 5834, 6090, 6362, 6602, 6874, 7130, 7402, 7658, 7914, 8098, 8154, 8354, 8490, 8626, 8746, 8946, 9202, 9466, 9666, 9858, 10050, 10178, 10242, 10498, 10626, 10690, 10762, 11018, 11282, 11546, 11810, 11938, 12114, 12306, 12562, 12746, 12882, 13082, 13338, 13602, 13730, 13922, 14106]
    image = pygame.image.load("C:\Users\user\Desktop\drum1.png")   # 載入背景圖片
    drumr_image = pygame.transform.scale(image, (50,50))             # 重新設定鼓的大小(紅)

    image = pygame.image.load("C:\Users\user\Desktop\drum2.png")   # 載入背景圖片
    drumb_image = pygame.transform.scale(image, (50,50))             # 重新設定鼓的大小(藍)

    good = pygame.Rect(335,190,100,100)                                  # 存放 Rect 物件，記錄good的位置及大小    
    image = pygame.image.load("C:\Users\user\Desktop\good.png")    # 載入背景圖片
    good_image = pygame.transform.scale(image, (100,100))               # 重新設定good的大小  
    
    bad = pygame.Rect(360,190,100,100)                                  # 存放 Rect 物件，記錄bad的位置及大小    
    image = pygame.image.load("C:\Users\user\Desktop\bad.png")     # 載入背景圖片
    bad_image = pygame.transform.scale(image, (50,30))                  # 重新設定bad的大小    
    # print(drums)
      
    dx = 8                                          # 鼓移動的間隔
    score = 0                                       # 得分  
    clock = pygame.time.Clock()                     # 建立時間元件物件
    startTime=time.time()
    endTime = time.time()
    pressr = 0   #按下的參數(紅)
    pressb = 0   #按下的參數(藍)
    timing = 0
    combo = 0    #當前combo
    maxcombo = 0 #最大combo

 
    while (endTime-startTime <=60):            # 設定遊戲時間
        clock.tick(30)                              # 設定while迴圈每秒執行30次
        timing += 1 
        for event in pygame.event.get():
            if event.type == QUIT:                  # 關閉程式視窗
                pygame.quit()
            elif event.type == KEYUP:
                if event.key == 308:
                  pressr = 1
                  # new_drums1.append(370 + 8 * timing)
                if event.key == 307:
                  pressb = 1
                  # new_drums2.append(370 + 8 * timing)
        screen.blit(background,(0,0))               # 重繪視窗
        
        max = 99999999
        for i in range(len(new_drums1)):#紅鼓的運行及打擊            
            new_drums1[i] -= dx                                    
            if pressr == 1:
              if (abs(min(new_drums1) - 375)) <= 35:#若按下且在範圍內
                new_drums1[new_drums1.index(min(new_drums1))] = max
                score += 5 * (1 + combo / 100)#加上combo的計分，越多越高分  
                screen.blit(good_image, good) 
                pressr = 0
                combo += 1
              elif (abs(min(new_drums1) - 375)) >= 35:#若按下但不在範圍內
                screen.blit(bad_image, bad) 
                pressr = 0
                combo = 0
            if min(new_drums1) <= 340:#若超過
              new_drums1[new_drums1.index(min(new_drums1))] = max
              screen.blit(bad_image, bad)
              combo = 0
            screen.blit(drumr_image, pygame.Rect(new_drums1[i],220,50,50))
       
        for r in range(len(new_drums2)):#藍鼓的運行及打擊
            new_drums2[r] -= dx 
            if pressb == 1:
              if (abs(min(new_drums2) - 375)) <= 35:
                new_drums2[new_drums2.index(min(new_drums2))] = max
                score += 3 * (1 + combo / 100)  
                screen.blit(good_image, good) 
                pressb = 0
                combo += 1
              elif (abs(min(new_drums2) - 375)) >= 35:
                screen.blit(bad_image, bad) 
                pressb = 0
                combo = 0
            if min(new_drums2) <= 340:
              new_drums2[new_drums2.index(min(new_drums2))] = max
              screen.blit(bad_image, bad)
              combo = 0
            screen.blit(drumb_image, pygame.Rect(new_drums2[r],220,50,50))
            
        if maxcombo < combo:#刷新maxcombo
          maxcombo = combo   
          
        msgstr1 = str(int(score))                       # 分數
        msg1 = font.render(msgstr1,True,(255,0,0))      # 第1個參數是顯示的文字；第2個參數:True比較平滑；第3個參數是字體的颜色。
        screen.blit(msg1,(210,230))                     # 顯示分數
        msgstr2 = str(combo)                            # combo
        msg2 = font.render(msgstr2,True,(0,0,255))      
        screen.blit(msg2,(210,190))                     # 顯示combo
        pygame.display.update()                         # 更新視窗
        endTime=time.time()
   
    # 遊戲結束，停止播放背景音樂，顯示分數
    pygame.mixer.music.stop()
    mixer.music.load('C:\Users\user\Desktop\gameover.mp3')
    mixer.music.play()
    # print(new_drums1,new_drums2)

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT+40)) 
    screen.fill(BACKGROUNDCOLOR) 
    image = pygame.image.load("C:\Users\user\Desktop\score_Basemap.png")  # 載入圖片
    background.blit(image,(0,0))                    # 繪製圖片
    screen.blit(background,(0,0))                   # 重繪視窗
    
    if score >= 300 and score < 500:
        level = "Good!"            # 分數 300~499 Good!
    elif score >= 500:
        level = "Excellent!"       # 分數 >500 Excellent!
    else:
        level = "OK!"              # 分數 <300 OK!

    msgstr1 = "YOUR SCORE : " + str(int(score))  
    msg1 = font.render(msgstr1,True,(255,0,0))      
    screen.blit(msg1,(550,170))                     
    msg2 = font.render(level,True,(0,128,128))
    screen.blit(msg2,(550,250)) 
    msgstr3 = "YOUR MAX COMBO : " + str(maxcombo)
    msg3 = font.render(msgstr3,True,(0,0,255))
    screen.blit(msg3,(550,210)) 
    """以上為顯示分數、combo、評價"""
    
    pygame.display.update()    # 更新視窗
  
    drawText('PLAY AGAIN (y/n)?', font, screen, 430, 600)    
    pygame.display.update()
    # 按下y鍵再玩一次，n鍵離開。
    waitForYN()
        
mixer.music.stop()
pygame.quit()



