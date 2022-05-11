#飞机子弹的图片路径
        self.bullet=bullet;
        #飞机的类型，0代表自己，1代表敌人
        self.type=type;
        #飞机的宽度
        self.width=w;
        #飞机的高度
        self.height=h;
        #存放子弹的数组
        self.allbullet=[];
        #用于判断子弹多长时间发射一次和fps相关
        self.time=0;
        #当前这个飞机的速度
        self.speedx=1;
        self.speedy=1;
        # 攻击速度,值越小攻击越快最小为1
        self.advancespeed = advancespeed;
        #每个飞机自己携带的分数，目前随机
        self.myselfMark=random.randint(1,3)
        #运动轨迹
        self.runType=random.randint(0, 3)
        #是否死亡 1表示死亡 0表示活着
        self.isDeath=0
        #爆炸图片播放那一张
        self.showboomTime=0
        #爆炸数据
        self.boom=boom
        #开始攻击
        self.attack();
    def death(self):
        #死亡状态
        self.isDeath=1;
    def showboom(self):
        #显示boom的动画
        if self.showboomTime==len(self.boom)-1:
            return ;
        if self.time%5==0:
            self.showboomTime+=1;
        self.screen.blit(self.boom[self.showboomTime], (self.x, self.y))
    def run(self,x,y):
        if self.isDeath==1:
            self.showboom();
            return 1;
        self.x = x - self.width / 2;
        self.y = y - self.height / 2;
        self.screen.blit(self.img, (self.x, self.y))
    def attack(self):
        #飞机发射子弹的函数
        if self.time%self.advancespeed==0 and self.isDeath==0:
            self.allbullet.append(bullet(self.screen,self.bullet,self.x-self.width/2,self.y,self.width,self.height,128,128,self.type))
        self.time+=1
    def ai(self):
        if self.isDeath==1:
            self.showboom();
            return
        #这里分为四种的运动轨迹随机决定
        if self.type==1:
            if self.runType==0:
                self.y+=self.speedy*2;
            elif self.runType==1:
                self.y+=self.speedy;
                if self.x<=0-self.width/2 or self.x>=500-self.width/2:
                    self.speedx=0-self.speedx
                self.x+=self.speedx
            elif self.runType==2:
                self.y += self.speedy;
                if self.x<=0-self.width/2 or self.x>=500-self.width/2:
                    self.speedx = 0 - self.speedx
                self.x -= self.speedx
            elif self.runType==3:
                self.y += self.speedy;
                if self.x<=0-self.width/2 or self.x>=500-self.width/2:
                    self.speedx = 0 - self.speedx
                    self.speedy=0-self.speedy
                self.x -= self.speedx
            self.screen.blit(self.img, (self.x, self.y))
            self.attack()
    def __del__(self):
        return

class bullet:
    def __init__(self,screen,img,x,y,airplanex,airplaney,w,h,type):
        #游戏场景传参
        self.screen=screen;
        #子弹的图片的路径
        self.img=img;
        if type==0:
            # 子弹的y坐标
            self.y=y-airplaney;
            # 子弹的x坐标
            self.x = x + airplanex / 2;
        else:
            self.y=y+airplaney-20;
            self.x = x+airplanex/2+w/2-12;
        #子弹图片的宽度
        self.width=w
        #子弹图片的高度
        self.height=h
        #子弹需要一直往前飞
        self.run()
        #子子弹是谁的
        self.type = type
        if self.type==0:
            self.speed=5
        else:
            self.speed=3
    def advance(self):
        if self.type==0:
            self.y-=self.speed;
        else:
            self.y+=self.speed;
        self.run();

    def run(self):
        self.screen.blit(self.img, (self.x, self.y))
    def __del__(self):
        return



