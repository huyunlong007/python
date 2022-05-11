import pygame
import sys
import traceback
from pygame.locals import *
from random import *
import myplane

# 初始化
pygame.init()
# 设置窗口大小
bg_size = width, height = 400, 700  # 实际上是元组
screen = pygame.display.set_mode(bg_size)  # 设置窗口
pygame.display.set_caption("飞机大战")  # 窗口标题
# 加载背景图片,对于普通图像的显示效果有没有convert都是一样的，但是 使用 convert 可以转换格式，提高 blit 的速度
background = pygame.image.load("images:background.png").convert()

def main():
    # 创建时钟对象（可以控制游戏循环频率）
    clock = pygame.time.Clock()

    # 生成玩家飞机
    me = myplane.MyPlane(bg_size)

    # 玩家三条命
    life_num = 3

    # 游戏暂停,默认为非暂停状态
    paused = False

    # 控制玩家飞机图片切换，展示突突突的效果
    switch_image = True
    # 切换延时
    delay = 100

    running = True
    while running:
        # 获取事件
        for event in pygame.event.get():
            # 结束事件触发结束操作
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        # 检测用户键盘操作,分别为上下左右
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            me.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.moveRight()


        # 在屏幕上面绘制背景图像，并指定位置
        screen.blit(background, (0, 0))

        # 绘制子弹补给、炸弹补给等各种元素
        # 未暂停且生命大于0
        if paused == False and life_num > 0:
            # 绘制玩家飞机,如果飞机为激活状态
            if me.active:
                # 在屏幕上绘制玩家飞机,switch_image为是否切换图片
                if switch_image:
                    screen.blit(me.image1, me.rect)
                # 代表切换一下飞行图片
                else:
                    screen.blit(me.image2, me.rect)
            # 代表飞机遭到碰撞，激活爆炸事件
            else:
                print("飞机损毁")

            delay -= 1
            if delay == 0:
                delay = 100
            # 每5帧切换一下飞行图片样式
            if delay % 5 == 0:
                switch_image = not switch_image

        # 在屏幕上面绘制背景图像，并指定位置
        screen.blit(me.image1, me.rect)

        # 更新整个待显示的  Surface 对象到屏幕上，将内存中的内容显示到屏幕上
        pygame.display.flip()
        # 通过时钟对象指定循环频率，每秒循环60次
        # 帧速率是指程序每秒在屏幕山绘制图
        clock.tick(60)

if __name__ == "__main__":
    try:
        main()
    # 服务正常退出
    except SystemExit:
        print("游戏正常退出！")
        # pass忽略错误并继续往下运行，其实这里以及退出了
        pass
    # 服务出现其他的异常
    except:
        # 直接将错误打印出来
        traceback.print_exc()
        pygame.quit()


