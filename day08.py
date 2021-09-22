'''分析一个水杯的属性和功能，使用类描述并创建对象
高度，容积，颜色，材质
能存放液体
'''
class glasses:
    __high = 0
    __tj = 0
    __color =""
    __cz=""
    def sethigh(self,high):
        self.__high= high
    def gethigh(self):
        return self.__high
    def setcolor(self,color):
        self.__color = color
    def getcolor(self):
        return self.__color
    def setcz(self,cz):
        self.__cz = cz
    def getcz(self):
        return self.__cz
    def settj(self,tj):
        self.__tj = tj
    def gettj(self):
        return self.__tj
    def cun(self):
        print(self.__color,"的",self.__cz,"杯子里存放了高度为",self.__high,"厘米体积为",self.__tj,"立方厘米的水")
g=glasses()
g.setcolor("蓝色的")
g.setcz("玻璃")
g.sethigh(10)
g.settj(60)
g.cun()
'''有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）'''
class pc:
    __psize=0.0
    __money=0.0
    __cpu=0
    __nc=0
    __djsc=0
    def work(self):
        print("我拿屏幕为",self.__psize,"英寸的笔记本码字")
    def pg(self):
        print("我拿待机时长",self.__djsc,"小时价格",self.__money,"的笔记本看视频")
    def sm(self):
        print("我拿CPU型号为",self.__cpu,"内存",self.__nc,"GB看视频")
    def setpsize(self,psize):
        self.__psize = psize
    def getpsize(self):
        return self.__psize
    def setmoney(self,money):
        self.__money=money
    def getmoney(self):
        return self.__money
    def setcpu(self,cpu):
        self.__cpu=cpu
    def getcpu(self):
        return self.__cpu
    def setnc(self,nc):
        self.__nc=nc
    def getnc(self):
        return self.__nc
    def setdjsc(self,djsc):
        self.__djsc=djsc
    def getdjsc(self):
        return self.__djsc
pc=pc()
pc.setnc(256)
pc.setcpu("asdjkb")
pc.setdjsc(18)
pc.setmoney(6000)
pc.setpsize(48)
pc.work()
pc.pg()
pc.sm()