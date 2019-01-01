import pygame,sys,time
from pygame.locals import *
from pygame import mixer

mixer.init()
mixer.music.load('C:\\Users\\USER\\Desktop\\Jack\\107-1course\\PBC\\Project\\1230\\drum.mp3')
mixer.music.play()

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("GAME")
back = pygame.image.load("C:\\Users\\USER\\Desktop\\Jack\\107-1course\\PBC\\Project\\newback.jpg").convert()
arrup = pygame.image.load("C:\\Users\\USER\\Desktop\\Jack\\107-1course\\PBC\\Project\\up.png").convert()
arrdown = pygame.image.load("C:\\Users\\USER\\Desktop\\Jack\\107-1course\\PBC\\Project\\down.png").convert()
arrleft = pygame.image.load("C:\\Users\\USER\\Desktop\\Jack\\107-1course\\PBC\\Project\\left.png").convert()
arrright = pygame.image.load("C:\\Users\\USER\\Desktop\\Jack\\107-1course\\PBC\\Project\\right.png").convert()
screen.fill((255,255,255))
screen.blit(back,(0,0))
clock = pygame.time.Clock()
pox1 = 35
pox2 = 175
pox3 = 315
pox4 = 435
poy = 600
# screen.blit(arrright,(pox1,poy))
# screen.blit(arrleft,(pox2,poy))
# screen.blit(arrup,(pox3,poy))
# screen.blit(arrdown,(pox4,poy))
starttime = round(time.time(),2)
timedict = {}


def record():
  while True:
    for event in pygame.event.get():
      
      if event.type == pygame.QUIT:
        # print(timedict)
        pygame.quit()
        sys.exit()
      pygame.display.update()
      
      if event.type == pygame.KEYDOWN:
        now = round(time.time(),2)
        if event.key == 273:
          timedict[now] = "up"
        elif event.key == 274:
          timedict[now] = "down"
        elif event.key == 275:
          timedict[now] = "right"
        elif event.key == 276:
          timedict[now] = "left"
        elif event.key == 13:#enter鍵代碼
          global endtime
          endtime = round(time.time(),2)
          mixer.music.stop()
          print("RECORDED")
          return


def play():
  while True:
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        # print(timedict)
        pygame.quit()
        sys.exit()
    mixer.music.load('C:\\Users\\USER\\Desktop\\Jack\\107-1course\\PBC\\Project\\1230\\drum.mp3')
    mixer.music.play()
    now = round(time.time(),2)
    
    while now < endtime + endtime - starttime:
      now = round(time.time(),2)
      # print(round(now - (endtime - starttime),2))
      try:
        if timedict[round(now - (endtime - starttime),2)] == "up":
          print("UP!!")
          while poy > -100:
            clock.tick(100)
            screen.blit(arrup,(pox3,poy))
            poy -= 3
            pygame.display.update()
        elif timedict[round(now - (endtime - starttime),2)] == "down":
          print("DOWN!!")
        elif timedict[round(now - (endtime - starttime),2)] == "right":
          print("RIGHT!!")
        elif timedict[round(now - (endtime - starttime),2)] == "left":
          print("LEFT!!")
      except:
        True

def main():
  record()
  play()
  
main()

"""目前進度:
構想是先記錄該首歌的節奏，紀錄完再開始玩
record為記錄每次按下上下左右的時間，當記錄完整首輸入enter後，便直接開始play(之後可加delay)，
目前play雖能與record的時間對到(可以print出來)，但是圖片跑不出來><(不確定哪裡出錯)，
運算有點複雜所以沒加太多註解，進度也沒有非常多，有甚麼問題可以私訊我!!!
或是我們可以一起討論~~"""

"""更新:時間的部分有對到的問題(不夠精確or過於精確)
因使用python內的time函數，有點難對，之後會想辦法修正
目前是不夠精確，導致按一次可能會有好幾次跑出來"""
 
"""以下是只有物件移動(圖片)，跟可以輸入上下左右的code"""

# while True:
  # for event in pygame.event.get():
    # if event.type == pygame.QUIT:
      # pygame.quit()
      # sys.exit()
    # elif event.type == pygame.KEYDOWN:
      # if event.key == 273:
        # print("UP")
      # if event.key == 274:
        # print("DOWN")
      # if event.key == 275:
        # print("RIGHT")
      # if event.key == 276:
        # print("LEFT")
  # poy -= 3
  # screen.blit(back,(0,0))
  # screen.blit(arrright,(pox1,poy))
  # screen.blit(arrleft,(pox2,poy))
  # screen.blit(arrup,(pox3,poy))
  # screen.blit(arrdown,(pox4,poy))
  # clock.tick(100)
  # if poy < -100:
    # poy = 600 
  # pygame.display.update()
