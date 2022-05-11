import pygame

# 玩家飞机类,pygame.sprite模块里面包含了一个名为Sprite类，他是pygame本身自带的一个精灵。
class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        # convert_alpha()更改图像的像素格式，包括每个像素的alpha,相当于图片背景变为透明
        self.image1 = pygame.image.load('images:me1.png').convert_alpha()
        self.image2 = pygame.image.load('images:me2.png').convert_alpha()
        # 飞机摧毁图片,以数字形式保存
        self.destory_image = []
        self.destory_image.extend([
            pygame.image.load('images:me_destroy_1.png').convert_alpha(),
            pygame.image.load('images:me_destroy_2.png').convert_alpha(),
            pygame.image.load('images:me_destroy_3.png').convert_alpha(),
            pygame.image.load('images:me_destroy_4.png').convert_alpha()
        ])
        # 定义屏幕宽高
        self.width = bg_size[0]
        self.height = bg_size[1]

        # get_rect()是一个处理矩形图像的方法，返回值包含矩形的居中属性,这里返回飞机图片1的位置,可以获取图片的宽高等属性
        self.rect = self.image1.get_rect()

        # 飞机的初始化位置,//是整除，位置居中以及高度为图片下框离屏幕最下方60
        self.rect.left = (self.width - self.rect.width)//2
        self.rect.top = self.height - self.rect.height - 60

        # 设置飞机的速度
        self.myPlaneSpeed = 10
        self.active = True

        # 设置飞机是否是无敌状态（重生3秒内无敌）
        self.invincible = True

        # 飞机碰撞检测，会忽略掉图片中白色的背景部分,从指定 Surface 对象中返回一个 Mask
        # 用于快速实现完美的碰撞检测，Mask 可以精确到 1 个像素级别的判断。
        # Surface 对象中透明的部分设置为 1，不透明部分设置为 0。
        self.mask = pygame.mask.from_surface(self.image1)

    # 玩家飞机向上移动
    def moveUp(self):
        # 说明还没定格，即还未到达游戏界面上边界
        if self.rect.top > 0:
            self.rect.top -= self.myPlaneSpeed
        # 说明移动到达上边界了
        else:
            self.rect.top = 0

    # 玩家飞机向下移动
    def moveDown(self):
        # 底部需要划出60的高度用来展示其他数据（炸弹数，生命数等）
        if self.rect.bottom < self.height - 60:
            # self.rect.bottom指的是飞机图片下边界
            self.rect.bottom += self.myPlaneSpeed
        else:
            self.rect.bottom = self.height - 60

    # 玩家飞机向左移动
    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.myPlaneSpeed
        else:
            self.rect.left = 0

    # 玩家飞机向右移动
    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.right += self.myPlaneSpeed
        else:
            self.rect.right = self.width

    # 玩家飞机重生
    def reset(self):
        self.active = True
        # 重生时处于无敌状态
        self.invincible = True
        # 重生飞机的初始化位置,//是整除，位置居中以及高度为图片下框离屏幕最下方60
        self.rect.left = (self.width - self.rect.width) // 2
        self.rect.top = self.height - self.rect.height - 60


