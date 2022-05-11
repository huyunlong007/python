# -*- coding: UTF-8 -*-
# animation.py

# 导入需要的模块
import pygame
from pygame.locals import *
import sys
import airplane
import random
class Game:
  def __init__(self):
    # 初始化pygame
    pygame.init()
    #初始化字体文件
    pygame.font.init()
    #初始化游戏分数
    self.mark=0
    # 设置帧率（屏幕每秒刷新的次数）
    self.FPS = 60

    # 获得pygame的时钟
    self.fpsClock = pygame.time.Clock()

    # 设置窗口大小
    self.screen = pygame.display.set_mode((500, 800), 0, 32)

    # 设置标题
    pygame.display.set_caption('飞机大战')

    # 定义颜色
    self.WHITE = (255, 255, 255)
    #用于存放爆炸图片
    self.boom=[pygame.image.load("boom_1.gif")
      ,pygame.image.load("boom_2.gif")
      ,pygame.image.load("boom_3.gif")
      ,pygame.image.load("boom_4.gif")
      ,pygame.image.load("boom_5.gif")
      ,pygame.image.load("boom_6.gif")
      , pygame.image.load("boom_7.gif")
      , pygame.image.load("boom_8.gif")
      , pygame.image.load("boom_9.gif")]
    # 加载一张背景图片
    self.img = pygame.image.load('bg.jpg')
    #加载开始游戏按钮
    self.startGameImage=pygame.image.load('start.png')

    # 初始化背景图片的位置
    self.imgx = 0
    self.imgy = 0
    # 全局的时间变量
    self.time = 0;
    #敌人子弹的图片数据
    self.allEnemyButtlueImg=[pygame.image.load('buttle3.png')]
    # 存放所有敌人图片数据的一个列表
    self.allEnemyImg = [pygame.image.load('em1.png'), pygame.image.load('em2.png')]
    # 存放所有敌人变量的一个列表
    self.allEnemy = [];
    #是否开始了游戏 开始游戏状态为0 死亡状态为1 为开始为2
    self.isStart=2
    #最后一个爆炸动画
    self.lastTime=0
    #开始执行动画
    self.run()
  def initGame(self):
    # 创建一个自己角色
    self.myself = airplane.airplane(self.screen, 30, pygame.image.load('airplane.png'), 250, 800,
                                    pygame.image.load('buttle.png'),
                                    0, 120, 79, self.boom)
    self.isStart=0
  def run(self):
    # 程序主循环
    while True:

      # 每次都要重新绘制背景白色
      self.screen.fill(self.WHITE)

      # 背景的循环滚动
      self.imgy += 2
      if self.imgy == 854:
        self.imgy = 0
      # 背景的绘制，绘制两张图片实现循环滚动的效果
      self.screen.blit(self.img, (self.imgx, self.imgy))
      self.screen.blit(self.img, (self.imgx, self.imgy - 854))
      #如果游戏isstart为flase则游戏不会继续刷新
      if self.isStart==0:
        self.startGame();
      elif self.isStart == 1:
        self.clearAll();
      else:
        self.showstartGame()
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type==MOUSEBUTTONDOWN:
          x, y = pygame.mouse.get_pos()
          if(x>170 and x<170+161and y>300 and y<300+43):
            self.isStart=0
            self.initGame();


      # 刷新屏幕
      pygame.display.update()

      # 设置pygame时钟的间隔时间
      self.fpsClock.tick(self.FPS)
  def showMark(self):
    a = pygame.font.SysFont('幼圆', 50)
    text = a.render(str(self.mark),True,(255,0,0))
    b=len(str(self.mark))
    self.screen.blit(text, [500-b*30,10])
  def showstartGame(self):
    self.screen.blit(self.startGameImage,(170,300))
  def addMark(self,m):
    self.mark+=m;
  def clearMark(self):
    self.mark=0;
  def startGame(self):
    # 获取鼠标位置点
    x, y = pygame.mouse.get_pos()
    # 飞机的运行函数
    self.myself.run(x, y);
    # 所有子弹每一帧的位置
    for item in self.myself.allbullet:
      if item.y <= 0:
        # 当子弹行驶出地图边界之后移除列表中的当前元素并且销毁对象
        self.myself.allbullet.remove(item)
        del item
      else:
        # 如果没有行驶出边界范围则继续行驶
        item.advance()
        for enemy in self.allEnemy:
          try:
            # 判断我方子弹是否与敌人相撞，并且相撞的时候敌人还活着
            if (
                    item.x > enemy.x and item.x < enemy.x + enemy.width and item.y >= enemy.y and item.y < enemy.y + enemy.height and enemy.isDeath == 0):
              self.myself.allbullet.remove(item)
              del item
              enemy.death()
              self.addMark(enemy.myselfMark)
          except:
            continue;
    self.showMark()
    # 发射子弹的函数具体的射速由对象内部决定
    self.myself.attack();
    # 外部计算时间的一个变量没time % FPS == 0 时为1秒钟
    self.time += 1
    if self.time==self.lastTime:
      self.isStart=1
    # 飞机随机生成时间
    if self.time % (self.FPS * 2) == 0:
      # 每过一秒钟新生成一架飞机，添加到allEnemy这个列表之中，y从0开始 x在窗口大小随机生成
      self.allEnemy.append(
        airplane.airplane(self.screen, 15, self.allEnemyImg[random.randint(0, 1)], random.randint(0, 500 - 179), -134,
                          self.allEnemyButtlueImg[0], 1, 179, 134, self.boom))
    # 循环执行该列表，敌人飞机的运动轨迹
    for item in self.allEnemy:
      # 飞机超出下边界后去除
      if item.y > 800 + item.height:
        self.allEnemy.remove(item)
        del item
      # 飞机死亡并且存在子弹数为0后去除
      elif item.isDeath == 1 and len(item.allbullet) == 0:
        self.allEnemy.remove(item)
        del item
      # 否则飞机继续运行
      else:
        item.ai()
        item.attack()
        for i in item.allbullet:
          if i.y <= -96 or i.y >= 896:
            # 当子弹行驶出地图边界之后移除列表中的当前元素并且销毁对象
            item.allbullet.remove(i)
            del i
          else:
            # 如果没有行驶出边界范围则继续行驶
            if (
                    i.x > self.myself.x and i.x < self.myself.x + self.myself.width and i.y >= self.myself.y and i.y < self.myself.y + self.myself.height and self.myself.isDeath == 0):
              self.myself.death()
              self.lastTime=self.time+50;
            i.advance()

  def clearAll(self):
    self.mark=0
    for i in self.allEnemy:
      for j in i.allbullet:
        del j;
      del i;
    for j in self.myself.allbullet:
      del j
    del self.myself
    # 存放所有敌人变量的一个列表
    self.allEnemy = [];
    # 是否开始了游戏
    self.isStart = 2
    self.lastTime=0


game=Game()




